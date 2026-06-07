# JudgmentOps

**JudgmentOps is the control plane for what a coding agent is allowed to do, what "done" means, and what it must remember.**

It is not another coding agent. It is an open protocol for preserving human judgment across long-running agent work through versioned intent contracts, quality gates, redaction rules, and failure memory.

Coding agents can produce correct code and still complete the wrong task. They lose constraints between turns, optimize for tests instead of user outcomes, expose private context in public artifacts, and repeat failures that the organization already paid to learn from.

- Implicit requirements and boundaries are lost between turns
- "Do not touch X" constraints are silently ignored
- Tests pass while user experience and business goals do not
- Private or sensitive context leaks into external artifacts
- The same class of mistake is repeated because there is no structured memory of prior failures
- Human strategic intent is diluted across long-running, multi-agent workflows

**Generation answers "can the agent make a change?" JudgmentOps answers "is this the right change, within the right boundaries, with evidence that it is safe to ship?"**

## What JudgmentOps Provides

JudgmentOps is an open-source judgment layer for agentic coding. It converts high-level human judgment into machine-actionable artifacts that coding agents can consume and respect:

1. **Intent Contract** — Explicit scope, success criteria, non-goals, and execution boundaries derived from human input.
2. **Quality Gate** — Measurable criteria that must be satisfied before work is considered complete. Goes beyond "tests pass."
3. **Redaction Gate** — Rules and detection for preventing leakage of private locations, credentials, project names, and commentary into external outputs.
4. **Failure Memory** — Structured, queryable records of past failures, their root causes, and the judgment rules that would have prevented them.
5. **Judgment Casebook** — A growing collection of concrete evaluation scenarios with precise judgment rules extracted from them.
6. **Agent Adapter Layer** — Conventions and hooks so that existing agents (Codex, Copilot, Claude, Cursor, custom agents) can ingest contracts, gates, and memory without rewriting their core loops.

## Quick Example

Given a vague GitHub issue:

> "The login page is slow and sometimes errors on mobile."

JudgmentOps produces:

- An Intent Contract that narrows scope to measurable performance and error conditions on specific flows, declares non-goals, and sets explicit success metrics.
- A Quality Gate that requires p95 latency targets, error budget, mobile viewport testing, and human sign-off on the critical user path.
- Redaction and failure memory checks before any external delivery.

The agent is no longer free to "improve login however it sees fit."

## Repository Map

```
judgmentops/
├── README.md
├── docs/
│   ├── MANIFESTO.md
│   ├── PROTOCOL.md
│   ├── CASEBOOK.md
│   ├── OPENAI_APPLICATION.md
│   ├── GOOGLE_APPLICATION.md
│   ├── MICROSOFT_APPLICATION.md
│   ├── ONE_PAGER.md
│   ├── PITCH_EMAIL.md
│   ├── ROADMAP.md
│   └── POSITIONING.md
├── schemas/
│   ├── intent_contract.schema.json
│   ├── quality_gate.schema.json
│   ├── failure_memory.schema.json
│   ├── redaction_gate.schema.json
│   └── judgment_case.schema.json
├── examples/
│   ├── 01_issue_to_intent_contract/
│   ├── 02_pr_review_judgment_gate/
│   ├── 03_external_prompt_redaction/
│   ├── 04_failure_memory_loop/
│   └── 05_product_failure_despite_tests/
├── cli/
│   └── judgmentops.py
├── tests/
│   └── test_schemas.py
└── .github/workflows/lint.yml
```

## Status

Early public prototype. The core value is the judgment framework, casebook, and protocol — not the demonstration CLI.

## Safety and Scope

- Local-first by default. No data leaves your machine unless you explicitly export.
- Redaction is best-effort and requires human review before any external sharing.
- Never commit secrets, private company data, customer data, or internal prompts to this repository or any shared case.

See SECURITY.md for responsible use.

Contributions that improve the judgment cases, protocol precision, or evaluation harnesses are especially welcome.

## Runnable Evaluation Prototype

JudgmentOps now includes a minimal paired evaluation harness under `evals/`.

- Three concrete paired cases (vague performance task, PR review with data/audit risk, external prompt redaction).
- Each case has a raw baseline prompt and a judgmentops_prompt that includes the relevant Intent Contract, Quality Gate, Redaction Gate, and/or Failure Memory.
- `evals/run_eval.py --list` shows cases.
- `evals/run_eval.py --case <id> --baseline-output <file> --judgmentops-output <file>` validates the case and runs simple rule-based scoring on the two agent outputs (intent preservation, scope control, quality evidence, redaction safety, failure prevention, human review readiness).
- Goal: enable reproducible before/after experiments that measure whether judgment scaffolding changes agent behavior on the same task. Early, transparent, and rule-based — not a full benchmark claim yet.

See `evals/README.md` and the scoring_rubrics for details.

The Codex adapter (`adapters/codex/`) exports an active contract + gate (+ memory) as `AGENTS.md` and `CODEX_TASK.md` that can be fed directly to Codex.
