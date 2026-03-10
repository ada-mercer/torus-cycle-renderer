# torus-cycle-renderer

Torus-based internal-state visualization toolkit with three render pipelines:
- **Matplotlib** (fast scripted GIF/MP4)
- **Plotly** (better depth handling, WebGL, PNG frame export for GIF stitching)
- **PyVista** (VTK-based offscreen rendering for stronger production-style mesh/curve output)

The project is designed so that **physics/state logic** is separate from **visual styling/rendering**.

Important repository stance:
- this repo is a **visualization / structure-testing lab**, not a full particle-state solver;
- current renders intentionally prioritize **pure resonant modes** to build intuition about internal dynamics before adding mixed, leaky, or only-partially-resonant states;
- weak-boson and quark branches should be read as **resonant probes / correspondence branches**, not as claims that those sectors are already represented here as fully closed physical states.

---

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
# optional PyVista backend:
pip install -e .[pyvista]
```

After install, use PATH-friendly commands:
- `render-frame`
- `render-cycle`

---

## Quick commands

### 1) Single frame (Matplotlib)
```bash
render-frame \
  --backend matplotlib \
  --particle electron \
  --spin-state ++ \
  --loop-anchor-mode evolving \
  --time 0.4 \
  --output output/electron_frame.png
```

### 1b) Single frame (W+ / W- / Z0 branch)
```bash
render-frame \
  --backend matplotlib \
  --particle wplus \
  --time 0.4 \
  --output output/wplus_frame.png

render-frame \
  --backend matplotlib \
  --particle wminus \
  --time 0.4 \
  --output output/wminus_frame.png

render-frame \
  --backend matplotlib \
  --particle zboson \
  --time 0.4 \
  --output output/z0_frame.png
```

### 2) Single frame (Plotly)
```bash
render-frame \
  --backend plotly \
  --particle electron \
  --spin-state ++ \
  --loop-anchor-mode evolving \
  --time 0.4 \
  --output output/electron_frame.html
```

### 3) Full cycle GIF (Matplotlib)
```bash
render-cycle \
  --backend matplotlib \
  --particle electron \
  --spin-state ++ \
  --loop-anchor-mode evolving \
  --duration 3.2 --fps 14 \
  --format gif \
  --output output/electron_cycle_matplotlib.gif
```

### 3b) Exact cycle-count animation (returns to first frame)
```bash
render-cycle \
  --backend matplotlib \
  --particle wplus \
  --cycles 2 --fps 12 \
  --format gif \
  --output output/wplus_cycles2.gif
```

### 3c) Full loop-state return (including moving anchors)
```bash
render-cycle \
  --backend matplotlib \
  --particle uquark \
  --full-loop-cycle \
  --fps 24 \
  --format gif \
  --output output/uquark_full_loop_cycle.gif
```

### 4) Full cycle GIF (Plotly)
```bash
render-cycle \
  --backend plotly \
  --particle electron \
  --spin-state ++ \
  --loop-anchor-mode evolving \
  --duration 3.2 --fps 14 \
  --format gif \
  --output output/electron_cycle_plotly.gif
```

### 4b) Parallel frame rendering (Matplotlib path)
```bash
render-cycle \
  --backend matplotlib \
  --particle electron \
  --full-loop-cycle \
  --frame-workers 4 \
  --fps 24 \
  --format gif \
  --output output/electron_parallel_fullcycle.gif
