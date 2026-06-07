#!/usr/bin/env python3
"""
export_codex_task.py — Codex adapter for JudgmentOps.

Takes an Intent Contract + Quality Gate (+ optional Failure Memory) and
exports two files directly usable as Codex context:

- AGENTS.md (repo-level guidance, can be committed)
- CODEX_TASK.md (task-specific instructions for the current work)

Usage example:
  python adapters/codex/export_codex_task.py \
    --intent-contract examples/01_issue_to_intent_contract/output.intent_contract.json \
    --quality-gate examples/01_issue_to_intent_contract/output.quality_gate.json \
    --failure-memory examples/04_failure_memory_loop/output.failure_memory.json \
    --out-dir /tmp/codex-context

Pure stdlib, local only. No network.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"

def load_json(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)

def format_list(items: list) -> str:
    if not items:
        return "- (none specified)"
    return "\n".join(f"- {item}" for item in items)

def render_agents_md(contract: Dict[str, Any], gate: Dict[str, Any], memory: Optional[Dict[str, Any]] = None) -> str:
    tmpl = (TEMPLATE_DIR / "AGENTS.md.template").read_text(encoding="utf-8")

    intent_summary = f"- {contract.get('id')}: {contract.get('title')}\n  Scope: {contract.get('scope', '')[:200]}..."
    gate_summary = f"- {gate.get('id')} (for {gate.get('intent_contract_id')})\n  {len(gate.get('criteria', []))} criteria; blocking={gate.get('blocking')}"

    mem_text = ""
    if memory:
        mem_text = f"- Last relevant: {memory.get('id')}: {memory.get('summary', '')}"

    return (tmpl
            .replace("{intent_contract_summary}", intent_summary)
            .replace("{quality_gate_summary}", gate_summary)
            )

def render_codex_task(contract: Dict[str, Any], gate: Dict[str, Any], memory: Optional[Dict[str, Any]] = None, task_desc: str = "Complete the work described in the active intent contract.") -> str:
    tmpl = (TEMPLATE_DIR / "CODEX_TASK.md.template").read_text(encoding="utf-8")

    success = format_list(contract.get("success_criteria", []))
    non_goals = format_list(contract.get("non_goals", []))
    constraints = format_list(contract.get("constraints", []))

    gate_lines = []
    for c in gate.get("criteria", []):
        gate_lines.append(f"- {c.get('description')}: {c.get('pass_condition')}")
    gate_text = "\n".join(gate_lines) if gate_lines else "- (see full gate JSON)"

    mem_text = "(none provided for this task)"
    if memory:
        mem_text = f"{memory.get('id')}: {memory.get('summary')}\nPreventive rule: {memory.get('preventive_rule', '')}"

    return (tmpl
            .replace("{task_description}", task_desc)
            .replace("{intent_id}", contract.get("id", "unknown"))
            .replace("{scope}", contract.get("scope", ""))
            .replace("{success_criteria}", success)
            .replace("{non_goals}", non_goals)
            .replace("{constraints}", constraints)
            .replace("{gate_criteria}", gate_text)
            .replace("{failure_memory}", mem_text)
            )

def main(argv: Optional[list] = None) -> int:
    parser = argparse.ArgumentParser(description="Export JudgmentOps artifacts as Codex-ready files")
    parser.add_argument("--intent-contract", required=True, help="Path to intent_contract.json")
    parser.add_argument("--quality-gate", required=True, help="Path to quality_gate.json")
    parser.add_argument("--failure-memory", help="Optional path to failure_memory.json")
    parser.add_argument("--out-dir", required=True, help="Directory to write AGENTS.md and CODEX_TASK.md")
    parser.add_argument("--task-desc", default="Complete the work described in the active intent contract while satisfying the quality gate.", help="Short task description")
    args = parser.parse_args(argv)

    ic_path = Path(args.intent_contract)
    qg_path = Path(args.quality_gate)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    contract = load_json(ic_path)
    gate = load_json(qg_path)
    memory = None
    if args.failure_memory:
        memory = load_json(Path(args.failure_memory))

    agents = render_agents_md(contract, gate, memory)
    codex_task = render_codex_task(contract, gate, memory, args.task_desc)

    (out_dir / "AGENTS.md").write_text(agents, encoding="utf-8")
    (out_dir / "CODEX_TASK.md").write_text(codex_task, encoding="utf-8")

    print(f"Wrote {out_dir / 'AGENTS.md'}")
    print(f"Wrote {out_dir / 'CODEX_TASK.md'}")
    print("These files are ready to be used as Codex repository guidance / task context.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
