# Effective Charge Projection Ansatz v1

Status: exploratory derivation scaffold

This note proposes a first explicit projection rule turning the quark-like sector label
\[
Q=(\delta,\chi,c)
\]
into an effective electromagnetic charge assignment.

It is intentionally conservative: the goal is not to force a final result, but to define the simplest ansatz that is compatible with the current closure, EM-sign, and weak-chirality scaffolds.

---

## 1) Objective

Previous notes established:
- closure-defect class \(\delta\) governs admissibility,
- EM orientation sign \(\chi\) governs coupling sign,
- chirality class \(c\) governs weak participation.

The missing piece is a map of the form
\[
q_{eff}=q_{eff}(\delta,\chi,c)
\]
that can produce quark-like fractional charge magnitudes without collapsing all structure into one label.

---

## 2) Minimal factorized form

The safest first ansatz is factorized:
\[
q_{eff}=q_*\,\chi\,f(\delta,c),
\qquad q_*>0.
\]

Interpretation:
- \(q_*\): universal charge scale,
- \(\chi\): sign branch,
- \(f(\delta,c)\ge 0\): projection weight.

This preserves the already-locked EM sign structure:
\[
\mathrm{sign}(q_{eff})=\chi.
\]

So the new work is entirely in the magnitude map \(f\).

---

## 3) Constraints on the projection weight

A viable first ansatz for \(f\) should satisfy:

### P1. Nonnegativity
\[
f(\delta,c)\ge 0.
\]

### P2. Neutral closed-sector normalization
For closure-neutral individually closed sectors:
\[
f(0,c)=1
\]
for the electron/positron-like reference normalization.

This means the electron-like branch recovers
\[
q_{e^\pm}=\pm q_*.
\]

### P3. Order-3 hierarchy compatibility
For the minimal quark defect basis
\[
\delta\in\left\{0,\frac13,\frac23\right\},
\]
we want distinct low-order magnitudes associated to \(1/3\) and \(2/3\).

### P4. Chirality as modulation, not sign source
The chirality label should be allowed to modulate magnitude or selection weight, but not replace the EM sign role of \(\chi\).

### P5. Composite additivity at effective-charge level
For well-separated composite constituents, effective charges should add in the usual way:
\[
Q_{eff}^{\text{comp}} = \sum_a q_{eff}^{(a)}.
\]

This is needed to compare composite sector assignments against observed integer hadron-like charges.

---

## 4) Zeroth-order projection rule

The simplest nontrivial starting point is:
\[
f_0(\delta,c)=\delta,
\qquad \delta\in\left\{0,\frac13,\frac23\right\}.
\]

Then
\[
q_{eff}^{(0)} = q_*\,\chi\,\delta.
\]

This immediately gives the order-3 charge hierarchy:
\[
|q|\in\left\{0,\frac13 q_*,\frac23 q_*\right\}.
\]

### Problem with raw zeroth order
This cannot serve as the full rule, because it gives
\[
f_0(0,c)=0
]
for closed sectors, whereas electron-like branches need full unit charge magnitude.

So \(f_0\) is useful only as the **quark-sector sub-map**, not as the universal rule.

---

## 5) Branch-dependent normalized projection

A better first ansatz is to separate the sector family:
\[
f(\delta,c;\mathcal F)=
\begin{cases}
1, & \mathcal F=\text{closed reference branch} \\
\delta\,g(c), & \mathcal F=\text{quark-like defect branch}
\end{cases}
\]

where:
- \(\mathcal F\) is a sector-family label,
- \(g(c)\) is a chirality-dependent weight with
\[
g(c)\approx 1
\]
at leading order for the dominant left-coupled quark branch.

This gives:
- electron/positron-like branch: full charge \(\pm q_*\),
- quark-like branch: fractional effective charges.

This is the cleanest first universalization that does not break the electron normalization.

---

## 6) First quark-sector charge table

Take the leading quark-sector rule
\[
f_q(\delta,c)=\delta g(c)
\]
with
\[
g(L)=1,
\qquad g(R_{supp})=\zeta,
\qquad 0<\zeta\le 1.
\]

Then the leading left-dominant effective charges are:
\[
q_u = q_*\chi_u\left(\frac13\right),
\qquad
q_d = q_*\chi_d\left(\frac23\right).
\]

This already creates the basic fractional hierarchy.

### Sign choice and naming
If one later chooses branch names so that
\[
\chi_u=+1,
\qquad
\chi_d=-1,
\]
then
\[
q_u=+\frac13 q_*,
\qquad
q_d=-\frac23 q_*.
\]

This does **not yet** match the observed Standard Model quark magnitudes.
That mismatch is important and informative.

---

## 7) Why the first raw quark map is still useful

Even though the direct map above gives the wrong magnitude ordering relative to observed \((2/3,1/3)\), it does something useful:

- it shows that closure algebra naturally creates a fractional hierarchy,
- it keeps sign and magnitude roles separate,
- it identifies the exact place where extra structure is needed.

So the failure is productive: it tells us the naive map
\[
|q|\propto \delta
\]
is too simple.

---

## 8) First corrected projection ansatz

The next simplest correction is to use the **distance from closure-neutral completion** rather than the raw defect itself.

On the order-3 subgroup,
\[
\bar\delta := 1-\delta
\quad \text{(modulo choosing representatives in }[0,1]).
\]

For the quark defect set:
\[
\delta_u=\frac13 \Rightarrow \bar\delta_u=\frac23,
\qquad
\delta_d=\frac23 \Rightarrow \bar\delta_d=\frac13.
\]

