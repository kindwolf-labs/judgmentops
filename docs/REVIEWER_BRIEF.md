# JudgmentOps Reviewer Brief

## 30-Second Summary

JudgmentOps is an open-source AI Agent Operating Protocol for converting natural-language goals into auditable, repeatable, and self-improving execution workflows.

It does not replace an AI agent. It supplies the execution contract, persistent context, acceptance evidence, review checkpoints, public/private boundaries, and failure lessons that help an agent remain aligned across long-running work.

## The Problem

Strong models can produce locally plausible outputs while completing the wrong task. Goals drift, constraints disappear between sessions, tests substitute for user outcomes, sensitive context crosses boundaries, and prior failures are repeated.

One-off prompts do not provide a durable system for governing this work. They are difficult to inspect, transfer, compare, and improve.

## The Proposed Protocol

JudgmentOps makes the governing layer explicit:

- **Execution Contracts** preserve the goal, scope, non-goals, and hard constraints.
- **Memory and Skill Layers** carry durable context and reusable procedures.
- **Quality Gates** define the evidence required before acceptance.
- **Multi-Agent Review** introduces independent review for blind spots.
- **Failure Memory** converts defects into preventive rules.
- **Public/Private Boundaries** protect artifacts before external delivery.

The repository includes JSON schemas, a 20-case casebook, worked examples, a local CLI, three paired evaluation fixtures, and a thin agent adapter.

## Why Now

Model capability is improving faster than the reliability of long-running AI-assisted work. As agents take on larger tasks, the bottleneck shifts from producing an answer to preserving the reason, boundaries, and quality standard behind the work.

This is especially important for open-source maintainers and small teams that need reliable workflows without building a private agent platform.

## Why This Is Useful To AI Companies

JudgmentOps provides:

- A public vocabulary for project-owned judgment artifacts.
- Concrete failure scenarios beyond code-generation correctness.
- A paired evaluation format for comparing raw tasks with governed tasks.
- A portable integration surface for repository guidance, hooks, and agent memory.
- Open evidence about where structured workflow governance helps and where it does not.

## What Support Would Enable

Support would fund repeated agent runs, paired evaluations, failure analysis, improved scoring, adapter development, public documentation, and reproducible case reports. Results, including negative or inconclusive findings, would remain public.

## What Success Would Look Like In Three Months

- A cleaner runner and broader public evaluation suite.
- Published paired results across representative maintenance workflows.
- A multi-agent review prototype.
- More contract templates and end-to-end examples.
- At least one documented external integration experiment.
- A public report describing methods, limitations, results, and next questions.
