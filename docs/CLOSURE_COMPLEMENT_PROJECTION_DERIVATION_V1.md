# Closure-Complement Projection Derivation v1

Status: derivation scaffold / justification note

This note addresses the key open question left by `EFFECTIVE_CHARGE_PROJECTION_ANSATZ_V1.md`:

> Why should the EM projector respond to the **closure complement** \((1-\delta)\) rather than to the raw closure defect \(\delta\)?

The result here is not a final proof. It is a structured derivation path showing why the complement rule is more natural than the raw-defect rule once one takes the universal projector picture seriously.

---

## 1) Objective

We want to justify the quark-like effective charge ansatz
\[
q_{eff}=q_*\chi(1-\delta)g(c)
\]
by relating it to the logic of the universal torus-to-EM projector.

The central idea will be:

> the EM projector should couple to the **coherently completed portion** of an internal cycle, not to the unresolved defect remainder.

If true, then the projector weight should scale with the closure complement
\[
1-\delta,
\]
not with \(\delta\) itself.

---

## 2) Starting assumptions

We keep four existing framework assumptions.

### A1. Universal projector
There is one sector-independent map
\[
\Xi \to A_\mu \to F_{\mu\nu} \to J^\mu,
\]
with no particle-specific redefinition of the EM channel.

### A2. Closure-defect label
A quark-like branch returns after one nominal orbit as
\[
\Delta\varphi = 2\pi(N+\delta),
\qquad 0<\delta<1.
\]
So the branch is not individually closure-neutral.

### A3. EM source arises from coherent projected content
The projected current \(J^\mu\) is derived from the projected field, so whatever contributes stably to EM charge/current must survive the projector as a coherent, not self-canceling, component.

### A4. Unresolved closure defect is not a stable asymptotic observable by itself
The closure-defect algebra already says that non-neutral defect is what prevents isolated asymptotic admissibility.
So raw defect should be interpreted as the **unresolved remainder**, not the completed observable sector.

---

## 3) Raw defect vs completed portion

Consider one nominal internal cycle normalized to unit measure.

If a branch carries defect \(\delta\), then its cycle decomposes conceptually into:
- a coherently completed portion of size \(1-\delta\),
- an unresolved remainder of size \(\delta\).

Schematically:
\[
1 = (1-\delta) + \delta.
\]

Interpretation:
- \(1-\delta\): the portion of the orbit that is already organized into a closure-compatible coherent sector,
- \(\delta\): the leftover piece that prevents isolated completion.

If the EM projector measures the part of the internal state that appears as a stable coherent source, it is natural for it to track the former, not the latter.

---

## 4) Why the raw-defect rule is conceptually backward

Suppose we tried the naive assignment
\[
|q_{eff}|\propto \delta.
\]

Then the larger the unresolved defect, the larger the effective visible EM charge.

That is conceptually backwards if the projector is meant to detect **coherent projected content**.

Why?
- larger \(\delta\) means the single-sector cycle is **less** complete,
- less completion means less directly coherent asymptotic contribution,
- so one should not expect a larger stable projected charge from a more incomplete orbit.

Thus, under the universal-projector interpretation, the raw-defect rule already has the wrong qualitative monotonicity.

---

## 5) Coherence principle for projection

We now state the central working principle.

### P-CP1 (coherence principle)
The magnitude of a projected EM source should scale with the amount of internal cycle content that is:
1. phase-coherent under the projector,
2. not self-canceling under one nominal orbit,
3. compatible with the closure-neutral observable channel.

Call this coherent projected fraction \(C_{EM}\).

Then the natural source ansatz is
\[
|q_{eff}| \propto C_{EM}.
\]

For a defect-bearing single cycle, the simplest first identification is
\[
C_{EM}=1-\delta.
\]

This is exactly the complement rule.

---

## 6) Why the complement is the first natural coherent fraction

A single incomplete cycle can be viewed as one full closure slot minus the unresolved remainder.

The unresolved remainder cannot by itself define the asymptotically visible source because it is precisely the piece that still requires:
- partner sectors,
- weak assistance,
- or composite completion.

So the asymptotically projectable part should be the part that is already closure-compatible within the single-sector branch.

That quantity is naturally:
\[
1-\delta.
\]

So the complement rule follows from a simple source-visibility reading:

> EM projection measures what the branch has already completed, not what it still lacks.

---

## 7) Projector analogy with interference/cancellation

There is another way to see the same point.