Then define
\[
f_q^{(1)}(\delta,c)=\bar\delta\,g(c)=(1-\delta)g(c).
\]

For left-dominant branches \(g(L)=1\):
\[
q_u = q_*\chi_u\frac23,
\qquad
q_d = q_*\chi_d\frac13.
\]

This is the first ansatz that reproduces the desired **magnitude ordering**.

---

## 9) Why the corrected ansatz is structurally plausible

The corrected rule
\[
|q|\propto 1-\delta
\]
can be interpreted as follows:

- \(\delta\) measures how incomplete the single-sector cycle is,
- \(1-\delta\) measures how much of a unit closure slot is effectively projected into the EM channel.

So the effective EM magnitude is not proportional to the raw defect, but to the **closure-complement available to the EM projection**.

This is conceptually reasonable if:
- closure defect lives in one internal bookkeeping channel,
- projected EM charge measures the complementary coherent portion seen by the universal projector.

This is the first nontrivial ansatz that both respects the closure algebra and moves toward observed quark charge magnitudes.

---

## 10) Trial identification with quark-like branches

Use the order-3 defect assignments:
\[
\delta_u=\frac13,
\qquad
\delta_d=\frac23.
\]

Use orientation signs:
\[
\chi_u=+1,
\qquad
\chi_d=-1.
\]

Then the corrected leading projection gives:
\[
q_u = +\frac23 q_*,
\qquad
q_d = -\frac13 q_*.
\]

This is exactly the observed quark-charge ordering at the level of magnitude/sign pattern.

Important caveat:
- this is currently an **ansatz-level success**, not yet a full derivation.

---

## 11) Meson-like and baryon-like checks under the corrected ansatz

### Meson-like neutral pair
Take an up-like branch and its opposite-sign partner:
\[
q_u + q_{\bar u} = +\frac23 q_* - \frac23 q_* = 0.
\]
Likewise for down-like pairs:
\[
q_d + q_{\bar d} = -\frac13 q_* + \frac13 q_* = 0.
\]
So neutral pair structure works as expected.

### Baryon-like charge examples
For a composite with two up-like and one down-like branch:
\[
2q_u + q_d = 2\cdot\frac23 q_* - \frac13 q_* = +q_*.
\]
For one up-like and two down-like branches:
\[
q_u + 2q_d = \frac23 q_* - 2\cdot\frac13 q_* = 0.
\]

This is an encouraging result:
- the corrected projection rule naturally supports integer composite charges from fractional constituents.

---

## 12) Chirality modulation beyond leading order

So far we used
\[
g(L)=1,
\qquad g(R_{supp})=\zeta.
\]

This allows the next refinement:
\[
q_{eff}=q_*\chi(1-\delta)g(c).
\]

Interpretation:
- sign from orientation,
- magnitude skeleton from closure-complement,
- chirality modulation from weak participation.

At leading order, one can set \(g(c)=1\) for the dominant observable branch.
Later, chirality dependence can encode small splitting, suppression, or transition weighting.

---

## 13) Minimal universal projection proposal

Combining closed reference and quark-like defect branches, the simplest unified ansatz is:
\[
f(\delta,c;\mathcal F)=
\begin{cases}
1, & \mathcal F=\text{closed reference branch}, \\
(1-\delta)g(c), & \mathcal F=\text{quark-like defect branch}.
\end{cases}
\]

Hence
\[
q_{eff}=q_*\chi\,f(\delta,c;\mathcal F).
\]

This keeps the electron normalization intact while producing the desired quark-like hierarchy on the defect branch.

---

## 14) What this ansatz gets right

At first-pass level, it achieves all of the following:

1. preserves the EM sign map \(q\propto \chi\),
2. does not identify raw closure defect directly with electric charge,
3. uses the order-3 defect basis naturally,
4. reproduces the quark-like magnitude pattern
\[
|q_u|:|q_d| = 2:1,
\]
5. supports integer composite charges from fractional constituents.

That is a strong structural checkpoint.

---

## 15) What remains open

This note does **not** yet derive:
- why the EM projector should see exactly the closure complement \((1-\delta)\),
- whether \(g(c)\) is exactly 1 for dominant branches,
- how color-phase structure modifies the projection,
- how sea/quasi-bound/environmental effects renormalize effective constituent charge,
- whether the same ansatz survives a deeper field-theoretic derivation.

So the present result is a highly structured ansatz, not yet a canonical lock.

---

## 16) Working conclusion

The first explicit effective-charge projection ansatz worth carrying forward is:
\[
q_{eff}=q_*\chi(1-\delta)g(c)
\]
for quark-like defect branches, with
\[
\delta_u=\frac13,
\qquad
\delta_d=\frac23,
\qquad
g(L)\approx1.
\]

This yields the leading pattern
\[
q_u=+\frac23 q_*,
\qquad
q_d=-\frac13 q_*,
\]
while remaining compatible with:
- the composite closure algebra,
- the EM sign map,
- and weak-chirality asymmetry.

This is the first projection rule in the current chain that actually looks capable of reproducing quark-like charge structure without obvious contradiction.

---

## 17) Next tasks

1. Derive whether the complement rule \((1-\delta)\) can be obtained from the universal projector rather than posited.
2. Add a small composite test table to the quark docs using this ansatz.
3. Check whether current renderer branch labels should be annotated with candidate effective charge under this projection.
4. Compare against weak-assisted closure locks to see whether the same \(\delta\) assignment stays consistent across both charge and closure channels.
