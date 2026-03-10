# Toy Projector for Closure Complement v1

Status: explicit toy derivation / sanity model

Purpose: give a concrete toy projector showing how a defect-bearing torus cycle can project an electromagnetic source weight proportional to the **closure complement**
\[
1-\delta
\]
rather than to the raw defect
\[
\delta.
\]

This is not a final physical projector. It is a deliberately simplified model meant to test the logic of the closure-complement rule.

---

## 1) Objective

We want an explicit toy mechanism behind the slogan:

> the unresolved defect remainder washes out under projection, while the coherently completed portion survives.

The aim is to show that this statement can be made mathematically concrete, even before the final universal projector is known.

---

## 2) Setup: one nominal orbit with defect

Parameterize one nominal internal orbit by
\[
s\in[0,1].
\]

Let the branch carry closure defect \(\delta\in(0,1)\). The internal phase after one nominal orbit is then
\[
\phi(1)-\phi(0)=2\pi(N+\delta),
\qquad N\in\mathbb Z.
\]

Interpretation:
- the cycle is almost closed,
- but after one nominal orbit a residual phase fraction \(2\pi\delta\) remains.

We split the orbit into two conceptual pieces:
- coherent segment of length \(1-\delta\),
- defect remainder of length \(\delta\).

---

## 3) Toy field on the orbit

Take the simplest orbit field with orientation sign \(\chi\in\{\pm1\}\):
\[
\Xi(s)=\chi\,A_0\,e^{i\phi(s)}.
\]

To keep the model simple, assume near-uniform phase flow on one nominal orbit:
\[
\phi(s)=2\pi(N+\delta)s.
\]

Since integer winding factors drop out of a full-cycle phase average, the relevant nontrivial part is just
\[
\Xi(s)\sim \chi A_0 e^{i2\pi\delta s}
\]
up to an overall periodic factor.

---

## 4) Naive full-orbit average and why it is not the right observable

If one averages over the entire nominal orbit,
\[
\langle \Xi\rangle_{full} := \int_0^1 \Xi(s)\,ds,
\]
then
\[
\langle \Xi\rangle_{full}
\propto
\chi A_0 \int_0^1 e^{i2\pi\delta s}ds
= \chi A_0\frac{e^{i2\pi\delta}-1}{i2\pi\delta}.
\]

Magnitude:
\[
|\langle \Xi\rangle_{full}|
\propto
\frac{|\sin(\pi\delta)|}{\pi\delta}.
\]

This does **not** equal \(1-\delta\).

That is important: it tells us the physical projector cannot simply be an undifferentiated full-orbit average of the raw complex phase. A more structured observable is needed.

This is actually useful, because it clarifies what the complement rule is really saying:
- not “any average gives \(1-\delta\),”
- but “the relevant EM source projector must preferentially retain the coherent closure-compatible part.”

---

## 5) The right toy observable: coherent-window projector

The simplest such structured projector is a **coherent-window projector**:
\[
\mathcal P_c[\Xi]
:=
\int_0^1 W_\delta(s)\,\Xi(s)\,ds,
\]
where \(W_\delta(s)\) is a window that selects the closure-compatible segment.

Take the minimal toy choice:
\[
W_\delta(s)=
\begin{cases}
1, & 0\le s\le 1-\delta,\\
0, & 1-\delta < s \le 1.
\end{cases}
\]

Then
\[
\mathcal P_c[\Xi]=\chi A_0\int_0^{1-\delta} e^{i2\pi\delta s}ds.
\]

For small-to-moderate \(\delta\), the phase variation across the coherent segment is modest compared with the gross mismatch introduced by the defect remainder, so the leading-order coherent contribution is
\[
\mathcal P_c[\Xi]
\approx \chi A_0(1-\delta).
\]

Thus the projected magnitude scales as
\[
|\mathcal P_c[\Xi]|\propto 1-\delta.
\]

This is the first explicit toy realization of the complement rule.

---

## 6) Why the defect remainder washes out in this toy model

The remainder interval
\[
s\in(1-\delta,1]
\]
contains the portion of the nominal orbit that fails to align with closure completion.

If we write the full orbit integral as
\[
\int_0^1 ds = \int_0^{1-\delta} ds + \int_{1-\delta}^{1} ds,
\]
then the second term is precisely the part carrying the unresolved return mismatch.

In the toy model, that remainder is removed by the coherence window because it is interpreted as:
- non-closure residue,
- non-asymptotic contribution,
- not part of the stable source-bearing component.

So the complement rule arises because the projector is not measuring “everything present,” but only “what survives as coherent source content.”

---

## 7) Smoothed version of the same projector