Suppose the universal projector is linear at the field level:
\[
A_\mu = \mathcal P_\mu[\Xi].
\]

Then under one incomplete cycle, the unresolved defect portion behaves like a piece that fails to line up with the closure-compatible sector. Such a piece tends naturally to contribute as:
- leakage,
- cancellation,
- or non-asymptotic residue,

rather than as a stable coherent source.

In contrast, the closure-completed portion can add constructively under repeated projection.

So even without writing the full projector explicitly, the sign of the argument is clear:
- unresolved defect -> incoherent / self-limiting contribution,
- closure complement -> coherent / source-like contribution.

This again favors
\[
|q_{eff}|\propto 1-\delta.
\]

---

## 8) Order-3 defect basis check

Now apply the complement rule on the minimal quark defect set:
\[
\delta\in\left\{\frac13,\frac23\right\}.
\]

Then
\[
1-\frac13 = \frac23,
\qquad
1-\frac23 = \frac13.
\]

So the branch with the **smaller closure defect** gets the **larger coherent projected EM fraction**, while the branch with the larger defect gets the smaller one.

This is exactly the qualitative ordering one would expect if charge magnitude tracks coherent projected completion.

---

## 9) Why this fits quark-like charge ordering better than the raw rule

Take the working branch assignments:
\[
\delta_u=\frac13,
\qquad
\delta_d=\frac23.
\]

Then:
- raw rule gives
  \[
  |q_u|:|q_d| = 1:2,
  \]
  which is wrong for the observed ordering;

- complement rule gives
  \[
  |q_u|:|q_d| = 2:1,
  \]
  which is exactly the desired ordering.

This by itself is not a proof, but it is strong evidence that the complement rule matches the projector-coherence interpretation more naturally than the raw-defect rule.

---

## 10) Composite-charge consistency under the complement rule

If the effective charges are
\[
q_u = +\frac23 q_*,
\qquad
q_d = -\frac13 q_*,
\]
then common composite sums work immediately:

### Two-up one-down
\[
2q_u + q_d = 2\cdot\frac23 q_* - \frac13 q_* = +q_*.
\]

### One-up two-down
\[
q_u + 2q_d = \frac23 q_* - 2\cdot\frac13 q_* = 0.
\]

### Pair-neutral channels
\[
q_u + q_{\bar u}=0,
\qquad
q_d + q_{\bar d}=0.
\]

So the complement rule not only has the better single-sector interpretation; it also supports the right composite arithmetic structure.

---

## 11) First derivation-level slogan

A useful compressed statement is:

> The closure defect \(\delta\) measures what the branch still owes to become asymptotically complete; the EM projector measures what the branch already contributes coherently. Therefore the first projected charge weight is the closure complement \(1-\delta\).

That is the cleanest one-line version of the derivation scaffold.

---

## 12) Chirality modulation slot

Nothing in the complement argument removes the chirality factor.

So the next refined rule remains
\[
q_{eff}=q_*\chi(1-\delta)g(c).
\]

Interpretation:
- \(\chi\): sign branch,
- \(1-\delta\): coherent closure-complement weight,
- \(g(c)\): chirality modulation / selection factor.

The complement argument only justifies the middle factor.

---

## 13) What this derivation still does not prove

This note does **not** yet derive:
- the explicit universal projector kernel \(\mathcal P_\mu\),
- a full field-theoretic proof that incoherent defect pieces cancel under projection,
- the exact form of \(g(c)\),
- the role of color-phase structure in modifying the complement weight,
- whether the same complement rule survives beyond the order-3 defect basis.

So this remains a structured justification note, not a final proof.

---

## 14) Working conclusion

Within the universal-projector picture, the most natural first interpretation is:

- raw defect \(\delta\) = unresolved non-asymptotic remainder,
- closure complement \(1-\delta\) = coherently projectable portion.

Therefore the effective EM charge magnitude should scale first with the closure complement, not with the raw defect:
\[
|q_{eff}|\propto 1-\delta.
\]

This is why the ansatz
\[
q_{eff}=q_*\chi(1-\delta)g(c)
\]
is currently the best-motivated projection rule in the quark-like branch program.

---

## 15) Next tasks

1. Try to write an explicit toy projector showing cancellation of the defect remainder under one incomplete orbit.
2. Test whether color-phase branches preserve or refine the complement rule.
3. Add a short summary of this argument into the quark foundation docs.
4. Compare against assisted-closure scripts to ensure the same \(\delta\) assignments remain coherent across closure and charge reasoning.
