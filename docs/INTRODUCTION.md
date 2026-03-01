# Introduction

This project visualizes internal particle-cycle structure on a torus using a clean split between:

- **State/theory layer** (particle classes and equations)
- **Rendering layer** (matplotlib/plotly visuals, style, export)

It is intended as a mathematically disciplined visualization environment, not a final experimentally-validated particle solver.

---

## 1) Geometry

Internal coordinates:
\[
(u,v) \in [0,2\pi)\times[0,2\pi), \quad T^2 = S^1\times S^1.
\]

Embedding (major radius \(R\), minor radius \(r\)):
\[
\mathbf X(u,v)=\big((R+r\cos v)\cos u,\ (R+r\cos v)\sin u,\ r\sin v\big).
\]

Project conventions:
- \(u\equiv\theta\): major cycle
- \(v\equiv\phi\): minor cycle

---

## 2) Channel convention

Current lock in code/docs:
- **bosic** channel \(p\) is associated with \(u=\theta\) (major direction)
- **fermic** channel \(p_f\) is associated with \(v=\phi\) (minor direction)

This is implemented in electron loop/dynamics mappings and period derivations.

---

## 3) State model

The electron path uses a **single-mode state** (`ElectronState`) with no superposition.
Core fields include:
- winding sector
- resonant mode integers
- spin state
- anchor mode (`static` / `evolving`)
- channel ratio controls (`p_f`, `p`)

The rendered deformation uses one phase law:
\[
\varphi(u,v,t)=\nu_p u + \nu_{pf} v - \omega t_{eff} + \phi_s.
\]

---

## 4) Spin convention

For matter-branch spin rendering:
- spin inversion flips **bosic transport chirality**
- fermic orientation remains fixed

Interpretation: up/down is a transport handedness flip, not an antimatter flip.

---

## 5) Rendering separation

Renderer config owns visual controls such as:
- torus/loop color
- opacity/transparency
- wire/grid settings
- display time scaling

Particle classes do **not** own color/theme decisions.

---

## 6) Backends

- **Matplotlib backend**
  - robust scripted GIF/MP4 path
  - fast iteration
- **Plotly backend**
  - stronger depth behavior for multi-object scenes
  - interactive HTML + PNG frame path for GIF stitching

Both consume the same particle/state math.

---

## 7) What is strong vs provisional

### Strong
- clean state/render split
- explicit torus-coordinate math
- anchor-aware cycle closure timing
- reproducible dual-backend generation

### Provisional
- physical calibration to real observables is still an open program
- spin semantics are rendering/model conventions, not full Dirac-observable closure yet

Use this repo as a rigorous visualization lab and iteration ground.
