# Derivation Validation Against Implementation

Status: validation note / implementation audit

This note checks the repository implementation against `FULL_WAVE_EQUATION_DERIVATION.md` and the current M1 internal wave formulation.

Its purpose is not to repeat the derivation, but to mark clearly which claims are:
- exact,
- reduced/intermediate,
- or exploratory.

---

## 1) Validation summary

### Validated exactly against the current code
- torus carrier geometry
- linear single-mode deformation law for the electron branch
- mode-frequency form used in `particles/electron.py`
- steady-state shifted operator solved in `math/steady_state.py`
- rational phase-closed loop construction used in `docs/RESONANT_LOOP_DERIVATION.md`

### Validated as reduced renderer correspondence choices
- visible-time rescaling \(t_{eff}=t\,(p/p_f)\)
- spin label entering via bosic chirality + phase offset
- branch-level mass-gap insertion for weak correspondence branches

### Not yet fully derived from the full wave equation
- quark closure-defect fractions from first principles
- weak-assisted compensation algebra from the wave operator alone
- coherence/projector derivation of effective charge
- full gluon/color dynamics

---

## 2) Electron branch

### Code
- `src/torus_cycle_renderer/particles/electron.py`

### Exact statement
The electron deformation law
\[
\delta r(u,v,t)=A\cos\big(mode_p\,u+mode_{pf}\,v-\omega t_{eff}+\phi_s\big)
\]
with
\[
\omega^2 = 1 + \frac{mode_p^2}{R^2} + \frac{mode_{pf}^2}{r^2}
\]
is an exact single-mode solution of the reduced full wave equation when
\[
\Omega_0=1,
\qquad c_{int}=1,
\qquad \tau=t_{eff}.
\]

### Limitation
The replacement
\[
\tau\to t_{eff}=t\,(p/p_f)
\]
remains an implementation/correspondence choice rather than a direct derivation from the linear action.

### Verdict
**Validated as exact reduced-mode implementation plus one timing-policy bridge.**

---

## 3) Steady-state solver

### Code
- `src/torus_cycle_renderer/math/steady_state.py`

### Exact statement
The solver constructs the shifted first-derivative operators
\[
D_u=\partial_u+in_b,
\qquad
D_v=\partial_v+in_f,
\]
and solves
\[
\left(-c_{int}^2\Delta_n + \Omega_0^2\right)\psi=\omega^2\psi.
\]

That matches the full torus steady-state eigenproblem directly.

### Verdict
**Fully validated against the full linear derivation.**

---

## 4) Resonant loop derivation

### Docs/code
- `docs/RESONANT_LOOP_DERIVATION.md`
- `electron.py::loop_geometry()`
- `loops/loop_model.py`

### Exact statement
The loop model is a rational transport curve chosen so that the phase of a single exact torus-wave mode closes after one loop:
\[
\Delta\varphi = 2\pi\big(mode_p\chi_p k_p + mode_{pf}k_{pf}\big) \in 2\pi\mathbb Z.
\]

### Verdict
**Validated as the correct transport/closure derivation for the single-mode branch.**

---

## 5) Photon branch

### Code
- `src/torus_cycle_renderer/particles/photon.py`

### Status
The photon branch remains a torus-wave correspondence model on the common carrier. Its implementation is compatible with the single-mode linear-wave picture, but is not presented as a full gauge-field derivation.

### Verdict
**Validated as reduced branch-level correspondence, not full gauge derivation.**

---

## 6) Weak branches

### Code
- `w_plus.py`
- `w_minus.py`
- `z_boson.py`

### Exact/reduced statement
The weak branches use single-mode structures plus positive mass-gap-like modifications. At the wave-equation level this is consistent with a branch-modified linear operator of the form
\[
\Omega_0^2 \to \Omega_0^2 + m_{gap}^2.
\]

### Limitation
This does not constitute a full derivation of electroweak gauge structure from the torus wave equation alone.

### Verdict
**Validated as branch-modified linear correspondence models.**

---

## 7) Quark derivation chain

### Docs
- `docs/NATURAL_EMERGENCE_OF_INCOMPLETE_QUARK_CYCLES.md`
- `docs/COMPOSITE_CLOSURE_ALGEBRA_V1.md`
- `docs/CLOSURE_CHARGE_CHIRALITY_COMPATIBILITY_V1.md`
- `docs/EFFECTIVE_CHARGE_PROJECTION_ANSATZ_V1.md`
- `docs/QUARK_DERIVATION_CHAIN_INDEX.md`

### Status under the full wave equation
The full linear torus wave equation supplies:
- the carrier,
- the mode basis,
- the closure/spectral environment,
- the correct setting for rational transport and admissibility.

But the current quark branch derivations require additional assumptions that are not yet derivable from that equation alone:
- closure-defect values,
- weak-assisted phase compensation,
- projector/coherence charge map,
- color-phase modulation logic.

### Verdict
**Structurally compatible with the full wave equation, but not fully derived from it.**

---

## 8) Gluon branch

### Code/docs
- `src/torus_cycle_renderer/particles/gluon.py`
- `docs/DOWN_GLUON_RENDER_FOUNDATION.md`

### Status
The gluon branch is still exploratory. It lives on the same carrier and uses compatible mode/transport language, but is not yet justified by a completed full-wave derivation chain.

### Verdict
**Exploratory and not yet validated beyond carrier-level compatibility.**

---

## 9) Repository-wide conclusion

The renderer repository is now justified at the following level:

### Strongly justified
- common torus carrier
- exact linear wave equation backbone
- exact single-mode branch solutions
- exact steady-state shifted-operator solver
- exact phase-closed resonant transport for those single modes

### Partially justified / reduced
- branch-specific visible timing policies
- weak mass-gap correspondence branches
- branch styling as probe modes

### Not yet fully justified from the wave equation alone
- quark closure-defect values and charge projection
- full weak/gauge emergence
- full color dynamics

So the correct overall statement is:

> The torus-cycle-renderer now possesses a fully documented linear torus wave-equation backbone, while several non-electron sectors remain branch-level or exploratory extensions built on top of that backbone rather than fully derived consequences of it.
