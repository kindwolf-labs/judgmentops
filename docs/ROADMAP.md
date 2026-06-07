# JudgmentOps 30 / 60 / 90 Day Roadmap

This roadmap is written from the perspective of the initial public prototype. Dates are relative to the first public commit.

## 30 Days (Foundation and Visibility)

Goal: Make the judgment thesis concrete, public, and credible enough for labs, platforms, and grant programs to evaluate seriously.

- Publish the initial public repository with:
  - README, manifesto, full protocol, 20-case casebook, schemas, 5 examples, minimal CLI, tests, and GitHub Action.
  - Complete application materials (OpenAI, Google, Microsoft) plus one-pager and pitch emails.
- Seed the first 20 cases and ensure each has a crisp judgment rule and mapping to a protocol element.
- Run the initial lint and schema validation in CI.
- Write and publish a short public essay or README section that states the thesis sharply without hype.
- Submit (or prepare for submission) to OpenAI Codex OSS / Open Source Fund using the prepared materials.
- Begin light outreach to 3–5 people at AI labs or platform teams who are already thinking about long-horizon agent reliability.

Success criteria: Repo is public, cloneable, and contains everything a reviewer needs to understand the problem and the proposed solution. At least one external party has given substantive feedback on the casebook or protocol.

## 60 Days (Evaluation and Community Scaffolding)

Goal: Move from "interesting set of cases" to "evaluatable claim with harness and early data."

- Expand the public casebook to 50+ cases. Prioritize cases contributed or validated by people outside the initial authors (OSS maintainers, platform teams running agents internally).
- Build and publish a minimal open benchmark / evaluation harness:
  - Takes a judgment case + optional judgment artifacts.
  - Runs a configurable agent (initially local scripted or API-based).
  - Applies redaction, scope, and gate checks.
  - Produces scores + traces.
  - All harness code and at least one public result set are open source.
- Prototype a GitHub Action that can consume intent contracts / quality gates from a repo and post status on PRs (read-only at first).
- Publish a public essay or report that uses early harness data to illustrate the delta between "raw task" and "task + judgment artifacts" for at least one model family.
- Open the contribution process for new cases with clear acceptance criteria (see CONTRIBUTING.md).
- Begin multi-agent comparison experiments (same case run with different agent implementations or different scaffolding levels) and publish methodology + results.

Success criteria: A working, documented harness exists. At least 10 new cases have been added with external input. There is public, reproducible evidence (even if small) that the judgment layer changes outcomes on the documented failure classes.

## 90 Days (Adoption Surface and External Validation)

Goal: Create real surfaces where other projects and organizations can plug in, plus a credible public report.

- Launch a hosted (or easily self-hostable) case explorer:
  - Browse cases, filter by failure class, protocol element, or affected surface.
  - See model behavior traces (with and without scaffolding) where available.
  - Export cases in the canonical JSON schema for use in other harnesses.
- Publish a substantial public report: "Agent outputs with and without a judgment layer on 50+ real failure modes." Include methodology, limitations, and raw (anonymized) traces where possible.
- Ship at least one production-grade integration example:
  - GitHub Action that enforces quality/redaction gates on PRs for a real open source project (or a well-documented synthetic one).
  - Or a thin adapter that surfaces active contracts and failure memory inside an existing popular coding agent or IDE extension.
- Formalize the community contribution guide: how to propose a new case, how cases are reviewed, how protocol changes are proposed and versioned.
- Begin discussions with at least two organizations (one platform/AI lab, one software org or OSS project) about structured adoption experiments. Document the integration points and any required changes to the adapter layer.
- Update the 30/60/90 roadmap based on what was learned; publish the next horizon (6 months) with clearer milestones around hosted evaluation services, policy integration, and multi-vendor agent comparisons.

Success criteria: The project has visible adoption surfaces beyond the original repo (Action, adapter, explorer, third-party use of schemas/cases). There is a substantial public report that others can cite. At least one external organization is actively experimenting with the artifacts in their own workflows.

## Principles That Govern the Roadmap

- The value is in the judgment framework (cases + protocol + evaluable artifacts), not in building a large CLI or hosted agent product.
- Every major artifact (new cases, harness, integrations) must remain open and usable by multiple agent implementations.
- Evaluation work prioritizes public, reproducible, model-agnostic results over impressive internal demos.
- Scope is deliberately constrained. We will say no to many interesting ideas that would turn this into a general agent platform.

This roadmap will be updated as the project learns from real usage and from the organizations that are already paying the cost of judgment failures in production agentic work.
