# AgentGuard Skills

Agent Skills that teach AI coding assistants (Claude Code, Cursor, Codex and others) how to integrate [AgentGuard](https://www.npmjs.com/package/@actaclad/agentguard) — the AI trust platform for observability, guardrails, quality and governance of LLM and agent applications.

## Skills

| Skill | Description |
|---|---|
| [agentguard](./skills/agentguard) | Detects your stack, installs or upgrades the AgentGuard SDK, instruments LLM and agent calls, verifies the first trace, then guides you through Security, Observability, AI Quality and Governance. |

## Quick start: add AgentGuard with your coding agent

Paste this prompt into Claude Code, Cursor, Copilot, Codex, or another coding agent, from your application's folder:

```
Install the AgentGuard AI skill from github.com/harish-ai-engineer/AgentGuard-Skill and use it to add AgentGuard tracing and guardrails to this application following best practices.
```

The agent sets everything up. When it needs your keys, it stops and asks you (see [Prerequisites](#prerequisites)).

## Installation

### Claude Code plugin

```
/plugin marketplace add harish-ai-engineer/AgentGuard-Skill
/plugin install agentguard@agentguard
```

### Cursor plugin

Install as a [Cursor plugin](https://cursor.com/docs/plugins) from this repo.

### Manual

Copy or symlink `skills/agentguard` into your agent's skills directory (for Claude Code: `.claude/skills/` in a project or `~/.claude/skills/` for all projects; other agents: see their docs).

## Prerequisites

An AgentGuard project and its API keys, from **Project Settings → API Keys** in the console, plus your app's LLM provider key (e.g. `OPENAI_API_KEY`). You don't need to set them up in advance: when they're missing, the agent creates `.env` with empty entries and waits. Fill in the values in `.env` and reply "done" — the agent then sends and checks the first trace. Don't paste keys into the chat: anything in the chat is sent to the model provider and kept in the chat history.

```bash
AGENTGUARD_PUBLIC_KEY=pk-lf-...
AGENTGUARD_SECRET_KEY=sk-lf-...
AGENTGUARD_BASE_URL=https://<your-agentguard-host>
AGENTGUARD_PROJECT_ID=<project-id>
```

The agent needs terminal access: it installs packages, runs your app once, and reads the resulting trace from the AgentGuard API.

## Usage

Once installed, ask your agent, for example:

- "Add AgentGuard to this app."
- "Check my existing AgentGuard integration and fix any gaps."
- "Which AgentGuard guardrails should I enable for this app?"
