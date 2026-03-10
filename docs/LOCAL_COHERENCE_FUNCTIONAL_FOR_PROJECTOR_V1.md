# Local Coherence Functional for the EM Projector v1

Status: derivation scaffold / toy-to-structured bridge

Purpose: replace the manual coherent window/region used in earlier toy projectors with a first derived local coherence functional
\[
W[\Xi](\theta_f,\theta_b,\tau)
\]
built from the internal field itself.

This is the natural next step after the toy orbit and toy torus-surface projector notes.

---

## 1) Objective

Earlier toy notes used hand-defined objects:
- coherent segment vs defect segment on one orbit,
- coherent region \(\Omega_{coh}\) vs defect region \(\Omega_{def}\) on the torus.

Those were useful, but ad hoc.

The goal here is to define a **field-derived weight**
\[
0\le W[\Xi]\le 1
\]
that automatically prefers regions of the torus where the internal pattern is locally closure-compatible and phase-coherent under projection.

---

## 2) Starting field representation

Let the internal field be
\[
\Xi(\theta_f,\theta_b,\tau)=A(\theta_f,\theta_b,\tau)e^{i\Phi(\theta_f,\theta_b,\tau)}.
\]

We assume:
- \(A\ge0\) is local amplitude,
- \(\Phi\) is local phase.

The projector should not respond equally to every point of the torus. It should weight strongly only those points where the phase structure is locally compatible with coherent closure.

---

## 3) Local closure mismatch indicator

The simplest local diagnostic is a closure-mismatch scalar built from phase gradients.

Define the local phase-gradient vector
\[
\nabla\Phi := (\partial_{\theta_f}\Phi,\partial_{\theta_b}\Phi).
\]

For a perfectly closure-compatible local branch, the phase flow should align with a local rational winding direction associated with the candidate sector.

Let the reference sector direction be encoded by a normalized tangent vector
\[
\hat t_0 = \frac{1}{\sqrt{n_f^2+n_b^2}}(n_f,n_b).
\]

Define local directional mismatch
\[
M_{dir}(\theta_f,\theta_b,	au)
:=1-rac{\nabla\Phi\cdot \hat t_0}{|\nabla\Phi|+\varepsilon},
\qquad \varepsilon>0\text{ small}.
\]

Interpretation:
- \(M_{dir}\approx0\): phase flow locally aligned with closure-compatible direction,
- \(M_{dir}>0\): phase flow locally misaligned.

---

## 4) Local phase-smoothness indicator

A second natural ingredient is local phase smoothness / consistency.

Define
\[
M_{curv}(\theta_f,\theta_b,	au):=|\Delta_{T^2}\Phi|,
\]
where
\[
\Delta_{T^2}=\frac{1}{R_f^2}\partial_{\theta_f}^2+\frac{1}{R_b^2}\partial_{\theta_b}^2.
\]

Interpretation:
- small \(M_{curv}\): locally smooth phase transport,
- large \(M_{curv}\): rapid local twist / mismatch / likely incoherent residue.

This is only a first proxy, but it captures the idea that defect-bearing residue should be phase-irregular relative to the coherent core.

---

## 5) First local coherence functional

Combine amplitude support with mismatch penalties:
\[
W[\Xi]
:=
\frac{A^2}{A^2+A_*^2}
\exp\big(-\alpha M_{dir}-\beta M_{curv}\big),
\qquad
\alpha,\beta>0.
\]

Where:
- \(A_*\) is a small amplitude floor scale,
- \(\alpha\) controls directional selectivity,
- \(\beta\) controls curvature/mismatch suppression.

Properties:
- \(0\le W[\Xi]\le 1\),
- regions with negligible amplitude are suppressed,
- regions with locally aligned, smooth phase flow are kept,
- misaligned / irregular regions are exponentially suppressed.

This is the first field-derived replacement for the manual coherence window.

---

## 6) Toy torus-surface projector with derived coherence weight

Replace the manual projector weight by \(W[\Xi]\):
\[
\mathcal P_\mu^{(coh)}[\Xi]
:=
C_\mu\int_{T^2} W[\Xi](\theta_f,\theta_b,\tau)\,\Xi(\theta_f,\theta_b,\tau)\,d\mu.
\]

Then the toy projected source is
\[
q_{toy}:=q_*\mathcal N\,\Re\big(u^\mu\mathcal P_\mu^{(coh)}[\Xi]\big).
\]

