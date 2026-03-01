# Resonant Loop Derivation on the Torus

This note defines a closed resonant loop directly in torus coordinates, with tangent set by local momentum transport.

## 1) Torus coordinates and local tangent basis
Use torus angular coordinates
\[
(u,v) \in [0,2\pi)\times[0,2\pi),
\]
with embedding
\[
\mathbf X(u,v)=\big((R+r\cos v)\cos u,\ (R+r\cos v)\sin u,\ r\sin v\big).
\]

Local tangent basis directions are
\[
\mathbf e_u = \partial_u \mathbf X / \|\partial_u \mathbf X\|,
\qquad
\mathbf e_v = \partial_v \mathbf X / \|\partial_v \mathbf X\|.
\]

Interpretation:
- \(\mathbf e_u\): "fermic-cycle" direction (major-cycle transport axis)
- \(\mathbf e_v\): "bosic-cycle" direction (minor-cycle transport axis)

---

## 2) Momentum-transport tangent at a point
Given the requested rule at point \(p\):
\[
\mathbf m = p_f\,\mathbf e_u + p\,\mathbf e_v,
\]
(the unit-vector directions are carried by \(\mathbf e_u,\mathbf e_v\)).

In coordinate-speed form, this implies
\[
\frac{du}{ds} : \frac{dv}{ds} \sim p_f : p.
\]

To force closure, choose integer winding numbers \((k_f,k_b)\in\mathbb Z_{>0}^2\) approximating
\[
\frac{k_f}{k_b} \approx \frac{p_f}{p}.
\]
(Implementation: rational approximation with bounded denominator.)

---

## 3) Closed loop ansatz in torus coordinates
Define a loop parameter \(s\in[0,1]\):
\[
u(s)=u_0 + 2\pi k_f s,
\qquad
v(s)=v_0 + 2\pi k_b s.
\]

At \(s=1\):
\[
\Delta u = 2\pi k_f,
\qquad
\Delta v = 2\pi k_b,
\]
so the curve closes on the torus (same spatial point modulo \(2\pi\)).

---

## 4) Single-mode resonant phase constraint
For a no-superposition state, use one mode \((\nu_f,\nu_b)\):
\[
\Phi \propto \cos\big(\nu_f u + \nu_b v - \omega t_{eff} + \phi_s\big).
\]

To pick a consistent starting point \((u_0,v_0)\), impose phase lock:
\[
\nu_f u_0 + \nu_b v_0 - \omega t_{eff} + \phi_s = 0.
\]
With \(u_0=0\):
\[
v_0 = \frac{\omega t_{eff} - \phi_s}{\nu_b}\quad(\nu_b\neq 0).
\]

---

## 5) Phase and amplitude closure after one loop
After one loop in \(s\):
\[
\Delta\varphi = \nu_f\Delta u + \nu_b\Delta v
= 2\pi(\nu_f k_f + \nu_b k_b)
\in 2\pi\mathbb Z.
\]
So both phase and amplitude return exactly:
\[
\cos(\varphi+\Delta\varphi)=\cos\varphi.
\]

Hence the loop is:
1. geometrically closed,
2. phase-closed,
3. amplitude-closed,
for a single-mode state.

---

## 6) Two anchor modes (both supported)
Let \(v_0(t)\) denote the loop start anchor.

1. **Evolving anchor mode** (`evolving`):
\[
v_0(t)=\frac{\omega t_{eff}-\phi_s-\nu_f u_0}{\nu_b}
\]
The start point follows instantaneous phase lock over time.

2. **Static anchor mode** (`static`):
\[
v_0=\frac{-\phi_s-\nu_f u_0}{\nu_b}
\]
The start point is fixed in time (locked at \(t=0\)); loop geometry still closes and field evolves.

Both modes keep geometric closure by the integer winding construction.

## 7) Cycle-period derivation for rendering
Define the effective time scaling used by the particle dynamics as
\[
t_{eff} = s_t\, t,
\]
(where currently \(s_t = p/p_f\) in the electron model).

Single-mode phase:
\[
\varphi = \nu_p u + \nu_{pf} v - \omega t_{eff} + \phi_s.
\]

### Static anchor period
Only phase return is required:
\[
\omega t_{eff} = 2\pi m \Rightarrow T_{static}=\frac{2\pi}{\omega s_t}.
\]

### Evolving anchor period
Anchor depends on time:
\[
v_0(t)=\frac{\omega t_{eff}-\phi_s-\nu_p u_0}{\nu_{pf}}.
\]
For start-point return modulo \(2\pi\), require
\[
\frac{\omega t_{eff}}{\nu_{pf}}=2\pi n.
\]
Smallest compatible positive period:
\[
T_{evolving}=|\nu_{pf}|\,\frac{2\pi}{\omega s_t}=|\nu_{pf}|\,T_{static}.
\]

This period law is now implemented in `Electron.cycle_time()` and consumed by the render pipeline.

## 8) Practical electron default
For a readable electron presentation with \(p_f/p\approx 3\), choose
\[
(k_f,k_b)=(3,1)
\]
(or a nearby rational approximation if parameters vary).

This yields a complete closed resonant transport loop in one rendered cycle, with no superposition artifacts.
