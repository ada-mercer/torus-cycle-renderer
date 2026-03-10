# Gluon Compensation Term Ansatz

Status: derivation scaffold / first explicit gluon-term proposal

This note proposes a first candidate mathematical form for the gluon/color compensation term
\[
\eta^{(g)}
\]
introduced abstractly in `COUPLED_QUARK_GLUON_WEAK_CLOSURE_ALGEBRA.md`.

The goal is not to claim a final QCD derivation, but to move from
- symbolic placeholder,

to
- explicit reduced ansatz tied to the renderer's current color-transport picture.

---

## 1) Motivation

The coupled closure law currently reads
\[
\sum_a \delta_a
-
\sum_j m_j\eta_j^{(w)}
-
\sum_k n_k\eta_k^{(g)}
\in \mathbb Z.
\]

The weak compensation term already has a plausible branch-level role.
The gluon term has so far remained only symbolic.

We now seek the simplest useful candidate form for
\[
\eta^{(g)}.
\]

---

## 2) Design requirements

A first candidate \(\eta^{(g)}\) should satisfy:

### G1. Interaction, not constituent status
It should represent coupling/transport holonomy, not another quark defect.

### G2. Vanish when color coupling is absent
If there is no effective color-mediated coupling, the gluon compensation term should vanish.

### G3. Depend on relative color/phase organization
It should respond to phase mismatch or transport mismatch between coupled quark branches.

### G4. Be scalar-reduced but holonomy-inspired
The working ansatz may be scalar, but should be interpretable as the reduction of a deeper color transport law.

---

## 3) Minimal reduced color-holonomy ansatz

For a pair of coupled quark branches \(a,b\), define a reduced color-phase mismatch
\[
\Delta\varphi_{ab}^{(col)} := \varphi_a^{(col)} - \varphi_b^{(col)}.
\]

Let the gluon branch carry a transport strength parameter
\[
\kappa_g > 0,
\]
representing the effective amplitude of color-mediated cycle support.

Then the simplest scalar candidate compensation unit is
\[
\boxed{
\eta_{ab}^{(g)}
:=
\kappa_g\,\frac{1-\cos\big(\Delta\varphi_{ab}^{(col)}\big)}{2}
}
\]

Interpretation:
- zero when the color phases are already aligned,
- maximal when they are opposite,
- positive and bounded,
- naturally interaction-like rather than defect-like.

This is the first reduced color-holonomy ansatz.

---

## 4) Why this form is natural

The factor
\[
\frac{1-\cos(\Delta\varphi)}{2}
\]
is the simplest positive phase-mismatch measure with the right properties:
- it is zero at perfect alignment,
- it is smooth,
- it is bounded,
- it is insensitive to overall common phase shifts,
- it behaves like a quadratic mismatch measure for small phase differences.

For small mismatch,
\[
\eta_{ab}^{(g)}
\approx
\kappa_g\,\frac{(\Delta\varphi_{ab}^{(col)})^2}{4}.
\]

So weak color mismatch gives small compensation, while strong mismatch increases the interaction contribution.

---

## 5) Pairwise coupled closure law

For a two-branch coupled system, the scalar closure law becomes
\[
\delta_a + \delta_b
-
 m_w\eta^{(w)}
-
 n_g\eta_{ab}^{(g)}
\in \mathbb Z.
\]

This says:
- the two quark defects contribute incomplete closure,
- weak assistance may compensate some part,
- gluon/color-mediated mismatch can contribute an additional closure-support term.

That is already a meaningful mathematical upgrade from a purely symbolic \(\eta^{(g)}\).

---

## 6) Three-quark generalization

For a three-quark coupled state, define pairwise color-mismatch contributions
\[
\eta_{12}^{(g)},\qquad \eta_{23}^{(g)},\qquad \eta_{31}^{(g)}.
\]

