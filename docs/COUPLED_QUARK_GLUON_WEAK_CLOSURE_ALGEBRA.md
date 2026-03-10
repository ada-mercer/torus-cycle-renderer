# Coupled Quark–Gluon–Weak Closure Algebra

Status: derivation scaffold / coupled-sector extension

This note extends the earlier quark closure-defect program from isolated defect bookkeeping to a coupled closure law involving:
- multiple quark-like branches,
- gluon/color-mediated interaction,
- weak-assisted compensation.

The goal is to replace the too-simple question

> does a single quark close?

with the more physical question

> when does a coupled multi-quark interacting state close?

---

## 1) Motivation

Earlier notes introduced the quark-like closure-defect idea:
\[
\Delta\phi_a = 2\pi(N_a+\delta_a),
\qquad 0\le \delta_a<1.
\]

This says a single quark branch may be closure-incomplete.

The present refinement is:
- other quarks may contribute complementary defect content,
- but global closure may still require an interaction sector to realize that closure dynamically,
- so closure is a property of the **coupled state**, not just the isolated constituent.

---

## 2) Single-branch defect reminder

For quark-like branch \(q_a\), define one-cycle return
\[
\Delta\phi_a = 2\pi(N_a+\delta_a),
\qquad N_a\in\mathbb Z,
\qquad 0\le \delta_a<1.
\]

Interpretation:
- \(N_a\): integer-return part,
- \(\delta_a\): unresolved closure defect.

An isolated closure-complete branch would satisfy
\[
\delta_a=0.
\]

The working quark hypothesis is that generic quark-like branches satisfy
\[
\delta_a\neq 0.
\]

---

## 3) Coupled-state closure law

Let a coupled state contain:
- quark-like sectors \(q_a\),
- gluon/color-mediated interaction contribution \(\Gamma_g\),
- weak-assisted contribution \(\Gamma_w\).

Then the total cycle return is postulated to satisfy
\[
\sum_a \Delta\phi_a + \Gamma_g + \Gamma_w \in 2\pi\mathbb Z.
\]

Dividing by \(2\pi\), define the reduced interaction phases
\[
\gamma_g := \Gamma_g/(2\pi),
\qquad
\gamma_w := \Gamma_w/(2\pi).
\]

Then the scalar coupled-closure condition becomes
\[
\boxed{
\sum_a \delta_a + \gamma_g + \gamma_w \in \mathbb Z
}
\]

This is the first coupled closure law.

---

## 4) Additive compensation form

A more implementation-friendly form introduces discrete compensation units.

Let:
- \(\eta_j^{(w)}\): weak compensation units,
- \(\eta_k^{(g)}\): gluon/color compensation units,
- \(m_j,n_k\in\mathbb Z\): participation counts.

Then define the coupled residual
\[
\delta_{comp}
:=
\sum_a \delta_a
-
\sum_j m_j\eta_j^{(w)}
-
\sum_k n_k\eta_k^{(g)}.
\]

The coupled-state closure condition is
\[
\boxed{
\delta_{comp} \in \mathbb Z
}
\]

This is the cleanest scalar algebra for current use.

---

## 5) Interpretation of the three pieces

### A. Quark defects
\[
\sum_a \delta_a
\]
represents incomplete constituent closure content.

### B. Weak compensation
\[
\sum_j m_j\eta_j^{(w)}
\]
represents branch/transition/chirality-sensitive assistance.

### C. Gluon compensation
\[
\sum_k n_k\eta_k^{(g)}
\]
represents color-mediated closure support and transport locking.

This separates:
- constituent incompleteness,
- weak-assisted compensation,
- gluon/color-mediated coupling.

---

## 6) Why gluon terms should not be treated as ordinary quark defects

The gluon contribution is best understood not as another constituent defect, but as an **interaction holonomy**.

In a reduced scalar description we write it as \(\gamma_g\) or \(\eta^{(g)}\), but conceptually it is closer to:
\[
\Gamma_g \sim \oint_C A_g
\]
or, more properly in a nonabelian setting,
\[
U_g(C)=\mathcal P\exp\left(i\oint_C A_g\right).
\]

