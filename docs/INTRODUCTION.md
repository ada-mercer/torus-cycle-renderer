# Introduction

This repository is a **torus-cycle visualization lab** for inner-structure particle models.
It is designed to keep theory/state logic separate from rendering/styling logic.

It is **not** a full validated particle solver yet.

Most important reading rule for this repo:
- a rendered branch is often a **clean resonant-mode representative**, not a claim that the full physical sector is exhausted by that one mode;
- the current repository policy is to render **pure resonant modes first**, because they make closure, chirality, phase transport, and loop timing easiest to inspect;
- sectors suspected to be only partially resonant or resonance-assisted in the full theory should therefore be read here as **probe states** or **resonant skeletons**.

---

## 1) Core geometry

Internal coordinates:
\[
(u,v)\in[0,2\pi)\times[0,2\pi),\qquad T^2=S^1\times S^1.
\]

Embedding:
\[
\mathbf X(u,v)=\big((R+r\cos v)\cos u,\ (R+r\cos v)\sin u,\ r\sin v\big).
\]

Project conventions:
- \(u\equiv\theta\): major cycle
- \(v\equiv\phi\): minor cycle

---

## 2) Channel convention (locked in code)

- **bosic channel** \(p\) is associated with major angle \(u\)
- **fermic channel** \(p_f\) is associated with minor angle \(v\)

This convention is used in:
- `particles/electron.py`
- `docs/RESONANT_LOOP_DERIVATION.md`
- `docs/ELECTRON_STEADY_STATE_EXAMPLE.md`

---

## 3) What is implemented right now

### Electron model (current production path)
A single-mode state (`ElectronState`) with:
- discrete spin state (`++`, `+-`, `-+`, `--`)
- winding sector label
- resonant mode integers
- anchor mode (`static`/`evolving`)
- channel scales (`pf_value`, `p_value`)

Current nuance: in `Electron`, rendered dynamics are primarily driven by resonant mode + transport winding; the explicit \((n_f,n_b)\)-shifted operator path is available in the solver-backed branch (`math/steady_state.py`).

Interpretation boundary:
- the current renderer electron path is best read as a **matter-branch observable slice**,
- bosic chirality is the best current interpretation of the observable spin projection in this repo,
- deeper fermic-branch / lifted-sign structure from the broader theory is not yet represented here as a full first-class renderer sign model.
- see `docs/SIGN_ARCHITECTURE_AND_INTERPRETATION.md`.

Important split:
- `math/steady_state.py` realizes the full linear steady-state shifted-operator problem directly;
- most particle classes in `particles/` are compact branch ansätze built on that same torus-wave backbone rather than direct runtime PDE evolvers.

Phase/deformation law:
\[
\varphi(u,v,t)=mode_p\,u + mode_{pf}\,v - \omega\,t_{eff} + \phi_s,
\qquad
\delta r\propto\cos\varphi.
\]

with
\[
t_{eff}=t\cdot\frac{p}{p_f},
\qquad
\omega=\sqrt{1+\frac{mode_p^2}{R^2}+\frac{mode_{pf}^2}{r^2}}.
\]

Transport loop:
\[
u(s)=u_0+2\pi\chi_p k_p s,
\qquad
v(s)=v_0+2\pi k_{pf}s,
\qquad s\in[0,1],
\]
where \(\chi_p\in\{+1,-1\}\) is bosic chirality from spin state.

### Photon model
`Photon` now has a dedicated state path (`PhotonState`) with:
- helicity-like handedness slot (`helicity=±1`),
- pure bosic branch lock: `pf_value = 0`,
- pure major-cycle transport (no \(\phi\)-direction transport component),
- traveling-wave deformation with a small harmonic texture term.

This is still correspondence-level visualization logic (not full gauge-field evolution).
See `docs/PHOTON_BRANCH_FOUNDATION.md` for the branch-level connection to the full torus-wave derivation.

### W± weak-boson correspondence models
`WPlus` / `WMinus` provide first-pass weak-channel state paths with:
- helicity slot (`helicity=±1`),
- charged, massive branch lock via positive `mass_gap`,
- active transport in both torus directions (helical loop),
- conjugate charged orientation between `W+` and `W-`,
- single-mode deformation with weak texture term.

Interpretation note:
- these classes are best read as **weak-channel resonant probe branches**;
- they are especially useful if the full weak-boson sector is suspected not to sit in one perfectly self-closing isolated resonant state;
- the render therefore isolates a clean resonant component of the weak sector rather than claiming a complete electroweak field solution or a final isolated-state description.

### Z0 neutral weak-boson correspondence model
`ZBoson` provides a first-pass neutral weak-channel state path with:
- helicity slot (`helicity=±1`),
- neutral, massive branch lock via positive `mass_gap`,
- active transport in both torus directions without charged-conjugate orientation,
- single-mode deformation with neutral-branch texture term.

These are renderer-level weak-channel correspondence branches: useful as clean probe modes, but not full electroweak gauge solvers or locked final isolated-state descriptions.
See `docs/WEAK_BOSON_WPLUS_CLASS_FOUNDATION.md`, `docs/WMINUS_BRANCH_FOUNDATION.md`, and `docs/ZBOSON_BRANCH_FOUNDATION.md`.
These branch notes now also point into the EM projector / radiative / selection-rule chain, not only the torus-wave backbone.

