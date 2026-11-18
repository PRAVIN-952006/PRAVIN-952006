# Workflow Guard

Workflow Guard is a small, local-first static checker for GitHub Actions workflow files. It highlights a focused set of high-signal supply-chain and privilege-boundary risks before a workflow is merged:

- workflow or job scopes that grant write access to `GITHUB_TOKEN`;
- third-party actions referenced by mutable tags instead of full commit SHAs;
- `pull_request_target`, which executes with the target repository's privileges;
- untrusted pull-request expressions interpolated into shell commands.

It is intentionally a focused complement to broader tools such as OpenSSF Scorecard and CodeQL, not a replacement for them. Findings are advisory and require review in the context of the repository.

## Usage

```bash
python -m workflow_guard .github/workflows --format text
python -m workflow_guard .github/workflows --format json
```

The checker uses only the Python standard library. It does not execute workflow code, resolve remote actions, or require repository credentials.

From the project directory, the module can also be installed in editable mode:

```bash
python -m pip install -e .
workflow-guard .github/workflows
```

## Development

```bash
python -m unittest discover -s tests -v
```

## Design notes

The initial rules are based on GitHub's [secure use reference](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions) and the OpenSSF Scorecard dangerous-workflow and pinned-dependencies checks. YAML is parsed conservatively so the tool remains dependency-free; unsupported YAML constructs are reported rather than silently treated as safe.

## Limitations

This prototype does not prove that a SHA belongs to the intended upstream action, evaluate reusable workflows, or understand every YAML feature. A clean result is not a security guarantee.

## License

MIT