```

### 5) Geometry export bridge
```bash
render-frame --backend matplotlib --particle electron --export-geometry --output output/electron_geom_frame.png
# emits:
#   output/electron_geom_frame_geom.npz
#   output/electron_geom_frame_torus.obj
#   output/electron_geom_frame_loop.obj
```

---

## Architecture (current)

- `src/torus_cycle_renderer/particles/`
  - particle state + dynamics
  - electron single-mode resonant model
  - photon branch (pure bosic)
  - weak-boson correspondence branch (`W+`, `W-`, `Z0`)
  - spin/anchor conventions
- `src/torus_cycle_renderer/math/`
  - torus geometry and utility math
- `src/torus_cycle_renderer/rendering/`
  - shared scene-geometry sampling
  - matplotlib renderer
  - plotly renderer
  - pyvista renderer
  - animation pipeline
  - geometry export bridge
- `src/torus_cycle_renderer/cli.py`
  - PATH entrypoints (`render-frame`, `render-cycle`)

### Design rule
- Particle classes own **state/dynamics**.
- Renderer config owns **visual style** (colors, opacity, time-scale in display space).

---

## Documentation map

- `docs/INTRODUCTION.md` — implementation-accurate theory model + conventions
- `docs/MODELING_SCOPE_AND_INTERPRETATION.md` — what the renders do and do not mean; pure resonant-mode policy; weak/quark interpretation; gravity-deformation picture
- `docs/FULL_WAVE_EQUATION_DERIVATION.md` — full torus-carrier linear wave derivation in repo notation, including the shifted-operator spectrum and the exact single-mode branch form
- `docs/DERIVATION_VALIDATION_AGAINST_IMPLEMENTATION.md` — implementation audit marking what is exact, reduced, or exploratory relative to the full wave derivation
- `docs/CONSTRAINED_TORUS_TO_EM_PROJECTOR_ANSATZ.md` — constrained family of torus-to-EM projector kernels built on the torus-wave backbone
- `docs/EM_FAR_FIELD_AND_MULTIPOLE_CONSEQUENCES.md` — first far-field / multipole consequences of the constrained projector family
- `docs/EM_PROJECTOR_STATUS_MAP.md` — short exact/constrained/open status map for the EM emergence program
- `docs/TRANSPORT_CURRENT_IMAGE_ANSATZ.md` — first explicit candidate form for the transport-current image \(\mathcal V_i[\Xi]\) in the EM projector
- `docs/RADIATIVE_BRANCH_AND_ATTRACTOR_QUANTIZATION.md` — radiative extension where transfer is continuous at first pass and discreteness emerges through resonant-state attractors
- `docs/EM_SELECTION_RULES_FROM_RESONANT_ATTRACTORS.md` — first selection-rule formulation from projected transport, resonance matching, coherence, and closure admissibility
- `docs/EM_RATE_AND_LINEWIDTH_ANSATZ.md` — first quantitative ansatz for transition rates, line widths, and intensities built from the EM selection score
- `docs/EM_CALIBRATION_STRATEGY.md` — staged strategy for fixing charge normalization, transport ratios, widths, and global rate scales without overfitting
- `docs/PHOTON_BRANCH_FOUNDATION.md` — photon branch note tying the current pure-bosic path back to the full torus-wave backbone
- `docs/WMINUS_BRANCH_FOUNDATION.md` — charged-conjugate weak probe branch note for the current `WMinus` implementation
- `docs/ZBOSON_BRANCH_FOUNDATION.md` — neutral weak probe branch note for the current `ZBoson` implementation
- `docs/NATURAL_EMERGENCE_OF_INCOMPLETE_QUARK_CYCLES.md` — derivation scaffold for quark closure defect, composite closure, and weak-assisted compensation
- `docs/COMPOSITE_CLOSURE_ALGEBRA_V1.md` — first explicit additive algebra for isolated, assisted, and composite closure of defect-bearing quark-like sectors
- `docs/CLOSURE_CHARGE_CHIRALITY_COMPATIBILITY_V1.md` — compatibility layer linking closure-defect class, EM sign branch, and weak-chiral bias
- `docs/EFFECTIVE_CHARGE_PROJECTION_ANSATZ_V1.md` — first explicit projection ansatz from `(delta, chi, c)` to quark-like effective charge assignments
- `docs/CLOSURE_COMPLEMENT_PROJECTION_DERIVATION_V1.md` — justification scaffold for why the EM projector should see closure complement `(1-delta)` rather than raw defect `delta`
- `docs/TOY_PROJECTOR_FOR_CLOSURE_COMPLEMENT_V1.md` — explicit toy projector model showing how coherent-window projection yields a `(1-delta)` source weight
- `docs/TOY_TORUS_SURFACE_PROJECTOR_V1.md` — torus-surface lift of the toy projector acting directly on `Xi(theta_f, theta_b, tau)`
- `docs/LOCAL_COHERENCE_FUNCTIONAL_FOR_PROJECTOR_V1.md` — first field-derived local coherence weight `W[Xi]` replacing manual coherent windows/regions
- `docs/COUPLED_QUARK_GLUON_WEAK_CLOSURE_ALGEBRA.md` — coupled closure extension including multi-quark defect content plus gluon/color and weak-assisted compensation terms
- `docs/GLUON_COMPENSATION_TERM_ANSATZ.md` — first explicit candidate form for the gluon/color compensation term in the coupled closure law
- `docs/DOWN_GLUON_RENDER_FOUNDATION.md` / `docs/UP_QUARK_RENDER_FOUNDATION.md` — branch-facing entry points into the coupled closure and gluon-compensation story
- `docs/QUARK_DERIVATION_CHAIN_INDEX.md` — compact guide to the quark derivation chain, current conclusions, and open gaps
- `docs/ELECTRON_STEADY_STATE_EXAMPLE.md` — concrete electron walkthrough (state, equations, spin)
- `docs/ELECTRON_STRUCTURE.md` — electron DOF card + spin entry + EM-emergence hypotheses
- `docs/RESONANT_LOOP_DERIVATION.md` — loop derivation and period law
- `docs/RENDERING_BACKENDS.md` — backend behavior and practical workflow
- `docs/CODE_GUIDE.md` — code map, interfaces, extension points
- `docs/WEAK_BOSON_WPLUS_CLASS_FOUNDATION.md` — derivation-to-class contract for first weak-boson renderer path
- `docs/UP_QUARK_RENDER_FOUNDATION.md` — up-quark prototype foundation + promotion criteria
- `docs/DOWN_GLUON_RENDER_FOUNDATION.md` — down-quark + gluon prototype foundation + promotion criteria
- `scripts/render_weak_pair.py` — side-by-side W+ / W- cycle renderer
- `scripts/analyze_up_quark_resonance.py` — scan low-order weak-assisted lock candidates for up-quark prototype
- `scripts/analyze_down_quark_resonance.py` — scan low-order weak-assisted lock candidates for down-quark prototype
- `scripts/render_up_quark_prototype.py` — render helper for prototype up-quark branch
- `scripts/render_down_quark_prototype.py` — render helper for prototype down-quark branch
- `scripts/render_gluon_prototype.py` — render helper for prototype gluon branch
- `scripts/render_comparison_panel.py` — comparison panel for `u/d/gluon/W+/Z0`
- `scripts/render_pf_orbit_comparison_parallel.py` — parallel full-cycle on/off comparison for `electron` + `uquark`
- shared loop math: `../docs/theory/LOOP_TANGENCY_AND_CLOSURE_DERIVATION.md`

---

## Current conventions locked in code

1. **Axis convention**
   - bosic momentum channel \(p\) wraps major angle \(\theta\equiv u\)
   - fermic channel \(p_f\) wraps minor angle \(\phi\equiv v\)

2. **Spin convention (matter branch)**
   - spin inversion flips **bosic transport chirality**
   - fermic orientation stays fixed (no antimatter flip)

3. **Cycle period**
   - `cycle_time()` = base visual period
   - `loop_cycle_time()` = full return to original loop state

---

## Notes on Plotly PNG/GIF export

Plotly GIF/MP4 path uses Kaleido/Chrome under the hood.
If export fails, install Chrome + Chromium runtime dependencies for your OS.
(See `docs/RENDERING_BACKENDS.md` troubleshooting.)
