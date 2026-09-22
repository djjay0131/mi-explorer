# Active Context

*Stub — seeded by `/governance:establish` 2026-09-22. Populate properly via
Constellize `memory:establish`.*

Holds: what is being worked on right now, and why.

## Now

Repository onboarding. Governance adopted 2026-09-22 (agentic-governance
v0.9, delta at `llm/governance/governance-delta.md`, ADR-0001). ARC
environment built and verified (ADR-0003).

## Next

ARENA Chapter 1.1 — vendor the exercises into
`chapter1_transformer_interp/exercises/part1_transformer_from_scratch/`
(ADR-0002) and start at `LayerNorm`. Roadmap:
`llm/plans/arena-progression.md`.

## Watch out for

- `ssh falcon1` needs `SSH_AUTH_SOCK=/home/djjay/.ssh/agent.sock`, or it
  fails with a misleading `Permission denied (publickey)`.
- Do not submit to a V100 partition (ADR-0003).
