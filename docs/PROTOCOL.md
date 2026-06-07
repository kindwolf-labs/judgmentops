# JudgmentOps Protocol

This document defines the core elements of the JudgmentOps judgment layer. Each element is specified with purpose, required and optional fields, an example, and common anti-patterns.

The protocol is designed to be:

- Authorable and reviewable by humans.
- Consumable by agents as structured context or tool input.
- Minimal enough to be adopted incrementally.
- Strict enough to make drift detectable.

## 1. Intent Contract

### Purpose
Captures the human intent for a unit of work at a level of precision that survives long execution chains and handoffs between agents. It replaces vague requests and implicit assumptions with explicit scope, success criteria, and boundaries.

### Required Fields
- `id`: Unique identifier for the contract.
- `title`: Short human-readable name.
- `source`: Origin of the intent (e.g., issue URL, meeting note, Slack thread, verbal).
- `scope`: What is in scope. Must be specific enough that "is this change in scope?" is answerable.
- `success_criteria`: Measurable or observable conditions that, if met, mean the work succeeded from the human's perspective.
- `non_goals`: Explicit exclusions. What the work must not do, even if locally reasonable.
- `constraints`: High-level constraints (performance, security, compatibility, legal, brand, etc.) that are not negotiable within this contract.
- `created_at`: Timestamp.
- `author`: Human or role who established the intent.

### Optional Fields
- `priority`: Relative priority or sequencing constraints.
- `dependencies`: Other contracts or work this depends on.
- `reviewers`: Humans who must approve material changes to scope or success criteria.
- `notes`: Additional context that does not fit other fields.

### Example
```json
{
  "id": "ic-2025-06-001",
  "title": "Reduce p95 login latency on mobile web",
  "source": "https://github.com/example-org/web-app/issues/4821",
  "scope": "Login flow (credential and OAuth) on mobile viewports (iOS Safari, Chrome Android). Includes network, rendering, and client-side validation paths. Excludes account creation, credential recovery, and desktop experience.",
  "success_criteria": [
    "p95 time-to-interactive for login button click to post-auth landing < 1200ms on 4G emulated mobile, measured over 100 samples.",
    "Error rate on login attempts < 0.5% in the target flows (excluding upstream auth provider outages).",
    "No regression in accessibility (WCAG 2.2 AA) or existing e2e login tests."
  ],
  "non_goals": [
    "Changing the visual design system or component library used for login.",
    "Modifying backend auth service or token formats.",
    "Adding new login methods (passkeys, magic links)."
  ],
  "constraints": [
    "Must not increase bundle size by more than 3KB gzipped for the login chunk.",
    "Must continue to satisfy existing Content-Security-Policy and rate-limiting rules.",
    "No new third-party scripts or trackers on the login path."
  ],
  "created_at": "2025-06-07T14:22:00Z",
  "author": "product-eng-lead"
}
```

### Anti-patterns
- Writing scope as "improve login" or "make it faster."
- Omitting non_goals, allowing the agent to interpret any improvement as acceptable.
- Success criteria that are only "tests pass" or "no errors in console."
- Treating the contract as a one-time prompt rather than a persistent artifact that is re-checked on every material change.

## 2. Execution Constraints

### Purpose
A machine-checkable or human-reviewable set of hard boundaries that the agent must respect during execution. Execution Constraints are often derived from the Intent Contract but can also come from organization policy, security baselines, or prior incidents.

### Required Fields
- `id`
- `applies_to`: Scope of work or contract IDs this constraint governs.
- `rule`: Clear, actionable statement of what must or must not occur.
- `enforcement`: How the constraint is expected to be checked (static analysis, test, redaction gate, human review, etc.).
- `rationale`: Why this constraint exists (links to incidents or policy preferred).

### Optional Fields
- `severity`: Must-fix, should-fix, advisory.
- `exceptions`: Documented, approved exceptions with expiration.
- `automated_check`: Reference to a script, linter rule, or test name that can detect violation.

### Example
```json
{
  "id": "ec-2025-06-017",
  "applies_to": ["ic-2025-06-001"],
  "rule": "No new network requests to domains outside the allowlist during the login flow on mobile. Current allowlist: auth.example.com, cdn.example.com, and required static asset hosts.",
  "enforcement": "redaction_gate + runtime instrumentation + human review of diff",
  "rationale": "Past incident where a performance optimization pulled in an analytics script that violated GDPR consent on the login path (see failure memory fm-2024-11-003).",
  "severity": "must-fix",
  "automated_check": "scripts/check_login_network_allowlist.py"
}
```

