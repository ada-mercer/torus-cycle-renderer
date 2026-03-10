# W− Branch Foundation

Status: implementation-facing foundation note

This note defines how to read the current `WMinus` branch against the full torus-wave derivation.

---

## 1) Role in the repo

`WMinus` is the charged-conjugate companion to `WPlus`.
It is best read as a **weak-channel resonant probe branch** on the common torus-wave carrier.

For the full derivation chain, read first:
- `docs/FULL_WAVE_EQUATION_DERIVATION.md`
- `docs/DERIVATION_VALIDATION_AGAINST_IMPLEMENTATION.md`
- `docs/CONSTRAINED_TORUS_TO_EM_PROJECTOR_ANSATZ.md`
- `docs/EM_FAR_FIELD_AND_MULTIPOLE_CONSEQUENCES.md`
- `docs/TRANSPORT_CURRENT_IMAGE_ANSATZ.md`
- `docs/RADIATIVE_BRANCH_AND_ATTRACTOR_QUANTIZATION.md`
- `docs/EM_SELECTION_RULES_FROM_RESONANT_ATTRACTORS.md`
- `docs/EM_RATE_AND_LINEWIDTH_ANSATZ.md`
- `docs/WEAK_BOSON_WPLUS_CLASS_FOUNDATION.md`

---

## 2) Branch-level wave statement

At the reduced wave level, the branch uses the same single-mode torus-wave structure as `WPlus`, but with opposite charged-channel orientation in the phase and loop definition.

Its reduced frequency law is of the branch-modified form
\[
\omega_W^2 = \Omega_W^2 + \frac{m_u^2}{R^2}+\frac{m_v^2}{r^2},
\qquad \Omega_W>0,
\]
which is the weak-branch analog of the exact reduced torus-wave spectrum.

So the branch remains a clean weak-channel mode on the common carrier, with the charged-conjugate sign structure implemented at the renderer/correspondence level.

---

## 3) Implementation reading

Code:
- `src/torus_cycle_renderer/particles/w_minus.py`

Interpretation:
- exact at the level of a branch-modified reduced single-mode operator,
- correspondence-level in its charged weak-boson interpretation,
- not a full electroweak gauge derivation.

---

## 4) Working conclusion

`WMinus` should be read as the charged-conjugate weak-channel probe branch paired to `WPlus`, built on the same torus-wave backbone and kept intentionally compact at the renderer level.

In EM-projector language, it plays the same reduced role as `WPlus` but with opposite charged-branch orientation, making it the natural charged-conjugate test branch for sign inheritance, current-channel reversal, and charged transition comparison.
