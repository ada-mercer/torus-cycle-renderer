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

## 6) Practical electron default
For a readable electron presentation with \(p_f/p\approx 3\), choose
\[
(k_f,k_b)=(3,1)
\]
(or a nearby rational approximation if parameters vary).

This yields a complete closed resonant transport loop in one rendered cycle, with no superposition artifacts.
