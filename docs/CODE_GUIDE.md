# Code Guide

This guide maps theory concepts to code locations.

Interpretation guardrail:
- the codebase currently prioritizes **clear resonant-mode representatives** over full physical-state closure;
- when extending classes, preserve the distinction between a renderable probe mode and a claimed full particle solution.
- also preserve the distinction between **branch identity**, **observable handedness/spin/helicity**, and any **deeper internal lifted-state sign** that the broader theory may discuss but the repo does not yet fully encode.
- see `docs/SIGN_ARCHITECTURE_AND_INTERPRETATION.md`.

---

## Package layout

- `src/torus_cycle_renderer/cli.py`
  - `render_frame_main()`
  - `render_cycle_main()`
- `src/torus_cycle_renderer/particles/`
  - `base.py` (`AbstractParticle`, `ParticleParams`)
  - `families.py` (family classes + policy checks)
  - `electron.py` (`ElectronState`, `Electron`)
  - `photon.py`
  - `w_plus.py` (`WPlusState`, `WPlus`)
  - `w_minus.py` (`WMinusState`, `WMinus`)
  - `z_boson.py` (`ZBosonState`, `ZBoson`)
  - `u_quark.py` (`UQuarkState`, `UQuark`) [prototype]
  - `d_quark.py` (`DQuarkState`, `DQuark`) [prototype]
  - `gluon.py` (`GluonState`, `Gluon`) [prototype]
- `src/torus_cycle_renderer/math/`
  - `torus.py` (surface + frame grid)
  - `steady_state.py` (operator/eigen tools)
  - `resonance.py`
  - `loop_constraints.py` (channel-tangent winding helpers)
- `src/torus_cycle_renderer/loops/`
  - `loop_model.py` (`ParticleLoop`, `LoopGeometry`, full-cycle helpers)
- `src/torus_cycle_renderer/rendering/`
  - `scene_data.py` (shared scene sampling dataclass/helper)
  - `renderer.py` (matplotlib)
  - `plotly_renderer.py` (plotly)
  - `pyvista_renderer.py` (pyvista / VTK offscreen)
  - `animation.py` (frame stitching + frame-time helper)
  - `geometry_export.py` (NPZ/OBJ)

---

## Core interfaces

### Particle contract
`AbstractParticle` requires:
- `name`
- `params`
- `deformation(u,v,t)`
- `resonant_loop(t, points)` (legacy-compatible)
- `loop_geometry(t, points, reference_uv)` (current renderer path)
- `cycle_time()` (base visual period)
- `loop_cycle_time()` (full return to original loop state)

### Renderer contract
Renderers consume only `AbstractParticle` and renderer config.

---

## Electron implementation map

`electron.py`:
- `ElectronState`: explicit single-mode state
- `_effective_omega()`: mode frequency
- `_transport_winding()`: rational winding from `p_f/p`
- `deformation(...)`: mode phase field
- `loop_geometry(...)`: loop via `ParticleLoop` (with optional `p_f`-relative orbit drift)
- `resonant_loop(...)`: compatibility shim returning loop `u,v`
- `cycle_time()`: base period law
- `loop_cycle_time()`: full return period for loop state

---

## CLI entrypoints (PATH)

Installed by `pyproject.toml`:
- `render-frame`
- `render-cycle`

### Useful arguments
- state: `--particle --spin-state --loop-anchor-mode`
  - CLI particles: `electron`, `photon`, `wplus` (`w+` alias), `wminus` (`w-` alias), `zboson` (`z0`/`z` aliases), `uquark` (`u` alias), `dquark` (`d` alias), `gluon` (`g` alias)
  - exploratory-status branches: `uquark`, `dquark`, `gluon`
- style: `--torus-color --loop-color --time-scale`
- backend: `--backend matplotlib|plotly`
- output: `--output`
- exact loop counts: `--cycles N` (runs for N full cycle returns)
- full loop-state closure: `--full-loop-cycle`
- frame-level parallelism (matplotlib path): `--frame-workers N`

---

## Extension points

1. Add new particle class
   - implement `AbstractParticle`
   - decide explicitly whether it is a **reference resonant mode**, a **probe state for a partially resonant sector**, or an attempted **full-state correspondence**
   - register in `scenes/default_scene.py` (or keep as prototype if not yet ready)

2. Add new render profile
   - add config fields in renderer dataclass
   - expose via CLI args

3. Add validation tests
   - closure test on `resonant_loop` endpoint
   - phase-period consistency test via `cycle_time()`
   - full-return check via `loop_cycle_time()` (modulo `2π`)

---

## Theory-document alignment

- `docs/INTRODUCTION.md` tracks the current implementation boundary (what is coded vs exploratory).
- `docs/FULL_WAVE_EQUATION_DERIVATION.md` is the full torus-carrier wave derivation for the repo.
- `docs/DERIVATION_VALIDATION_AGAINST_IMPLEMENTATION.md` marks what is exact, reduced, or exploratory relative to that derivation.
- `docs/CONSTRAINED_TORUS_TO_EM_PROJECTOR_ANSATZ.md`, `docs/EM_FAR_FIELD_AND_MULTIPOLE_CONSEQUENCES.md`, and `docs/EM_PROJECTOR_STATUS_MAP.md` now document the EM emergence side at the same exact/constrained/open split.
- `docs/ELECTRON_STEADY_STATE_EXAMPLE.md` is the equation-to-code map for `Electron`.
- `docs/ELECTRON_STRUCTURE.md` is the compact DOF/spin/field-emergence theory card.
- `../docs/theory/LOOP_TANGENCY_AND_CLOSURE_DERIVATION.md` defines the shared loop constraint math.

When behavior in `particles/electron.py` or `math/steady_state.py` changes, update those derivation-facing docs in the same PR.
