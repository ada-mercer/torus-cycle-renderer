# Photon Branch Foundation

Status: implementation-facing foundation note

This note defines how to read the current `Photon` branch against the full torus wave derivation.

---

## 1) Role in the repo

The current photon branch is best read as a **pure bosic probe branch** on the common torus carrier.

It is:
- a clean branch-level correspondence model,
- compatible with the full linear torus wave backbone,
- not yet a full gauge-field derivation from first principles.

For the full derivation chain, see:
- `docs/FULL_WAVE_EQUATION_DERIVATION.md`
- `docs/DERIVATION_VALIDATION_AGAINST_IMPLEMENTATION.md`
- `docs/CONSTRAINED_TORUS_TO_EM_PROJECTOR_ANSATZ.md`
- `docs/TRANSPORT_CURRENT_IMAGE_ANSATZ.md`
- `docs/RADIATIVE_BRANCH_AND_ATTRACTOR_QUANTIZATION.md`
- `docs/EM_SELECTION_RULES_FROM_RESONANT_ATTRACTORS.md`
- `docs/EM_RATE_AND_LINEWIDTH_ANSATZ.md`

---

## 2) Carrier and convention lock

The branch uses the shared torus carrier
\[
(u,v)\in T^2,
\]
with repo convention:
- bosic channel \(p\) on major angle \(u\),
- fermic channel \(p_f\) on minor angle \(v\).

For the photon correspondence branch, the implementation uses a pure-bosic limit at the renderer level:
- `pf_value = 0`
- no minor-direction transport contribution in the loop path

This should be read as a branch-level modeling lock, not yet a complete derivation of the physical photon from the full gauge sector.

---

## 3) Relation to the full wave equation

From `FULL_WAVE_EQUATION_DERIVATION.md`, exact single-mode solutions of the linear torus wave equation take the form
\[
\varphi(u,v,\tau)=A\cos\big(\nu_p u + \nu_{pf} v - \omega\tau + \phi_0\big),
\]
with
\[
\omega^2 = \Omega_0^2 + c_{int}^2\left(\frac{\nu_p^2}{R^2}+\frac{\nu_{pf}^2}{r^2}\right).
\]

The photon branch uses the same exact single-mode structural backbone, but interpreted in the pure-bosic direction.

So at the branch level:
- the carrier and single-mode logic are fully compatible with the full wave derivation,
- the physical interpretation as a photon remains correspondence-level rather than a completed gauge derivation.

---

## 4) Renderer-level meaning

The current photon renderer is useful for:
- visualizing a clean traveling-wave branch,
- isolating bosic transport structure,
- comparing a pure bosic branch against matter and weak branches.

In the newer EM-projector language, the photon branch is best interpreted as:
- a **transport/radiative branch** rather than a static monopole source branch,
- a branch whose main EM content is carried by the projected current image rather than by a nonzero static charge monopole,
- a branch through which projected transfer may be continuous at first pass, while observed discreteness can still emerge from resonant-state attractors of the interacting matter system.

It should not be overread as:
- a final electrodynamic field solver,
- a completed derivation of Maxwell emergence,
- a complete photon theory.

---

## 5) Validation status

### Exact / strongly justified
- common torus carrier
- exact single-mode torus-wave form as reduced backbone
- pure-branch visualization policy

### Reduced / correspondence-level
- branch interpretation as a photon
- pure bosic transport lock at the renderer level

### Not yet fully derived here
- full gauge emergence
- universal projector completion
- full EM field reconstruction from the branch alone
- quantitative transition rates and line strengths beyond the current projector/selection/rate ansätze

---

## 6) Working conclusion

The current `Photon` implementation is best understood as a **pure bosic single-mode correspondence branch** sitting on top of the full linear torus wave-equation backbone.

That is the strongest honest statement currently justified by both the theory notes and the repository implementation.
