# Z Boson Branch Foundation

Status: implementation-facing foundation note

This note defines how to read the current `ZBoson` branch against the full torus-wave derivation.

---

## 1) Role in the repo

`ZBoson` is the neutral weak-channel companion branch in the current renderer repository.
It is best read as a **neutral weak-channel resonant probe branch** on the common torus-wave carrier.

For the full derivation chain, read first:
- `docs/FULL_WAVE_EQUATION_DERIVATION.md`
- `docs/DERIVATION_VALIDATION_AGAINST_IMPLEMENTATION.md`
- `docs/CONSTRAINED_TORUS_TO_EM_PROJECTOR_ANSATZ.md`
- `docs/EM_FAR_FIELD_AND_MULTIPOLE_CONSEQUENCES.md`
- `docs/TRANSPORT_CURRENT_IMAGE_ANSATZ.md`
- `docs/RADIATIVE_BRANCH_AND_ATTRACTOR_QUANTIZATION.md`
- `docs/EM_SELECTION_RULES_FROM_RESONANT_ATTRACTORS.md`
- `docs/EM_RATE_AND_LINEWIDTH_ANSATZ.md`

---

## 2) Branch-level wave statement

At the wave-equation level, the current `ZBoson` path uses the same torus single-mode backbone as the other reduced branches, but introduces:
- a positive neutral weak mass-gap term,
- a two-branch neutral mixture at the renderer level,
- no charged-conjugate sign inversion in the loop definition.

So the branch can be understood as a compact neutral weak-sector ansatz built on the branch-modified linear torus operator.

The primary reduced frequency law remains of the form
\[
\omega_Z^2 = \Omega_Z^2 + \frac{m_u^2}{R^2}+\frac{m_v^2}{r^2},
\qquad \Omega_Z>0,
\]
with the implemented deformation using a mixed neutral branch superposition.

---

## 3) Implementation reading

Code:
- `src/torus_cycle_renderer/particles/z_boson.py`

Interpretation:
- exact at the level of branch-modified reduced torus-wave building blocks,
- reduced/intermediate in its neutral two-branch mixing ansatz,
- not a full derivation of the physical Z sector from electroweak gauge dynamics.

---

## 4) Working conclusion

`ZBoson` should be read as a neutral weak-channel probe branch built on the common torus-wave backbone, using a compact mixed neutral ansatz to avoid an unrealistically trivial single-wave appearance while staying inside the renderer's reduced-mode policy.

Sign/chirality reading:
- neutrality belongs to branch identity through the neutral mixing sector,
- any helicity/handedness tag remains separate from charged/neutral branch identity,
- weak coupling chirality should not be collapsed into the neutral branch label itself.

This keeps `Z` aligned with the layered weak-sector interpretation summarized in `book/dev/INTERNAL_GEOMETRY_WEAK_SECTOR_SIGN_CHIRALITY_SYNTHESIS_V1.md`.

In EM-projector language, it is the natural neutral weak test branch: vanishing monopole content at leading order should coexist with nontrivial higher-moment / transport structure, making it a useful branch for checking the distinction between charged and neutral projector output.
