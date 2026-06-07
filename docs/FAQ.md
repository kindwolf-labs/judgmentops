# Frequently Asked Questions

## Is This Just A Prompt Library?

No. Prompts may carry some task context, but JudgmentOps defines persistent artifacts around the execution loop: contracts, memory, quality gates, review checkpoints, redaction rules, and failure learning. The goal is to make work repeatable and auditable across sessions and agents.

## Is This A Chatbot?

No. JudgmentOps does not provide a conversational assistant or generate answers by itself. It supplies governance artifacts that an AI agent or human-led workflow can consume.

## Is This A Smart Contract?

No. “Contract” means an explicit agreement about goal, scope, constraints, outputs, and acceptance evidence. It is not a blockchain or financial contract.

## Is This A Finished Product?

No. It is an early protocol and workflow prototype. The repository contains working schemas, examples, a local CLI, paired evaluation fixtures, tests, and a thin adapter, but it is not yet a polished end-user application or a validated benchmark.

## Who Is This For?

- Open-source maintainers using coding agents for larger changes.
- Individuals and small teams building repeatable AI-assisted workflows.
- Agent-platform teams exploring durable project guidance and review.
- Researchers evaluating failures beyond local output correctness.
- Contributors interested in workflow governance, redaction, and failure learning.

## Why Does This Matter To AI Companies?

As agents handle longer tasks, reliability depends on more than model capability. AI companies need ways to evaluate whether agents preserve scope, constraints, user outcomes, trust boundaries, and prior lessons. JudgmentOps offers public cases and a portable artifact format for studying that layer.

## What Is The Technical Artifact?

The current technical surface includes:

- JSON schemas in `schemas/`.
- Protocol definitions in `docs/PROTOCOL.md`.
- A 20-case failure casebook.
- A deterministic CLI in `cli/`.
- Paired evaluation fixtures and scoring in `evals/`.
- An adapter in `adapters/codex/`.
- Worked examples and automated tests.

## What Are The Next Milestones?

- Improve the runner and scoring methodology.
- Add more contract templates and end-to-end workflows.
- Publish real paired model results.
- Build a multi-agent review harness.
- Document external integration experiments.
- Publish case-study reports with limitations and negative findings.

## How Can Contributors Help?

Contributors can add concrete failure cases, improve schemas, strengthen evaluation rubrics, build adapters, document workflows, test public/private boundary rules, or contribute reproducible paired results. See `CONTRIBUTING.md`.