This preserves the earlier logic:
- sign comes from the orientation sign carried by \(\Xi\),
- magnitude comes from the portion of the field surviving the local coherence filter.

---

## 7) How the complement rule reappears

Suppose the field naturally separates into two torus sectors:
\[
\Xi = \Xi_{coh} + \Xi_{def},
\]
with:
- \(\Xi_{coh}\): smooth, direction-aligned, high-coherence part,
- \(\Xi_{def}\): irregular, mismatch-bearing, low-coherence part.

Then the local functional is constructed precisely so that
\[
W[\Xi]\approx 1 \quad \text{on coherent support},
\qquad
W[\Xi]\approx 0 \quad \text{on defect support}.
\]

If the normalized high-coherence support fraction is
\[
\mathfrak C[\Xi]
:=
\frac{1}{\mathrm{Area}(T^2)}
\int_{T^2}W[\Xi] \, d\mu,
\]
then the complement rule becomes
\[
\mathfrak C[\Xi]\approx 1-\delta.
\]

So the previous hand-drawn coherent fraction is replaced by a derived one:
\[
1-\delta
\longrightarrow
\mathfrak C[\Xi].
\]

This is the key upgrade.

---

## 8) First connection to effective charge

Under this interpretation, the effective charge ansatz becomes
\[
q_{eff}
\sim
q_*\chi\,\mathfrak C[\Xi] \, g(c).
\]

In the simplest defect-bearing branch where the derived coherence fraction satisfies
\[
\mathfrak C[\Xi]\approx 1-\delta,
\]
we recover the earlier ansatz:
\[
q_{eff}=q_*\chi(1-\delta)g(c).
\]

But now the complement factor is no longer just postulated — it is interpreted as the integrated output of a local coherence functional.

---

## 9) First color-phase extension slot

A natural place for color-phase to enter is through the phase field itself.

Let the quark-like field carry an additional color branch phase
\[
\Phi \to \Phi + \varphi_{col}^{(a)},
\qquad a\in\{1,2,3\}.
\]

Then color-phase does not have to redefine charge sign. Instead it can modify:
- local alignment mismatch \(M_{dir}\),
- local curvature mismatch \(M_{curv}\),
- hence the coherence weight \(W[\Xi]\).

This means color-phase may affect the **shape or normalization of the coherent projected fraction**, without replacing the roles of \(\delta\) or \(\chi\).

That is the cleanest first integration point.

---

## 10) Why this is better than a manual mask

The manual coherent-region picture was useful but arbitrary.

The local coherence functional improves this because:
- it depends on the field itself,
- it can vary smoothly across the torus,
- it naturally suppresses low-amplitude and phase-irregular regions,
- it provides a path toward a genuine projector kernel derived from dynamics.

So this is the first semi-structured bridge between the toy mask and a real field-dependent projection rule.

---

## 11) What this still does not prove

This note does **not** yet provide:
- a unique local mismatch functional,
- a proof that the chosen \((M_{dir},M_{curv})\) pair is the right one,
- an action-level derivation of \(W[\Xi]\),
- a quantitative color-phase fit,
- a numerical implementation against actual renderer states.

So it remains a derivation scaffold.

---

## 12) Working conclusion

The best current upgrade from the toy projector program is to replace manual coherent windows by a local field-derived coherence functional
\[
W[\Xi](\theta_f,\theta_b,\tau)
=
\frac{A^2}{A^2+A_*^2}
\exp\big(-\alpha M_{dir}-\beta M_{curv}\big).
\]

The integrated coherence fraction
\[
\mathfrak C[\Xi]
=
\frac{1}{\mathrm{Area}(T^2)}
\int_{T^2}W[\Xi]d\mu
\]
then becomes the natural projector-side replacement for the heuristic closure complement.

In the first defect-bearing approximation,
\[
\mathfrak C[\Xi]\approx 1-\delta,
\]
so the effective-charge rule becomes
\[
q_{eff}\sim q_*\chi\,\mathfrak C[\Xi]g(c),
\]
with the previous complement ansatz recovered as the leading coarse-grained limit.

---

## 13) Next tasks

1. Define a tiny numerical diagnostic computing \(\mathfrak C[\Xi]\) for renderer prototype fields.
2. Add explicit color-phase trial branches \(\varphi_{col}^{(a)}\) and compare their effect on \(\mathfrak C[\Xi]\).
3. Patch branch docs to reference this local-coherence upgrade.
4. If useful, derive a simplified action or penalty functional whose Euler-Lagrange structure favors the same coherence weight.