So the scalar gluon term should be read as the first reduction of a deeper color-transport closure contribution.

---

## 7) Continuous phase-transport version

A more structural formulation uses total phase transport along the full coupled cycle.

For each quark-like branch define \(\phi_a(s)\), and let interaction phases be \(\Phi_g(s)\), \(\Phi_w(s)\). Then
\[
\Phi_{tot}(s)
=
\sum_a \phi_a(s)+\Phi_g(s)+\Phi_w(s).
\]

Closure requires
\[
\Phi_{tot}(1)-\Phi_{tot}(0)=2\pi n,
\qquad n\in\mathbb Z.
\]

Equivalently,
\[
\sum_a \Delta\phi_a + \Delta\Phi_g + \Delta\Phi_w = 2\pi n.
\]

This is the continuous form behind the discrete scalar law.

---

## 8) Holonomy/operator version

The most structural version treats closure as state return under a coupled transport operator.

Let the internal state live in a joint space
\[
\Psi(s) \in \mathcal H_{int}\otimes\mathcal H_{color}.
\]

Let the transport law be
\[
\frac{D\Psi}{ds}
=
\left(\sum_a \mathcal K_a + \mathcal A_g + \mathcal A_w\right)\Psi.
\]

Then after one full cycle,
\[
\Psi(1)
=
\mathcal P\exp\left[
\int_0^1 ds\left(\sum_a \mathcal K_a + \mathcal A_g + \mathcal A_w\right)
\right]\Psi(0).
\]

The strongest closure condition is
\[
\boxed{
\Psi(1)=e^{i2\pi n}\Psi(0)
}
\]

The scalar defect law is the reduced abelianized shadow of this operator condition.

---

## 9) Meson-like and baryon-like coupled closure

### Meson-like candidate
For a 2-body state:
\[
\delta_1+\delta_2+\gamma_g+\gamma_w \in \mathbb Z.
\]

### Baryon-like candidate
For a 3-body state:
\[
\delta_1+\delta_2+\delta_3+\gamma_g+\gamma_w \in \mathbb Z.
\]

The important point is that the interaction terms need not vanish.
A hadronic-like closure state may therefore be impossible to characterize correctly using quark defects alone.

---

## 10) Why this is better than the old isolated-closure story

Earlier scalar closure reasoning focused mainly on
\[
\sum_a \delta_a \in \mathbb Z.
\]

The present extension is stronger because it distinguishes:
- constituent closure content,
- dynamical interaction mediation,
- weak-assisted branch compensation.

That is more plausible for a non-asymptotic quark sector.

---

## 11) Practical working law for current theory work

The recommended current lock is:
\[
\boxed{
\sum_a \delta_a
-
\sum_j m_j\eta_j^{(w)}
-
\sum_k n_k\eta_k^{(g)}
\in \mathbb Z
}
\]

with explicit interpretation:
- \(\delta_a\): quark closure defects,
- \(\eta^{(w)}\): weak-assisted compensation units,
- \(\eta^{(g)}\): gluon/color-mediated compensation units.

This should be treated as the first usable scalar coupled closure law.

---

## 12) Exact / reduced / exploratory status

### Exact at the level of formal structure
- closure of the full coupled state should be the real criterion, not isolated single-particle closure
- a coupled closure law should include interaction-sector contributions

### Reduced working ansatz
- the scalar defect law with weak/gluon compensation terms

### Exploratory / not yet derived
- exact numerical values of \(\eta^{(g)}\)
- exact relation between color representation and compensation units
- whether weak assistance is genuinely fundamental or only an intermediate derivation scaffold in the strong sector

A first explicit candidate form for the gluon compensation term is now proposed in:
- `docs/GLUON_COMPENSATION_TERM_ANSATZ.md`

---

## 13) Working conclusion

The natural next refinement of the quark program is:

> quark-like branches are not expected to close in isolation; closure belongs to the coupled multi-quark interacting state and should be formulated through a total closure law that includes both constituent defect content and interaction-mediated compensation.

The simplest usable form of that statement is the scalar coupled closure law above. The deeper version is a holonomy/state-return condition for the full interacting internal state.
