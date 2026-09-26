# AgentGuard skill — test checklist

Run a fresh agent with only this skill loaded against each app in `sample-apps/`. Record pass/fail per row.

## Sample apps to build

| App | Stack | Exercises |
|---|---|---|
| node-openai | Node + OpenAI chat | Basic path, class instrumentation, flush |
| node-langgraph-bedrock | Node + LangGraph + Bedrock + one tool | Single linked trace, framework-built client, tool guarding |
| py-openai | Python + OpenAI | Auto-detect, extras, policy() context |
| py-langchain | Python + LangChain agent | Framework tracing via the installed README |
| node-existing-broken | Node + OpenAI, AgentGuard already integrated on an old SDK version (e.g. 2.0.0) with planted gaps: `init()` after client creation, second `init()`, no session id, no `flush()` in a script, one guardrail already enabled | Audit mode: no reinstall, finds and fixes each gap, leaves working code alone, reports existing guardrail |

## Criteria

| # | Check | Pass when |
|---|---|---|
| 1 | Stack detection | Findings table lists the correct language, providers, frameworks, lifecycle |
| 2 | Install | Correct package + only needed extras, via the project's package manager |
| 3 | Code | `init` before first client use; context in one place; flush where needed; no app behavior change |
| 4 | Secrets | No key printed or requested in chat; `.env.example` has placeholders only |
| 5 | First trace | Agent ran the app, fetched the trace via the API, and gave a working trace link |
| 6 | Trace quality | Model, tokens, cost, nesting, user/session ids present |
| 7 | Guardrails guidance | States they are off by default; recommendations match the app; observe-first; block handling offered |
| 8 | Pillar guidance | Observability, AI Quality, Security, Governance covered with working full links |
| 9 | No overreach | Agent did not enable guardrails or change console settings unasked |
| 10 | Audit mode | Existing integration detected; baseline table reported (met / gap); only gaps fixed; no duplicate `init()`; old SDK upgraded to latest, changed calls updated, trace re-verified (or rolled back with a reason) |
| 11 | Baseline | Final trace passes every row of the baseline table in instrumentation.md |
