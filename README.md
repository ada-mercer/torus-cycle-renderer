# torus-cycle-renderer

Fresh-start torus-cycle rendering project for internal particle-cycle visualization.

## Goals
- Keep **particle model** separate from **rendering engine**.
- Render a torus surface with a time-dependent deformation field.
- Overlay a resonant loop trajectory on the surface.
- Make output dimensions image-friendly (for social/media/docs).

## Architecture
- `particles/` -> abstract particle API + concrete particles (`Electron`, `Photon`)
- `math/` -> torus geometry and deformation utilities
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
  --width 1280 --height 720 \
  --time 0.0 \
  --output output/electron_frame.png
```

## First Demo
The default scene renders:
1. a deformed torus surface,
2. a resonant loop tied to particle phase dynamics.

This is a clean baseline to iterate math without carrying legacy assumptions.
