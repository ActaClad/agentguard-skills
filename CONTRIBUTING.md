# Contributing

Thanks for helping improve the AgentGuard skill. By taking part you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md). To report a security problem, follow [SECURITY.md](SECURITY.md) instead of opening an issue.

## Proposing a change

- **Small, self-contained fixes** (a wrong instruction, a typo, a clearer step): open a pull request directly.
- **Anything larger** (a new reference file, routing changes, behaviour changes): open an issue first so we can agree on the approach.

## Writing skill files

[`AGENTS.md`](AGENTS.md) holds the authoring rules, and every pull request is reviewed against it. In short:

- Every line must help an agent act. Keep each reference file at 100 lines or fewer.
- Don't copy SDK code into the skill; the agent reads the README of the SDK version it installed.
- Routing lives only in the `## Use case specific references` list in `SKILL.md`.
- Check facts against the AgentGuard code (SDK exports, console routes, API endpoints) before writing them.

## Before you open a pull request

1. **Run the repo checks** (the same ones CI runs):
   ```bash
   python3 .github/scripts/check_repo.py
   claude plugin validate --strict .
   claude plugin validate --strict .claude-plugin/plugin.json
   ```
2. **Test the change on a sample app.** Load the plugin locally with `claude --plugin-dir .`, open an app from `tests/sample-apps/`, and score the run against [`tests/checklist.md`](tests/checklist.md). Run the same prompt without the skill as a baseline.
3. **Bump the version** in all three manifests together (`.claude-plugin`, `.cursor-plugin`, `.codex-plugin`), following the rules in `AGENTS.md`, and add an entry to [`CHANGELOG.md`](CHANGELOG.md).
4. **Fill in the pull request template**, including your test results.

Pull requests to `main` need one approving review and a passing CI run.

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE).
