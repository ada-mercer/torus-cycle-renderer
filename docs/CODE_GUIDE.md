# Code Guide

This guide maps theory concepts to code locations.

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
- `src/torus_cycle_renderer/math/`
  - `torus.py` (surface + frame grid)
  - `steady_state.py` (operator/eigen tools)
  - `resonance.py`
- `src/torus_cycle_renderer/rendering/`
  - `renderer.py` (matplotlib)
  - `plotly_renderer.py` (plotly)
  - `animation.py` (frame stitching)
  - `geometry_export.py` (NPZ/OBJ)

---

## Core interfaces

### Particle contract
`AbstractParticle` requires:
- `name`
- `params`
- `deformation(u,v,t)`
- `resonant_loop(t, points)`
- `cycle_time()`

### Renderer contract
Renderers consume only `AbstractParticle` and renderer config.

---

## Electron implementation map

`electron.py`:
- `ElectronState`: explicit single-mode state
- `_effective_omega()`: mode frequency
- `_transport_winding()`: rational winding from `p_f/p`
- `deformation(...)`: mode phase field
- `resonant_loop(...)`: closed parametric loop with anchor mode
- `cycle_time()`: anchor-aware period law

---

## CLI entrypoints (PATH)

Installed by `pyproject.toml`:
- `render-frame`
- `render-cycle`

### Useful arguments
- state: `--particle --spin-state --loop-anchor-mode`
- style: `--torus-color --loop-color --time-scale`
- backend: `--backend matplotlib|plotly`
- output: `--output`

---

## Extension points

1. Add new particle class
   - implement `AbstractParticle`
   - register in `scenes/default_scene.py`

2. Add new render profile
   - add config fields in renderer dataclass
   - expose via CLI args

3. Add validation tests
   - closure test on `resonant_loop` endpoint
   - phase-period consistency test via `cycle_time()`
