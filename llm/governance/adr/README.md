# Architecture Decision Records

Decisions that shape this repository. An ADR **is** the decision, not a
report of one: if a durable choice was made and no ADR records it, the
decision is an orphan (agentic-governance
`llm/governance/architecture-governance.md` §No Orphan Decisions).

Resolve canon paths against the `Canon checkout` declared in
`llm/governance/governance-delta.md` §Canon Location.

## Index

| ADR | Title | Status | Date |
|---|---|---|---|
| [0001](0001-adopt-agentic-governance.md) | Adopt agentic-governance v0.9 with a lean layout and no design authority | Accepted | 2026-09-22 |
| [0002](0002-mirror-arena-directory-tree.md) | Mirror upstream ARENA's directory tree for exercise code | Accepted | 2026-09-22 |
| [0003](0003-arc-substrate-and-gpu-exclusions.md) | Run on VT ARC, with V100 excluded by the torch build | Accepted | 2026-09-22 |

## Lifecycle

`Proposed` → `Accepted` → (`Superseded` | `Deprecated`)

- **Proposed** — drafted, under review. Carries no authority yet.
- **Accepted** — decided. Binding until superseded.
- **Superseded** — replaced by a later ADR, which is named in
  §Superseded By. The file is never deleted; the trail is the point.
- **Deprecated** — no longer applies and nothing replaced it.

## Writing one

Copy `0000-template.md` to `NNNN-<kebab-title>.md`, using the next free
number. Fill every section; "None." is a legitimate answer, an empty
heading is not. Alternatives Considered is not optional — an ADR that
records no rejected option has not recorded a decision.

A status flip on an existing ADR, and a row added to the index table
above, are L0 under this repo's allowlist. Everything else here is L1+.