### Anti-patterns
- Constraints written only in natural language comments inside code.
- "Do not do X" rules that are never checked until after the change has shipped.
- Overly broad constraints ("be careful with performance") that give the agent no actionable boundary.

## 3. Quality Gate

### Purpose
Defines the minimum bar for "done" from the perspective of human intent and system integrity. A quality gate is satisfied only when evidence (tests, measurements, reviews) demonstrates that all criteria are met. Passing unit tests is usually necessary but never sufficient.

### Required Fields
- `id`
- `intent_contract_id`: The contract this gate protects.
- `criteria`: Array of individual criteria. Each criterion has a `description`, `evidence_type` (test, metric, manual_review, static_analysis, etc.), and `pass_condition`.
- `blocking`: Whether failure of this gate blocks progression (merge, release, handoff).

### Optional Fields
- `waiver_process`: How a criterion can be temporarily waived and by whom.
- `measured_at`: When the gate was last evaluated.
- `evidence_links`: Links to artifacts (test runs, dashboards, recordings) that demonstrate passage.

### Example (abbreviated)
```json
{
  "id": "qg-2025-06-001",
  "intent_contract_id": "ic-2025-06-001",
  "criteria": [
    {
      "description": "p95 login latency target on mobile 4G",
      "evidence_type": "synthetic_monitoring",
      "pass_condition": "p95 <= 1200ms over last 100 samples in staging"
    },
    {
      "description": "No new console errors or unhandled promise rejections on login path in supported mobile browsers",
      "evidence_type": "browser_automation",
      "pass_condition": "zero occurrences in 50 login runs across target devices"
    },
    {
      "description": "Critical user path review",
      "evidence_type": "manual_review",
      "pass_condition": "Signed off by designated product reviewer with session recording attached"
    }
  ],
  "blocking": true
}
```

### Anti-patterns
- Gate that only says "all existing tests pass."
- Criteria that cannot be evidenced (e.g., "feels faster").
- Gates that are defined after the work is complete rather than before execution begins.
- Gates owned only by the agent with no human sign-off path for high-risk work.

## 4. Redaction Gate

### Purpose
Prevents internal-only information from leaving the trust boundary in agent-generated artifacts (PR descriptions, commit messages, external prompts, documentation, error reports, etc.). Redaction is applied before any content is proposed for external consumption.

### Required Fields
- `id`
- `patterns`: List of patterns (regex, literal strings, structural rules) that must trigger redaction or blocking.
- `replacement`: How matched content should be replaced (e.g., `[REDACTED_INTERNAL_PATH]`, `[REDACTED_TOKEN]`).
- `applies_to`: Categories of output (pr_description, commit_message, external_prompt, release_note, etc.).

### Optional Fields
- `report_format`: Schema for the redaction report (see examples).
- `escalation`: What to do when high-severity patterns are detected (block, require human, log).

### Example
```json
{
  "id": "rg-2025-06-003",
  "patterns": [
    { "type": "path", "match": "(?i)(/(?:Users|home)/|[A-Z]:\\\\|example-private|secret-project)" },
    { "type": "token", "match": "(?i)(FAKE_TOKEN_DO_NOT_USE_[a-z0-9]{8,}|test_[a-z0-9]{16,})" },
    { "type": "project", "match": "(?i)(secret-project-xyz|internal-codename-x|private-.*-service)" }
  ],
  "replacement": "[REDACTED]",
  "applies_to": ["pr_description", "external_prompt", "release_note", "error_report"]
}
```

See `examples/03_external_prompt_redaction/` for a full redaction report example.

### Anti-patterns
- Relying solely on the agent's "do not leak secrets" instruction.
- Redacting only after the content has already been pasted into a public PR or sent to an external model.
- Treating redaction as a one-time cleanup rather than a gate that runs on every candidate external artifact.

## 5. Failure Memory

### Purpose
A structured, searchable record of past failures that includes not only what went wrong, but the judgment rules and constraints that would have prevented the failure. Agents and humans consult failure memory before and during work to avoid repeating known classes of error.

### Required Fields
- `id`
- `date`
- `summary`: One-sentence description of the observed failure.
- `agent_behavior`: What the agent(s) did.
- `surface_symptom`: What was noticed first (tests passed, user complained, audit finding, etc.).
- `root_judgment_failure`: The missing or violated judgment element (intent, constraint, gate, redaction, memory itself).
- `preventive_rule`: The specific rule or check that would have caught this.
- `related_contracts` or `related_cases`: Links to intent contracts or casebook entries.

