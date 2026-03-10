# Full Wave Equation Derivation on the Torus Carrier

Status: derivation note / implementation-facing theory backbone

This note gives the full torus-carrier wave derivation that underlies the renderer repository at the level of the current M1 internal-geometry picture.

It serves two goals:
1. provide the cleanest full linear wave-equation derivation in repo notation;
2. make explicit which implemented renderer branches are exact solutions of reduced versions of that equation, and which are only correspondence ansätze.

This document is intentionally more formal than `INTRODUCTION.md` and more general than `ELECTRON_STEADY_STATE_EXAMPLE.md`.

---

## 1) Carrier geometry and notation lock

Use torus angles
\[
(u,v)\in[0,2\pi)\times[0,2\pi),
\qquad T^2=S^1\times S^1.
\]

Repository convention lock:
- major angle \(u\): bosic channel \(p\)
- minor angle \(v\): fermic channel \(p_f\)

Internal metric:
\[
ds_{int}^2 = R^2du^2 + r^2dv^2,
\]
where:
- \(R\): major-cycle radius
- \(r\): minor-cycle radius

Laplace-Beltrami operator on this flat torus:
\[
\Delta_{T^2} = \frac{1}{R^2}\partial_u^2 + \frac{1}{r^2}\partial_v^2.
\]

---

## 2) Field variable and sector factorization

Introduce a complex internal field
\[
\Phi(u,v,\tau): T^2\times\mathbb R_\tau\to\mathbb C.
\]

The cleanest M1-compatible sector treatment is the background-phase factorization (the W2 choice from the upstream notes):
\[
\Phi(u,v,\tau)=e^{i(n_b u+n_f v)}\,\varphi(u,v,\tau),
\qquad n_b,n_f\in\mathbb Z.
\]

Interpretation:
- \((n_b,n_f)\): winding/topological sector label
- \(\varphi\): wave excitation content within that sector

Because the exponential prefactor already carries the winding, \(\varphi\) remains periodic on the torus:
\[
\varphi(u+2\pi,v,\tau)=\varphi(u,v,\tau),
\qquad
\varphi(u,v+2\pi,\tau)=\varphi(u,v,\tau).
\]

---

## 3) Shifted derivative form

Define the shifted derivatives
\[
D_u := \partial_u + in_b,
\qquad
D_v := \partial_v + in_f.
\]

Then
\[
\partial_u\Phi = e^{i(n_bu+n_fv)}D_u\varphi,
\qquad
\partial_v\Phi = e^{i(n_bu+n_fv)}D_v\varphi.
\]

Hence the sector-shifted torus operator is
\[
\Delta_n := \frac{1}{R^2}D_u^2 + \frac{1}{r^2}D_v^2.
\]

This is exactly the operator structure implemented numerically in `math/steady_state.py`, where
- `n_b` corresponds to the major-angle shift,
- `n_f` corresponds to the minor-angle shift.

---

## 4) Action and Euler–Lagrange equation

Use the linear action
\[
S[\varphi] = \int d\tau\int_{T^2} dudv\,Rr\,\mathcal L,
\]
with Lagrangian density
\[
\mathcal L = \frac{1}{2}|\partial_\tau\varphi|^2
- \frac{c_{int}^2}{2}\left(
\frac{|D_u\varphi|^2}{R^2} + \frac{|D_v\varphi|^2}{r^2}
\right)
- \frac{\Omega_0^2}{2}|\varphi|^2.
\]

Varying with respect to \(\varphi^*\) gives the Euler–Lagrange equation
\[
\partial_\tau^2\varphi - c_{int}^2\Delta_n\varphi + \Omega_0^2\varphi = 0.
\]

Equivalently, in the unfactored field:
\[
\partial_\tau^2\Phi - c_{int}^2\Delta_{T^2}\Phi + \Omega_0^2\Phi = 0.
\]

This is the full linear torus wave equation in the current M1-ready form.

---

## 5) Fourier-mode decomposition and exact spectrum

Because \(\varphi\) is periodic, expand it as
\[
\varphi(u,v,\tau)=\sum_{r,s\in\mathbb Z} A_{rs}(\tau)e^{i(ru+sv)}.
\]

Then
\[
D_u e^{i(ru+sv)} = i(r+n_b)e^{i(ru+sv)},
\qquad
D_v e^{i(ru+sv)} = i(s+n_f)e^{i(ru+sv)}.
\]

Therefore each mode satisfies
\[
\ddot A_{rs} + \omega_{rs}^2 A_{rs}=0,
\]
with
\[
\omega_{rs}^2 = \Omega_0^2 + c_{int}^2\left(
\frac{(r+n_b)^2}{R^2} + \frac{(s+n_f)^2}{r^2}
\right).
\]

This is the exact shifted torus spectrum.

---

## 6) Steady-state eigenproblem

For harmonic time dependence
\[
\varphi(u,v,\tau)=\psi(u,v)e^{-i\omega\tau},
\]
we obtain
\[
\left(-c_{int}^2\Delta_n + \Omega_0^2\right)\psi = \omega^2\psi.
\]

That is precisely the steady-state eigenproblem solved in
- `src/torus_cycle_renderer/math/steady_state.py`

with the numerical operator
\[
H = -c_{int}^2\Delta_n + \Omega_0^2.
\]

So the repo already contains a direct numerical realization of the full linear steady-state wave equation.

---

## 7) Conserved quadratic quantity

For the linear theory, define
\[
\mathcal E = \frac{1}{2}|\partial_\tau\varphi|^2
+ \frac{c_{int}^2}{2}\left(
\frac{|D_u\varphi|^2}{R^2} + \frac{|D_v\varphi|^2}{r^2}
\right)
+ \frac{\Omega_0^2}{2}|\varphi|^2.
\]

