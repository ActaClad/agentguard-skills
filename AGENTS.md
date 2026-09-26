# Agent Instructions

## Editing the skill

- **Every line must earn its place.** Keep each reference at 100 lines or fewer, including frontmatter.
- **Never commit SDK code.** The skill tells the agent to read the installed SDK README, so code always matches the client's version. Pseudo-code for logic-specific bits is fine.
- **Routing lives in exactly two places:** one line per reference in the `## Use case specific references` list in `SKILL.md`, and the reference file's frontmatter `description`.
- **Check facts against the AgentGuard code** (SDK exports, console routes, API endpoints) before writing them. Console page paths come from `web/src/components/layouts/routes.tsx` in the AgentGuard repo.
- After changing a skill, run the affected sample apps in `tests/checklist.md`.

## Plugin version bumps

The plugin ships with three manifests: `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.codex-plugin/plugin.json`. Their `version` fields **must stay identical** — bump all three together, in the same change as the skill edit.

- **Patch**: fixes and clarifications to skill instructions.
- **Minor**: new reference, new capability, or support for a new SDK major version.
- **Major**: removing or renaming a skill.
- **No bump**: README, AGENTS.md, tests, typos.
