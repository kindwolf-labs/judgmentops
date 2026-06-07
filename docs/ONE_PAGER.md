# JudgmentOps — One-Pager

**The missing judgment layer for Codex-era software agents.**

## The Thesis

The next bottleneck for coding agents is not generation. It is the preservation of human judgment — intent, scope, constraints, quality standards, redaction boundaries, and failure memory — across long-running, multi-turn, multi-agent software work.

Strong models still produce scope errors, leaked internals, repeated failures, and "tests green, product red" outcomes when the relevant judgment is carried only implicitly or not at all.

## What JudgmentOps Is

An open-source (Apache-2.0), model- and vendor-agnostic judgment layer that turns high-level human judgment into structured, reviewable, machine-actionable artifacts:

- **Intent Contracts** — Explicit scope, success criteria, non-goals, and constraints.
- **Quality Gates** — Measurable bars that go beyond test passage.
- **Redaction Gates** — Protection against internal leakage before external delivery.
- **Failure Memory** — Structured records of past failures plus the rules that would have prevented them.
- **Human Approval Checkpoints** — Explicit pauses for high-risk work.
- **Agent Adapter Layer** — Thin conventions so existing agents can consume the above.

## What It Is Not

- Not a coding assistant or agent framework.
- Not a prompt library.
- Not a replacement for Codex, Copilot, or any other generation-focused agent.
- Not a security product or guaranteed redaction solution.

It is scaffolding that makes those systems more reliable for the kind of work that actually ships and maintains production software.

## Current Artifacts (Early Prototype)

- Detailed protocol (PROTOCOL.md)
- 20 analyzed public judgment cases with root causes and preventive rules (CASEBOOK.md)
- Strict but simple JSON schemas for all core artifacts
- Five worked examples (vague issue → contract+gate; PR review gate; prompt redaction; failure memory; technical pass / product fail)
- Minimal local demonstration CLI (no network, pure Python)
- Application and positioning materials for labs, platforms, and grant programs
- GitHub Action skeleton for linting and schema validation

## Why It Matters

- **OSS maintainers**: Encode institutional knowledge ("we never expose X", "this module has an untested performance contract") once; agents respect it repeatedly.
- **AI labs**: Frontier models will hit the same long-chain failure classes that every large software org has already experienced. Judgment infrastructure is a first-class research and product problem.
- **Enterprise teams**: Compliance, audit, and risk regimes require explicit representation of intent and constraints. Without it, scaling agent autonomy is unsafe.
- **Platform providers**: A portable judgment substrate is a natural integration point for governance, policy, and evaluation features.

## Status and Intent

Early public prototype. The intellectual asset is the judgment framework and casebook, not the CLI. The project is deliberately narrow and designed for adoption by multiple agent implementations.

All materials are Apache-2.0. No data leaves the user's machine by default. Redaction is best-effort and always requires human review before external use.

## Contact and Next Steps

- Repository: (to be published)
- Primary value for contributors: new high-signal judgment cases, protocol precision, and evaluation harness work.
- Primary value for labs and platforms: a concrete, evaluable artifact set for the judgment preservation problem.

We are seeking feedback, adoption experiments, and collaboration on the evaluation story from teams that are already running agentic coding at non-trivial scale and duration.
