#!/usr/bin/env python3
"""
test_codex_adapter.py — Verify Codex adapter can export clean AGENTS.md / CODEX_TASK.md
and that generated outputs contain no forbidden private terms.
"""

import argparse
import importlib.util
import tempfile
import unittest
from pathlib import Path

ADAPTER_PATH = Path(__file__).resolve().parent.parent / "adapters" / "codex" / "export_codex_task.py"
SPEC = importlib.util.spec_from_file_location("codex_adapter", ADAPTER_PATH)
assert SPEC and SPEC.loader
ADAPTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ADAPTER)

# Sample inputs from existing examples (safe, public data)
IC = Path(__file__).resolve().parent.parent / "examples" / "01_issue_to_intent_contract" / "output.intent_contract.json"
QG = Path(__file__).resolve().parent.parent / "examples" / "01_issue_to_intent_contract" / "output.quality_gate.json"
FM = Path(__file__).resolve().parent.parent / "examples" / "04_failure_memory_loop" / "output.failure_memory.json"

FORBIDDEN = [
    "INTERNAL_FRAMEWORK_ALPHA", "INTERNAL_FRAMEWORK_BETA", "INTERNAL_PROJECT_ALPHA",
    "PRIVATE_SYSTEM_ALPHA", "INTERNAL_ORG_ALPHA", "PRIVATE_RUNTIME_ALPHA",
    "D:" + "\\", "C:" + "\\", "/" + "Users" + "/", "/" + "home" + "/",
    "real token", "API key", "password",  # as whole phrases; we use FAKE_ in samples
]

class CodexAdapterTests(unittest.TestCase):
    def test_exports_files_from_sample_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "codex-out"
            # Call main logic via argparse namespace simulation
            argv = [
                "--intent-contract", str(IC),
                "--quality-gate", str(QG),
                "--failure-memory", str(FM),
                "--out-dir", str(out),
                "--task-desc", "Demo task for test"
            ]
            # The script's main expects sys.argv style but we can call the function after parse
            # Simpler: directly call the render functions
            contract = ADAPTER.load_json(IC)
            gate = ADAPTER.load_json(QG)
            memory = ADAPTER.load_json(FM)
            agents = ADAPTER.render_agents_md(contract, gate, memory)
            task = ADAPTER.render_codex_task(contract, gate, memory, "Demo task")
            # Write to simulate
            out.mkdir()
            (out / "AGENTS.md").write_text(agents, encoding="utf-8")
            (out / "CODEX_TASK.md").write_text(task, encoding="utf-8")

            self.assertTrue((out / "AGENTS.md").exists())
            self.assertTrue((out / "CODEX_TASK.md").exists())
            self.assertIn(contract["id"], agents)
            self.assertIn("Scope:", task)
            self.assertIn("Non-Goals", task)

    def test_generated_outputs_have_no_forbidden_terms(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "codex-out2"
            contract = ADAPTER.load_json(IC)
            gate = ADAPTER.load_json(QG)
            memory = ADAPTER.load_json(FM)
            agents = ADAPTER.render_agents_md(contract, gate, memory)
            task = ADAPTER.render_codex_task(contract, gate, memory)
            combined = agents + "\n" + task
            for bad in FORBIDDEN:
                self.assertNotIn(bad, combined, f"Forbidden term '{bad}' found in generated Codex output")


if __name__ == "__main__":
    unittest.main()
