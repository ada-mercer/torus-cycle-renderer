# Electron Steady-State Example (with Spin)

This document gives a concrete, minimal electron example using the current torus-wave model and code path.

---

## 1) Setup

We model the electron as a solver-backed fermion in a winding sector.

Current project defaults:
- sector: \((n_f,n_b)=(1,1)\)
- radii: \(R_f=2.1\), \(R_b=0.72\) (from current particle config)
- baseline constants: \(c_{int}=1\), \(\Omega_0=1\)
- solve lowest eigenmode (`mode_index = 0`)

The steady-state eigenproblem is:
\[
H\psi = \omega^2\psi,
\qquad
H = -c_{int}^2\Delta_n + \Omega_0^2,
\]
with
\[
\Delta_n = \frac{1}{R_f^2}(\partial_{\theta_f}+in_f)^2 + \frac{1}{R_b^2}(\partial_{\theta_b}+in_b)^2.
\]

---

## 2) Simplest mode solution (analytic picture)

For a pure Fourier basis mode:
\[
\psi_{rs}(\theta_f,\theta_b)=e^{i(r\theta_f+s\theta_b)},
\]
we get
\[
\omega_{rs}^2=
\Omega_0^2 + c_{int}^2\left(\frac{(r+n_f)^2}{R_f^2}+\frac{(s+n_b)^2}{R_b^2}\right).
\]

Define shifted integers:
\[
\nu_f=r+n_f,
\qquad
\nu_b=s+n_b.
\]
Then
\[
\omega^2 = \Omega_0^2 + c_{int}^2\left(\frac{\nu_f^2}{R_f^2}+\frac{\nu_b^2}{R_b^2}\right).
\]

For the lowest shell \((\nu_f,\nu_b)=(0,0)\):
\[
\omega=\Omega_0=1.
\]

This is the simplest steady harmonic state (up to global phase).

---

## 3) Numerical steady state used in code

In the solver-backed path, we discretize \(T^2\) and solve the sparse eigenproblem directly.

The solved field is complex:
\[
\psi(\theta_f,\theta_b) = A(\theta_f,\theta_b)e^{i\phi(\theta_f,\theta_b)}.
\]

Time evolution for rendering uses
\[
\psi_t = \psi\,e^{-i\omega t}.
\]

Surface deformation is taken from normalized real amplitude:
\[
\delta R(\theta_f,\theta_b,t) \propto \Re[\psi_t].
\]

This drives the deformed torus geometry.

---

## 4) How spin enters in the current renderer

Spin state is currently implemented as a **phase-selection rule** over the solved mode.

Allowed labels:
- `++`
- `+-`
- `-+`
- `--`

Each label maps to a target phase \(\phi_*\):
- `++` \(\to 0\)
- `+-` \(\to +\pi/2\)
- `-+` \(\to -\pi/2\)
- `--` \(\to \pi\)

For each \(u\)-column, the loop chooses \(v\) where solved phase is closest to \(\phi_*\).
This yields a spin-conditioned resonant loop trajectory.

### Important interpretation note
This is a **rendering-level spin injection rule**, not yet a full Dirac-spinor measurement map.
It is a disciplined and explicit interim mechanism that can later be replaced by a stricter spin observable derived from the Dirac branch.

---

## 5) Minimal reproduction

Render simplest electron steady-state views with different spin labels:

```bash
python scripts/render_frame.py --particle electron --spin-state ++ --time 0.4 --output output/electron_steady_pp.png
python scripts/render_frame.py --particle electron --spin-state=-- --time 0.4 --output output/electron_steady_mm.png
```

(Use `--spin-state=--` with `=` to avoid CLI parsing ambiguity.)

---

## 6) What is physically strong vs provisional

### Strong now
- steady-state solution of chosen torus operator is real (numerically solved),
- winding-sector embedding is explicit,
- rendered deformation/loop are derived from solved complex field.

### Provisional now
- electron sector and constants are policy defaults,
- spin mapping is phase-target proxy (not final Dirac observable map),
- no global data-calibration lock yet.

---

## 7) Next hardening steps

1. Add explicit CLI control for sector/mode index (`--nf --nb --mode-index`).
2. Add Dirac-branch solver and compare spin-conditioned loops against spinor bilinear observables.
3. Add calibration notebook/script tying \((R_f,R_b,\Omega_0)\) to chosen correspondence constraints.
4. Promote from “rendering spin proxy” to “operator-derived spin readout”.
