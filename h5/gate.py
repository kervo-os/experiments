#!/usr/bin/env python3
"""H5 volume-gate counter. Rules in GATE.md — change those first."""
import glob
import json
import os
import sys

GATE_SESSIONS = 10
GATE_JUDGED = 10


def count(workspace):
    sessions, agent_obs, judged = set(), set(), set()
    for path in sorted(glob.glob(os.path.join(workspace, ".kervo", "events", "*.jsonl"))):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            actor = str(e.get("Actor", ""))
            if e.get("Type") == "hook:SessionStart":
                sessions.add("hook:" + (e.get("Ref") or e["ID"]))
            elif e.get("Kind") == "observation" and actor.startswith("agent:"):
                agent_obs.add(e["ID"])
                sessions.add("wb:" + actor + ":" + str(e.get("At", ""))[:10])  # (actor, UTC date)
            elif e.get("Kind") == "transition" and actor.startswith("human:") and e.get("Ref") in agent_obs:
                judged.add(e["Ref"])
    return len(sessions), len(judged)


def main(paths):
    total_s = total_j = 0
    for p in paths:
        s, j = count(p)
        total_s += s
        total_j += j
        print(f"{os.path.basename(os.path.abspath(p)):24s} sessions={s:3d}  judged-writebacks={j:3d}")
    fired = total_s >= GATE_SESSIONS and total_j >= GATE_JUDGED
    print(f"{'GATE':24s} sessions={total_s}/{GATE_SESSIONS}  judged={total_j}/{GATE_JUDGED}  -> {'FIRE' if fired else 'not yet'}")
    return 0 if fired else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: gate.py <workspace-path> [...]")
    sys.exit(main(sys.argv[1:]))