A hard cutoff is crude. A smoother and more realistic toy version is:
\[
W_\delta^{(sm)}(s)=\frac{1}{2}\left[1-\tanh\left(\frac{s-(1-\delta)}{\sigma}\right)\right],
\qquad 0<\sigma\ll1.
\]

Then
\[
\mathcal P_c^{(sm)}[\Xi]=\int_0^1 W_\delta^{(sm)}(s)\,\Xi(s)\,ds.
\]

As \(\sigma\to0\), this tends to the sharp-window projector above.
For small \(\sigma\), the integrated weight remains approximately
\[
\int_0^1 W_\delta^{(sm)}(s)ds \approx 1-\delta.
\]

So the complement scaling is stable under smoothing.

---

## 8) Toy current extraction

To connect more directly with EM language, define a toy projected source amplitude
\[
q_{toy} := q_*\,\mathcal N\,\Re\big(\mathcal P_c[\Xi]\big),
\]
with normalization \(\mathcal N\) chosen so that a fully closed reference branch gives unit charge scale.

Since orientation sign sits in \(\Xi\), this gives
\[
q_{toy}\propto q_*\chi(1-\delta)
\]
at leading order.

This reproduces exactly the desired structure:
\[
q_{eff}=q_*\chi(1-\delta)
\]
up to chirality modulation and normalization refinements.

---

## 9) Order-3 check

Apply the toy rule to
\[
\delta_u=\frac13,
\qquad
\delta_d=\frac23.
\]

Then the coherent-window projector gives weights
\[
1-\delta_u = \frac23,
\qquad
1-\delta_d = \frac13.
\]

With orientation choices
\[
\chi_u=+1,
\qquad
\chi_d=-1,
\]
we obtain
\[
q_u\propto +\frac23 q_*,
\qquad
q_d\propto -\frac13 q_*.
\]

So the toy projector reproduces the desired quark-like charge ordering.

---

## 10) Why this is better than a raw-defect projector

If instead one defined a “defect-only projector” by integrating only over the remainder interval,
\[
\mathcal P_d[\Xi]=\int_{1-\delta}^{1}\Xi(s)ds,
\]
then the leading weight would scale like
\[
|\mathcal P_d[\Xi]|\propto \delta.
\]

But this would mean the less-complete branch projects more strongly into the stable EM source channel.
That is precisely the wrong monotonicity if EM charge is meant to reflect coherent asymptotic source content.

So the coherent-window projector is preferred over the defect-window projector on conceptual grounds.

---

## 11) Best interpretation of the toy model

This toy projector should not be read literally as “nature applies a hard window.”

Its real purpose is to demonstrate a structural point:

- a projector that keeps the closure-compatible part and suppresses the unresolved remainder naturally yields a weight proportional to \(1-\delta\);
- a projector that instead treats the defect remainder as the source would yield \(\delta\) and the wrong physical ordering.

So the toy model is evidence that the complement rule is not arbitrary; it is the natural output of a coherence-selecting projector.

---

## 12) Relation to the universal projector program

In the full theory, the universal projector should not be a hand-drawn window on orbit parameter \(s\).
It should arise from a genuine map
\[
\Xi(\theta_f,\theta_b,\tau) \to A_\mu(x)
\]
whose source-bearing part automatically suppresses incoherent or non-closure residue.

The present toy model suggests what that full projector should do qualitatively:
- retain closure-compatible coherent content,
- suppress unresolved defect residue,
- preserve orientation sign.

That is exactly the logic required for
\[
q_{eff}=q_*\chi(1-\delta)g(c).
\]

---

## 13) What this toy model does not prove

This note does **not** yet provide:
- a full torus-surface projector kernel \(\mathcal P_\mu\),
- a derivation from the field action,
- a unique reason for the sharp/smoothed window shape,
- the chirality modulation factor \(g(c)\),
- color-phase dependence.

So it is still a toy derivation, not a final result.

---

## 14) Working conclusion

A simple coherence-selecting toy projector can be written explicitly so that:
- the closure-compatible segment contributes coherently,
- the defect remainder is suppressed as non-asymptotic residue,
- the projected source weight scales as
\[
1-\delta.
\]

Therefore the complement rule
\[
q_{eff}=q_*\chi(1-\delta)g(c)
\]
is not just numerically convenient; it is the natural outcome of the first explicit projector model that treats EM charge as a measure of coherent source-bearing completion.

---

## 15) Next tasks

1. Lift the toy orbit projector to a toy **torus-surface** projector using \((\theta_f,\theta_b)\) rather than a single orbit parameter.
2. Test whether color-phase branches modify only normalization or also the effective coherent window.
3. Add a compact summary of this toy model into the quark foundation docs.
4. If useful, implement a tiny numerical sketch to compare full-orbit, defect-window, and coherent-window projection weights across \(\delta\in[0,1]\).
