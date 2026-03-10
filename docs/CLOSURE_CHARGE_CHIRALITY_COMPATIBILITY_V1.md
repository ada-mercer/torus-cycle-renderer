# Closure–Charge–Chirality Compatibility v1

Status: derivation scaffold / compatibility layer

This note adds a first compatibility layer on top of the composite closure algebra. The goal is not to finish the full electroweak story, but to show how three structures can coexist without contradiction:

1. closure-defect class,
2. effective EM charge sign,
3. weak-chiral bias.

---

## 1) Objective

We already have a first closure algebra for quark-like sectors:
\[
\delta \in \mathbb R/\mathbb Z,
\qquad
\text{admissible composite} \iff \sum_a \delta_a \in \mathbb Z.
\]

The next question is:

> Can closure defect, charge assignment, and weak coupling bias be placed on the same sector labels without forcing contradiction?

This note argues: **yes, at first-pass compatibility level**.

---

## 2) Three distinct labels

To avoid overloading one quantity, assign three separate labels to a quark-like sector \(Q\):
\[
Q \equiv (\delta,\chi,c).
\]

Where:
- \(\delta\in\mathbb R/\mathbb Z\): closure-defect class,
- \(\chi\in\{+1,-1\}\): orientation / EM-sign branch,
- \(c\in\mathcal C\): chirality-coupling class (left-biased vs suppressed-right slot).

Interpretation:
- \(\delta\) controls **closure admissibility**,
- \(\chi\) controls **EM coupling sign**,
- \(c\) controls **weak-transition participation strength**.

These should not be identified with each other.

---

## 3) EM sign structure stays independent

From the EM derivation scaffold, the signed coupling is
\[
q = q_*\chi,
\qquad q_*>0,
\qquad \chi\in\{+1,-1\}.
\]

So EM sign comes entirely from \(\chi\), not from \(\delta\).

### Immediate consequence
Two sectors can share the same closure-defect class but have opposite EM sign if they lie on opposite orientation branches.

This is good: it means closure algebra does not have to carry the entire burden of charge sign.

---

## 4) Weak chirality bias stays independent

From the weak-channel construction, charged weak transitions are left-biased at leading order.

So the weak label should be represented by a chirality participation class, schematically:
\[
c \in \{L, R_{supp}\}
\]
or, more generally, by a weight pair
\[
(\kappa_L,\kappa_R),
\qquad \kappa_L > \kappa_R.
\]

Again, this should not be identified with closure defect directly.

### Immediate consequence
A sector may:
- carry a closure defect,
- have a given EM orientation sign,
- and still be left-biased under weak transitions

without any of these labels being forced to coincide numerically.

---

## 5) First compatibility principle

The simplest consistent rule is:

> Closure class, EM orientation sign, and weak chirality participation are **independent labels constrained only at the composite level**.

So the state space is not one number but a product-like label space:
\[
\mathcal S_Q \sim \mathcal D \times \mathcal O \times \mathcal W,
\]
with:
- closure-defect sector \(\mathcal D\),
- orientation-sign sector \(\mathcal O\),
- weak-chirality sector \(\mathcal W\).

This is the least ad hoc compatibility rule because it avoids forcing one observable structure to fake another.

---

## 6) Minimal order-3 defect basis with independent sign branch

Take the first defect basis:
\[
\mathcal D = \left\{0,\frac13,\frac23\right\}.
\]
Take the orientation sector:
\[
\mathcal O = \{+1,-1\}.
\]
Take the weak-chirality sector as left-biased by default:
\[
\mathcal W = \{L, R_{supp}\}.
\]

Then a quark-like candidate sector can be written as
\[
Q_{\alpha} = (\delta_{\alpha},\chi_{\alpha},c_{\alpha}).
\]

This gives enough structure to track:
- closure neutrality,
- charge sign,
- weak selection behavior,

without contradiction.

---

## 7) Composite constraints split naturally into three channels

A composite should satisfy different constraints in different channels.

### A. Closure-neutrality constraint
\[
\sum_a \delta_a \in \mathbb Z.
\]

### B. EM charge constraint
Total charge is
\[
Q_{\text{EM}} = q_*\sum_a \chi_a.
\]
This may vanish or not, depending on the composite type.

### C. Weak-transition compatibility
Allowed weak transitions must respect the chirality rule of the participating sectors, schematically:
\[
\text{charged weak transition strength} \propto \sum_a \kappa_L^{(a)} - \sum_a \kappa_R^{(a)}
\]
with left-biased sectors dominating at leading order.

So the three constraints are related but not identical.

---

## 8) Why closure class should not be identified with charge directly

It is tempting to try to read electric charge directly off the closure defect, e.g. by saying “\(1/3\) defect means charge \(1/3\).” That is too quick.

