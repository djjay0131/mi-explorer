# Governance Delta: mi-explorer

Status: Active
Last updated: 2026-09-22
Governance: agentic-governance v0.9

This file localizes the canonical governance in
[`agentic-governance`](https://github.com/djjay0131/agentic-governance) for
this project. Canonical docs defer to this file wherever project specifics
are needed. Keep it short — durable design content belongs in the
design-authority document and ADRs, not here. This file declares project
facts, never policy; changing it is semantic (L1) and it is permanently
deny-listed from the L0 fast track.

## Mission

mi-explorer is a **learning** repository: a worked path through the ARENA
mechanistic-interpretability curriculum, starting with Chapter 1.1
(transformer from scratch) and continuing into the interpretability
chapters. Its output is a trained understanding plus the artifacts that
evidence it — implementations that pass ARENA's own tests, notebooks that
record what was actually confusing, and results traceable to the job that
produced them.

It is **not** a research project, not a deliverable for an external
deadline, and not a reusable interpretability tool. Work that outgrows the
curriculum belongs in a sibling repo, recorded by an ADR here.

## Design-Authority Document

**None.** This repo has no architecture of its own to govern — the
curriculum is upstream ARENA
(`ARENA-education/ARENA_materials`, <https://learn.arena.education>), and
the exercise structure is theirs, not a design decision of this repo's.
Declaring an interim design authority here would name a document that does
not do that job.

Decisions that *are* this repo's own — where exercise code lives, what
substrate runs it, when to diverge from the curriculum — are recorded as
ADRs under the ADR directory declared below. If this repo ever grows a
design surface of its own, supersede this section by ADR and declare a spec
directory at the same time.

## Project Principles

1. **Implement before importing.** Every exercise gets an honest attempt
   before the ARENA solution is read. A solution pasted in place of an
   attempt teaches nothing and leaves no evidence of learning.
2. **A green test is not understanding.** `tests.py` passing means the
   tensor shapes and values line up. Record separately what the component
   *does* and why it is shaped that way.
3. **Look at the activations.** Before trusting an aggregate — a loss
   curve, an accuracy, an attention summary — print the raw thing on real
   examples, randomly chosen rather than cherry-picked.
4. **Record the confusion.** What was wrong on the first attempt is the
   durable artifact. Notebooks keep the wrong turn, not a cleaned-up
   narrative that implies it was obvious.
5. **Every number names its origin.** A reported result carries the Slurm
   job id and the commit that produced it, or it is not reportable.

## Domain Review Questions

Added to the canonical review checklist's Alignment Review section.

- Does the implementation pass ARENA's `tests.py` **unmodified**, or was
  the test adjusted to fit the implementation?
- Was there an honest attempt before the solution was consulted, and does
  the record show it?
- Does any reported number name the Slurm job id and commit that produced
  it?
- Were raw activations or samples inspected before an aggregate was
  trusted?
- Does this belong in a learning repo at all, or has it outgrown the
  curriculum and earned its own repo?

## Repository Layout

The paths this repo binds. The canon prescribes the shape
(agentic-governance `llm/governance/project-operating-system.md`
§Repository Areas); this block binds it here, so nothing downstream
hardcodes a path. Declare only the slots this repo uses — an absent slot
is not a violation, an undeclared path is.

- Governance directory: `llm/governance/`
- ADR directory: `llm/governance/adr/`
- Plans directory: `llm/plans/`
- Memory-bank path: `llm/memory_bank/`
- Artifacts directory (the data plane): `docs/`

Deliberately **not** declared: constitution, spec, sprints and features
directories. This repo has no role charters, no design-authority document
(see above), no sprint cadence and no feature backlog. Declaring them
would create four directories that exist only to satisfy a check.

Exercise code is **not** a governance slot. It lives at
`chapter1_transformer_interp/exercises/part1_transformer_from_scratch/`
and mirrors upstream ARENA's tree exactly, because ARENA's `solutions.py`
and `tests.py` locate themselves by walking parent directories for a
directory named `chapter1_transformer_interp` and then importing
`part1_transformer_from_scratch.tests`. Any other layout requires patching
the path preamble of every file pulled from upstream. Recorded as ADR-0002.

## Roadmap

Path: `llm/plans/arena-progression.md`

## Canon Location

Where the canonical `agentic-governance` repo lives, declared once. **This is
the only machine-specific path this repo is permitted to contain** — every
canon citation in `CLAUDE.md`, `AGENTS.md` and the check command below resolves
against it, so it changes in one place instead of a dozen.

- Canon checkout: `~/.claude/plugins/marketplaces/agentic-governance`
- Canon repository: `https://github.com/djjay0131/agentic-governance`
- Plugin registered: `repo` (`.claude/settings.json`), and additionally at
  user level (`~/.claude/settings.json`) on the machine this was onboarded
  from.

Note that this checkout is the **marketplace cache clone**, not a hand-made
checkout. `${CLAUDE_PLUGIN_ROOT}/..` — which canon's own skills assume
resolves to the canon repo root — does **not** resolve there for a
cache-installed plugin: it lands on the plugin version directory's parent,
which holds only version folders and no `VERSION` or `llm/`. Verified on
onboarding: `ls ~/.claude/plugins/marketplaces/agentic-governance/VERSION`
→ `0.9.1`.

**Deliberately not verified by `--layout`.** A canon checkout is
environment-specific: CI fetches canon into a runner temp directory and has no
such path, so asserting it would fail every CI run for a repo whose local
declaration is perfectly correct. Verify it yourself when you change it —
`ls <canon checkout>/VERSION`.

## Governance Check Command

```
node "${CLAUDE_PLUGIN_ROOT}/scripts/governance-checks.mjs" --layout
```

From a plain shell with no plugin loaded, run the same script under the
`Canon checkout` declared in §Canon Location above
(`plugin/scripts/governance-checks.mjs`).

No `--delta` or `--adr-dir` override is needed: the paths declared in
§Repository Layout are the checker's canonical defaults. No `--base`
override is needed either — this repo's default branch is `master`, and the
checker falls back through `origin/main` → `origin/master` before diffing,
emitting a `WARN: origin/main not found` line that is expected here and not
a failure.

## L0 Path Allowlist

The fenced block below is an instance of the canonical rule set in
agentic-governance `llm/governance/l0-fast-track.md` §Template Allowlist,
which also defines the block grammar and the diff shapes (§L0 Path
Allowlist). The check command parses **this** block, not that one.

```l0-allowlist
# Instance of agentic-governance `llm/governance/l0-fast-track.md`
# §Template Allowlist — the source of this rule set and its grammar.
allow llm/memory_bank/** path-only
allow llm/governance/adr/README.md index-table-rows
allow llm/governance/adr/[0-9][0-9][0-9][0-9]-*.md status-line-only
allow llm/plans/arena-progression.md checkbox-only
allow llm/** link-target-only
allow docs/** link-target-only
deny chapter1_transformer_interp/**
deny .github/**
deny llm/governance/governance-delta.md
deny llm/governance/adr/0000-template.md
```

`deny src/**` and `deny scripts/**` from the template are omitted: this repo
has neither directory. Exercise code is denied under its real path above.

## Platform Enforcement Reality

Verified 2026-09-22 against `djjay0131/mi-explorer` via `gh api`, not assumed.

- **Branch protection on `master`: available, not yet configured.**
  `gh api repos/djjay0131/mi-explorer/branches/master/protection` returns
  `404 Branch not protected` — the endpoint is reachable and the branch
  simply has no rules. This is a **public** repo on a free personal plan,
  where protection is available; contrast `mats-12-application`, where a
  private free-plan repo returns `403` and protection is genuinely
  unavailable. Do not copy that repo's conclusion here.
- **Default branch is `master`, not `main`.** Canon's branch-protection and
  check guidance is written for `main`. Every rule here binds `master`.
- **Required status checks: available** (same endpoint), pending a CI
  workflow to require.
- **Token/identity model:** all agent sessions authenticate with the
  owner's token. Chief Architect, Chief Reviewer, Repository Steward and
  Governance Auditor are procedural roles, not distinct identities. A
  "required approval" on this repo would be the owner approving the owner.
- **Hardening path:** requiring the governance-checks status check is real
  enforcement and is worth turning on. Requiring a second approving review
  is not available in substance until a second human or a dedicated machine
  account exists.

## Steward Activation Status

Status: INACTIVE

Steward merge authority ships inert (agentic-governance
`llm/governance/l0-fast-track.md` §Per-Repo Activation). To activate, record
here:

- Activation ADR: none — required before activation
- Activation PR: none — required, human-approved and human-merged

No activation is planned for this repo. It is single-operator and
low-volume; the L0 lane's value is proportional to merge traffic, and there
is not enough here to pay for the certification.

## Milestone Labels

- `ch1-transformer` — Chapter 1.1–1.2, transformer from scratch and intro
  to mech interp
- `ch1-circuits` — Chapter 1.4x, IOI and circuit analysis
- `ch1-saes` — Chapter 1.3x, SAEs and feature analysis
- `infra` — ARC environment, Slurm, tooling

## Special Labels

- `attempt-before-solution` — marks work where the ARENA solution was
  consulted; the review question above applies.
- `needs-raw-inspection` — an aggregate is reported without raw examples
  having been looked at.

## Constitution Adjustments

None. This repo declares no constitution directory; the canonical executive
charters apply unmodified.

## Related Repos

- `djjay0131/mats-12-application` — the J-Lens / MATS 12 mech-interp work
  this repo builds foundations for. Authority does not flow between them;
  mi-explorer is upstream in learning order only.
- `djjay0131/agentic-governance` — canon. This repo pins v0.9 and follows
  it; it never amends canon locally.
