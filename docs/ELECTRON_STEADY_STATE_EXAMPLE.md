# Electron Steady-State Example (Implementation-Aligned)

This document maps the **current code path** in `particles/electron.py` to equations.
It describes what is implemented now (not full future theory ambitions).

For the full derivation chain, read first:
- `docs/FULL_WAVE_EQUATION_DERIVATION.md`
- `docs/DERIVATION_VALIDATION_AGAINST_IMPLEMENTATION.md`

This note should be read as the electron-specific reduced implementation map sitting on top of that full torus-wave backbone.

---

## 1) State object and conventions

`ElectronState` (single-mode, no superposition):

- `spin_state` in `{++, +-, -+, --}`
- `winding = (n_f, n_b)`
- `resonant_mode = (mode_p, mode_pf)`
- `transport_winding = (k_pf, k_p)` optional
- `loop_anchor_mode` in `{static, evolving}`
- channel scales: `pf_value`, `p_value`
- geometric/deformation parameters: radii, amplitude, phase speed

Convention lock:
- `mode_p` multiplies major angle `u` (bosic axis)
- `mode_pf` multiplies minor angle `v` (fermic axis)

Implementation note:
- in the current `Electron` path, `winding=(n_f,n_b)` is a validated sector label,
  while actual rendered dynamics are driven by `resonant_mode` and transport winding.
  (The full \(n_f,n_b\)-shifted operator path exists in `math/steady_state.py` / `SolverBackedParticle`.)

---

## 2) Mode phase and deformation

Code-equivalent phase law:
\[
\varphi(u,v,t)=mode_p\,u + mode_{pf}\,v - \omega t_{eff} + \phi_s,
\]
with
\[
t_{eff}=t\cdot\frac{p}{p_f}.
\]

Deformation field:
\[
\delta r(u,v,t)=A\cos\varphi(u,v,t).
\]

Implemented frequency:
\[
\omega=\sqrt{1+\frac{mode_p^2}{R^2}+\frac{mode_{pf}^2}{r^2}}.
\]
(Here `1` is the baseline \(\Omega_0^2\) choice in code.)

This is the exact single-mode spectrum of the reduced full wave equation when one identifies
\[
\Omega_0=1,
\qquad c_{int}=1,
\qquad \tau=t_{eff}.
\]

So the mode shape and frequency law are not merely heuristic: they are the exact reduced single-mode branch of the linear torus wave backbone. The visible-time replacement \(t\mapsto t_{eff}\) remains the renderer-level correspondence choice.

---

## 3) Spin entry points in code

Two spin effects are active:

1. **Bosic chirality** \(\chi_p\in\{+1,-1\}\) via `SPIN_BOSIC_CHIRALITY`
2. **Phase sector offset** \(\phi_s\) via `SPIN_PHASE_SHIFT`

Current mapping:

| spin_state | \(\chi_p\) (bosic chirality) | \(\phi_s\) |
|---|---:|---:|
| `++` | +1 | 0 |
| `+-` | +1 | +\(\pi/2\) |
| `-+` | -1 | -\(\pi/2\) |
| `--` | -1 | \(\pi\) |

Interpretation: spin inversion flips major-cycle handedness; fermic orientation remains fixed for the matter branch.

---

## 4) Resonant transport loop

Implemented loop parameterization:
\[
u(s)=u_0 + 2\pi\chi_p k_p s,
\qquad
v(s)=v_0 + 2\pi k_{pf}s,
\qquad s\in[0,1].
\]

Where:
- `(k_pf, k_p)` comes from rational approximation of \(p_f/p\) (unless manually provided)
- for `pf_value=1`, `p_value=1/3`, default winding is approximately `(k_pf,k_p)=(3,1)`

Closure at \(s=1\):
\[
\Delta u=2\pi\chi_p k_p,\qquad \Delta v=2\pi k_{pf},
\]
so loop position closes modulo \(2\pi\) in both angles.

---

## 5) Anchor mode behavior

### Static anchor
Start point fixed from \(t=0\) phase lock.

### Evolving anchor
Start point follows phase-lock condition:
\[
v_0(t)=\frac{\omega t_{eff}-\phi_s-mode_p u_0}{mode_{pf}}.
\]

This changes cycle closure timing and is reflected in `Electron.cycle_time()`.

---

## 6) Cycle period used by renderer

Let
\[
T_{static}=\frac{2\pi}{\omega (p/p_f)}.
\]
Then
\[
T_{evolving}=|mode_{pf}|\,T_{static}.
\]

`render-cycle` uses this value unless `--cycle-time` is explicitly passed.

---

## 7) Practical verification notes (from implementation check)

For all four spin states in the default electron setup:
- loop closes modulo \(2\pi\) in both angles,
- changing spin from up-like to down-like flips the sign of \(\Delta u\) while \(\Delta v\) stays fixed,
- phase closure remains integer-multiple \(2\pi\) over one full loop.

So the code behavior matches the intended bosic-chirality spin rule.

In the full derivation language, the resonant loop is the phase-closed transport path associated with that exact reduced single-mode solution, not a separate dynamical theory.

---

## 8) Example commands

```bash
render-cycle --backend plotly --particle electron --spin-state ++ --loop-anchor-mode evolving --duration 3.2 --fps 14 --format gif --output output/electron_spin_up.gif
render-cycle --backend plotly --particle electron --spin-state=-- --loop-anchor-mode evolving --duration 3.2 --fps 14 --format gif --output output/electron_spin_down.gif
```

(`--spin-state=--` uses `=` to avoid CLI parsing ambiguity.)