Reason:
- closure class measures return mismatch on the internal cycle,
- charge sign comes from orientation branch \(\chi\),
- weak bias comes from chirality participation,
- observed effective charge magnitude may depend on how these structures project together.

So the safe first statement is:

> closure defect can help organize charge structure, but it should not yet be equated directly with electric charge magnitude without an additional projection rule.

That keeps the theory honest.

---

## 9) A first compatibility ansatz for effective charge magnitude

A minimal exploratory ansatz is to separate:
\[
q_{eff} = q_*\,\chi\,f(\delta,c),
\]
where:
- \(\chi\) fixes sign,
- \(f(\delta,c)\) is a nonnegative projection weight depending on closure class and chirality participation.

The simplest order-3 trial would be:
\[
f\left(\frac13, c\right) \sim \frac13,
\qquad
f\left(\frac23, c\right) \sim \frac23,
\]
up to sector normalization and composite/environmental corrections.

This gives a way for thirds in the closure algebra to become candidate thirds in effective charge magnitude, **without** forcing that identity at the algebraic level.

---

## 10) Up/down-like trial compatibility map

A conservative first trial assignment is:
\[
Q_u \sim \left(\frac13,\chi_u,c_u\right),
\qquad
Q_d \sim \left(\frac23,\chi_d,c_d\right).
\]

Then effective charge magnitudes might arise via projection weights:
\[
|q_u| \propto f\left(\frac13,c_u\right),
\qquad
|q_d| \propto f\left(\frac23,c_d\right).
\]

At this stage, the compatibility claim is **not** that this already reproduces observed quark charges exactly. The claim is more modest:

- the closure algebra supplies a natural discrete hierarchy,
- the EM sign map supplies sign cleanly,
- the weak sector supplies chirality asymmetry cleanly,
- so a unified charge/chirality projection is now plausible rather than impossible.

---

## 11) Meson-like and baryon-like composites under the compatibility layer

### Meson-like composite
A meson-like closure-neutral pair could satisfy:
\[
\delta_a + \delta_b \in \mathbb Z,
\qquad
\chi_a + \chi_b = 0.
\]

So closure neutrality and EM neutrality can both be realized together, but they are separate conditions.

### Baryon-like composite
A baryon-like composite could satisfy:
\[
\delta_1 + \delta_2 + \delta_3 \in \mathbb Z,
\]
while allowing
\[
\chi_1 + \chi_2 + \chi_3 \neq 0
\]
if the composite is electrically charged.

This is important: closure-neutrality does **not** force EM neutrality.
That is exactly what we need.

---

## 12) Weak-assisted closure under the compatibility layer

For weak-assisted closure, the condition becomes:
\[
\sum_a \delta_a - \sum_j m_j\eta_j \in \mathbb Z,
\]
while the weak process itself is weighted by chirality participation.

So the weak channel now plays two conceptually separate roles:
1. **closure compensation** through \(\eta_j\),
2. **transition selection/bias** through chirality label \(c\).

This is actually a feature, not a bug. The weak sector is naturally the place where both assisted closure and left-bias can coexist.

---

## 13) Minimal compatibility table

| Structure | Symbol | First role | Current safe interpretation |
|---|---|---|---|
| Closure-defect class | \(\delta\) | internal return mismatch | controls closure admissibility |
| Orientation sign | \(\chi\) | EM sign branch | controls sign of coupling |
| Chirality class | \(c\) or \((\kappa_L,\kappa_R)\) | weak participation | controls left-bias / suppression |
| Effective charge | \(q_{eff}\) | projected observable | emerges from sign + projection weight |

This is the cleanest current bookkeeping layer.

---

## 14) What this layer achieves

It shows that the quark-like sector can consistently carry:
- a nontrivial closure class,
- an EM sign branch,
- a weak-chiral bias,

without forcing one of those structures to fake another.

That is the key compatibility result.

---

## 15) What remains open

This note does **not** yet derive:
- the exact projection rule \(f(\delta,c)\),
- the observed quark charge magnitudes from first principles,
- the full flavor structure,
- the color dependence beyond placeholder phase-branch language,
- the final electroweak/QCD mapping.

So this is a compatibility note, not a completed Standard Model replacement.

---

## 16) Working conclusion

A clean first-pass unified label for quark-like sectors is:
\[
Q = (\delta,\chi,c),
\]
with:
- closure class \(\delta\) governing admissibility,
- orientation sign \(\chi\) governing EM coupling sign,
- chirality class \(c\) governing weak participation.

This is enough to make the incomplete-cycle picture compatible with both charge structure and weak left-bias at a structural level.

The next real derivation task is then:

> construct the projection rule that turns \((\delta,\chi,c)\) into quantitative effective charge assignments.