Then the simplest symmetric total gluon compensation is
\[
\boxed{
\eta_{123}^{(g)}
:=
\eta_{12}^{(g)} + \eta_{23}^{(g)} + \eta_{31}^{(g)}
}
\]

or explicitly,
\[
\eta_{123}^{(g)}
=
\kappa_g\sum_{(ab)}
\frac{1-\cos\big(\Delta\varphi_{ab}^{(col)}\big)}{2}.
\]

Then baryon-like coupled closure becomes
\[
\delta_1+\delta_2+\delta_3
-
 m_w\eta^{(w)}
-
 n_g\eta_{123}^{(g)}
\in \mathbb Z.
\]

This is the cleanest first three-body ansatz.

---

## 7) Transport-winding refinement

Because the current renderer also assigns transport windings, a better gluon ansatz may include winding mismatch as well.

Let each quark branch carry effective transport winding vector
\[
\mathbf k_a=(k_{u,a},k_{v,a}).
\]

Define the normalized pairwise winding mismatch
\[
W_{ab}:=
\frac{\|\mathbf k_a-\mathbf k_b\|}{\|\mathbf k_a\|+\|\mathbf k_b\|+\varepsilon}.
\]

Then a refined pairwise gluon term is
\[
\boxed{
\eta_{ab}^{(g)}
=
\kappa_g
\frac{1-\cos\big(\Delta\varphi_{ab}^{(col)}\big)}{2}
(1+\lambda_g W_{ab})
}
\]
with \(\lambda_g\ge0\).

Interpretation:
- color-phase mismatch provides the base interaction compensation,
- transport mismatch can strengthen the amount of required gluon mediation.

This feels closer to the current renderer logic, where color and transport are both present.

---

## 8) Holonomy interpretation

This scalar ansatz should be read as the reduction of a deeper color-transport contribution.

At the operator level, one expects something like
\[
U_g(C)=\mathcal P\exp\left(i\oint_C A_g\right).
\]

The scalar quantity \(\eta^{(g)}\) is then interpreted as the first reduced measure of the nontrivial color holonomy of the coupled cycle.

So the present ansatz is not arbitrary: it is intended as a compressed summary of how strongly the color connection deviates from trivial return.

---

## 9) Exact / reduced / exploratory status

### Exact at formal level
- the interaction contribution should enter the coupled closure law
- a color-mediated term should depend on relative coupled-state organization, not just isolated constituent data

### Reduced working ansatz
- the cosine phase-mismatch form
- the winding-refined multiplicative factor

### Exploratory / not yet derived
- exact normalization \(\kappa_g\)
- exact transport coefficient \(\lambda_g\)
- nonabelian reduction to the scalar form
- exact relation to SU(3)-like color representation structure

---

## 10) Recommended current working form

For current M1/renderer work, the recommended pairwise gluon compensation ansatz is
\[
\boxed{
\eta_{ab}^{(g)}
=
\kappa_g
\frac{1-\cos\big(\Delta\varphi_{ab}^{(col)}\big)}{2}
(1+\lambda_g W_{ab})
}
\]

and for a three-quark coupled state
\[
\boxed{
\eta_{123}^{(g)} = \sum_{(ab)} \eta_{ab}^{(g)}
}
\]

with the full scalar coupled closure condition
\[
\boxed{
\sum_a \delta_a
-
\sum_j m_j\eta_j^{(w)}
-
 n_g\eta_{123}^{(g)}
\in \mathbb Z.
}
\]

This is the first explicit candidate form for the gluon compensation term that is both mathematically usable and consistent with the present quark/closure/color program.

---

## 11) Working conclusion

The gluon compensation term should be modeled first not as another constituent defect, but as a reduced measure of **color-mediated phase/transport mismatch** across the coupled quark state.

The simplest useful ansatz is therefore a positive color-phase mismatch term, optionally strengthened by transport-winding mismatch. That gives the first explicit mathematical content to \(\eta^{(g)}\) while keeping the derivation honest about its current exploratory status.
