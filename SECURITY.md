# Security Policy

## Supported Versions

This is an early prototype. Security-relevant fixes will be addressed in subsequent tagged releases.

## Reporting a Vulnerability

If you discover a vulnerability in the CLI, schemas, or examples that could lead to leakage or unsafe automation, please open a private security advisory on GitHub or email the maintainers (see repository contacts once established).

Do **not** open a public issue for security reports.

## Responsible Use Guidelines

JudgmentOps is a judgment layer, not a security product. The following rules are mandatory for anyone using or contributing to the project:

- **Never commit secrets, credentials, access keys, or tokens** to this repository or to any shared judgment case, even in redacted form if the redaction is uncertain.
- **Never submit private company data, customer data, internal project names, or proprietary code** as part of examples, cases, or test fixtures.
- **Never submit private prompts, internal agent instructions, or unreleased product plans**.
- Redaction gates provided by this project are best-effort only. They are not a substitute for human review.
- All artifacts intended for external consumption (PR descriptions, release notes, public prompts, documentation) **must** be reviewed by a human before sharing.
- The project is local-first by design. No data is sent to any remote service unless you explicitly run export or integration commands you control.

## Scope of the Redaction Gate

The redaction examples and CLI are illustrative. They detect common patterns (internal-looking paths, placeholder tokens, known private project naming conventions). They will miss sophisticated or novel leakage vectors.

Treat every output that will leave your organization as requiring the same review process you would apply to any AI-generated artifact today.

## Agentic Automation Risk

Using any judgment artifact (intent contracts, quality gates, failure memory) to drive fully autonomous long-running agents without human checkpoints increases risk. The protocol explicitly includes Human Approval Checkpoints for high-impact work. Ignoring them is a misuse of the framework.

If you find a way to make the redaction or judgment enforcement components themselves create new leakage or bypass opportunities, treat it as a security issue and report privately.
