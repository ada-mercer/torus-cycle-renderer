# Quark/Gluon Sign and Closure Interpretation

This note records the current best interpretation boundary for the quark/gluon prototype branches in the renderer repository.

It exists to prevent a common failure mode:
- collapsing **closure defect**,
- **EM sign branch**,
- **color/coherence modifiers**,
- and **observable handedness**

into one variable too early.

The quark/gluon branches in this repo are prototype correspondence branches built to visualize defect-bearing and color-transport structure on the common torus-wave carrier. They are not yet full first-principles isolated particle solutions.

---

## 1) Repository-level rule

When reading quark/gluon prototype branches, distinguish four roles:

1. **Closure-defect class**
   - examples: `delta = 1/3`, `delta = 2/3`
   - tells you how incomplete the isolated closure is

2. **EM sign branch**
   - broader-theory role often denoted by an orientation sign such as `chi`
   - determines the sign of effective charge at the reduced ansatz level

3. **Color/coherence modifier**
   - examples: `color_phase`, coherence weight, support reshaping
   - modulates projected support and coupled closure behavior

4. **Observable handedness / spin-helicity-like projection**
   - for quark prototypes: currently represented operationally through spin state / bosic handedness conventions inherited from the shared quark layer
   - for gluon prototype: currently represented through explicit `helicity`

The current repo prototypes most faithfully represent pieces of **(1)**, **(3)**, and **(4)**.
They do **not** yet encode the full broader-theory EM sign-branch ontology as a first-class renderer sign model.

---

## 2) Quark prototypes

Current best reading:
- `UQuark` and `DQuark` are **defect-bearing isolated representatives** of non-asymptotic sectors,
- they are not free asymptotic particle claims,
- `closure_defect` is the primary prototype branch label,
- effective EM charge should be read from the broader ansatz `q_eff ~ q_* chi (1-delta) g(c)`, not from raw defect alone and not from color phase alone,
- `color_phase` is best read as a coherence/support-shape modifier or coupled-closure ingredient,
- current spin-state handling remains an observable/probe-level handedness choice rather than a fully derived quark-spin ontology.

So the quark prototypes should not be overread as already exposing the full separate labels
\[(\delta,\chi,c,\text{spin})\]
canonically in code.

---

## 3) Gluon prototype

Current best reading:
- `Gluon` is a color-transport / coherence-mediating prototype branch,
- it should not be read as carrying ordinary EM sign in the same way as charged matter branches,
- `helicity` is an observable handedness / loop-orientation slot,
- dual-mode structure and effective gap are renderer-level branch parameters, not final derivations of gluon ontological structure.

This prototype is most useful as a coupled-closure / compensation visualization branch, not as a free isolated gluon claim.

---

## 4) Documentation policy

When editing quark/gluon docs or code comments:

- use **closure-defect** language for `1/3`, `2/3`, or incomplete-cycle class,
- use **EM sign branch** language only when explicitly discussing the broader effective-charge ansatz,
- use **color/coherence modifier** language for `color_phase` and support-shape interpretation,
- use **observable handedness / helicity** language for rendered loop orientation or spin/helicity-like branch tags,
- do not claim the repo already encodes all four roles as separate first-class state variables unless the code actually does.

---

## 5) Practical takeaway

The quark/gluon renderer branches currently hold up best when read as:
- prototype visualizations of defect-bearing and color-transport structure,
- useful for closure/composite intuition,
- not yet complete first-class encodings of the broader quark-sign and coupled-closure ontology.

That is the correct scope boundary for the present repository.
