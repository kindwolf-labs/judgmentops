#!/usr/bin/env python3

import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


CLI_PATH = Path(__file__).resolve().parent.parent / "cli" / "judgmentops.py"
SPEC = importlib.util.spec_from_file_location("judgmentops_cli", CLI_PATH)
assert SPEC and SPEC.loader
CLI = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CLI)


class RedactionTests(unittest.TestCase):
    def test_report_does_not_repeat_sensitive_matches(self) -> None:
        unix_location = "/" + "Users" + "/demo/private.txt"
        drive_location = "Q:" + "\\" + "private" + "\\" + "file.txt"
        fake_token = "FAKE_TOKEN_DO_NOT_USE_12345678"
        source_text = f"{unix_location}\n{drive_location}\n{fake_token}\n"

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "input.txt"
            output = root / "output.txt"
            report = root / "report.json"
            source.write_text(source_text, encoding="utf-8")

            args = argparse.Namespace(
                input=str(source),
                output=str(output),
                report=str(report),
            )
            self.assertEqual(CLI.cmd_redact(args), 0)

            redacted = output.read_text(encoding="utf-8")
            report_data = json.loads(report.read_text(encoding="utf-8"))
            serialized_report = json.dumps(report_data)

            for sensitive_value in (unix_location, drive_location, fake_token):
                self.assertNotIn(sensitive_value, redacted)
                self.assertNotIn(sensitive_value, serialized_report)

            self.assertEqual(len(report_data["matches"]), 3)
            self.assertTrue(
                all("matched_length" in match for match in report_data["matches"])
            )
            self.assertTrue(
                all("matched_text" not in match for match in report_data["matches"])
            )


if __name__ == "__main__":
    unittest.main()
