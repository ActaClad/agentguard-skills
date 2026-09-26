---
name: agentguard
description: >-
  Integrate the AgentGuard SDK into an AI application: detect the stack, install the right SDK, wire it in, verify the first trace, then guide the user through Observability, AI Quality, Security and Governance in the AgentGuard console. Use when the user wants to add AgentGuard, check an existing AgentGuard integration, trace or guard LLM/agent calls, or asks what to do after integrating.
---

# AgentGuard

AgentGuard traces and guards LLM and agent calls. One `init()` at startup auto-instruments the app's LLM clients. Guardrails are configured per project in the console and enforced inside the SDK, in the app's process.

## Core principles

1. **The installed SDK README is the source of truth.** It matches the exact version you installed. Read it before writing code:
   - Node: `node_modules/@actaclad/agentguard/README.md`
   - Python: `python -c "import importlib.metadata as m; print(m.metadata('actaclad-agentguard').get_payload())"`

   The console docs at `<AGENTGUARD_BASE_URL>/docs/onboarding` are secondary: a fetch shows only the Node.js code, and some pages lag the SDK. When they disagree, follow the README.
2. **Never handle secrets in chat.** Check presence only, never print values. If keys are missing, ask the user to create them in the console under **Project Settings → API Keys** and put them in the app's `.env` or secret manager.
3. **Instrumentation must not change what the app returns.** Guardrails start disabled; enabling or blocking is the user's decision, made after integration.

## Credentials

Both SDKs read the same variables:

| Variable | Needed for |
|---|---|
| `AGENTGUARD_PUBLIC_KEY` (`pk-lf-…`), `AGENTGUARD_SECRET_KEY` (`sk-lf-…`) | Everything |
| `AGENTGUARD_BASE_URL` | Everything; the customer's own host, there is no shared default |
| `AGENTGUARD_PROJECT_ID` | Guardrails; without it the SDK traces only and logs a warning |

## Reading project data

There is no CLI. Use the public REST API with basic auth, passing credentials from env so they never appear in output:

```bash
curl -s -u "$AGENTGUARD_PUBLIC_KEY:$AGENTGUARD_SECRET_KEY" "$AGENTGUARD_BASE_URL/api/public/<resource>"
```

Useful resources: `traces`, `traces/<traceId>`, `observations`, `scores`, `guardrails?projectId=<projectId>` (the guardrail config exactly as the SDK receives it).

## Console links

Project pages live at `<AGENTGUARD_BASE_URL>/project/<projectId>/<page>`; a single trace is `traces/<traceId>`. Always give the user the full link, not just a page name.

## Use case specific references

- integrating the SDK into an application, or checking and fixing an existing integration: references/instrumentation.md
- guiding the user through the console after integration (guardrails, prompts, scores, LLM evals, human review, governance): references/post-integration-guide.md
