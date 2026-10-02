# Changelog

All notable changes to the AgentGuard skill are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.1.7] - 2026-09-29

### Fixed

- Python SDK 1.6.0+ needs no extra package for `pii-redaction`, `prompt-injection` and `toxic-content`; the skill now tells the agent not to install the `[guardrails]` extra for them.
- Codex manifest: removed the undocumented `Interactive` capability, and set marketplace authentication to `ON_USE`, since the plugin has nothing to sign in to.

## [0.1.6] - 2026-09-28

### Fixed

- Scoped the "no registration needed" guardrail note to Node SDK 3.0.0+; on Node 2.x the agent upgrades the SDK instead.

## [0.1.5] - 2026-09-28

### Added

- Apache-2.0 `LICENSE`.
- Sample apps for repeatable tests: `node-openai`, `py-openai`, `node-existing-broken`.
- `.agents/plugins/marketplace.json`, so Codex can install the plugin from this repo.
- README section describing what the skill runs and sends.

### Changed

- The repo moved to `ActaClad/agentguard-skills`; install links updated.
- `SKILL.md` description is written in the third person.
- Reference files no longer carry frontmatter; routing lives only in `SKILL.md`.
- Key prefixes are no longer shown in the docs.

### Fixed

- Removed the incorrect instruction to register ML guardrails or set `AGENTGUARD_ENABLE_ML_GUARDRAILS`.
- Added the `mcp` extra to the Python install list.

### Removed

- The bundled `skill-creator` authoring skill.

## [0.1.4] - 2026-09-28

### Added

- Provider coverage table: which LLM calls each SDK traces, and what the agent tells the user for calls that are not covered.

## [0.1.3] - 2026-09-28

### Changed

- `init()` is written exactly as the SDK README shows, with no wrapper code; the agent checks the keys itself.
- `fail` and `on_block` keep their defaults unless the user asks.

## [0.1.2] - 2026-09-27

### Changed

- Troubleshooting no longer describes the old `localhost` fallback for a missing base URL.

## [0.1.1] - 2026-09-27

### Added

- The first trace uses a harmless test message, labelled user `agentguard-test` and feature `integration-test`.
- Troubleshooting entry for a missing `AGENTGUARD_BASE_URL`.

### Changed

- Content capture is turned on in the client's `.env` by default, with instructions to turn it off.

## [0.1.0] - 2026-09-27

### Added

- The `agentguard` skill: detects the stack, installs or upgrades the SDK, adds the integration, verifies the first trace, and guides the user through Security, Observability, AI Quality and Governance.
- Audit mode for apps that already use AgentGuard.
- Credential flow: the agent creates `.env` and waits for the user to fill it in.
- Content capture, environment label and legacy env-var handling.
- Plugin manifests for Claude Code, Cursor and Codex.

[0.1.7]: https://github.com/ActaClad/agentguard-skills/releases/tag/v0.1.7
