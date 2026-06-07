# JudgmentOps Paired Evaluation Fixtures (Early Prototype)

This directory contains the smallest runnable evidence layer for the JudgmentOps thesis.

## Purpose

Show that providing structured judgment artifacts (Intent Contracts, Quality Gates, Redaction Gates, Failure Memory) measurably changes the behavior of a coding agent on the same underlying task.

We use *paired cases*: the identical task described once in a baseline prompt (raw/vague request) and once in a judgmentops_prompt (same task + explicit judgment scaffolding).

## Structure

```
evals/
  paired_cases/
    01_vague_issue/          # Performance task on dashboard (scope creep risk)
      baseline_prompt.md
      judgmentops_prompt.md
      expected_judgment.md
      scoring_rubric.json
    02_pr_review/            # PR review with data surface + audit risk
      ...
    03_external_redaction/   # Sanitizing internal script for public docs
      ...
  run_eval.py
  README.md
```

Each case is concrete and drawn from the existing examples/casebook patterns.

## Running

List cases:

```bash
python evals/run_eval.py --list
```

Validate + score (provide outputs from an agent run, e.g. Codex or simulated):

```bash
python evals/run_eval.py --case 01_vague_issue \
  --baseline-output /tmp/baseline.txt \
  --judgmentops-output /tmp/with-judgment.txt
```

The runner:
- Validates all required files and that the rubric JSON is loadable.
- Applies simple rule-based scoring (keyword presence for intent/scope/quality/failure signals + strict no-forbidden redaction check).
- Reports per-criterion and aggregate scores + delta.

Scoring is intentionally lightweight and transparent (no ML, no external calls). It rewards outputs that demonstrate the judgment elements were respected.

## Scoring Rubric Dimensions (all cases)

- intent_preservation
- scope_control
- quality_evidence
- redaction_safety (heavily weighted on redaction case)
- failure_prevention
- human_review_readiness

See individual scoring_rubric.json for case-specific weighting and checks.

## Status

Early prototype. The goal is to enable reproducible before/after experiments, not to publish a definitive benchmark yet. Results (including negative) from real model runs should be published alongside the fixtures and runner.

Contributions: more cases, better heuristics in the runner, or integration with actual agent harnesses are welcome.