### Up/down-quark prototype branches (exploratory)
`UQuark` and `DQuark` are implemented as prototypes with closure-defect + weak-assist lock hypotheses.
They are now selectable in CLI, but remain exploratory in theory status.

Interpretation note:
- quark renders should be read as **defect-bearing resonant probe branches** or **resonant skeletons** for non-asymptotic sectors suspected not to admit a simple fully resonant isolated state;
- they are best interpreted as isolated representatives of incomplete-closure sectors, not as free asymptotic particle states;
- current visual closure choices are intentionally kept low-order and readable, not presented as proof that the physical quark sector is exactly that closed mode;
- the current theory direction now extends beyond isolated defect bookkeeping toward **coupled closure**, where other quarks plus gluon/color-mediated and possibly weak-assisted compensation may be required for full cycle completion.

See `docs/UP_QUARK_RENDER_FOUNDATION.md`, `docs/DOWN_GLUON_RENDER_FOUNDATION.md`, `docs/COUPLED_QUARK_GLUON_WEAK_CLOSURE_ALGEBRA.md`, and `docs/GLUON_COMPENSATION_TERM_ANSATZ.md`.

### Gluon prototype branch (exploratory)
`Gluon` is implemented as an exploratory color-transport / coherence-mediating prototype branch.
It is now selectable in CLI, but remains exploratory in theory status and is not yet integrated into the closure-charge derivation chain at the same level as the quark branches.
See `docs/DOWN_GLUON_RENDER_FOUNDATION.md`.

### Rendering stack
- Matplotlib: fast scripted GIF/MP4 (now with optional parallel frame rendering)
- Plotly: depth-strong interactive/static export
- Geometry export (`npz` + `obj`) for external engines

### Loop architecture (current)
Loop generation has been split into a dedicated layer:
- `loops/loop_model.py`
  - `ParticleLoop` (loop construction/transport)
  - `LoopGeometry` (u/v coordinates + metadata)
  - phase-lock helpers for full return-cycle handling

Particles now expose `loop_geometry(...)` and can still keep `resonant_loop(...)` as a compatibility shim.

---

## 4) Wave-theory correspondence level

The full derivation is now documented in:
- `docs/FULL_WAVE_EQUATION_DERIVATION.md`
- `docs/DERIVATION_VALIDATION_AGAINST_IMPLEMENTATION.md`
- `docs/CONSTRAINED_TORUS_TO_EM_PROJECTOR_ANSATZ.md`
- `docs/EM_FAR_FIELD_AND_MULTIPOLE_CONSEQUENCES.md`
- `docs/TRANSPORT_CURRENT_IMAGE_ANSATZ.md`
- `docs/RADIATIVE_BRANCH_AND_ATTRACTOR_QUANTIZATION.md`
- `docs/EM_SELECTION_RULES_FROM_RESONANT_ATTRACTORS.md`
- `docs/EM_RATE_AND_LINEWIDTH_ANSATZ.md`
- `docs/EM_CALIBRATION_STRATEGY.md`
- `docs/EM_PROJECTOR_STATUS_MAP.md`

The short version is that the repo sits on the linear torus wave equation
\[
\partial_\tau^2\varphi - c_{int}^2\Delta_n\varphi + \Omega_0^2\varphi = 0,
\]
with exact shifted spectrum
\[
\omega_{rs}^2 = \Omega_0^2 + c_{int}^2\left(\frac{(r+n_b)^2}{R^2}+\frac{(s+n_f)^2}{r^2}\right).
\]

The current electron deformation law is an exact single-mode solution of the reduced linear theory when the repo's visible-time variable is identified with the internal wave time. The repo then adds a renderer-level timing policy through `t_eff`.

Important: current electron rendering uses a **single explicit mode**; it does not yet run full time-dependent PDE evolution for general superpositions.

### Current repository policy for mode choice
The default modeling policy is:
1. render **pure resonant modes** first,
2. understand their closure and transport structure clearly,
3. only then move toward mixed, leaking, metastable, or partially resonant states.

This means many classes here are intentionally cleaner than the full physical state may eventually be.

---

## 5) Spin semantics used here

For the matter branch in current code:
- spin inversion flips **bosic chirality** (major-cycle handedness)
- fermic orientation is kept fixed
- spin state also selects a phase offset \(\phi_s\)

So spin affects both:
1. transport handedness (\(\chi_p\)) and
2. phase sector (\(\phi_s\)).

---

## 6) Implemented vs exploratory

### Implemented and testable in this repo
- torus geometry + loop closure
- spin-dependent bosic chirality
- anchor-aware cycle timing
- full loop-state return timing (`loop_cycle_time`)
- renderer/backend separation
- parallelized rendering paths (per-frame + per-job)

### Exploratory (not yet fully implemented here)
- full Dirac-level spinor dynamics
- nonlinear/leaky wave channels in production renderer
- full electromagnetic emergence model
- direct calibration to measured particle observables

Use this repo as a disciplined visualization + structure-testing environment.
