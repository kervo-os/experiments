# H5 volume gate — counting rules

The pre-registered flywheel re-run (H5) fires when the **adopted
production workspace** (not kervo's own repo — self-dogfood is excluded
by design) accumulates:

- **≥ 10 artifact-present sessions**, and
- **≥ 10 judged write-backs**.

Both are counted mechanically from the workspace's committed ledger
(`.kervo/events/*.jsonl`) by `gate.py`, so the trigger cannot be argued
after the fact. Rules, fixed before the counts matter:

## Judged write-backs

An observation event whose `Actor` starts with `agent:` (a consumer
write-back, never a human capture) that later received a transition
event whose `Actor` starts with `human:`. The judgment direction does
not matter — deprecating a bad proposal is as much a judged write-back
as verifying a good one.

## Artifact-present sessions

The union of two signals, deduplicated:

1. **Hooked consumers** (Claude Code): distinct session refs of
   `hook:SessionStart` events. The hook fires only in initialized
   workspaces, so every such session is artifact-present by
   construction.
2. **Unhooked consumers** (Codex has no per-repo hook system): distinct
   `(actor, UTC date)` pairs over `agent:`-actor observation events. A
   write-back proves an artifact-present session happened — the agent
   followed the protocol it can only have read from the injected block.
   This undercounts (a session that wrote nothing back is invisible),
   which is the conservative direction: the gate can only fire later
   than reality, never earlier.

## Why sessions are undercounted and we accept it

Signal 2 misses silent sessions by design. The alternative — manual
session diaries — reintroduces the human bookkeeping kervo exists to
remove. A gate that errs late costs days; a gate that errs early costs
the pre-registration.

Run: `python3 gate.py <workspace-path> [<workspace-path> ...]`
