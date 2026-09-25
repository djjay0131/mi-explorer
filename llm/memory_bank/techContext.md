# Tech Context

*Stub — seeded by `/governance:establish` 2026-09-22. Populate properly via
Constellize `memory:establish`.*

Holds: substrate, environment, and the traps in them. Decisions live in
ADR-0003, not here; this file is the operational detail.

## Where work runs

```
agents4research (Ubuntu VM, inside VT network — no GPU)
  └─ ssh falcon1.arc.vt.edu           ARC login node; has outbound network
       └─ sbatch / salloc             GPU compute node
```

`ssh falcon1` requires the agent socket — the key is passphrase-protected:

```bash
export SSH_AUTH_SOCK=/home/djjay/.ssh/agent.sock
```

Without it: `Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password)`.

## Environment

`/scratch/djjay/mi-explorer/` — `venv/`, `ARENA_materials/`, `hf-cache/`,
`logs/`. Python 3.12.3 via `module load Python/3.12.3-GCCcore-13.3.0`.

| Package | Version | Note |
|---|---|---|
| torch | 2.14.0+cu130 | no CC 7.0 kernels — see GPUs below |
| transformers | 4.57.6 | ARENA pins `>=4.51,<5` |
| transformer_lens | 2.18.0 | ARENA pins `>=2.16.1,<3` |
| einops / jaxtyping / datasets | 0.8.2 / 0.3.11 / 5.0.1 | |

`transformer_lens` exposes **no `__version__`**; use
`importlib.metadata.version("transformer_lens")`.

Jobs run offline: `HF_HOME=/scratch/djjay/mi-explorer/hf-cache` and
`HF_HUB_OFFLINE=1`. The cache is populated from the **login** node, which has
network; compute-node network access is never assumed.

## GPUs

Slurm account `agents4research`. **Never submit to a V100 partition** — the
torch build has no CC 7.0 kernels and the job dies mid-forward-pass with
`CUDA error: no kernel image is available for execution on the device`
(ADR-0003, job 593869).

Use `a30_normal_q` by default. Also supported: `t4`, `l40s`, TinkerCliffs
`a100`/`h200`, Owl `b200`. gpt2-small peaks at 0.77 GB, so an A30's 24 GB is
ample.

## Do not reuse

`/scratch/djjay/mats12/venv` carries `transformers 5.16.1`, which breaks
TransformerLens 2.x at `HookedTransformer.from_pretrained`.