Then the total internal wave energy
\[
E_{int}=\int_{T^2} dudv\,Rr\,\mathcal E
\]
is conserved by the linear dynamics.

This is the cleanest wave-level quantity from which future mappings to the M1 correspondence slots \((p_f,p,M)\) may be built.

At the current renderer level, that mapping is not yet fully derived.

---

## 8) Exact single-mode solutions

For any integers \((r,s)\), the function
\[
\varphi(u,v,\tau)=A\cos\big((r+n_b)u + (s+n_f)v - \omega_{rs}\tau + \phi_0\big)
\]
is an exact real solution of the linear torus wave equation, provided \(\omega_{rs}\) satisfies the spectrum above.

Equivalently, in the simplified no-sector-shift case \((n_b,n_f)=(0,0)\),
\[
\varphi(u,v,\tau)=A\cos\big(\nu_p u + \nu_{pf} v - \omega\tau + \phi_0\big)
\]
is exact when
\[
\omega^2 = \Omega_0^2 + c_{int}^2\left(\frac{\nu_p^2}{R^2}+\frac{\nu_{pf}^2}{r^2}\right).
\]

This is the full derivational origin of the repo’s single-mode deformation forms.

---

## 9) Connection to the implemented electron branch

The current `Electron` class uses
\[
\delta r(u,v,t)=A\cos\big(mode_p\,u + mode_{pf}\,v - \omega t_{eff} + \phi_s\big),
\]
with
\[
\omega = \sqrt{1 + \frac{mode_p^2}{R^2} + \frac{mode_{pf}^2}{r^2}}.
\]

This is an exact single-mode solution of the reduced linear wave equation if one identifies
\[
\Omega_0=1,
\qquad c_{int}=1,
\qquad \tau = t_{eff}.
\]

So the deformation law itself is fully derivable from the linear torus wave equation.

### Important implementation note
The repo then introduces the policy-level visible-time rescaling
\[
t_{eff}=t\cdot \frac{p}{p_f},
\]
which is not itself derived from the wave action above. It is a renderer-level correspondence choice for observable timing.

Therefore:
- the **mode shape and frequency form** are fully derivable,
- the **time-rescaling policy** remains an interpretive bridge.

---

## 10) Connection to the resonant loop ansatz

The resonant loop model is not a second independent theory. It is a transport curve chosen so that the single-mode phase remains closed along a rational torus winding.

Take the loop
\[
u(s)=u_0 + 2\pi\chi_p k_p s,
\qquad
v(s)=v_0 + 2\pi k_{pf}s,
\qquad s\in[0,1].
\]

Then the single-mode phase changes by
\[
\Delta\varphi = 2\pi\big(mode_p\chi_p k_p + mode_{pf}k_{pf}\big).
\]

If the winding integers are chosen so that the right-hand side is an integer multiple of \(2\pi\), the phase closes on the loop.

So the resonant loop is derived as a **phase-closed transport path for an exact torus-wave mode**.

That is the correct relation between the full wave equation and the repo’s loop derivation.

---

## 11) Photon and weak-branch relation to the full wave equation

The same single-mode logic extends immediately.

### Photon-like branch
The repo photon branch uses a pure bosic transport limit with \(p_f=0\) at the renderer/correspondence level. Its deformation remains single-mode traveling-wave structure on the torus carrier.

### Weak branches
The weak branches use the same mode form but add a positive mass-gap term. In wave-equation language, that corresponds to replacing
\[
\Omega_0^2 \to \Omega_0^2 + m_{gap}^2
\]
in the reduced branch spectrum.

So these branches are derivable as exact modes of a **branch-modified linear torus operator**, though not yet as full electroweak gauge-field derivations.

---

## 12) Quark and gluon status under the full wave equation

The full linear wave equation does **not by itself** derive the current quark and gluon branches completely.

What it does provide is:
- the common torus carrier,
- the exact single-mode basis,
- the spectral language for mode content,
- the correct setting for closure and transport constraints.

The extra ingredients used in the current quark/gluon docs remain additional hypotheses:
- closure-defect classes,
- weak-assisted compensation,
- coherence/projector ansätze,
- color-phase modulation.

So for these sectors, the full wave equation is the **carrier backbone**, not yet the whole branch derivation.

---

## 13) Exact vs reduced vs exploratory claims

### Exact within current linear theory
- torus wave equation
- shifted-operator spectrum
- steady-state eigenproblem
- single-mode cosine/exponential solutions
- phase closure along rational resonant loops

### Reduced/interpretive choices in current renderer
- visible-time rescaling \(t\mapsto t_{eff}\)
- branch-specific transport-winding heuristics from channel values
- phase-offset interpretation for spin labeling

### Exploratory / not yet fully derived
- full quark closure-defect chain from first principles
- universal projector from torus field to EM fields
- full weak/gauge emergence
- full color-sector dynamics

---

## 14) Working conclusion

The torus-cycle-renderer now has a fully writable wave-equation backbone:
\[
\partial_\tau^2\varphi - c_{int}^2\Delta_n\varphi + \Omega_0^2\varphi = 0,
\]
with exact mode spectrum
\[
\omega_{rs}^2 = \Omega_0^2 + c_{int}^2\left(
\frac{(r+n_b)^2}{R^2} + \frac{(s+n_f)^2}{r^2}
\right).
\]

The implemented electron deformation law is an exact single-mode solution of the reduced linear theory, and the resonant loop construction is the corresponding phase-closed transport path on the torus.

That is the strongest full derivational statement currently justified by both the upstream M1 notes and the repository implementation.
