# Resonant Loop Derivation (Code-Aligned)

This file derives the loop model implemented in `particles/electron.py`.

---

## 1) Torus and tangent basis

Coordinates:
\[
(u,v)\in[0,2\pi)\times[0,2\pi).
\]

Embedding:
\[
\mathbf X(u,v)=\big((R+r\cos v)\cos u,\ (R+r\cos v)\sin u,\ r\sin v\big).
\]

Local tangent directions:
\[
\mathbf e_\theta \equiv \mathbf e_u,
\qquad
\mathbf e_\phi \equiv \mathbf e_v.
\]

Convention lock:
- bosic \(p\) aligns with \(\mathbf e_\theta\) (major axis)
- fermic \(p_f\) aligns with \(\mathbf e_\phi\) (minor axis)

---

## 2) Transport tangent rule

At loop point:
\[
\mathbf m \propto p_f\,\mathbf e_\phi + p\,\mathbf e_\theta.
\]

For closure, use integer windings \((k_{pf},k_p)\):
\[
\frac{k_{pf}}{k_p} \approx \frac{p_f}{p}.
\]

Implemented via bounded rational approximation.

---

## 3) Closed loop ansatz

\[
u(s)=u_0 + 2\pi\,\chi_p\,k_p\,s,
\qquad
v(s)=v_0 + 2\pi\,k_{pf}\,s,
\qquad s\in[0,1].
\]

Here \(\chi_p\in\{+1,-1\}\) is spin-dependent bosic chirality.

Closure at \(s=1\):
\[
\Delta u = 2\pi\chi_p k_p,\qquad \Delta v = 2\pi k_{pf}.
\]
So position closes modulo \(2\pi\).

---

## 4) Single-mode phase lock

Mode phase:
\[
\varphi = mode_p\,u + mode_{pf}\,v - \omega t_{eff} + \phi_s.
\]

Anchor condition at \((u_0,v_0)\):
\[
mode_p u_0 + mode_{pf} v_0 - \omega t_{eff} + \phi_s = 0.
\]

With \(u_0=0\):
\[
v_0(t)=\frac{\omega t_{eff}-\phi_s}{mode_{pf}}.
\]

(static anchor uses the same at \(t=0\), i.e. fixed \(v_0\)).

---

## 5) Phase closure after one loop

\[
\Delta\varphi = mode_p\Delta u + mode_{pf}\Delta v
= 2\pi\big(mode_p\chi_p k_p + mode_{pf}k_{pf}\big)
\in 2\pi\mathbb Z.
\]

So amplitude/phase are periodic on the closed loop.

---

## 6) Cycle period for rendering

Define
\[
t_{eff}=s_t t,
\]
with \(s_t\) supplied by model policy (`_time_scale()`).

### Static anchor
\[
T_{static}=\frac{2\pi}{\omega s_t}.
\]

### Evolving anchor
Need start-point return modulo \(2\pi\):
\[
\frac{\omega t_{eff}}{mode_{pf}}\in 2\pi\mathbb Z
\Rightarrow
T_{evolving}=|mode_{pf}|\,T_{static}.
\]

This is exactly what `Electron.cycle_time()` returns.

---

## 7) Spin interpretation used here

Spin inversion flips **bosic chirality only** (\(\chi_p\)).
Fermic orientation remains fixed for matter branch.

So up/down loops differ by major-direction handedness, not by fermic inversion.
