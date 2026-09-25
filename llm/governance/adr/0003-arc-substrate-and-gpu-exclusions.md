# ADR-0003: Run on VT ARC, with V100 excluded by the torch build

Status: Accepted
Date: 2026-09-22
Deciders: Jason

## Context

The machine this repo is worked from (`agents4research`, an Ubuntu VM
inside the VT network) has **no GPU**. ARENA Chapter 1.1 is small enough to
run on CPU, but later chapters — SAEs, circuit analysis, activation caching
over real datasets — are not.

VT ARC is already provisioned for this operator under Slurm account
`agents4research`, and was the verified substrate for the `mats-12-application`
J-Lens work. The existing environment there cannot be reused: that venv
carries `transformers 5.16.1`, and ARENA pins `transformers>=4.51,<5`
alongside `transformer_lens>=2.16.1,<3`, whose API is incompatible with
transformers 5.

## Decision

Run all GPU work on **VT ARC**, from a dedicated environment at
`/scratch/djjay/mi-explorer/` (its own venv, its own HuggingFace cache, a
clone of upstream ARENA materials). Do not reuse `/scratch/djjay/mats12/venv`.

**Exclude the V100 partitions.** Default to `a30_normal_q` for interpretability
work; `t4`, `l40s`, TinkerCliffs `a100`/`h200` and Owl `b200` are also
available and supported.

Keep the local CPU path viable for Chapter 1.1 only, as a fallback.

## Rationale

PyPI's `torch 2.14.0+cu130` ships no compute-capability 7.0 kernels. A V100
job therefore survives model construction and dies at the first real matmul:

```
torch.AcceleratorError: CUDA error: no kernel image is available for
execution on the device
```

Verified directly — job 593869 on `fal132` (Tesla V100-PCIE-16GB) failed
exactly this way, after a `UserWarning` naming the supported CCs (7.5, 8.0,
8.6, 9.0, 10.0, 12.0). Job 593890 on an A30 then completed the same workload
cleanly: gpt2-small loaded offline, forward pass with cache, 208 cache
entries, 0.77 GB peak.

This exclusion is worth an ADR rather than a note because V100 is the
*attractive* wrong choice: it has the shortest queue on Falcon (4–5 idle
nodes against `t4` pending on Resources), so the natural reflex — take the
free nodes — lands precisely on the broken configuration, and the failure
appears deep in a forward pass rather than at import.

Reinstalling torch from the `cu126` index would restore V100 support but
would likely drop B200 (CC 10.0). Given A30/L40S/H200 capacity is ample and
this repo's jobs are small, that trade is not worth making.

## Alternatives Considered

### Alternative 1: Reuse the mats-12 venv

Zero setup cost and 9.5 GB of warm HF cache. Rejected: `transformers 5.16.1`
violates ARENA's pin and breaks TransformerLens 2.x at
`HookedTransformer.from_pretrained` — the first cell of exercise 1.1.

### Alternative 2: Install torch from the cu126 index to regain V100

Would make every Falcon partition usable. Rejected: buys the lowest-value
GPUs at the likely cost of B200, for a workload that fits comfortably in an
A30's 24 GB.

### Alternative 3: Run everything locally on CPU

Viable for 1.1 alone. Rejected as a standing choice: the chapters this repo
exists to reach need a GPU.

## Consequences

### Positive

- A verified, offline-capable environment: jobs run with `HF_HUB_OFFLINE=1`
  against a login-node-populated cache, so compute-node network access is
  never assumed.
- The failure mode most likely to waste an afternoon is documented before it
  is hit a second time.

### Negative / Tradeoffs

- The shortest-queue partition is off-limits, so queue waits are slightly
  worse than the cluster's best case.
- A second environment to maintain alongside mats-12's.

### Risks

- A future `pip install --upgrade torch` could silently change which GPUs
  work. Mitigated by re-running the smoke job after any torch change.
- ARC key access depends on a passphrase-protected key held by an agent;
  `ssh falcon1` fails confusingly without `SSH_AUTH_SOCK` set.

## Impacted Areas

- [ ] Product
- [ ] Domain model
- [ ] Data architecture
- [ ] AI architecture
- [ ] Domain-specific systems (see governance delta)
- [x] Integrations
- [ ] UX
- [ ] Security/privacy
- [x] Implementation
- [ ] Documentation

## Related Documents

- `llm/plans/arena-progression.md`
- `llm/memory_bank/techContext.md`

## Related Issues / PRs

- The establish PR that introduces this ADR.
- ARC evidence: Slurm jobs 593869 (V100, FAIL), 593890 (A30, PASS),
  593891 (A30, weight verification).

## Supersedes

None.

## Superseded By

None.
