# Rendering Backends Strategy

## Why two backends
Matplotlib is great for lightweight scripted output and GIF pipelines, but mplot3d uses painter-style sorting that can be imperfect for multi-object occlusion.

To improve depth correctness while keeping Matplotlib, the project now supports:
- **Matplotlib backend** (default): fast pipeline + existing GIF flow
- **Plotly backend**: stronger z-buffer style multi-object ordering in interactive/WebGL rendering

## Geometry export bridge
Any frame can now export geometry:
- `*_geom.npz` (raw arrays)
- `*_torus.obj` (surface mesh)
- `*_loop.obj` (polyline)

This allows rendering the same solved state in external engines (VTK/Blender/etc.) without changing physics code.

## Recommended workflow
1. Iterate quickly with Matplotlib (`--backend matplotlib`).
2. Validate occlusion/depth with Plotly (`--backend plotly`).
3. For production visuals, export geometry and render in a dedicated 3D engine if needed.
