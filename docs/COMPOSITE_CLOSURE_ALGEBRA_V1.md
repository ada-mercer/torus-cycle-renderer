# Composite Closure Algebra v1

Status: derivation scaffold / working algebra

This note gives a first explicit algebra for how defect-bearing quark-like cycles can combine into admissible composite states in M1.

It is intended as the next step after `NATURAL_EMERGENCE_OF_INCOMPLETE_QUARK_CYCLES.md`.

---

## 1) Objective

Define a minimal closure algebra that distinguishes clearly between:

1. **isolated closure**,
2. **assisted closure**,
3. **composite closure**.

The main target is a compact rule for when a collection of defect-bearing sectors can be admitted as a stable composite endpoint.

---

## 2) Starting point

For a quark-like branch, write one-orbit return as
\[
\Delta\varphi_a = 2\pi (N_a + \delta_a),
\qquad N_a\in\mathbb Z,
\qquad 0\le \delta_a < 1.
\]

Here:
- \(N_a\) is the integer-return part,
- \(\delta_a\) is the closure defect.

Interpretation:
- \(\delta_a=0\): individually closed sector,
- \(\delta_a\neq 0\): incomplete cycle.

---

## 3) Minimal additive closure law

For a composite built from sectors \(a=1,\dots,n\), define total return phase
\[
\Delta\varphi_{\text{tot}}=
\sum_{a=1}^n \Delta\varphi_a
=2\pi\left(\sum_a N_a + \sum_a \delta_a\right).
\]

Since the integer parts always combine into an integer, composite closure is controlled by defect sum alone.

### Composite closure condition
\[
\sum_a \delta_a \in \mathbb Z.
\]

This is the basic M1 composite admissibility rule.

---

## 4) Defect classes modulo 1

It is natural to work modulo 1:
\[
\delta_a \in \mathbb R / \mathbb Z.
\]

Then defects form an additive class algebra under
\[
[\delta_1] + [\delta_2] = [\delta_1 + \delta_2].
\]

A composite is admissible exactly when its total class is the neutral element:
\[
[\delta_{\text{tot}}]=[0].
\]

So the closure-defect algebra is just an additive defect-cancellation algebra on the compact group \(\mathbb R/\mathbb Z\), with the physically relevant working subset usually taken to be a small rational set.

---

## 5) Minimal rational quark sector

The smallest nontrivial composite-friendly choice is the order-3 subgroup
\[
\left\{0,\frac13,\frac23\right\}\subset \mathbb R/\mathbb Z.
\]

Addition table modulo 1:

| + | 0 | 1/3 | 2/3 |
|---|---:|---:|---:|
| 0 | 0 | 1/3 | 2/3 |
| 1/3 | 1/3 | 2/3 | 0 |
| 2/3 | 2/3 | 0 | 1/3 |

This already gives the key closure patterns:
- \(1/3 + 2/3 = 0\) mod 1,
- \(1/3 + 1/3 + 1/3 = 0\) mod 1,
- \(2/3 + 2/3 + 2/3 = 0\) mod 1.

So this algebra naturally supports:
- pair cancellation,
- three-body cancellation,
- nontrivial defect-bearing isolated constituents.

---

## 6) Meson-like composite closure

A meson-like composite is the simplest two-sector neutral closure.

### Rule
For two sectors \(a,b\), require
\[
\delta_a + \delta_b \in \mathbb Z.
\]

### In the order-3 defect set
This means the admissible pairings are:
\[
\frac13 + \frac23 = 1,
\qquad
\frac23 + \frac13 = 1.
\]

So a meson-like closure channel appears naturally as a two-sector defect-canceling pair.

### Interpretation
This is the simplest realization of:
- incomplete constituents,
- complete composite.

---

## 7) Baryon-like composite closure

A baryon-like composite is the minimal irreducible three-sector closure channel.

### Rule
For three sectors \(a,b,c\), require
\[
\delta_a + \delta_b + \delta_c \in \mathbb Z.
\]

### In the order-3 defect set
Two simplest uniform examples are:
\[
\frac13 + \frac13 + \frac13 = 1,
\qquad
\frac23 + \frac23 + \frac23 = 2.
\]

So triple closure appears naturally as a three-body defect completion rule.

### Structural significance
This is why thirds are the first compelling denominator in the incomplete-cycle picture:
- they support pair closure,
- but also support irreducible triple closure.

---

## 8) Assisted closure algebra

Sometimes a quark-like sector may not close by composition alone, but may be assisted by a weak channel carrying compensating phase \(\eta_w\).

