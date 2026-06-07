# JudgmentOps: Meta / Llama Submission Brief

## 30-Second Summary

JudgmentOps is an open-source AI Agent Operating Protocol for Llama-powered personal, creator, developer, and small-team workflows.

It does not replace Llama or another execution model. It provides the judgment layer around the model: execution contracts, durable memory, quality gates, independent review, failure learning, and public/private boundary rules. The goal is to turn capable model access into repeatable, auditable work.

## Why This Matters To Meta

Meta has publicly positioned Llama as an open model ecosystem for developers, startups, researchers, creators, and small organizations. Meta also operates products used for creation, messaging, community, and small-business interaction.

Those surfaces create an important workflow question: after people gain access to a capable model, how do they convert it into dependable recurring work without building a private agent platform?

JudgmentOps is a small, open proposal for that protocol layer.

## Why This Matters To Llama

Llama's openness makes it adaptable across local, hosted, and domain-specific deployments. That flexibility increases the value of a model-independent way to express:

- What the user is trying to achieve.
- Which constraints are binding.
- What context must persist.
- What evidence is required before acceptance.
- What prior failures should change the next run.
- What information may cross a public boundary.

A public workflow protocol can help Llama adopters compare implementations, share reusable practices, and evaluate reliability beyond one-off answer quality.

## The Problem: Open Models Need Repeatable Workflows, Not Only Access

Model access is necessary, but it does not make long-running work reliable by itself.

One-off prompts are difficult to audit, repeat, transfer, and improve. Goals drift across turns, important context disappears, outputs vary, review is inconsistent, and known failures recur. Individuals and small teams often lack the infrastructure to make these rules durable.

The next adoption layer is not only "Which model can answer?" It is also "Which workflow can preserve the goal and produce reviewable evidence?"

## The Protocol

JudgmentOps defines:

- **Execution Contracts:** goals, scope, non-goals, constraints, outputs, and acceptance criteria.
- **Memory Layers:** durable project context, decisions, and relevant prior lessons.
- **Quality Gates:** blocking evidence required before work is accepted.
- **Multi-Agent Review:** independent execution or review passes for blind spots.
- **Failure Learning:** structured failure memory and preventive rules.
- **Public/Private Boundaries:** redaction and approval rules before external delivery.

These artifacts are versionable, inspectable, and portable across model runtimes.

## Current Evidence From Software-Agent Failure Cases

The repository does not claim a proven benchmark. It currently provides:

- 20 synthetic evaluation scenarios derived from recurring software-delivery failure patterns.
- Five worked examples.
- Three paired fixtures comparing a raw task with the same task plus judgment artifacts.
- A transparent rule-based scoring runner.
- JSON schemas and automated tests.
- A thin adapter demonstrating how contracts and gates become agent-readable task context.

The cases cover scope drift, locally green tests with broken user outcomes, unsafe retries, failed rollback planning, accessibility regressions, redaction failures, multi-agent handoff gaps, and repeated incident patterns.

## How Meta / Llama Support Would Be Used

Support would be used to:

1. Run repeated paired evaluations with Llama-powered execution and review roles.
2. Add creator, developer, and small-team workflow fixtures.
3. Build a small Llama adapter and reproducible local/hosted runner examples.
4. Compare ordinary prompts with protocol-governed workflows.
5. Improve failure classification, scoring, and multi-agent review.
6. Publish prompts, fixtures, results, limitations, and negative findings.

No support would be used to imply endorsement, train a closed model, or operate private customer workflows.

## Three-Month Milestones

- Llama-oriented execution and review adapter examples.
- At least 10 additional public workflow fixtures.
- Published paired evaluation results on creator and developer tasks.
- A multi-agent review prototype.
- A failure-memory retrieval experiment.
- Two end-to-end public case studies.
- A report describing methodology, limitations, and next questions.

## Review Links

- [README](../README.md)
- [Reviewer Brief](REVIEWER_BRIEF.md)
- [Protocol](PROTOCOL.md)
- [Casebook](CASEBOOK.md)
- [One-Pager](ONE_PAGER.md)

## Public Meta Context

- [Meta Open Source AI](https://ai.meta.com/open/)
- [How companies are using Llama](https://about.fb.com/news/2024/05/how-companies-are-using-meta-llama/)
- [Open-source AI in entrepreneurship and small organizations](https://about.fb.com/news/2024/12/open-source-ai-is-leading-to-breakthroughs-in-healthcare-education-and-entrepreneurship/)

JudgmentOps is independent and is not affiliated with or endorsed by Meta.
