# JudgmentOps Manifesto

## Correct Code Can Still Be the Wrong Change

Coding agents are already good enough to make the next bottleneck visible. They can write a plausible patch, run tests, and explain the diff. Yet a locally correct patch can still violate the reason the work exists:

- An agent implements a feature that matches the literal request but violates an unstated constraint that every senior engineer on the project treats as obvious.
- A fix passes the test suite the agent was shown, but regresses a user flow the test suite never covered because the coverage gap itself was a human judgment.
- A pull request description accurately summarizes the diff while completely missing the architectural risk that the change introduced.
- A release note is generated from commits and omits a breaking change because the breaking nature of the change was never encoded anywhere the agent could read.

The failure is not always in generation. It is often in what the work failed to preserve.

## Judgment Is What Must Survive

Software work over time is a long chain of decisions under partial information. Human judgment holds that chain together:

- Intent is translated into scope and non-goals.
- Constraints (security, performance, maintainability, legal, brand) are applied as filters.
- Quality is defined not only as "correctness" but as fitness for a specific set of users and business outcomes.
- Past failures are remembered in a form that prevents repetition.
- External communication is filtered so that internal state does not leak.

When this judgment exists only in a maintainer's head, an old incident report, or a review comment, every handoff can erase part of it. Longer context can retain more text; it does not decide which sentences are binding, which exceptions expired, or which past failure must become a rule.

A usable system needs mechanisms for:
- Making high-level human constraints explicit and machine-checkable.
- Detecting when a locally successful step violates a global invariant.
- Recording the *reason* a previous attempt failed in a way that subsequent attempts can use without re-deriving it from raw history.
- Enforcing redaction and audience boundaries on everything that will leave the organization.

## Preserve The Reason, Not Just The Request

A request says what to do next. Judgment explains why, where the boundary lies, and what evidence would make the result trustworthy.

A judgment layer sits above the coding agent and supplies:

- Explicit contracts derived from human input.
- Gates that must be satisfied, not merely suggested.
- Structured memory of prior failures and the rules that would have prevented them.
- Redaction rules that operate before any content crosses trust boundaries.
- Checkpoints where human judgment is required because automation risk exceeds acceptable threshold.

The separation matters. Project judgment should belong to the repository and its maintainers, then flow through the instruction, hook, and memory surfaces of whichever agent performs the work.

## Who This Matters For

**OSS maintainers** maintain institutional knowledge that is rarely written down at the granularity agents require. A judgment layer lets them encode "we never do X in public APIs" and "this module has a hidden performance contract" once, then have agents respect it repeatedly.

**AI labs** need evaluations that distinguish a correct patch from a correct project outcome. Judgment artifacts make that distinction testable.

**Enterprise software teams** need durable records of intent, constraints, approval, and evidence. Agent autonomy without those records is difficult to review or audit.

**Teams using long-running agents** need a way to keep strategic constraints alive after work is decomposed across turns and tools.

## The Project

JudgmentOps exists to make the judgment layer concrete, evaluable, and adoptable. It provides:

- A protocol for expressing intent, constraints, quality, redaction, and failure memory.
- A growing casebook of concrete failure scenarios that test each element of the protocol.
- Schemas that are strict enough to be useful to agents and simple enough to be authored and reviewed by humans.
- Minimal demonstration tooling.
- Application and integration materials so that the ideas can be evaluated by the teams that actually ship long-running software work.

Generation still matters. But when a system can already produce the patch, the scarce capability is preserving the reason the patch should exist.

The work is early. The cases are incomplete. The protocol will change. The value is in treating judgment preservation as a distinct engineering problem rather than hoping that bigger models and longer contexts will eventually make it disappear.
