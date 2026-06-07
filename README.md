# JudgmentOps

**An open-source AI Agent Operating Protocol for converting natural-language goals into auditable, repeatable, and self-improving execution workflows.**

## Why This Matters

AI models are becoming stronger, but complex work performed across many steps, tools, and review cycles remains unreliable. A model can produce a plausible result while losing the original goal, crossing a boundary, overlooking a user outcome, or repeating a failure that was already discovered.

One-off prompts are difficult to audit, repeat, improve, and transfer. Individuals, maintainers, and small teams need a practical way to turn AI from a chat tool into a governed execution system.

JudgmentOps explores that missing protocol layer. It represents goals, constraints, evidence, review, and prior lessons as explicit artifacts that humans can inspect and agents can consume.

## What This Project Is

JudgmentOps is:

- A protocol for governing long-running agentic work.
- A set of schemas for contracts, gates, and failure memory.
- A small runner and evaluation suite for repeatable before-and-after tests.
- A thin adapter for exporting protocol artifacts into agent-readable repository guidance.

JudgmentOps is not:

- A chatbot.
- A conventional SaaS application.
- A blockchain smart contract.
- A replacement for an AI coding agent.
- Merely a prompt library.

It sits around an agent's execution loop and makes the human goal, operating boundaries, acceptance evidence, and learned failure rules explicit.

## What Problems It Addresses

| Problem | Protocol response |
| --- | --- |
| Prompt drift | Execution contracts that preserve goal, scope, and non-goals |
| Context loss | A memory layer for durable project and task context |
| Inconsistent outputs | Quality gates with observable acceptance evidence |
| Single-agent blind spots | Multi-agent or independent review checkpoints |
| Repeated failures | Failure memory that turns defects into preventive rules |
| Private data leakage risk | Public/private boundary rules and redaction gates |
| Non-reproducible work | Structured task specifications and acceptance gates |

## Core Concepts

### Execution Contract

A versioned statement of the goal, scope, constraints, non-goals, required outputs, and definition of success for a unit of work. In the current protocol, the Intent Contract is the primary execution contract.

### Memory Layer

Durable context that should survive a single chat session, such as project rules, prior decisions, known risks, and relevant failure history.

### Skill Layer

Reusable procedures for recurring work. A skill defines how an agent should perform a task without hiding the governing goal or acceptance criteria.

### Quality Gate

A blocking checklist of evidence required before work is accepted. Tests can be part of a gate, but product behavior, reviewability, safety, and human approval may also be required.

### Multi-Agent Review

An independent review step performed by another agent configuration or review pass. Its purpose is to expose assumptions and failure modes that the executing agent may have missed.

### Failure Memory

A structured record of what failed, why local behavior appeared reasonable, and which rule or check should prevent recurrence.

### Public/Private Boundary

Explicit rules for what may cross a trust boundary. Redaction gates inspect candidate public artifacts for private locations, credentials, project identifiers, and process commentary.

### Human Judgment Layer

The set of goals, constraints, exceptions, quality definitions, and prior lessons that determine whether an output is correct for the real situation, not merely plausible in isolation.

## Example Use Cases

- **Long-form writing workflow:** preserve audience, thesis, evidence requirements, review stages, and revision history.
- **Game prototype development and review:** define the playable goal, performance boundaries, review checkpoints, and acceptance evidence.
- **Business analysis report generation:** require source quality, assumptions, counterarguments, and executive-review criteria.
- **Open-source project preparation:** coordinate documentation, licensing, privacy review, tests, and release readiness.
- **AI news-to-article workflow:** separate source collection, verification, drafting, editorial review, and publication boundaries.
- **Local model or external agent evaluation:** run the same task with and without protocol artifacts and compare observable outcomes.

## Example Workflow

1. A human states a goal.
2. The system converts it into a TaskSpec or Execution Contract.
3. An agent executes under the declared constraints.
4. A Quality Gate reviews the output and required evidence.
5. Failure Memory records defects and the rules that would prevent them.
6. The next run retrieves those lessons and improves from prior results.

A minimal public example is available in [`examples/simple_task_contract.md`](examples/simple_task_contract.md).

## Why This Is Different From Prompt Engineering

Prompt engineering improves an individual interaction. JudgmentOps focuses on persistent work systems: memory, auditability, governance, review, failure learning, and repeatability.

The unit of value is not a single prompt. It is a repeatable execution loop whose inputs, boundaries, evidence, and lessons can be inspected and improved over time.

## What Reviewers Can Inspect

- [`docs/PROTOCOL.md`](docs/PROTOCOL.md): the protocol elements and their fields.
- [`schemas/`](schemas/): machine-readable contracts for core artifacts.
- [`docs/CASEBOOK.md`](docs/CASEBOOK.md): 20 concrete judgment-failure scenarios.
- [`evals/`](evals/): three paired evaluation fixtures and a transparent scoring runner.
- [`adapters/codex/`](adapters/codex/): a thin adapter that exports active contracts and gates as repository guidance.
- [`examples/`](examples/): worked protocol artifacts and a minimal task contract.
- [`docs/REVIEWER_BRIEF.md`](docs/REVIEWER_BRIEF.md): a one-page, forwardable project brief.

## Try The Current Prototype

List the paired evaluation cases:

```bash
python evals/run_eval.py --list
```

Run the test suite:

```bash
python tests/test_schemas.py
python -m unittest discover -s tests -p "test_*.py"
```

Export an active contract and quality gate into agent-readable context:

```bash
python adapters/codex/export_codex_task.py \
  --intent-contract examples/01_issue_to_intent_contract/output.intent_contract.json \
  --quality-gate examples/01_issue_to_intent_contract/output.quality_gate.json \
  --failure-memory examples/04_failure_memory_loop/output.failure_memory.json \
  --out-dir ./generated-agent-context
```

All current processing is local. The prototype does not make network calls.

## Current Status

- Early-stage protocol and workflow prototype.
- Exercised across multiple task types represented by the casebook, worked examples, and paired fixtures.
- Includes schemas, a deterministic demonstration CLI, a paired evaluation runner, and an agent adapter.
- Not yet a polished end-user product or a validated reliability benchmark.
- Seeking feedback, compute/API credits, and collaboration to evaluate reliability at larger scale.

Claims should remain proportional to the evidence: the repository demonstrates a testable protocol direction, not a proven universal solution.

## Roadmap

- Cleaner CLI runner.
- More example contract templates.
- Public end-to-end demo workflows.
- Broader evaluation suite with published model runs.
- Multi-agent review harness.
- Documentation and onboarding improvements.
- Case-study reports with methods, limitations, and negative results.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for the current 30/60/90-day plan.

## For Reviewers

If you are reviewing this project for an AI, open-source, or research support program, the key question is not whether this is a finished app. The key question is whether AI work needs a protocol layer for reliable long-running execution. This repository is an early attempt to make that layer explicit, testable, and open.

Start with the [Reviewer Brief](docs/REVIEWER_BRIEF.md), then inspect the [protocol](docs/PROTOCOL.md), [paired evaluations](evals/), and [adapter](adapters/codex/).

## Safety And Scope

- Local-first by default.
- Redaction is best-effort and requires human review before external sharing.
- Do not commit credentials, customer data, proprietary code, private prompts, or unreleased plans.
- High-impact work should retain explicit human approval checkpoints.

See [`SECURITY.md`](SECURITY.md) for responsible-use guidance.

## License And Contributions

JudgmentOps is licensed under Apache-2.0. Contributions that improve protocol precision, evaluation quality, adapters, or concrete failure cases are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).
