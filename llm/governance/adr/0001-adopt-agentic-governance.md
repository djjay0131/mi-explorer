# ADR-0001: Adopt agentic-governance v0.9 with a lean layout and no design authority

Status: Accepted
Date: 2026-09-22
Deciders: Jason

## Context

mi-explorer is a new, public, single-operator repository for working
through the ARENA mechanistic-interpretability curriculum. The portfolio
standard is `agentic-governance`; siblings `agentic-kg`, `agentic-kgis`,
`agentic-kgcs` and `mats-12-application` have all adopted it.

Those repos adopted governance against real architecture or a hard external
deadline. This one has neither. Its content is exercise code whose structure
is dictated by upstream ARENA, and its "decisions" are mostly about
substrate and process, not architecture. The risk of adopting canon
unmodified is ceremony: directories that exist to satisfy a check, and a
declared design-authority document that does not actually hold design
authority.

## Decision

Adopt agentic-governance **v0.9** in full at the document layer, with three
localizations recorded in `llm/governance/governance-delta.md`:

1. **Lean layout.** Declare only `llm/governance/`, `llm/governance/adr/`,
   `llm/plans/`, `llm/memory_bank/` and `docs/`. Do **not** declare
   constitution, spec, sprints or features directories.
2. **No design-authority document.** State plainly that the curriculum is
   upstream ARENA and this repo has no architecture of its own to govern,
   rather than nominating an interim document.
3. **Steward merge authority INACTIVE**, with no activation planned.

Platform enforcement is **available** here and will be used where it is
substantive: branch protection and a required governance-checks status
check. A required second approval will not be configured, because there is
no second identity for it to mean anything.

## Rationale

`--layout` asserts that every declared path exists, so declaring a slot this
repo will not fill converts governance into busywork and trains the operator
to ignore a failing check. Verified in the checker source: `checkLayout`
iterates only `LAYOUT.declared`, and the inverse drift scan flags an
undeclared slot's canonical default only when that directory actually exists
with content. A lean declaration is therefore both legal and fully enforced.

Naming an interim design authority — the route `agentic-kg` took with
`systemPatterns.md` — is the wrong call here. That repo had a real
architecture recorded in an imperfect document. This repo has no
architecture. "None, and here is why" is the smallest true statement, and it
is revisable by ADR the moment that stops being true.

Branch protection is **available**, unlike in `mats-12-application`, whose
ADR-0001 accepted convention-only enforcement because a private free-plan
repo returns `403`. mi-explorer is public, and the same endpoint returns
`404 Branch not protected` — reachable, merely unset. Copying the sibling's
conclusion would have left real enforcement on the table.

## Alternatives Considered

### Alternative 1: Full canonical layout

Declare all nine slots for parity with `agentic-kg`. Rejected: five of them
would be empty directories created solely to pass `--layout`, and a
`.gitkeep` in each would misstate the repo's shape.

### Alternative 2: No governance at all

It is a personal learning repo; governance could be skipped. Rejected: the
domain review questions are the part that improves the work here — forcing
an honest attempt before the solution is read, and a job id next to every
number. Those cost nothing and are exactly the habits the curriculum is
meant to build.

### Alternative 3: Convention-only enforcement, copying mats-12

Rejected on verified evidence: protection is available on this repo. See
Rationale.

## Consequences

### Positive

- The review questions and the L0 allowlist do real work from day one.
- A lean layout means every declared path is a path that exists, so a
  failing `--layout` is always a real finding.
- Enforcement matches what the platform actually offers, recorded honestly.

### Negative / Tradeoffs

- Adding a design spec later requires declaring a spec directory first,
  which is an extra ADR. That friction is intentional.
- Canon's guidance and this repo's `master` default branch disagree
  throughout; every binding had to be restated for `master`.

### Risks

- A single operator approving their own PRs makes "required approval"
  theater. Mitigated by not configuring it and saying so in the delta.

## Impacted Areas

- [ ] Product
- [ ] Domain model
- [ ] Data architecture
- [ ] AI architecture
- [ ] Domain-specific systems (see governance delta)
- [ ] Integrations
- [ ] UX
- [ ] Security/privacy
- [ ] Implementation
- [x] Documentation

## Related Documents

- `llm/governance/governance-delta.md`
- agentic-governance `llm/governance/l0-fast-track.md`,
  `llm/governance/governance-levels.md`,
  `llm/governance/branch-protection.md`

## Related Issues / PRs

- The establish PR that introduces this ADR.

## Supersedes

None.

## Superseded By

None.
