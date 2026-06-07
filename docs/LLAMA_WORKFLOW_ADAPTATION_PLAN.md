# Llama Workflow Adaptation Plan

## Purpose

This plan describes how JudgmentOps could be evaluated with Llama-powered workflows without coupling the protocol to one model host or deployment pattern.

The first objective is not to build another general agent framework. It is to make the existing contracts, gates, memory, and review steps consumable by Llama-based execution loops and measurable through public paired fixtures.

## Llama As Execution Agent

A Llama-powered agent receives:

- The natural-language task.
- An active Execution Contract.
- Relevant memory and reusable skill instructions.
- Blocking constraints and the current Quality Gate.
- Required output and evidence formats.

The agent performs the task while recording which contract clauses and evidence requirements it addressed. The integration can be local, hosted, or embedded in an existing agent runner.

## Llama As Review Agent

A separate Llama review pass evaluates the output against the contract rather than merely rewriting it.

The review role checks:

- Goal and scope preservation.
- Constraint violations.
- Missing required outputs.
- Unsupported claims or weak evidence.
- Public/private boundary failures.
- Whether human approval is still required.

The executing and reviewing roles should use separated context where practical so the review does not simply inherit the executor's assumptions.

## Llama As Failure-Memory Summarizer

After a failed gate or human rejection, a Llama summarization step can propose a structured Failure Memory entry:

- Observed failure.
- Why the output appeared plausible.
- Root judgment failure.
- Preventive rule.
- Tags and related cases.

The proposed entry remains subject to human review before it becomes durable memory.

## Llama As Intent-Contract Generator

Given a vague goal, Llama can draft an Execution Contract containing:

- Goal and scope.
- Non-goals.
- Constraints.
- Required outputs.
- Acceptance criteria.
- Questions requiring human resolution.

The contract generator must identify ambiguity rather than silently invent business rules. A human approves the contract before execution.

## Llama For Creator Workflows

Initial public creator fixtures can include:

- Content planning memos.
- Source-backed article outlines.
- Editorial review and revision loops.
- Campaign asset checklists.
- Multilingual adaptation with audience constraints.

The protocol should preserve the creator's goal and voice requirements while separating sourced facts, inference, and generated suggestions.

## Llama For Small-Team Developer Workflows

Initial developer fixtures can include:

- Issue-to-contract conversion.
- Scoped bug fixes.
- Pull-request risk review.
- Release-note generation with compatibility checks.
- Redaction before public documentation.
- Failure-memory retrieval before shared-infrastructure changes.

The existing Codex-oriented adapter demonstrates one delivery format. A Llama adapter should remain runtime-neutral and export plain Markdown or JSON context suitable for multiple Llama runners.

## Llama-Powered Public Evaluation Fixtures

Each fixture should include:

- A harmless public task.
- A baseline prompt.
- A protocol-governed prompt or structured context package.
- A published rubric.
- Executor output.
- Reviewer output.
- Human adjudication notes.
- Failure-memory update when a gate fails.

Fixtures should avoid private data and vendor-specific hidden prompts.

## Ordinary Prompt Versus Protocol-Governed Workflow

The primary comparison uses the same model family and underlying task:

| Condition | Context |
| --- | --- |
| Ordinary prompt | Task description and normal task materials |
| Protocol-governed | Same task plus Execution Contract, memory, Quality Gate, review role, and failure rules |

Measures can include:

- Scope violations.
- Missing required outputs.
- Unsupported claims.
- Gate pass rate.
- Redaction failures.
- Review disagreement.
- Recurrence of seeded failure patterns.
- Human correction effort.

Results should report variance, limitations, and negative findings rather than presenting a single score as proof.

## Implementation Sequence

1. Define a small runtime-neutral context bundle.
2. Add one Llama execution adapter example.
3. Add one independent Llama review role.
4. Convert the creator memo example into a paired fixture.
5. Run repeated trials with fixed settings.
6. Publish outputs and human adjudication.
7. Add failure-memory retrieval to the next iteration.

## Non-Goals

- Claiming Llama endorsement or affiliation.
- Building a hosted consumer application in the first phase.
- Treating model output as final approval for high-impact work.
- Hiding evaluation prompts, scoring rules, or negative results.
