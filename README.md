![AgentGuard](assets/logo.png)

# AgentGuard Skills

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/ActaClad/agentguard-skills)](https://github.com/ActaClad/agentguard-skills/releases)
[![CI](https://github.com/ActaClad/agentguard-skills/actions/workflows/check-repo.yml/badge.svg)](https://github.com/ActaClad/agentguard-skills/actions/workflows/check-repo.yml)

Agent Skills that teach AI coding assistants how to integrate [AgentGuard](https://actaclad.com), the AI trust platform for observability, guardrails, quality and governance of LLM and agent applications.

## Skills

| Skill | Description |
|---|---|
| [agentguard](./skills/agentguard) | Detects your stack, installs or upgrades the AgentGuard SDK, instruments LLM and agent calls, verifies the first trace, then guides you through Security, Observability, AI Quality and Governance. |

## Quick start

Paste this prompt into your coding agent from your application's folder:

```
Install the AgentGuard AI skill from github.com/ActaClad/agentguard-skills and use it to add AgentGuard tracing and guardrails to this application following best practices.
```

The agent sets everything up. When it needs your keys, it stops and asks you (see [Requirements](#requirements)).

## Supported agents

| Agent | Install |
|---|---|
| Claude Code | `/plugin marketplace add ActaClad/agentguard-skills`, then `/plugin install agentguard@agentguard` |
| Cursor | Install as a [Cursor plugin](https://cursor.com/docs/plugins) from this repo |
| Codex | `codex plugin marketplace add ActaClad/agentguard-skills` |
| GitHub Copilot and other CLIs | `gh skill install ActaClad/agentguard-skills agentguard` |
| Any agent with skills support | `npx skills add ActaClad/agentguard-skills` |

You can also copy or symlink `skills/agentguard` into your agent's skills directory (for Claude Code: `.claude/skills/` in a project, or `~/.claude/skills/` for all projects).

## Requirements

- **An application** in Node.js 20+ or Python 3.8+ that calls an LLM.
- **An AgentGuard account and project.** The keys come from **Project Settings → API Keys** in the console.
- **Your app's LLM provider key**, for example `OPENAI_API_KEY`. The agent runs your app once to produce the first trace.
- **A coding agent with terminal access.** It installs packages, runs your app and reads the trace from the AgentGuard API.

You don't need to set up the keys in advance. When they're missing, the agent creates `.env` with empty entries and waits. Fill in the values in `.env` and reply "done". Don't paste keys into the chat: anything in the chat is sent to the model provider and kept in the chat history.

```bash
AGENTGUARD_PUBLIC_KEY=<public-key>
AGENTGUARD_SECRET_KEY=<secret-key>
AGENTGUARD_BASE_URL=https://<your-agentguard-host>
AGENTGUARD_PROJECT_ID=<project-id>
AGENTGUARD_CAPTURE_CONTENT=true   # added by the agent; set to false to keep prompt/response text out of traces
```

## Usage

Once installed, ask your agent, for example:

- "Add AgentGuard to this app."
- "Check my existing AgentGuard integration and fix any gaps."
- "Which AgentGuard guardrails should I enable for this app?"

## What the skill runs and sends

The skill contains instructions only; it ships no scripts or servers. When you use it, your coding agent:

- reads your application's code and edits the files it integrates;
- installs the AgentGuard SDK with your project's package manager, and checks the latest version on npm or PyPI;
- creates or updates `.env` with empty AgentGuard entries, and adds `.env` to `.gitignore`;
- runs your app once with a harmless test message, which calls your LLM provider as your app normally does;
- calls your own AgentGuard host's public API with the keys from `.env` to read the resulting trace and your project's guardrail configuration.

Nothing is sent anywhere else. Key values are never printed, committed or requested in the chat.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md). To report a vulnerability, follow [SECURITY.md](SECURITY.md). Changes are listed in [CHANGELOG.md](CHANGELOG.md).

## License

[Apache License 2.0](LICENSE). Copyright (c) 2026 [ActaClad, Inc.](https://actaclad.com)
