#!/usr/bin/env python3
"""
test_evals.py — Verify paired evaluation case structure and rubric loading.
"""

import json
import unittest
from pathlib import Path

EVALS_ROOT = Path(__file__).resolve().parent.parent / "evals"
CASES_ROOT = EVALS_ROOT / "paired_cases"
REQUIRED = ["baseline_prompt.md", "judgmentops_prompt.md", "expected_judgment.md", "scoring_rubric.json"]


class EvalsStructureTests(unittest.TestCase):
    def test_all_cases_have_required_files(self) -> None:
        self.assertTrue(CASES_ROOT.exists(), "evals/paired_cases dir must exist")
        cases = [d.name for d in CASES_ROOT.iterdir() if d.is_dir()]
        self.assertGreaterEqual(len(cases), 3, "At least the 3 required paired cases")
        for case in cases:
            case_dir = CASES_ROOT / case
            for fname in REQUIRED:
                p = case_dir / fname
                self.assertTrue(p.exists(), f"Missing {fname} in case {case}")
                if fname.endswith(".json"):
                    with p.open(encoding="utf-8") as f:
                        data = json.load(f)
                    self.assertIn("criteria", data, f"Rubric {case} must have criteria")
                    self.assertIn("total_max", data, f"Rubric {case} must have total_max")

    def test_rubrics_have_expected_dimensions(self) -> None:
        expected_dims = {
            "intent_preservation", "scope_control", "quality_evidence",
            "redaction_safety", "failure_prevention", "human_review_readiness"
        }
        for case_dir in CASES_ROOT.iterdir():
            if not case_dir.is_dir():
                continue
            rubric = json.loads((case_dir / "scoring_rubric.json").read_text(encoding="utf-8"))
            ids = {c["id"] for c in rubric.get("criteria", [])}
            self.assertTrue(expected_dims.issubset(ids), f"Case {case_dir.name} rubric missing some required dimensions: {expected_dims - ids}")


if __name__ == "__main__":
    unittest.main()
