# Quark Derivation Chain Index

Status: navigation / synthesis note

This file documents the derivation chain and main insights developed so far for the quark-like branches in the torus-cycle-renderer repository.

It is intended as the shortest good starting point for future read-up.

---

## 1) Executive summary

Current best reading of the quark program:

- quark-like branches are **not** currently treated as fully self-closing isolated resonant states;
- they are modeled as **defect-bearing / incomplete cycles** on the common torus carrier;
- stable asymptotic admissibility is expected to arise only through:
  - composite closure,
  - weak-assisted closure,
  - or both;
- effective EM charge is currently best modeled not from raw defect \(\delta\), but from the **closure complement** \((1-\delta)\), with sign carried separately by orientation \(\chi\).

Compact current ansatz:
\[
q_{eff}=q_*\chi(1-\delta)g(c).
\]

---

## 2) Recommended reading order

### Step 1 — Why incomplete quark cycles are natural
- `docs/NATURAL_EMERGENCE_OF_INCOMPLETE_QUARK_CYCLES.md`

Core takeaway:
- incomplete closure is a natural consequence of one shared carrier geometry plus the refusal of free isolated quark closure.

### Step 2 — Composite closure algebra
- `docs/COMPOSITE_CLOSURE_ALGEBRA_V1.md`

Core takeaway:
- use additive defect classes
  \[
  \delta\in\mathbb R/\mathbb Z
  \]
  with admissibility rule
  \[
  \sum_a\delta_a\in\mathbb Z.
  \]

### Step 3 — Charge/chirality compatibility layer
- `docs/CLOSURE_CHARGE_CHIRALITY_COMPATIBILITY_V1.md`

Core takeaway:
- keep three labels separate:
  \[
  Q=(\delta,\chi,c)
  \]
  where closure, EM sign, and weak chirality do different jobs.

### Step 4 — First explicit charge projection ansatz
- `docs/EFFECTIVE_CHARGE_PROJECTION_ANSATZ_V1.md`

Core takeaway:
- raw defect mapping fails,
- complement mapping works structurally:
  \[
  q_{eff}=q_*\chi(1-\delta)g(c).
  \]

### Step 5 — Why complement is better than raw defect
- `docs/CLOSURE_COMPLEMENT_PROJECTION_DERIVATION_V1.md`

Core takeaway:
- the EM projector should measure the coherent completed part, not the unresolved remainder.

### Step 6 — Explicit toy projector on a single orbit
- `docs/TOY_PROJECTOR_FOR_CLOSURE_COMPLEMENT_V1.md`

Core takeaway:
- a coherence-selecting projector naturally suppresses the defect remainder and keeps a weight proportional to \(1-\delta\).

### Step 7 — Explicit toy projector on the torus surface
- `docs/TOY_TORUS_SURFACE_PROJECTOR_V1.md`

Core takeaway:
- the same complement logic can be lifted from a 1D orbit parameter to the full torus carrier.

### Step 8 — Local coherence functional upgrade
- `docs/LOCAL_COHERENCE_FUNCTIONAL_FOR_PROJECTOR_V1.md`

Core takeaway:
- replace the manual coherent window/region by a field-derived local coherence weight \(W[\Xi]\), and interpret the projected charge weight through the integrated coherence fraction.

### Step 9 — Coupled quark–gluon–weak closure extension
- `docs/COUPLED_QUARK_GLUON_WEAK_CLOSURE_ALGEBRA.md`

Core takeaway:
- closure is likely a property of the coupled multi-quark interacting state, not the isolated quark branch; the scalar working law therefore includes both weak and gluon/color-mediated compensation terms.

### Step 10 — First gluon compensation ansatz
- `docs/GLUON_COMPENSATION_TERM_ANSATZ.md`

Core takeaway:
- the gluon term is first modeled as a reduced color-holonomy mismatch contribution, with the simplest usable ansatz built from pairwise color-phase mismatch and optional transport-winding mismatch.

---

## 3) Main locked or semi-locked ideas so far

### A. Incomplete-cycle picture
Quark-like branches are best understood as:
- incomplete closure sectors,
- not free asymptotic isolated states,
- likely requiring partners or weak assistance for completion.

### B. Minimal defect basis
Current preferred defect basis:
\[
\delta\in\left\{0,\frac13,\frac23\right\}.
\]

Reason:
- smallest nontrivial basis supporting both pair cancellation and irreducible three-body closure.

### C. Composite closure rule
Admissible composite:
\[
\sum_a \delta_a \in \mathbb Z.
\]

### D. Weak-assisted closure rule
Assisted closure:
\[
\sum_a \delta_a - \sum_j m_j\eta_j \in \mathbb Z.
\]

### E. Distinct roles of labels
Use separate labels:
- \(\delta\): closure-defect class
- \(\chi\): EM sign branch
- \(c\): weak chirality participation
- observable handedness/spin-helicity-like projection: separate renderer/probe-level slot

Do **not** collapse these into one variable.
See also `docs/QUARK_GLUON_SIGN_AND_CLOSURE_INTERPRETATION.md` for the renderer-level interpretation boundary.

### F. Coupled closure extension
The isolated scalar defect law is now extended by the coupled-state working rule
\[
\sum_a \delta_a
-
\sum_j m_j\eta_j^{(w)}
-
\sum_k n_k\eta_k^{(g)}
\in \mathbb Z,
\]
where:
- \(\eta^{(w)}\): weak-assisted compensation units,
- \(\eta^{(g)}\): gluon/color-mediated compensation units.

