# torus-cycle-renderer

Torus-based internal-state visualization toolkit with two render pipelines:
- **Matplotlib** (fast scripted GIF/MP4)
- **Plotly** (better depth handling, WebGL, PNG frame export for GIF stitching)

The project is designed so that **physics/state logic** is separate from **visual styling/rendering**.

---

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
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
  - spin/anchor conventions
- `src/torus_cycle_renderer/math/`
  - torus geometry and utility math
- `src/torus_cycle_renderer/rendering/`
  - matplotlib renderer
  - plotly renderer
  - animation pipeline
  - geometry export bridge
- `src/torus_cycle_renderer/cli.py`
  - PATH entrypoints (`render-frame`, `render-cycle`)

### Design rule
- Particle classes own **state/dynamics**.
- Renderer config owns **visual style** (colors, opacity, time-scale in display space).

---

## Documentation map

- `docs/INTRODUCTION.md` — theory + project model + conventions
- `docs/ELECTRON_STEADY_STATE_EXAMPLE.md` — concrete electron walkthrough (state, equations, spin)
- `docs/RESONANT_LOOP_DERIVATION.md` — loop derivation and period law
- `docs/RENDERING_BACKENDS.md` — backend behavior and practical workflow
- `docs/CODE_GUIDE.md` — code map, interfaces, extension points
- `docs/CODE_GUIDE.md` — code-level guide (classes, configs, CLI, extension points)

---

## Current conventions locked in code

1. **Axis convention**
   - bosic momentum channel \(p\) wraps major angle \(\theta\equiv u\)
   - fermic channel \(p_f\) wraps minor angle \(\phi\equiv v\)

2. **Spin convention (matter branch)**
   - spin inversion flips **bosic transport chirality**
   - fermic orientation stays fixed (no antimatter flip)

3. **Cycle period**
   - `Electron.cycle_time()` uses anchor-aware closed-cycle derivation

---

## Notes on Plotly PNG/GIF export

Plotly GIF/MP4 path uses Kaleido/Chrome under the hood.
If export fails, install Chrome + Chromium runtime dependencies for your OS.
(See `docs/RENDERING_BACKENDS.md` troubleshooting.)
