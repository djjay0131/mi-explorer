# ADR-0002: Mirror upstream ARENA's directory tree for exercise code

Status: Accepted
Date: 2026-09-22
Deciders: Jason

## Context

ARENA ships each exercise as a notebook plus a `solutions.py` and a
`tests.py`. Those files locate themselves at import time rather than by
relative path:

```python
chapter = "chapter1_transformer_interp"
section = "part1_transformer_from_scratch"
root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists())
exercises_dir = root_dir / chapter / "exercises"
sys.path.append(str(exercises_dir))
import part1_transformer_from_scratch.tests as tests
```

The preamble walks parent directories looking for one named
`chapter1_transformer_interp`, then imports the section as a package. A repo
that stores the same code under `exercises/ch1/part1/` or
`src/mi_explorer/` breaks both the parent walk and the package import.

This repo's governance delta declares a control plane (`llm/`) and a data
plane (`docs/`). Exercise code is neither, so where it goes is an open
decision rather than something the two-plane rule settles.

## Decision

Store exercise code at the upstream path, mirrored exactly:

```
chapter1_transformer_interp/exercises/part1_transformer_from_scratch/
```

Declare in the delta's §Repository Layout and in `CLAUDE.md` that this tree
is **not** a governance slot, is not control plane, and must not be
flattened, renamed or reorganized. `tests.py` is vendored from upstream and
is not modified; the operator's work goes in `answers.py` alongside it.

## Rationale

Keeping the mirror means every file pulled from upstream — now and for
chapters 1.2 through 1.5x — runs unmodified. The alternative costs a patched
path preamble in every such file, forever, and each patch is a place where a
future `git pull` of updated materials silently conflicts.

It also keeps the honesty property the delta's principles ask for: when
`tests.py` is byte-identical to upstream, "the tests pass" means the
implementation is right, not that the test was bent to fit. Patching test
files to accommodate a directory choice would quietly erode exactly the
review question this repo added.

The cost is a top-level directory whose name describes ARENA's curriculum
rather than this repo. That is a cosmetic price for a structural guarantee.

## Alternatives Considered

### Alternative 1: Flat `exercises/` + `notebooks/`

Cleaner to read and separates notebooks from modules. Rejected: breaks the
parent walk and the package import, requiring a patched preamble in every
upstream file and turning each materials update into a merge conflict.

### Alternative 2: `src/mi_explorer/` + `notebooks/`

Treat it as a normal Python package. Rejected for the same import reasons,
and because it implies reusable library code. This repo's mission
explicitly is not tooling; work that becomes tooling moves to a sibling repo
under its own ADR.

## Consequences

### Positive

- Upstream notebooks, `solutions.py` and `tests.py` run with zero edits.
- `git pull` of updated ARENA materials stays a clean fast-forward.
- "Tests pass" keeps its meaning, because tests are never locally modified.

### Negative / Tradeoffs

- A top-level directory named for ARENA's chapter scheme, not for this repo.
- Later chapters add sibling top-level directories (`chapter0_fundamentals/`,
  `chapter2_rl/`), so the root will accumulate curriculum-shaped folders.

### Risks

- Someone "tidying" the tree breaks every exercise at once. Mitigated by the
  explicit prohibition in `CLAUDE.md` and by this ADR.

## Impacted Areas

- [ ] Product
- [ ] Domain model
- [ ] Data architecture
- [ ] AI architecture
- [ ] Domain-specific systems (see governance delta)
- [ ] Integrations
- [ ] UX
- [ ] Security/privacy
- [x] Implementation
- [x] Documentation

## Related Documents

- `llm/governance/governance-delta.md` §Repository Layout
- `CLAUDE.md` §Exercise code is not a governance slot
- Upstream: `ARENA-education/ARENA_materials`

## Related Issues / PRs

- The establish PR that introduces this ADR.

## Supersedes

None.

## Superseded By

None.
