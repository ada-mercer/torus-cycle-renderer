# W+ Class Foundation (Renderer + Theory Contract)

This document defines the minimal theory-to-code contract for introducing a renderable `W+` class.

## 1) Goal

Add a weak-channel resonant probe class that is:
- mathematically aligned with the weak-channel derivation,
- consistent with existing particle API (`AbstractParticle`),
- non-ad-hoc relative to photon/electron EM mapping,
- explicit about being a clean weak-sector probe branch rather than a final full isolated-state description.

## 2) Theory contract

For the full wave backbone, read first:
- `docs/FULL_WAVE_EQUATION_DERIVATION.md`
- `docs/DERIVATION_VALIDATION_AGAINST_IMPLEMENTATION.md`
- `docs/CONSTRAINED_TORUS_TO_EM_PROJECTOR_ANSATZ.md`
- `docs/EM_FAR_FIELD_AND_MULTIPOLE_CONSEQUENCES.md`
- `docs/TRANSPORT_CURRENT_IMAGE_ANSATZ.md`
- `docs/RADIATIVE_BRANCH_AND_ATTRACTOR_QUANTIZATION.md`
- `docs/EM_SELECTION_RULES_FROM_RESONANT_ATTRACTORS.md`
- `docs/EM_RATE_AND_LINEWIDTH_ANSATZ.md`

Use the charged weak branch from:
- `docs/theory/WEAK_BOSON_WPLUS_DERIVATION.md`

This class note should be read as a **branch-modified linear correspondence contract** built on the common torus-wave carrier, not as a standalone full electroweak derivation.

Core equations:

1. Mode phase:
\[
\phi = m_u u + h m_v v - \omega_W t + \phi_0,
\quad h\in\{+1,-1\}.
\]

2. Massive dispersion:
\[
\omega_W^2 = \Omega_W^2 + \frac{m_u^2}{R^2} + \frac{m_v^2}{r^2},
\quad \Omega_W>0.
\]

This is the weak-branch analog of the exact reduced torus-wave spectrum, i.e. a branch-modified linear operator where the mass-gap contribution plays the role of a positive extra baseline term in the mode frequency.

3. Deformation:
\[
\delta r = a\,[\cos\phi + \beta\sin(2\phi+\delta_h)].
\]

4. Helical loop:
\[
u(s)=2\pi k_u s + \alpha_u t,
\quad
v(s)=2\pi h k_v s + \alpha_v t,
\quad s\in[0,1].
\]

## 3) Class API contract

State object should provide:
- `helicity` (`±1`)
- `resonant_mode` (`mode_u`, `mode_v`)
- `transport_winding` (`k_u`, `k_v`)
- `mass_gap` (`Omega_W` proxy)
- geometry/deformation controls

Class behavior must implement:
- `params` (ParticleParams)
- `deformation(u,v,t)`
- `resonant_loop(t, points)`
- `cycle_time()`

## 4) Policy alignment

- Class should inherit from `WeakBosonParticle`.
- `resonance_coupling` must remain in `[0,1]` (family policy).
- Keep single-map compatibility with unified EM docs (`Xi -> A -> F -> J`) by avoiding particle-specific EM redefinitions.
- Interpret the class as a **weak-channel resonant probe branch**: a clean resonant component used for visualization and structure-testing, not a claim that the full weak-boson sector is already represented here as a fully self-closing isolated physical state.

## 5) Acceptance checks for first merge

A. **Build check:** class discoverable via `build_scene("wplus")`.

B. **Render check:**
- frame render succeeds on both backends,
- cycle render succeeds with stable closure.

C. **Helicity check:**
- flipping helicity changes handedness/sign of loop `v` winding term.

D. **Mass-gap check:**
- increasing `mass_gap` decreases `cycle_time` through `omega_W`.

E. **Non-ad-hoc check:**
- no new EM law path; weak branch differs only by sector/state parameters.

## 6) Current implementation status

Implemented in code as:
- `src/torus_cycle_renderer/particles/w_plus.py`
- `src/torus_cycle_renderer/particles/w_minus.py` (charged-conjugate companion)
- scene aliases: `wplus`, `w+`, `wminus`, `w-`
- side-by-side helper: `scripts/render_weak_pair.py`

This is a correspondence renderer class family: a clean weak-sector probe implementation sitting on the common torus-wave backbone, not yet a full electroweak gauge solver and not a locked final isolated-state description.

In the newer EM-projector language, the charged weak branch should be read as:
- carrying nonzero sign-definite EM branch content at the reduced projector level,
- participating in projected current/transport structure rather than only static charge bookkeeping,
- and serving as a branch-level test case for charged-sector sign inheritance and charged-transition selection rules.
