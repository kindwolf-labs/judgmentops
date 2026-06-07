#!/usr/bin/env python3
"""
test_schemas.py — Validate that JudgmentOps JSON schemas are well-formed
and contain the expected top-level required fields.

Pure stdlib only. No external dependencies.
"""

import json
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"

EXPECTED = {
    "intent_contract.schema.json": [
        "id", "title", "source", "scope", "success_criteria", "non_goals",
        "constraints", "created_at", "author"
    ],
    "quality_gate.schema.json": [
        "id", "intent_contract_id", "criteria", "blocking"
    ],
    "failure_memory.schema.json": [
        "id", "date", "summary", "agent_behavior", "surface_symptom",
        "root_judgment_failure", "preventive_rule"
    ],
    "redaction_gate.schema.json": [
        "id", "patterns", "replacement", "applies_to"
    ],
    "judgment_case.schema.json": [
        "id", "scenario", "what_agent_did", "why_looked_correct",
        "why_actually_failed", "judgment_rule", "quality_gate",
        "failure_memory_entry"
    ],
}


def load_schema(name: str) -> dict:
    path = SCHEMAS_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Schema not found: {path}")
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def check_schema(name: str, required_fields: list) -> list[str]:
    errors: list[str] = []
    try:
        schema = load_schema(name)
    except Exception as e:
        errors.append(f"{name}: failed to load or parse: {e}")
        return errors

    if not isinstance(schema, dict):
        errors.append(f"{name}: top level is not an object")
        return errors

    # Basic structural sanity
    if "$schema" not in schema:
        errors.append(f"{name}: missing $schema")
    if "title" not in schema:
        errors.append(f"{name}: missing title")

    props = schema.get("properties", {})
    if not isinstance(props, dict):
        errors.append(f"{name}: properties is not an object")
        return errors

    missing = [f for f in required_fields if f not in props]
    if missing:
        errors.append(f"{name}: missing required field definitions in properties: {missing}")

    # Check that the schema declares these as required at top level (best effort)
    declared_required = set(schema.get("required", []))
    for f in required_fields:
        if f not in declared_required:
            errors.append(f"{name}: field '{f}' is documented as required in spec but not listed in schema 'required' array")

    return errors


def main() -> int:
    all_errors: list[str] = []

    for name, fields in EXPECTED.items():
        errs = check_schema(name, fields)
        all_errors.extend(errs)
        status = "OK" if not errs else "FAIL"
        print(f"[{status}] {name}")

    if all_errors:
        print("\nErrors:")
        for e in all_errors:
            print("  -", e)
        return 1

    print("\nAll schemas validated successfully (basic structure + required fields present).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
