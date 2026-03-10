# Modeling Scope and Interpretation

This note explains how to read the repository correctly.

---

## 1) What this repo is

This repository is a **torus-cycle visualization and structure-testing lab**.
It is meant to make internal geometry, mode structure, chirality, closure, and loop timing legible.

It is **not** yet:
- a full particle-state solver,
- a full PDE evolution engine for arbitrary torus fields,
- a complete electroweak/QCD dynamics implementation,
- a proof that every rendered branch is already the full physical state of that sector.

---

## 2) Core interpretation rule

The main repository policy is:

> Render **pure resonant modes first**.

Why:
- they are the cleanest way to see closure,
- they isolate phase transport and chirality,
- they make return periods and anchor conventions readable,
- they help distinguish geometric structure from later dynamical complications.

So when reading the code and renders, the default assumption should be:
- a rendered object is often a **clean resonant representative**,
- not necessarily the full physical state.

---

## 3) Three categories to keep distinct

### A. Fully resonant state
A state believed to close cleanly as a physical asymptotic structure.

### B. Pure resonant mode used as a probe
A deliberately isolated resonant component used to understand dynamics, even if the full physical sector may be more complicated.

### C. Full physical state with mixed / leaky / partially resonant structure
A more realistic state that may include:
- superpositions,
- leakage channels,
- closure defects,
- resonance assistance,
- only approximate return behavior.

A large part of this repo currently lives in category **B**.

---

## 4) How to read each current branch

### Electron
Best read as the current **reference resonant branch**.
This is the cleanest implemented path and the nearest thing in the repo to a stable resonant baseline.

### Photon
Best read as a **pure bosic resonant branch**.
Useful as a clean traveling-wave correspondence model.

### W+, W-, Z0
Best read as **weak-channel resonant probes**.
If the full weak-boson sector is not expected to occupy one perfectly closed resonant state, these renders should be interpreted as isolated clean resonant components, not as full electroweak closures.

### Up / down quarks
Best read as **prototype resonant skeletons** for sectors suspected not to admit a simple fully resonant isolated state.
They are exploratory and intentionally cleaner than the likely full physical state.

### Gluon
Best read as a **prototype bosonic transport branch** rather than a closed QCD-equivalent solver state.

---

## 5) Why some renders use 2 or 3 fermic windings

Several branches intentionally use low-order fermic winding counts such as 2 or 3 to obtain a full loop-cycle return that is visually readable.

This should be interpreted as a **rendering closure convention**:
- it helps produce understandable animations,
- it keeps the loop cycle finite and inspectable,
- it does not by itself prove that the physical sector is exactly that low-order closed state.

In short:
- the closure is chosen to make the resonant structure visible,
- not to overclaim final physical closure.

---

## 6) Gravity picture used alongside the renderer

Within the broader M1 interpretation, gravity is most naturally read as a **perturbation of the internal geometry**.
A leading effect is plausibly a change in an effective radius scale, especially the fermic-radius-like scale.

Schematic picture:
\[
R_f \uparrow \;\Rightarrow\; p_f \downarrow \;\Rightarrow\; p \uparrow
\]
with
\[
M^2 = p_f^2 + p^2
\]
held approximately fixed locally.

Interpretation:
- gravity stretches the local fermic geometry,
- the fermic scale decreases,
- momentum budget shifts into the bosic sector,
- the observer-level gravitational field then bookkeeping this through the GR-side channel variables.

This is an interpretation guide for reading the internal geometry, not yet a full gravity solver inside this repo.

---

## 7) Safe wording for docs and code comments

Prefer:
- "reference resonant branch"
- "probe state"
- "resonant skeleton"
- "correspondence branch"
- "exploratory prototype"

Avoid unless actually derived/implemented:
- "full particle solution"
- "complete state"
- "exact physical closure"
- "fully solved electroweak/QCD dynamics"

---

## 8) Practical rule for contributors

When adding or editing a class, state explicitly which of these it is:
1. reference resonant mode,
2. probe for a partially resonant sector,
3. full-state correspondence attempt.

If that is not stated, readers will overinterpret the render.
