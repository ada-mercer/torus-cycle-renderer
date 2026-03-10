# Up-Quark Render Foundation (Prototype)

This note defines the current foundation for rendering a quark-like up branch.

## 1) Scope

This is a **prototype correspondence branch** now exposed in CLI (`--particle uquark`).

It remains exploratory in theory status even though it is render-selectable.

## 2) Theory contract

Derived in:
- `docs/theory/UP_QUARK_WEAK_ASSIST_DERIVATION.md`

Core assumptions:
- up branch carries closure-defect fraction `delta_u = 1/3`,
- weak-assisted compensation fraction `eta_w = 2/3`,
- low-order closure lock target: `(m_u, n_w) = (2, 1)`.

Interpretive layer:
- `delta_u = 1/3` should be read as a defect class in the first composite-closure algebra,
- the branch is therefore best understood as an isolated defect-bearing representative of a non-asymptotic sector rather than a free asymptotic particle state or a fully neutral closure class by itself,
- current best effective-charge reading is not raw `delta_u`, but the closure-complement projection weight `(1 - delta_u) = 2/3`, with sign carried separately by orientation branch,
- the more refined projector-side reading is via an integrated local coherence fraction `C[Xi]` on the torus surface, with coarse-grained approximation `C[Xi] ≈ 1 - delta_u`,
- color phase is currently interpreted as a modifier of coherence weighting / projected support shape, not as the primary source of EM sign,
- for the full derivation chain and open gaps, start with `docs/QUARK_DERIVATION_CHAIN_INDEX.md`.
- the current closure story is no longer just isolated defect bookkeeping; see `docs/COUPLED_QUARK_GLUON_WEAK_CLOSURE_ALGEBRA.md` for the coupled-state extension and `docs/GLUON_COMPENSATION_TERM_ANSATZ.md` for the first explicit gluon/color compensation term.

## 3) Prototype class

Implemented as:
- shared quark layer: `src/torus_cycle_renderer/particles/quark.py`
- concrete up branch: `src/torus_cycle_renderer/particles/u_quark.py`

Main state fields:
- spin state
- color phase branch
- primary/secondary resonant modes
- closure defect + weak assist phase
- transport winding + mixing + mass gap

## 4) Render helper scripts

- Resonance investigation:
  - `scripts/analyze_up_quark_resonance.py`

- Prototype rendering (direct class use):
  - `scripts/render_up_quark_prototype.py`

Example:
```bash
cd torus-cycle-renderer
PYTHONPATH=src .venv/bin/python scripts/render_up_quark_prototype.py --mode frame --output output/uquark_proto.png
PYTHONPATH=src .venv/bin/python scripts/render_up_quark_prototype.py --mode cycle --duration 1.8 --fps 14 --output output/uquark_proto_cycle.gif
```

## 5) Promotion criteria (before adding to main CLI choices)

P1. Stable visual closure across cycle samples (no jump artifacts).

P2. Weak-assisted resonance check passes with low-order lock (`2:1` preferred) in the analysis script.

P3. Parameter perturbation remains in same lock basin (robustness sanity).

P4. Documentation remains aligned with weak-channel and unified EM constraints.
