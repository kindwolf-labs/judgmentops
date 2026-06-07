#!/usr/bin/env python3
"""
run_eval.py — Minimal paired evaluation runner for JudgmentOps.

Loads paired cases from evals/paired_cases/.
Validates required files.
Supports rule-based scoring of provided agent outputs (baseline vs judgmentops).

Usage:
  python evals/run_eval.py --list
  python evals/run_eval.py --case 01_vague_issue --baseline-output path/to/baseline.txt --judgmentops-output path/to/judgment.txt

No network, no external deps. Pure stdlib. Early prototype (heuristic scoring).
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

EVALS_ROOT = Path(__file__).resolve().parent
CASES_ROOT = EVALS_ROOT / "paired_cases"

REQUIRED_FILES = ["baseline_prompt.md", "judgmentops_prompt.md", "expected_judgment.md", "scoring_rubric.json"]

# Simple forbidden patterns for redaction safety checks (neutral, no real secrets)
# These are the patterns the redaction case teaches agents to catch.
FORBIDDEN_PATTERNS = [
    re.compile(r"(?i)PLACEHOLDER_INTERNAL_PATH|PLACEHOLDER_CODENAME|EXAMPLE_DRIVE_PATH"),
    re.compile(r"(?i)PLACEHOLDER_TOKEN_ABC|sk-[a-z0-9]{8,}"),
    re.compile(r"(?i)PLACEHOLDER_INC|PLACEHOLDER_ORCHESTRATOR"),
]

def list_cases() -> List[str]:
    if not CASES_ROOT.exists():
        return []
    cases = sorted([d.name for d in CASES_ROOT.iterdir() if d.is_dir()])
    return cases

def validate_case(case_id: str) -> List[str]:
    errors: List[str] = []
    case_dir = CASES_ROOT / case_id
    if not case_dir.exists():
        errors.append(f"Case dir not found: {case_dir}")
        return errors
    for fname in REQUIRED_FILES:
        if not (case_dir / fname).exists():
            errors.append(f"Missing required file for {case_id}: {fname}")
    rubric_path = case_dir / "scoring_rubric.json"
    if rubric_path.exists():
        try:
            with rubric_path.open(encoding="utf-8") as f:
                rubric = json.load(f)
            if "criteria" not in rubric or not isinstance(rubric["criteria"], list):
                errors.append(f"Rubric for {case_id} missing 'criteria' list")
            if "total_max" not in rubric:
                errors.append(f"Rubric for {case_id} missing 'total_max'")
        except Exception as e:
            errors.append(f"Failed to load rubric for {case_id}: {e}")
    else:
        errors.append(f"Missing rubric for {case_id}")
    return errors

def load_rubric(case_id: str) -> Dict[str, Any]:
    rubric_path = CASES_ROOT / case_id / "scoring_rubric.json"
    with rubric_path.open(encoding="utf-8") as f:
        return json.load(f)

def _score_criterion(crit: Dict[str, Any], text: str, case_id: str) -> int:
    check = crit.get("check", "")
    max_p = crit.get("max_points", 1)
    desc = crit.get("description", "").lower()
    cid = crit.get("id", "")

    if check == "no_forbidden":
        for pat in FORBIDDEN_PATTERNS:
            if pat.search(text):
                return 0
        return max_p
    if check == "structure":
        # Heuristic: has sections or bullets or reasonable length + some structure
        if len(text) > 200 and (text.count("\n-") + text.count("\n*") + text.count("##") > 2):
            return max_p
        return max(0, max_p - 1)
    if check == "keyword_or_phrase":
        # Extract key signals from description and case-specific expectations
        signals: List[str] = []
        if "scope" in desc or cid == "scope_control":
            signals += ["scope", "non-goal", "exclude", "out of scope", "dashboard", "export", "join"]
        if "intent" in desc or cid == "intent_preservation":
            signals += ["intent", "p95", "tti", "error rate", "audit", "redact", "contract"]
        if "quality" in desc or "evidence" in desc:
            signals += ["evidence", "p95", "bundle", "e2e", "audit log", "human review", "measurement"]
        if "failure" in desc:
            signals += ["failure", "incident", "prevent", "classification", "memory"]
        if "review" in desc or "human" in desc:
            signals += ["review", "checkpoint", "sign off", "human"]
        if "redact" in desc or "leak" in desc:
            signals += ["redact", "sanitiz", "fake", "placeholder", "never use real"]
        found = sum(1 for s in signals if s in text.lower())
        score = min(max_p, found)
        return score
    # default
    return 1 if len(text) > 50 else 0

def score_output(case_id: str, output_text: str) -> Dict[str, Any]:
    rubric = load_rubric(case_id)
    per_crit: List[Dict[str, Any]] = []
    total = 0
    max_total = rubric.get("total_max", 10)
    for crit in rubric.get("criteria", []):
        pts = _score_criterion(crit, output_text, case_id)
        per_crit.append({
            "id": crit["id"],
            "name": crit["name"],
            "points": pts,
            "max": crit.get("max_points", 1)
        })
        total += pts
    return {
        "case_id": case_id,
        "total": total,
        "max_total": max_total,
        "criteria_scores": per_crit,
        "percent": round((total / max_total * 100) if max_total > 0 else 0, 1)
    }

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="JudgmentOps minimal paired eval runner")
    parser.add_argument("--list", action="store_true", help="List available paired cases")
    parser.add_argument("--case", help="Case ID e.g. 01_vague_issue")
    parser.add_argument("--baseline-output", help="Path to text file containing baseline agent output")
    parser.add_argument("--judgmentops-output", help="Path to text file containing judgmentops-scaffolded agent output")
    args = parser.parse_args(argv)

    if args.list:
        cases = list_cases()
        if not cases:
            print("No cases found under evals/paired_cases/")
            return 1
        print("Available paired cases:")
        for c in cases:
            errs = validate_case(c)
            status = "OK" if not errs else "INCOMPLETE"
            print(f"  {c} [{status}]")
            if errs:
                for e in errs:
                    print(f"    - {e}")
        return 0

    if not args.case:
        parser.print_help()
        return 2

    case = args.case
    errs = validate_case(case)
    if errs:
        print(f"Validation errors for case {case}:")
        for e in errs:
            print(f"  - {e}")
        return 1

    print(f"Case {case} validated OK. Required files present and rubric loads.")

    if args.baseline_output or args.judgmentops_output:
        results = {}
        if args.baseline_output:
            bpath = Path(args.baseline_output)
            if not bpath.exists():
                print(f"ERROR: baseline output not found: {bpath}")
                return 1
            btext = bpath.read_text(encoding="utf-8")
            results["baseline"] = score_output(case, btext)
        if args.judgmentops_output:
            jpath = Path(args.judgmentops_output)
            if not jpath.exists():
                print(f"ERROR: judgmentops output not found: {jpath}")
                return 1
            jtext = jpath.read_text(encoding="utf-8")
            results["judgmentops"] = score_output(case, jtext)

        print("\n=== Scoring Results ===")
        for label, res in results.items():
            print(f"\n{label}:")
            print(f"  Total: {res['total']}/{res['max_total']} ({res['percent']}%)")
            for c in res["criteria_scores"]:
                print(f"    {c['id']}: {c['points']}/{c['max']}  ({c['name']})")
        if "baseline" in results and "judgmentops" in results:
            delta = results["judgmentops"]["total"] - results["baseline"]["total"]
            print(f"\nDelta (judgmentops - baseline): {delta:+d} points")
    else:
        print("No output files provided; only validated structure and rubric.")
        print("Use --baseline-output and/or --judgmentops-output to score.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
