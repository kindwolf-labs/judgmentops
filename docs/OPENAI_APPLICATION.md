# OpenAI Codex for OSS / Open Source Fund Application

## Project Summary

JudgmentOps is an open-source control layer for long-running coding-agent work. It turns human intent into versioned contracts, executable quality and redaction gates, and reusable failure memory. Codex remains the system that plans, edits, and verifies code; JudgmentOps supplies the project-specific boundaries and evidence that help Codex keep doing the right work after the task spans many turns, files, or handoffs.

## The Problem

A coding agent can produce locally correct code while violating the real task: changing an excluded surface, weakening an undocumented guarantee, satisfying visible tests through the wrong behavior, exposing private context, or repeating a known incident pattern. These are not solved by asking for more code. They require durable project judgment that survives context compression and handoffs.

JudgmentOps makes that judgment inspectable and portable:

- Intent Contracts define scope, non-goals, success criteria, and hard constraints.
- Quality Gates define the evidence required before work is considered complete.
- Redaction Gates protect trust boundaries before artifacts are shared.
- Failure Memory turns incidents into preventive rules that future agent runs can retrieve.

The repository currently contains the protocol, five JSON schemas, 20 concrete evaluation scenarios, five worked examples, a deterministic demonstration CLI, and schema checks. It does not claim that the protocol is already proven. The next milestone is to test that claim publicly.

## Why Codex

JudgmentOps is complementary to Codex. It does not generate code, orchestrate tools, or replace an agent loop. Codex already supports durable repository guidance, lifecycle checks, and memory through native surfaces such as `AGENTS.md`, hooks, and optional memories. JudgmentOps proposes a portable schema and public evaluation corpus for the project judgment delivered through those surfaces: intent, hard constraints, acceptance evidence, and incident-derived rules.

The proposed evaluation asks a practical question: for the same Codex task, how much do explicit, structured judgment artifacts reduce globally wrong outcomes?

## How Credits Create Public Value

Credits would fund a reproducible, open evaluation rather than private product usage:

1. Convert at least 20 casebook scenarios into runnable task fixtures with deterministic checks where possible.
2. Run paired trials on Codex: raw task versus the same task with an intent contract, quality gate, and relevant failure memory.
3. Publish prompts, artifacts, scoring rules, aggregate results, and failure analysis under Apache-2.0.
4. Package the runner so OSS maintainers can add project-specific cases and reproduce the comparison.

The initial public report will measure scope violations, hard-constraint violations, acceptance-gate failures, private-context exposure, recurrence of seeded failure patterns, and human-review effort. Negative or mixed results will be published as well. No credits would be used for training, closed benchmarks, or general application traffic.

## Why Open Source

The useful output is not a private dashboard. It is a shared vocabulary, schemas, case format, runnable fixtures, and evidence about which artifacts help. OSS maintainers can encode project knowledge once and make it available to Codex and other agents without moving that knowledge into a vendor-specific prompt.

## 500-Character Version

JudgmentOps is an open control layer for long-running coding-agent work. Codex plans and edits; JudgmentOps supplies versioned intent, hard constraints, acceptance evidence, redaction rules, and prior failure lessons. Funding would turn 20 concrete scenarios into a public paired evaluation of Codex with and without these artifacts, publishing the runner, fixtures, scoring rules, results, and failures under Apache-2.0.

## 1000-Character Version

A coding agent can produce correct code and still complete the wrong task: cross an excluded boundary, weaken an undocumented guarantee, optimize for visible tests instead of the user outcome, expose private context, or repeat a known incident. JudgmentOps makes the missing project judgment explicit through versioned Intent Contracts, Quality Gates, Redaction Gates, and Failure Memory.

It is complementary to Codex, not a replacement. Codex supplies planning, editing, and verification; JudgmentOps supplies repo-owned constraints and acceptance evidence that survive long tasks and handoffs.

The repository includes a protocol, five schemas, 20 evaluation scenarios, five worked examples, a deterministic demonstration CLI, and schema checks. Credits would convert the casebook into runnable paired trials of Codex with and without judgment artifacts. The runner, fixtures, scoring rules, aggregate results, and failure analysis would be published under Apache-2.0, including negative findings.

## 2000-Character Version

Coding-agent progress is usually measured by whether a model can produce a correct change. Long-running work adds a second question: can the system preserve what the change is for, what it must not disturb, what evidence counts as done, and what the project already learned?

A model can satisfy the prompt and tests while crossing an excluded boundary, weakening an undocumented guarantee, regressing a user outcome, exposing private context, or repeating a known incident. JudgmentOps treats these as failures of preserved project judgment.

JudgmentOps is an open protocol built around four repo-owned artifacts:

- Intent Contracts: scope, non-goals, success criteria, and hard constraints.
- Quality Gates: evidence required before work is accepted.
- Redaction Gates: checks before artifacts cross a trust boundary.
- Failure Memory: incidents distilled into searchable preventive rules.

Codex remains the system that plans, edits, uses tools, and verifies code. JudgmentOps does not compete with that loop. It provides a portable schema for project judgment that can flow through Codex's native repository guidance, hooks, and memory surfaces.

The repository is an early prototype: a protocol, five schemas, 20 evaluation scenarios, five worked examples, a deterministic CLI, and schema checks. It does not yet prove that the protocol improves outcomes at scale. Producing that evidence is the proposed work.

Credits would convert at least 20 scenarios into paired evaluations: the same Codex task with raw context, then with the relevant contract, gates, and failure memory. We will publish the runner, fixtures, prompts, scoring rules, aggregate results, and analysis under Apache-2.0. Measures will include scope and constraint violations, acceptance failures, private-context exposure, repeated seeded failures, and human-review effort. Negative or inconclusive results will be included.

The public value is a reusable benchmark and evidence about when structured judgment helps Codex.

V2 adds a paired evaluation harness (`evals/`) and Codex adapter (`adapters/codex/`) so API credits can be used to generate reproducible before/after cases on the exact same tasks with and without explicit intent contracts, quality gates, redaction rules, and failure memory. The runner, fixtures, rubrics, and exported context files are all local and open.
