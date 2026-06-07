# Project Positioning

## What Is This?

JudgmentOps is an open-source AI Agent Operating Protocol. It converts a natural-language goal into a governed execution workflow built from explicit contracts, durable context, quality gates, review checkpoints, failure memory, and public/private boundary rules.

The protocol sits around an AI agent. The agent still performs the planning, generation, tool use, and verification. JudgmentOps defines what the work is for, what is outside scope, which constraints are binding, what evidence counts as complete, and which prior failures must not recur.

The current repository is an early implementation of that idea. It contains:

- A documented protocol.
- Machine-readable JSON schemas.
- A casebook of 20 concrete judgment failures.
- Worked examples.
- A deterministic local CLI.
- Three paired evaluation fixtures and a transparent scoring runner.
- A thin adapter that exports active contracts and gates into agent-readable repository guidance.

## Why Does It Matter?

AI systems are increasingly capable of producing useful local outputs. Longer work remains fragile because the governing human context is often implicit or scattered across chats, issues, reviews, and incident reports.

An agent can satisfy a visible request while violating the actual goal. It can change an excluded surface, pass tests while harming a user workflow, publish private context, or repeat a known failure. These are workflow and judgment-preservation problems, not only generation problems.

Individuals, open-source maintainers, and small teams need a lightweight way to make that governing layer explicit without building a complete private agent platform.

## Why Is It Not Just Prompts?

A prompt is usually one interaction. JudgmentOps treats the unit of value as a repeatable execution loop.

That loop has:

- Versioned inputs and constraints.
- Durable memory.
- Reusable skills.
- Blocking acceptance evidence.
- Independent review.
- Failure records that change future behavior.
- Explicit trust boundaries.
- A format that can be consumed by different agents.

Prompts can transport these artifacts, but they are not the artifacts themselves. The protocol can be stored, reviewed, versioned, tested, and compared independently of a single conversation.

## What Can Reviewers Inspect?

Reviewers do not need private context to evaluate the project:

1. Read `README.md` and `docs/REVIEWER_BRIEF.md`.
2. Inspect the artifact definitions in `docs/PROTOCOL.md`.
3. Review the JSON schemas under `schemas/`.
4. Read concrete failure scenarios in `docs/CASEBOOK.md`.
5. Run `python evals/run_eval.py --list`.
6. Inspect paired raw and governed tasks under `evals/paired_cases/`.
7. Run the tests.
8. Inspect how `adapters/codex/` translates contracts into agent-readable guidance.

The evidence is intentionally modest. The current runner uses transparent rules rather than claiming a definitive benchmark.

## What Happens Next?

The next phase focuses on evidence and usability:

- Cleaner CLI and contract templates.
- More representative paired evaluation cases.
- Published model runs, including negative results.
- A multi-agent review harness.
- End-to-end public workflow demonstrations.
- External integration experiments.
- Case-study reports with methods and limitations.

The project should be judged as an early, testable protocol proposal: not a finished application, and not a universal reliability claim.
