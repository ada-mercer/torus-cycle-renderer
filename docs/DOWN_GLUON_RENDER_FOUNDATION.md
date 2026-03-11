# Down-Quark + Gluon Render Foundation (Prototype)

This file records implementation foundations for two new prototype branches:
- down-quark (`DQuark`),
- gluon (`Gluon`).

## 1) Scope

Both are **prototype branches** and now exposed in CLI (`--particle dquark`, `--particle gluon`).

They remain exploratory in theory status even though they are render-selectable.

## 2) Down-quark prototype

Code:
- shared quark layer: `src/torus_cycle_renderer/particles/quark.py`
- concrete down branch: `src/torus_cycle_renderer/particles/d_quark.py`

Theory:
- `docs/theory/DOWN_QUARK_WEAK_ASSIST_DERIVATION.md`
- interpretive scaffold: `docs/NATURAL_EMERGENCE_OF_INCOMPLETE_QUARK_CYCLES.md`
- closure algebra: `docs/COMPOSITE_CLOSURE_ALGEBRA_V1.md`
- charge/chirality compatibility: `docs/CLOSURE_CHARGE_CHIRALITY_COMPATIBILITY_V1.md`
- effective-charge ansatz: `docs/EFFECTIVE_CHARGE_PROJECTION_ANSATZ_V1.md`
- toy torus projector lift: `docs/TOY_TORUS_SURFACE_PROJECTOR_V1.md`

Tools:
- `scripts/analyze_down_quark_resonance.py`
- `scripts/render_down_quark_prototype.py`

Interpretive layer:
- the down branch should be read as a defect-bearing isolated representative of a non-asymptotic sector,
- not as a closure-neutral asymptotic state or free isolated particle state by itself,
- current best effective-charge reading is the closure-complement projection weight `(1 - delta_d) = 1/3`, with sign carried separately by orientation branch rather than by defect class itself,
- the more refined projector-side reading uses an integrated local coherence fraction `C[Xi]` on the torus surface, with coarse-grained approximation `C[Xi] ≈ 1 - delta_d`,
- color-phase dependence should be interpreted first as changing coherence weighting or support geometry, not as replacing closure-defect or orientation roles,
- current spin-state handling should be read as an observable/probe-level handedness choice, not a complete quark-spin ontology,
- closure defect, EM sign branch, color/coherence modifier, and observable handedness should be kept conceptually separate,
- for the full derivation chain and open gaps, start with `docs/QUARK_DERIVATION_CHAIN_INDEX.md` and `docs/QUARK_GLUON_SIGN_AND_CLOSURE_INTERPRETATION.md`.
- the current closure story is now extended to the coupled-state level; see `docs/COUPLED_QUARK_GLUON_WEAK_CLOSURE_ALGEBRA.md` and `docs/GLUON_COMPENSATION_TERM_ANSATZ.md`.

## 3) Gluon prototype

Code:
- `src/torus_cycle_renderer/particles/gluon.py`

Theory:
- `docs/theory/GLUON_BRANCH_FOUNDATION.md`

Tool:
- `scripts/render_gluon_prototype.py`

Interpretive layer:
- the gluon branch is best read as an exploratory color-transport / coherence-mediating prototype,
- not yet as a closure-charge locked branch at the same derivational maturity as the up/down quark prototypes,
- `helicity` is an observable handedness / loop-orientation slot, not an EM-sign label,
- current value is mainly structural: visualizing dual-mode transport, color-phase organization, and possible coherence-reshaping behavior,
- but it now also has an explicit mathematical role in the coupled closure program: `docs/GLUON_COMPENSATION_TERM_ANSATZ.md` treats gluon/color interaction as a first reduced compensation term rather than leaving it purely symbolic,
- see `docs/QUARK_GLUON_SIGN_AND_CLOSURE_INTERPRETATION.md` for the current scope boundary.

## 4) Quick run commands

```bash
cd torus-cycle-renderer

# Down quark
PYTHONPATH=src .venv/bin/python scripts/analyze_down_quark_resonance.py
PYTHONPATH=src .venv/bin/python scripts/render_down_quark_prototype.py --mode frame --output output/dquark_proto.png

# Gluon
PYTHONPATH=src .venv/bin/python scripts/render_gluon_prototype.py --mode frame --output output/gluon_proto.png
```

## 5) Promotion gate

Promote either branch to default CLI only after:
- smooth cycle render,
- resonance/closure sanity checks pass,
- docs and equations are locked at same revision.
