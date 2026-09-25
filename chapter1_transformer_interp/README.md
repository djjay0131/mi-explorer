# chapter1_transformer_interp

A **mirror** of upstream ARENA's chapter-1 tree. Not control plane, not data
plane — see `CLAUDE.md` §Exercise code is not a governance slot, and ADR-0002
for why the structure is load-bearing rather than cosmetic.

## Provenance

Vendored from [`ARENA-education/ARENA_materials`](https://github.com/ARENA-education/ARENA_materials)
at the commit pinned in `UPSTREAM_SHA`.

`tests.py` and `solutions.py` are **byte-identical to upstream** and are never
edited here. That is what makes "the tests pass" mean the implementation is
right rather than that the test was bent to fit (delta §Project Principles 2,
and the review question that enforces it). Verify at any time:

```bash
SHA=$(cat chapter1_transformer_interp/UPSTREAM_SHA)
P=chapter1_transformer_interp/exercises/part1_transformer_from_scratch
gh api "repos/ARENA-education/ARENA_materials/contents/$P/tests.py?ref=$SHA" --jq .sha
git hash-object $P/tests.py     # must match
```

To take upstream fixes, re-vendor at a newer SHA and update `UPSTREAM_SHA` in
the same commit. Never hand-patch a vendored file.

## What is yours vs theirs

| File | Origin | Edit? |
|---|---|---|
| `1.1_..._exercises.ipynb` | upstream | only as scratch; your work belongs in `answers.py` |
| `tests.py` | upstream | **never** |
| `solutions.py` | upstream | **never** |
| `answers.py` | yours | this is the deliverable |

`solutions.py` is vendored because **`tests.py` itself imports it** —
`rand_float_test`, `rand_int_test` and `load_gpt2_test` each do
`from part1_transformer_from_scratch.solutions import Config, device`. Without
it, not a single test runs. The exercises notebook also imports it for
`TransformerSampler`. Its presence is a
build requirement, not an invitation. Principle 1 ("implement before
importing") is enforced by the `attempt-before-solution` label and the review
question, not by the file being absent.

## Running it

GPU work runs on VT ARC, never locally and never on the login node (ADR-0003).
Environment and the interactive-Jupyter recipe:
`llm/memory_bank/techContext.md`.

Do not submit to a V100 partition — the torch build ships no CC 7.0 kernels.