### Optional Fields
- `severity`
- `recurrence_count`
- `mitigation_applied`
- `tags`

### Example
```json
{
  "id": "fm-2025-05-014",
  "date": "2025-05-12",
  "summary": "Agent refactored authentication module to 'improve readability' and broke SSO for three enterprise tenants.",
  "agent_behavior": "Performed large-scale rename and extraction across auth/* without checking tenant-specific configuration or contract.",
  "surface_symptom": "Integration tests for SSO started failing in staging after merge.",
  "root_judgment_failure": "No intent contract limited scope to non-tenant code; no execution constraint prevented cross-tenant refactors without explicit approval.",
  "preventive_rule": "Any change touching auth/* or identity/* must reference an active intent contract that explicitly authorizes tenant-impacting work. Multi-tenant modules require human approval checkpoint before large refactors.",
  "related_cases": ["JC-003", "JC-007"]
}
```

### Anti-patterns
- Storing failures only as raw chat logs or commit messages.
- Recording only the symptom ("build broke") without the judgment rule.
- Never consulting prior failures before starting similar work.

## 6. Human Approval Checkpoint

### Purpose
Explicit points in the workflow where automation must pause and a designated human must review and approve before the agent continues. Checkpoints exist because some classes of risk (security policy changes, data model migrations, external contract changes, high-visibility user-facing behavior) cannot be fully reduced to automated gates in the current state of the art.

### Required Fields
- `id`
- `trigger_conditions`: When this checkpoint is required (e.g., "change set touches payment/*", "intent contract marked high_risk", "redaction_gate reports severity >= high").
- `required_approvers`: Roles or named humans.
- `evidence_required`: What the approver must see (diff, intent contract, quality gate status, redaction report, failure memory hits).
- `timeout_behavior`: What happens if no approval within time window.

### Optional Fields
- `escalation_path`
- `recorded_approval`: Link or signature once granted.

### Example
```json
{
  "id": "hac-2025-06-002",
  "trigger_conditions": [
    "intent_contract_id in high_risk_contracts",
    "diff touches (auth|billing|compliance)/*",
    "redaction_gate.escalation == 'require_human'"
  ],
  "required_approvers": ["security-lead", "product-owner-for-area"],
  "evidence_required": ["full_diff", "current_intent_contract", "quality_gate_status", "redaction_report", "failure_memory_hits"],
  "timeout_behavior": "block further agent execution on this contract until approval or explicit waiver"
}
```

### Anti-patterns
- Implicit "I'll look at the PR later" without a machine-enforced pause.
- Checkpoints that only require "LGTM" without the evidence package defined.
- Removing checkpoints over time without data showing that the risk has actually decreased.

## 7. Agent Adapter Layer

### Purpose
The conventions, file formats, and minimal hooks that allow existing coding agents to consume JudgmentOps artifacts without requiring the agent implementation itself to be rewritten.

The adapter layer is the primary integration surface. It is intentionally thin.

### Core Conventions
- Intent contracts, quality gates, redaction rules, and failure memory entries are stored as versioned JSON files (or served by a thin local service) in well-known locations or passed explicitly on the command line / context window.
- Agents are expected to read the active intent contract and quality gate at the start of a task and re-validate against them before proposing any external artifact.
- Redaction gate is invoked on any candidate output that will be shown to or sent outside the current trust boundary.
- Failure memory is consulted (via search or embedding) before significant planning or implementation steps.
- Human approval checkpoints are represented as explicit "pause and request approval" tool calls or status that the host environment can surface to a human.

### Minimal Adapter Interface (suggested)
An agent adapter should be able to:

1. Accept an intent contract ID or path and load it.
2. Accept a quality gate and report status against it.
3. Run or invoke a redaction gate on a string/blob and receive a redacted version + report.
4. Query failure memory with a description of the current task and receive relevant prior cases.
5. Surface a human approval checkpoint with the required evidence package.

### Anti-patterns
- Baking judgment logic only into one agent's private system prompt.
- Assuming that because the agent "saw the contract in the first message," it will still respect it on turn 47.
- Treating the adapter layer as a full agent framework rather than a narrow translation surface.

## Relationship Between Elements

- An Intent Contract is the root artifact for a unit of work.
- Execution Constraints and Quality Gates are derived from or attached to contracts.
- Redaction Gate and Failure Memory are cross-cutting and consulted continuously.
- Human Approval Checkpoints are inserted where residual risk after the above is still material.
- The Agent Adapter Layer makes the above consumable by concrete agent implementations.

These elements together form a judgment protocol that is independent of any single model, agent loop, or organization.
