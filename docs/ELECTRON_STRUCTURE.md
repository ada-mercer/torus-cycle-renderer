# Electron Structure Card (DOF, Spin, and Field-Emergence Hypotheses)

Status:
- **Implemented:** geometric/phase/loop pieces listed in Sections 1–4.
- **Correspondence hypothesis:** field-emergence picture in Section 5.

This file is the compact electron-theory reference for the current renderer implementation.

---

## 1) Electron state variables (degrees of freedom)

Current electron model (`particles/electron.py`) is a single-mode state:

\[
\mathcal E = (s,\,n_f,n_b,\,mode_p,mode_{pf},\,a,\,R,r,\,\omega_s,\,p_f,p,\,\text{anchor},\,k_{pf},k_p),
\]
where:

### Discrete DOF
- \(s\in\{++, +-, -+, --\}\): spin state label
- \((n_f,n_b)\in\mathbb Z^2\): winding sector label
- \((mode_p,mode_{pf})\in\mathbb Z^2\): single resonant mode indices
- `anchor` \(\in\{\text{static},\text{evolving}\}\)
- optional integer transport winding \((k_{pf},k_p)\)

Implementation nuance:
- in the current `Electron` renderer path, \((n_f,n_b)\) is validated metadata,
  while explicit dynamics are currently controlled by \((mode_p,mode_{pf})\), \((k_{pf},k_p)\), and continuous parameters.
  The \((n_f,n_b)\)-shifted operator is available in the solver-backed branch (`math/steady_state.py`).

### Continuous DOF
- \(R\): major radius, \(r\): minor radius
- \(a\): deformation amplitude
- \(\omega_s\): phase-speed control parameter (`phase_speed`, display-level)
- channel scales \((p_f,p)\) used for time scaling and winding ratio inference

### Derived quantities
- effective mode frequency:
\[
\omega = \sqrt{1 + \frac{mode_p^2}{R^2} + \frac{mode_{pf}^2}{r^2}}
\]
- effective time scaling:
\[
t_{eff}=t\,\frac{p}{p_f}
\]
- bosic chirality \(\chi_p\in\{+1,-1\}\) and spin phase offset \(\phi_s\)

---

## 2) Kinematics and closure

Phase field:
\[
\varphi(u,v,t)=mode_p\,u + mode_{pf}\,v - \omega t_{eff} + \phi_s.
\]

Surface deformation:
\[
\delta r(u,v,t)=a\cos\varphi.
\]

Loop transport:
\[
u(s)=u_0 + 2\pi\chi_p k_p s,
\qquad
v(s)=v_0 + 2\pi k_{pf}s,
\qquad s\in[0,1].
\]

Closure (modulo \(2\pi\)):
\[
\Delta u=2\pi\chi_p k_p,\qquad \Delta v=2\pi k_{pf}.
\]

---

## 3) How spin enters

Note on interpretation boundary:
- in the current renderer, spin is represented operationally through bosic chirality `chi_p` plus a phase-sector offset;
- in the deeper internal-geometry notes (`book/dev/INTERNAL_GEOMETRY_MAGNETIC_MOMENT_SIGN_CHECK_V1.md`), this bosic chirality is currently the best candidate for the **observable spin projection**, while fermic branch orientation is reserved for the particle/antiparticle sign slot.
- the more symmetric fermic-bosic oriented-pair sign is presently best treated as a deeper lifted-state label rather than the directly measured spin sign.

Spin affects two independent structures:

1. **Transport chirality (geometric handedness)**
   - via \(\chi_p\) in the major-cycle loop term
   - up-like states: \(\chi_p=+1\)
   - down-like states: \(\chi_p=-1\)

2. **Phase sector (internal phase branch)**
   - via \(\phi_s\in\{0,\pi/2,-\pi/2,\pi\}\)

Current mapping:

| spin state | \(\chi_p\) | \(\phi_s\) |
|---|---:|---:|
| `++` | +1 | \(0\) |
| `+-` | +1 | \(+\pi/2\) |
| `-+` | -1 | \(-\pi/2\) |
| `--` | -1 | \(\pi\) |

So in this model, spin is not only a phase label; it also flips spatial handedness of bosic transport.

---

## 4) Relation to core-momentum split

The implementation keeps the channel convention needed for directional split bookkeeping:

- bosic structure aligned with major-cycle direction,
- fermic structure aligned with minor-cycle direction,
- one can still map to directional channels via
\[
p_{k^\pm}=M\pm\frac12 p_k,
\qquad
M=\frac12(p_{k^+}+p_{k^-}).
\]

Renderer note: this repo visualizes/internal-tests the structure; it does not yet perform full global ADMC scattering calculations.

---

## 5) How electric and magnetic fields could arise (including spin)

This section is a **correspondence hypothesis**, not a fully implemented solver.

### 5.1 Bosic connection as gauge-potential seed
Introduce a bosic-cycle connection term in the internal phase flow:
\[
\partial_\mu \theta_b \;\to\; \partial_\mu \theta_b + gA_\mu.
\]
A coarse-grained effective potential can then be read from bosic phase transport.

### 5.2 Electromagnetic field definitions (standard)
\[
\mathbf E = -\nabla\Phi - \partial_t\mathbf A,
\qquad
\mathbf B = \nabla\times\mathbf A.
\]

### 5.3 Spin-coupled magnetic moment intuition
If bosic transport forms a circulating internal current, magnetic moment scales with its handedness:
\[
\boldsymbol\mu \propto q\,\chi_p\,\mathcal C_b\,\hat{\mathbf n},
\]
where \(\mathcal C_b\) is a bosic circulation measure (set by \(p\), loop radius, and winding).
Because \(\chi_p\) flips with spin branch, spin reversal flips the magnetic-moment sign/orientation.

### 5.4 Electric sector intuition
Electric response can arise from net orientation/phase asymmetry of bosic transport under interaction:
- static asymmetry -> effective charge/polarization slot,
- time-varying asymmetry -> radiative electric component,
- spin-phase branch \((\phi_s,\chi_p)\) modulates coupling strength/sign channels.

### 5.5 Practical interpretation for this repo
What is already visible in renders:
- spin-dependent bosic handedness,
- phase-sector differences,
- closed-loop transport geometry.

What remains to implement for full EM emergence:
- explicit \(A_\mu\) evolution equations,
- coupling to external fields and backreaction,
- quantitative mapping to \(q,\mu,g\)-factor observables.

---

## 6) Minimal falsifier checklist (for future promotion)

Promote the field-emergence hypothesis only if all hold:
1. one sign/branch convention predicts both electric and magnetic response consistently,
2. spin flip predicts correct magnetic-sign behavior without ad hoc patch terms,
3. the same parameter set reproduces at least one nontrivial electromagnetic observable family.