For a configuration with:
- quark sectors \(a=1,\dots,n\),
- weak assist multiplicity \(m_w\),

write the assisted composite condition as
\[
\sum_a \delta_a - m_w\eta_w \in \mathbb Z.
\]

More generally, if multiple assist channels exist,
\[
\sum_a \delta_a - \sum_j m_j \eta_j \in \mathbb Z.
\]

This is the natural extension of isolated defect cancellation to transition-assisted closure.

---

## 9) Three closure notions kept distinct

### A. Isolated closure
A single sector satisfies
\[
\delta = 0.
\]

### B. Assisted closure
A single or few-sector combination satisfies
\[
\sum_a \delta_a - \sum_j m_j\eta_j \in \mathbb Z.
\]

### C. Composite closure
A multi-sector bound configuration satisfies
\[
\sum_a \delta_a \in \mathbb Z.
\]

These should not be conflated.
A renderer may show a visually closed loop while the theory meaning is only assisted or composite closure.

---

## 10) Candidate up/down assignments in this algebra

A natural first working identification is:
\[
\delta_u = \frac13,
\qquad
\delta_d = \frac23.
\]

Then the simplest closure channels become:

### Meson-like
\[
\delta_u + \delta_d = 1.
\]

### Uniform triple up-like closure
\[
3\delta_u = 1.
\]

### Uniform triple down-like closure
\[
3\delta_d = 2.
\]

These are algebraically admissible. Which of them are physically preferred depends on further dynamical, charge, chirality, and interaction constraints not fixed by closure algebra alone.

---

## 11) Closure-neutral class and confinement-like interpretation

The neutral composite class is
\[
[0] \in \mathbb R/\mathbb Z.
\]

A free isolated defect-bearing sector lives in a non-neutral class:
\[
[\delta] \neq [0].
\]

A stable asymptotic composite must land in the neutral class.

This suggests an M1-native confinement picture:
- isolated quark-like sectors are non-neutral in closure class,
- admissible asymptotic states must be closure-neutral,
- binding/transition structure is what restores neutrality.

So the algebra itself already encodes a primitive confinement-like requirement.

---

## 12) Minimal worked examples

### Example 1: isolated up-like branch
\[
\delta_u = \frac13.
\]
Result:
\[
\delta_{\text{tot}} = \frac13 \notin \mathbb Z.
\]
Not asymptotically admissible.

### Example 2: up + down composite
\[
\delta_u + \delta_d = \frac13 + \frac23 = 1.
\]
Admissible as a closure-neutral pair.

### Example 3: three up-like sectors
\[
3\delta_u = 3\cdot \frac13 = 1.
\]
Admissible as a closure-neutral triple.

### Example 4: weak-assisted single up-like cycle
If
\[
\delta_u = \frac13,
\qquad \eta_w = \frac23,
\]
then one weak cycle gives
\[
\delta_u - \eta_w = -\frac13 \notin \mathbb Z.
\]
not closed,
but two weak-assist units give
\[
\delta_u - 2\eta_w = \frac13 - \frac43 = -1 \in \mathbb Z.
\]
closed.

This illustrates why low-order assisted closure can naturally differ from one-step visual closure.

---

## 13) What this algebra does and does not fix

### It fixes
- the basic additive closure rule,
- the distinction between isolated / assisted / composite closure,
- why thirds are an attractive first defect basis,
- why non-neutral isolated sectors are naturally excluded.

### It does not yet fix
- exact physical up/down assignment uniquely,
- the detailed relation between closure class and electric charge,
- the preferred meson/baryon spectrum,
- the dynamical energy penalty for non-neutral closure class,
- the full role of color beyond a phase-branch placeholder.

---

## 14) Working conclusion

The simplest M1-native composite closure algebra is:
\[
\delta \in \mathbb R/\mathbb Z,
\qquad
\text{admissible composite} \iff \sum_a \delta_a \in \mathbb Z.
\]

Restricting to the smallest nontrivial three-body-friendly defect basis gives
\[
\delta \in \left\{0,\frac13,\frac23\right\},
\]
which naturally supports both meson-like pair cancellation and baryon-like triple closure.

This is the cleanest first algebraic realization of incomplete quark cycles in M1.

---

## 15) Next tasks

1. Add a charge/chirality compatibility layer on top of this defect algebra.
2. Relate the closure-neutral class to actual composite selection rules.
3. Distinguish in code between:
   - visual loop return,
   - phase-defect return,
   - composite closure neutrality.
4. Check whether current quark render parameters are best interpreted as:
   - isolated defect representatives,
   - assisted closure candidates,
   - or composite closure fragments.
