# Security Policy

The AgentGuard skill runs inside a developer's coding agent: it installs packages, edits code, creates `.env` entries and calls the AgentGuard API. We take reports about it seriously.

## Reporting a vulnerability

Please **do not open a public issue** for security problems. Report them privately, either:

- by email to **info@actaclad.com**, or
- through GitHub's [private vulnerability reporting](https://github.com/ActaClad/agentguard-skills/security/advisories/new).

Include what you found, how to reproduce it, and the plugin version (`version` in `.claude-plugin/plugin.json`).

We aim to acknowledge reports within 3 business days and to keep you informed until the issue is resolved.

## Scope

In scope:

- instructions in `skills/` that could make an agent expose secrets, run unexpected commands, or send data anywhere other than the user's AgentGuard host and LLM provider;
- the plugin manifests and marketplace files.

Vulnerabilities in the AgentGuard SDKs or the AgentGuard service are out of scope for this repository. Report them through the same email address, which reaches the team.

## Supported versions

Only the latest release receives fixes.
