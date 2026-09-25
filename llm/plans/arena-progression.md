# ARENA Progression Roadmap

Status: Active
Last updated: 2026-09-22

The roadmap declared in `llm/governance/governance-delta.md` §Roadmap.
Checkbox state here is L0 (see the delta's allowlist); anything else on this
page is L1.

Curriculum: [ARENA](https://learn.arena.education), upstream
`ARENA-education/ARENA_materials`. Substrate: VT ARC (ADR-0003).

## Chapter 1 — Transformer Interpretability

### 1.1 Transformer from Scratch  `ch1-transformer`

- [ ] Environment verified end-to-end on ARC — **done as infra, job 593890/593891**
- [ ] Vendor `tests.py` + exercises notebook into
      `chapter1_transformer_interp/exercises/part1_transformer_from_scratch/`
- [ ] Understanding the inputs: tokenization, `to_tokens`, vocab inspection
- [ ] `LayerNorm`
- [ ] `Embed` / `PosEmbed`
- [ ] `Attention` — the core of the chapter; do not shortcut to the solution
- [ ] `MLP`
- [ ] `TransformerBlock`
- [ ] `DemoTransformer` assembled, weights loaded from reference GPT-2
- [ ] Logits match the reference model
- [ ] Training loop on a small corpus
- [ ] Sampling: greedy, top-k, top-p, beam

### 1.2 Intro to Mech Interp  `ch1-transformer`

- [ ] TransformerLens basics, `run_with_cache`
- [ ] Induction heads: detection and the induction circuit

### Later sections

- [ ] 1.4.1 Indirect Object Identification  `ch1-circuits`
- [ ] 1.3.x SAEs and feature analysis  `ch1-saes`

## Infrastructure  `infra`

- [x] ARC environment built at `/scratch/djjay/mi-explorer/` (ADR-0003)
- [x] V100 exclusion verified and recorded (ADR-0003)
- [ ] Reusable sbatch wrapper for notebook/GPU sessions
- [ ] Decide how notebook outputs get reviewed (stripped vs committed)

## Notes

Every completed item that reports a number names the Slurm job id and the
commit that produced it (delta principle 5). A checkbox is not evidence.
