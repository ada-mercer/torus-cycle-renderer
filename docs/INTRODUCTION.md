# Torus Cycle Renderer — Theory Introduction

## Purpose
This project renders *internal-state* particle visuals from a torus-based wave model, rather than purely hand-crafted geometry.

The core design goal is:
- **physics layer** (particle state + solver) separated from
- **rendering layer** (surface + loop visualization).

---

## Conceptual model
We use an internal two-cycle manifold:
\[
(\theta_f,\theta_b) \in T^2 = S^1 \times S^1,
\qquad 0\le\theta_f,\theta_b < 2\pi.
\]

A particle state is represented by:
1. a winding sector \((n_f,n_b)\), and
2. a complex internal field \(\Phi(\theta_f,\theta_b,\tau)\).

Using the W2 embedding:
\[
\Phi = e^{i(n_f\theta_f+n_b\theta_b)}\,\varphi,
\]
we work with shifted derivatives
\[
D_f = \partial_{\theta_f}+in_f,
\qquad
D_b = \partial_{\theta_b}+in_b.
\]

---

## Baseline wave equation
With torus radii \(R_f,R_b\), the internal operator is
\[
\Delta_n = \frac{1}{R_f^2}D_f^2 + \frac{1}{R_b^2}D_b^2.
\]

Baseline equation:
\[
\partial_\tau^2\varphi - c_{int}^2\Delta_n\varphi + \Omega_0^2\varphi = 0.
\]

For Fourier mode \(e^{i(r\theta_f+s\theta_b)}\),
\[
\omega_{rs}^2 = \Omega_0^2 + c_{int}^2\left(\frac{(r+n_f)^2}{R_f^2}+\frac{(s+n_b)^2}{R_b^2}\right).
\]

So the model has a discrete mode spectrum on \(T^2\).

---

## What the renderer shows
The renderer consumes a particle object and produces:
1. **deformed torus surface** using solved mode amplitude/phase,
2. **resonant loop** extracted from the solved phase field (spin-conditioned for fermions).

This means the default electron path is now *solver-backed*.

---

## Class architecture
- `AbstractParticle`: renderer contract
- Family layer:
  - `FermionParticle`
  - `BosonParticle`
  - `WeakBosonParticle`
- `SolverBackedParticle`: numerical steady-state + phase-loop extraction
- Concrete particles:
  - `Electron` (solver-backed, spin-aware)
  - `Photon` (current baseline, can be upgraded similarly)

### Policy enforcement
Family classes enforce constraints before/after solve:
- base particle policy: valid radii and deformation ranges,
- fermion policy: valid spin/winding plus nontrivial fermic channel content,
- weak-boson policy: bounded coupling regime.

Policy violations raise `PolicyViolation` and block rendering of invalid states.
---

## Numerical strategy
For steady states, we solve
\[
H\psi = \omega^2\psi,
\quad
H = -c_{int}^2\Delta_n + \Omega_0^2.
\]

Implementation notes:
- periodic finite-difference derivative matrices on \(T^2\),
- sparse Kronecker-structured operator,
- lowest modes via SciPy sparse eigensolver.

---

## Scope and honesty
Current outputs are mathematically grounded in the chosen operator and sector, but still depend on model/parameter policy choices (radii, baseline constants, selected sector/mode index).

So these are:
- **not arbitrary dummy curves**,
- but also **not final unique particle truths** yet.

The docs in this folder make assumptions explicit so calibration/validation can be tightened over time.
