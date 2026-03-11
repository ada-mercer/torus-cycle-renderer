# Sign Architecture and Interpretation

This note records the current best interpretation boundary for sign/chirality structure in the renderer repository.

It exists to prevent a common mistake:
- collapsing **branch identity**,
- **observable handedness/spin/helicity**,
- and **deeper internal lifted-state signs**

into one sign too early.

The renderer repo is a reduced observable/probe layer built on the torus-wave carrier. It does **not** yet encode the full internal sign ontology of the broader theory in a first-class code model.

---

## 1) Repository-level rule

When reading a rendered particle branch, distinguish three roles:

1. **Branch identity**
   - examples: electron matter branch, `W+`, `W-`, `Z`, photon
   - carries charged/neutral or matter/antimatter branch identity at the interpretation level

2. **Observable handedness / spin / helicity slot**
   - examples: bosic chirality for the electron matter branch, helicity for photon/W/Z classes
   - controls the rendered loop handedness and observable projection-level orientation

3. **Deeper internal lifted-state sign**
   - examples in broader theory: fermic-bosic oriented-pair sign, monodromy/bivector-like labels
   - currently not represented as a fully explicit first-class slot across the repo

The current repo most faithfully represents **(2)** and selected parts of **(1)**.
It should not be overread as already encoding the full content of **(3)**.

---

## 2) Electron matter branch

Current best reading:
- the renderer electron class is a **matter-branch observable slice**,
- bosic chirality is the best current interpretation of the **observable spin projection**,
- fermic matter/antimatter branch orientation is not yet exposed as a full first-class renderer sign slot,
- any deeper fermic-bosic oriented-pair sign should currently be treated as broader-theory structure, not directly as the renderer's spin variable.

So the current `electron.py` spin handling is best read as:
- operationally correct for the observable matter-branch spin slot,
- incomplete as a full particle/antiparticle + lifted-sign ontology.

---

## 3) Photon branch

Current best reading:
- photon branch identity = pure bosic / massless-like branch,
- helicity = observable handedness sign,
- no fermic branch sign is present.

This is already a clean separation and should be preserved.

---

## 4) Weak branches

Current best reading:
- `W+` / `W-` class identity carries the **charged branch identity**,
- `helicity` carries the **observable handedness / loop-orientation sign**,
- left-biased weak coupling belongs to the **interaction-selection layer**, not to branch identity or helicity alone,
- `Z` branch identity is neutral by channel construction, with any helicity tag remaining separate.

This is a good reduced-layer separation and should be kept explicit.

---

## 5) Documentation policy

When editing repo docs or code comments:

- use **branch identity** language when talking about `W+` vs `W-`, charged vs neutral, or matter-branch vs photon-like branch,
- use **spin/helicity/handedness** language when talking about rendered loop orientation or observable projection-level orientation,
- use **lifted-state / deeper internal sign** language only when explicitly stepping beyond what the repo directly implements,
- do not claim the repo already solves the full broader-theory sign structure unless the code model actually represents it.

---

## 6) Practical takeaway

The renderer repository currently holds up best when read as:
- a torus-wave-based visualization / structure-testing lab,
- with clean observable/probe branch representatives,
- not a complete first-principles encoding of every sign layer in the deeper internal geometry.

That is not a flaw; it is the correct scope boundary.
