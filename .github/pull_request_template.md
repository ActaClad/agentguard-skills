## What changed and why

<!-- Link the issue or review item this addresses. -->

## Checklist

- [ ] `python3 .github/scripts/check_repo.py` passes
- [ ] `claude plugin validate --strict .` and `claude plugin validate --strict .claude-plugin/plugin.json` pass
- [ ] Facts checked against the AgentGuard code (SDK exports, console routes, API endpoints)
- [ ] Version bumped in all three manifests, if skill behaviour changed (see `AGENTS.md`)
- [ ] `CHANGELOG.md` updated
- [ ] No keys, `.env` contents or customer data in the diff

## Test results

<!-- Sample app(s) from tests/sample-apps/, run with the skill and without it. Score against tests/checklist.md. -->

| App | With skill | Without skill |
|---|---|---|
|  |  |  |
