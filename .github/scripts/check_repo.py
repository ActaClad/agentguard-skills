#!/usr/bin/env python3
"""Enforce the repository rules written in AGENTS.md.

- Every skill has SKILL.md frontmatter with a valid `name` (matching its folder)
  and a non-empty `description` of at most 1,024 characters.
- Every reference listed in SKILL.md exists; reference files sit one level deep,
  have no frontmatter and are at most 100 lines.
- The three plugin manifests carry the same `version`.

Standard library only, so it runs on any CI image without installing anything.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFESTS = [
    ".claude-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    ".codex-plugin/plugin.json",
]
MAX_REFERENCE_LINES = 100
MAX_DESCRIPTION_CHARS = 1024
NAME_PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Parse the simple `key: value` / `key: >-` frontmatter SKILL.md uses."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    key = None
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if match:
            key, value = match.group(1), match.group(2).strip()
            fields[key] = "" if value in (">-", ">", "|", "|-") else value.strip("\"'")
        elif key and line.startswith((" ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def check_skill(skill_dir: Path) -> None:
    rel = skill_dir.relative_to(ROOT)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        fail(f"{rel}: missing SKILL.md")
        return
    text = skill_md.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    if meta is None:
        fail(f"{rel}/SKILL.md: missing or unterminated frontmatter")
        return

    name = meta.get("name", "")
    if not NAME_PATTERN.match(name):
        fail(f"{rel}/SKILL.md: name {name!r} must be lowercase letters, digits and hyphens, up to 64 characters")
    if name != skill_dir.name:
        fail(f"{rel}/SKILL.md: name {name!r} must match the folder name {skill_dir.name!r}")

    description = meta.get("description", "")
    if not description:
        fail(f"{rel}/SKILL.md: description is empty")
    elif len(description) > MAX_DESCRIPTION_CHARS:
        fail(f"{rel}/SKILL.md: description is {len(description)} characters (max {MAX_DESCRIPTION_CHARS})")

    for ref in sorted(set(re.findall(r"references/[\w.-]+\.md", text))):
        if not (skill_dir / ref).is_file():
            fail(f"{rel}/SKILL.md: lists {ref}, which does not exist")

    refs_dir = skill_dir / "references"
    if refs_dir.is_dir():
        for path in sorted(refs_dir.rglob("*")):
            ref_rel = path.relative_to(ROOT)
            if path.is_dir():
                fail(f"{ref_rel}: references must be one level deep (no subfolders)")
                continue
            if path.suffix != ".md":
                continue
            lines = path.read_text(encoding="utf-8").splitlines()
            if len(lines) > MAX_REFERENCE_LINES:
                fail(f"{ref_rel}: {len(lines)} lines (max {MAX_REFERENCE_LINES})")
            if lines and lines[0].strip() == "---":
                fail(f"{ref_rel}: reference files must not have frontmatter")


def check_manifest_versions() -> None:
    versions: dict[str, str] = {}
    for manifest in MANIFESTS:
        path = ROOT / manifest
        try:
            versions[manifest] = json.loads(path.read_text(encoding="utf-8"))["version"]
        except FileNotFoundError:
            fail(f"{manifest}: missing")
        except (json.JSONDecodeError, KeyError) as exc:
            fail(f"{manifest}: cannot read version ({exc})")
    if len(set(versions.values())) > 1:
        listed = ", ".join(f"{m}={v}" for m, v in versions.items())
        fail(f"manifest versions differ: {listed}")


def main() -> int:
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if not skills:
        fail("skills/: no skill folders found")
    for skill_dir in skills:
        check_skill(skill_dir)
    check_manifest_versions()

    if errors:
        for message in errors:
            print(f"::error::{message}")
        print(f"\n{len(errors)} problem(s) found.")
        return 1
    print(f"OK: {len(skills)} skill(s), manifests in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
