# Codex Adapter for JudgmentOps

This adapter converts JudgmentOps artifacts (Intent Contract + Quality Gate + optional Failure Memory) into files that Codex (and similar agents that read repo-level instructions) can consume directly.

## What it produces

- `AGENTS.md` — Repo-level standing instructions. Commit this (or a version of it) to your repository root so that Codex and other agents see the project judgment rules on every session.
- `CODEX_TASK.md` — Task-specific context for the current piece of work. Feed this (or paste its contents) into the agent for a specific task.

## Usage

```bash
python adapters/codex/export_codex_task.py \
  --intent-contract path/to/output.intent_contract.json \
  --quality-gate path/to/output.quality_gate.json \
  --failure-memory path/to/output.failure_memory.json \
  --out-dir ./codex-context-for-this-task \
  --task-desc "Short one-liner for the agent"
```

The generated files use only the data from the provided JSONs. No network, no secrets.

## Templates

The two .template files under `templates/` control the shape. They are simple and can be edited for project conventions.

## Integration notes for Codex

- Place a (possibly hand-curated) AGENTS.md in the repo root.
- For long-running or high-stakes work, generate a fresh CODEX_TASK.md from the active contract/gate before starting the Codex session.
- Codex's native AGENTS.md / repository instructions surface is the natural delivery mechanism for the judgment layer.

This adapter is intentionally tiny. It is a translation layer, not an agent itself.
