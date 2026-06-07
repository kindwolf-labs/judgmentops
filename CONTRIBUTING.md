# Contributing to JudgmentOps

Thank you for your interest. JudgmentOps exists to make long-running agentic software work more reliable by preserving human judgment.

We welcome contributions that sharpen the judgment layer rather than add generation features.

## What We Value Most

- High-signal judgment cases that reveal new classes of failure (see CASEBOOK.md format)
- Precise protocol improvements and clarifications in PROTOCOL.md
- Better schema definitions that remain simple enough for humans and agents to use
- Evaluation harnesses and benchmark ideas that measure judgment preservation, not just pass@K
- Documentation and application materials that help labs, maintainers, and enterprises understand why a judgment layer is necessary

## What Is Out of Scope for Early Contributions

- New coding agent features or wrappers around existing models
- Large new CLI subcommands that turn this into a general-purpose agent harness
- Prompt engineering collections without accompanying judgment structure

The intellectual asset is the judgment framework, not another coding assistant.

## Development Process

1. Fork and create a topic branch.
2. Make changes.
3. Add or update judgment cases, schemas, or examples as appropriate.
4. Run the local lint and schema tests: `python tests/test_schemas.py` and the commands in `.github/workflows/lint.yml`.
5. Submit a pull request with a clear description of the judgment insight or protocol change.

For large changes, open an issue first with a short problem statement and proposed judgment rule.

## Adding a Judgment Case

See the format in `docs/CASEBOOK.md`. Each case must answer:

- What the agent did
- Why it looked correct locally
- Why it actually failed at the level of human intent or system integrity
- The specific judgment rule that would have caught it
- The quality gate or redaction rule it maps to
- A minimal failure memory entry

Vague "the model was bad" cases will be closed. We are collecting failure modes that survive good models when judgment scaffolding is absent.

## Code Style

The demonstration CLI (`cli/judgmentops.py`) is intentionally minimal. Keep it readable, dependency-free where possible, and focused on demonstrating the protocol rather than becoming a full product.

Python code should pass `python -m py_compile`.

## License

By contributing, you agree that your contributions will be licensed under the Apache-2.0 License.

## Questions

Open an issue with the label `question` or `discussion`. We are particularly interested in real failure stories from OSS maintainers and teams using coding agents at scale.
