# torus-cycle-renderer

Fresh-start torus-cycle rendering project for internal particle-cycle visualization.

## Goals
- Keep **particle model** separate from **rendering engine**.
- Render a torus surface with a time-dependent deformation field.
- Overlay a resonant loop trajectory on the surface.
- Make output dimensions image-friendly (for social/media/docs).

## Architecture
- `particles/` -> abstract particle API + family layers (`FermionParticle`, `BosonParticle`, `WeakBosonParticle`) + concrete particles (`Electron`, `Photon`)
- `math/` -> torus geometry, resonance ODE tools, and steady-state solver
- `rendering/` -> renderer that only depends on abstract particle contract
- `scenes/` -> scene builder for demo compositions
- `scripts/` -> CLI entry points (single frame, animation)

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

python scripts/render_frame.py \
  --particle electron \
  --spin-state ++ \
  --width 1280 --height 720 \
  --time 0.0 \
  --output output/electron_frame.png
```

Depth-accurate alternative backend (Plotly, with mesh gridlines + higher transparency):
```bash
python scripts/render_frame.py \
  --backend plotly \
  --particle electron \
  --spin-state ++ \
  --time 0.0 \
  --output output/electron_frame.html
```

Geometry export (for external renderers):
```bash
python scripts/render_frame.py --particle electron --export-geometry --output output/electron_frame.png
# writes: *_geom.npz, *_torus.obj, *_loop.obj
```

Render full cycle GIF:
```bash
python scripts/render_cycle.py \
  --particle electron \
  --spin-state ++ \
  --loop-anchor-mode evolving \
  --frames 120 --fps 30 \
  --format gif \
  --output output/electron_cycle.gif
```

Loop anchor modes:
- `evolving`: start point follows phase lock over time
- `static`: start point fixed (t=0 lock), loop still closes each frame

## First Demo
The default scene renders:
1. a deformed torus surface,
2. a resonant loop tied to particle phase dynamics.

The resonant loop is now generated from solver-backed phase structure for the electron path, with SciPy used for numerical components.

This is a clean baseline to iterate math without carrying legacy assumptions.

## Documentation
- Theory intro: `docs/INTRODUCTION.md`
- In-depth electron example: `docs/ELECTRON_STEADY_STATE_EXAMPLE.md`
- Resonant loop derivation: `docs/RESONANT_LOOP_DERIVATION.md`
- Rendering backends: `docs/RENDERING_BACKENDS.md`

## Visual control note
For solver-backed fermions, visual pacing/loop smoothness now uses explicit channel parameters:
- `pf_value` (fermic scale)
- `p_value` (bosic scale)

The loop branch uses approximately `round(pf_value / p_value)` turns to avoid random phase-jump artifacts.