This should be read as the first scalar reduction of a deeper coupled holonomy/state-return closure condition.

### G. First explicit gluon compensation ansatz
The current candidate gluon contribution is now written as a reduced color-holonomy mismatch term, beginning with pairwise form
\[
\eta_{ab}^{(g)}
=
\kappa_g
\frac{1-\cos\big(\Delta\varphi_{ab}^{(col)}\big)}{2}
(1+\lambda_g W_{ab}),
\]
and three-body aggregation
\[
\eta_{123}^{(g)} = \sum_{(ab)}\eta_{ab}^{(g)}.
\]

This remains exploratory, but it is now explicit rather than purely symbolic.

### H. Best current effective-charge ansatz
For quark-like defect branches:
\[
q_{eff}=q_*\chi(1-\delta)g(c).
\]

Upgraded projector-side reading:
\[
q_{eff}\sim q_*\chi\,\mathfrak C[\Xi]g(c),
\qquad
\mathfrak C[\Xi]:=\frac{1}{\mathrm{Area}(T^2)}\int_{T^2}W[\Xi]d\mu,
\]
with the coarse-grained approximation
\[
\mathfrak C[\Xi]\approx 1-\delta.
\]

Leading trial assignment:
\[
\delta_u=\frac13,
\qquad
\delta_d=\frac23,
\qquad
\chi_u=+1,
\qquad
\chi_d=-1,
\qquad
g(L)\approx1.
\]

Then:
\[
q_u=+\frac23 q_*,
\qquad
q_d=-\frac13 q_*.
\]

---

## 4) Why this currently looks promising

The present chain already does several things well:

1. explains why isolated quark-like states should be problematic;
2. gives a clean additive closure algebra;
3. keeps EM sign and weak chirality separate from closure defect;
4. produces the correct quark-like charge ordering at ansatz level;
5. supports natural composite charge sums, e.g.
   \[
   2q_u+q_d=+q_*,
   \qquad
   q_u+2q_d=0.
   \]

This is enough to justify continued work.

---

## 5) What remains genuinely open

The following are **not yet** derived in a final sense:

- why the exact defect assignments must be \(1/3\) and \(2/3\),
- the final universal torus-to-EM projector,
- the derivation of the coherence functional from the action rather than by toy masking,
- the exact chirality modulation factor \(g(c)\),
- the role of color-phase structure in projection,
- the relationship between these quark-like branches and full QCD-level behavior.

So the current state is:
- structurally coherent,
- increasingly explicit,
- still exploratory.

---

## 6) Current interpretation of the renderer branches

### Up/down quark renders
Best read as:
- isolated defect-bearing representatives,
- resonant probe states,
- not final free asymptotic solutions,
- local branch views of a larger coupled-closure problem rather than complete closure objects in themselves.

### Weak bosons in this context
Best read as:
- natural assistance / transition channels,
- especially relevant when testing weak-assisted closure locks.

### Gluon branch
Still exploratory; not yet fully integrated or locked, but no longer purely disconnected from the closure program: it now has a first explicit mathematical role as a candidate color-mediated compensation term in the coupled closure law.

---

## 7) Practical doc map

### Renderer branch docs
- `docs/UP_QUARK_RENDER_FOUNDATION.md`
- `docs/DOWN_GLUON_RENDER_FOUNDATION.md`
- `docs/WEAK_BOSON_WPLUS_CLASS_FOUNDATION.md`

### Core derivation docs
- `docs/NATURAL_EMERGENCE_OF_INCOMPLETE_QUARK_CYCLES.md`
- `docs/COMPOSITE_CLOSURE_ALGEBRA_V1.md`
- `docs/CLOSURE_CHARGE_CHIRALITY_COMPATIBILITY_V1.md`
- `docs/EFFECTIVE_CHARGE_PROJECTION_ANSATZ_V1.md`
- `docs/CLOSURE_COMPLEMENT_PROJECTION_DERIVATION_V1.md`
- `docs/TOY_PROJECTOR_FOR_CLOSURE_COMPLEMENT_V1.md`
- `docs/TOY_TORUS_SURFACE_PROJECTOR_V1.md`

### Upstream framework docs used repeatedly
- `book/dev/INTERNAL_GEOMETRY_FORMULATION_V1.md`
- `book/dev/INTERNAL_GEOMETRY_EM_CHANNEL_DERIVATION_V1.md`
- `docs/theory/UNIFIED_EM_FROM_TORUS_MODES.md`

---

## 8) Best next steps from here

If continuing this thread, the strongest next tasks are:

1. replace the manual coherence window/region with a derived local coherence functional \(W[\Xi]\);
2. test whether color-phase shifts rescale or reshape the coherent projected fraction;
3. reconcile code-level diagnostics with the newer closure/complement interpretation;
4. annotate quark renderer docs with the current effective-charge and closure interpretation more explicitly.

---

## 9) One-paragraph summary

The current quark program in the renderer has evolved from a prototype visual hypothesis into a reasonably coherent derivation scaffold: quark-like branches are treated as incomplete closure sectors on a shared torus carrier, composites close through additive defect cancellation, charge sign is carried by orientation rather than closure defect, and the best current source-weight rule is that the EM projector sees the closure-complement \((1-\delta)\) rather than the raw defect \(\delta\). This is not yet a final derivation, but it is now organized enough to support disciplined next-step work instead of scattered intuition.
