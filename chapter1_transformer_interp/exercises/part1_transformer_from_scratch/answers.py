# %%
"""
ARENA 1.1 -- Transformer from Scratch.

Your implementations go here. `tests.py` and `solutions.py` alongside this
file are vendored byte-identical from upstream and must never be edited
(see chapter1_transformer_interp/README.md).

Work top to bottom. For each component: write it, run its checks, and only
then look at anything else. If you do consult `solutions.py`, label the PR
`attempt-before-solution` -- that is what the label exists for.

Each component is verified twice, which is the pattern worth internalising:
  rand_float_test / rand_int_test -- does it run and produce the right shape?
  load_gpt2_test                  -- does it reproduce the REAL GPT-2 layer?
Only the second one means your implementation is correct.
"""

import sys
from pathlib import Path

import einops
import torch as t
import torch.nn as nn
from jaxtyping import Float, Int
from torch import Tensor
from transformer_lens import HookedTransformer

# Same preamble as upstream: locate the exercises dir by walking parents for
# the chapter directory, so `import part1_transformer_from_scratch.tests`
# resolves. This is why the tree is mirrored (ADR-0002).
chapter = "chapter1_transformer_interp"
section = "part1_transformer_from_scratch"
root_dir = next(p for p in Path.cwd().parents if (p / chapter).exists())
exercises_dir = root_dir / chapter / "exercises"
if str(exercises_dir) not in sys.path:
    sys.path.append(str(exercises_dir))

import part1_transformer_from_scratch.tests as tests  # noqa: E402

device = t.device(
    "mps" if t.backends.mps.is_available() else "cuda" if t.cuda.is_available() else "cpu"
)

MAIN = __name__ == "__main__"

# %%

if MAIN:
    reference_gpt2 = HookedTransformer.from_pretrained(
        "gpt2-small",
        fold_ln=False,
        center_unembed=False,
        center_writing_weights=False,
    )
    tokens = reference_gpt2.to_tokens("The capital of France is")
    logits, cache = reference_gpt2.run_with_cache(tokens)
    print(reference_gpt2.cfg)

# %%
# --- LayerNorm ---------------------------------------------------------
# tests.rand_float_test(LayerNorm, [2, 4, 768])
# tests.test_layer_norm_epsilon(LayerNorm, cache["resid_post", 11])
# tests.load_gpt2_test(LayerNorm, reference_gpt2.ln_final, cache["resid_post", 11])

# %%
# --- Embed -------------------------------------------------------------
# tests.rand_int_test(Embed, [2, 4])
# tests.test_embed(Embed)
# tests.load_gpt2_test(Embed, reference_gpt2.embed, tokens)

# %%
# --- PosEmbed ----------------------------------------------------------
# tests.rand_int_test(PosEmbed, [2, 4])
# tests.test_pos_embed(PosEmbed)
# tests.load_gpt2_test(PosEmbed, reference_gpt2.pos_embed, tokens)

# %%
# --- Attention ---------------------------------------------------------
# The core of the chapter. Do not shortcut this one.
# tests.test_causal_mask(Attention.apply_causal_mask)
# tests.rand_float_test(Attention, [2, 4, 768])
# tests.load_gpt2_test(Attention, reference_gpt2.blocks[0].attn, cache["normalized", 0, "ln1"])

# %%
# --- MLP ---------------------------------------------------------------
# tests.rand_float_test(MLP, [2, 4, 768])
# tests.load_gpt2_test(MLP, reference_gpt2.blocks[0].mlp, cache["normalized", 0, "ln2"])

# %%
# --- TransformerBlock --------------------------------------------------
# tests.rand_float_test(TransformerBlock, [2, 4, 768])
# tests.load_gpt2_test(TransformerBlock, reference_gpt2.blocks[0], cache["resid_pre", 0])

# %%
# --- Unembed -----------------------------------------------------------
# tests.rand_float_test(Unembed, [2, 4, 768])
# tests.test_unembed(Unembed)
# tests.load_gpt2_test(Unembed, reference_gpt2.unembed, cache["ln_final.hook_normalized"])

# %%
# --- DemoTransformer ---------------------------------------------------
# tests.rand_int_test(DemoTransformer, [2, 4])
# tests.load_gpt2_test(DemoTransformer, reference_gpt2, tokens)

# %%
# --- Training ----------------------------------------------------------
# Small transformer trained on a real corpus. This is the slow part on CPU;
# run it on ARC (ADR-0003).

# %%
# --- Sampling ----------------------------------------------------------
# tests.test_sample_basic(TransformerSampler.sample_basic)
# tests.test_apply_temperature(TransformerSampler.apply_temperature)
# tests.test_apply_frequency_penalty(TransformerSampler.apply_frequency_penalty)
# tests.test_sample_top_k(TransformerSampler.sample_top_k)
# tests.test_sample_top_p(TransformerSampler.sample_top_p)
