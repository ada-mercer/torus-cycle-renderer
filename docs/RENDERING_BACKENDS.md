# Rendering Backends

The project intentionally supports three parallel render paths.

---

## 1) Matplotlib backend

Command switch:
```bash
--backend matplotlib
```

### Strengths
- fast and simple scripted pipeline
- stable GIF/MP4 generation
- good for batch iteration

### Limitations
- mplot3d uses painter-style ordering, so complex occlusion can be imperfect

---

## 2) Plotly backend

Command switch:
```bash
--backend plotly
```

### Strengths
- stronger multi-object depth behavior (WebGL)
- good interactive inspection
- can export PNG frames for GIF stitching

### Requirements for image export
Plotly static export depends on Kaleido/Chrome runtime dependencies.
If missing, install Chrome + required system libs.

---

## 3) PyVista backend

Command switch:
```bash
--backend pyvista
```

### Strengths
- VTK-based offscreen rendering with stronger mesh/curve presentation than matplotlib
- uses the same shared scene geometry path as the other backends
- exports static image frames cleanly for GIF/MP4 stitching through the existing CLI cycle path

### Limitations
- requires the optional `pyvista` dependency
- currently targets static image outputs directly; GIF/MP4 are built by stitching rendered PNG frames

---

## 4) Shared controls (all backends)

Both use:
- `--torus-color`
- `--loop-color`
- `--time-scale`
- same particle state arguments (`--particle`, `--spin-state`, `--loop-anchor-mode`)

So style can be matched across pipelines.

---

## 5) Geometry export bridge

`render-frame --export-geometry` writes:
- `*_geom.npz`
- `*_torus.obj`
- `*_loop.obj`

Use this when you want to render identical state geometry in an external engine (Blender/VTK/etc.).

---

## 6) Recommended workflow

1. Iterate quickly with Matplotlib GIF.
2. Validate depth-sensitive views in Plotly.
3. Export geometry for external production rendering when needed.
