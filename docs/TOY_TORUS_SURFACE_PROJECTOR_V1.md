# Toy Torus-Surface Projector v1

Status: explicit toy derivation / torus-surface lift

Purpose: extend the 1D orbit projector for closure complement to a toy projector acting directly on the internal carrier
\[
(\theta_f,\theta_b)\in T^2.
\]

This note is meant to show that the complement-rule logic can be expressed on the actual torus surface rather than only on a reduced orbit parameter.

---

## 1) Objective

We want a toy torus-surface projector
\[
\mathcal P_\mu[\Xi]
\]
that satisfies three qualitative requirements:

1. preserves orientation sign,
2. suppresses non-closure residue,
3. gives a leading source weight proportional to
\[
1-\delta.
\]

This remains a toy model, not the final universal projector.

---

## 2) Internal field on the torus

Use torus coordinates
\[
(\theta_f,\theta_b)\in[0,2\pi)\times[0,2\pi).
\]

Take a simple mode field with orientation sign \(\chi\in\{\pm1\}\):
\[
\Xi(\theta_f,\theta_b,\tau)
=
\chi\,A_0\,e^{i\Phi(\theta_f,\theta_b,\tau)}.
\]

For a defect-bearing quark-like branch, think of \(\Phi\) as containing:
- a closure-compatible phase sector,
- a mismatched remainder associated with defect \(\delta\).

We do not need the exact microscopic decomposition yet; the toy projector will encode it geometrically.

---

## 3) From orbit picture to surface picture

In the 1D toy model, one nominal orbit was split into:
- coherent segment of length \(1-\delta\),
- defect remainder of length \(\delta\).

On the torus surface, the natural analog is not a segment length but a **coherent region** of the carrier.

So define a decomposition of the torus into:
\[
T^2 = \Omega_{coh} \cup \Omega_{def},
\qquad
\Omega_{coh}\cap\Omega_{def}=\varnothing,
\]
with normalized area fractions
\[
\frac{\mathrm{Area}(\Omega_{coh})}{\mathrm{Area}(T^2)}=1-\delta,
\qquad
\frac{\mathrm{Area}(\Omega_{def})}{\mathrm{Area}(T^2)}=\delta.
\]

Interpretation:
- \(\Omega_{coh}\): torus region whose contribution is phase-compatible with coherent EM projection,
- \(\Omega_{def}\): region carrying unresolved non-closure residue.

---

## 4) Minimal coherent-region projector

The simplest torus-surface analog of the coherent-window projector is:
\[
\mathcal P_\mu^{(toy)}[\Xi]
:=
C_\mu\int_{T^2} W_\delta(\theta_f,\theta_b)\,\Xi(\theta_f,\theta_b,\tau)\,d\mu,
\]
where:
- \(C_\mu\) is a fixed projection coefficient into the EM channel,
- \(d\mu=R_fR_b\,d\theta_f d\theta_b\),
- \(W_\delta\) is a coherence weight on the torus.

Take the sharp toy choice
\[
W_\delta(\theta_f,\theta_b)=
\begin{cases}
1,&(\theta_f,\theta_b)\in\Omega_{coh},\\
0,&(\theta_f,\theta_b)\in\Omega_{def}.
\end{cases}
\]

Then the projector keeps only the coherent torus region.

---

## 5) Leading complement rule from the torus projector

If the field amplitude is approximately uniform over the coherent region at the scale relevant to the projector, then
\[
\mathcal P_\mu^{(toy)}[\Xi]
\approx
C_\mu\,\chi A_0\int_{\Omega_{coh}} e^{i\Phi}\,d\mu.
\]

When phase variation inside \(\Omega_{coh}\) is modest compared to the gross mismatch represented by the excluded defect region, the leading contribution is proportional to the coherent-region area:
\[
|\mathcal P_\mu^{(toy)}[\Xi]|
\propto
\mathrm{Area}(\Omega_{coh})
\propto
1-\delta.
\]

Thus the torus-surface projector gives the same leading scaling as the 1D orbit model:
\[
|\mathcal P_\mu^{(toy)}[\Xi]| \propto 1-\delta.
\]

---

## 6) Defect-region suppression on the torus

Why exclude \(\Omega_{def}\)?

Because in the toy interpretation this region carries the part of the internal pattern that is:
- not closure-compatible,
- not stably source-bearing as an isolated branch,
- expected to average away, leak, or require compensation.

So the surface projector is not supposed to sum blindly over all torus support. It is supposed to retain the portion that survives as coherent projected content.

That is the torus-surface analog of suppressing the defect remainder on the orbit.

---

## 7) Smoothed torus-surface projector

A sharp region split is again too crude. So define a smoothed coherence weight
\[
0\le W_\delta^{(sm)}(\theta_f,\theta_b)\le 1,
\]
with total normalized weight
\[
\frac{1}{\mathrm{Area}(T^2)}\int_{T^2}W_\delta^{(sm)}\,d\mu
\approx 1-\delta.
\]

Then
\[
\mathcal P_\mu^{(sm)}[\Xi]
:=
C_\mu\int_{T^2} W_\delta^{(sm)}(\theta_f,\theta_b)\,\Xi(\theta_f,\theta_b,\tau)\,d\mu.
\]

This is the natural torus-surface analog of the smoothed 1D coherent-window projector.

---

## 8) Toy current extraction on the surface

To connect with effective charge, define a toy projected source scalar
\[
q_{toy}:=q_*\,\mathcal N\,\Re\big(u^\mu\mathcal P_\mu^{(toy)}[\Xi]\big),
\]
where:
- \(u^\mu\) selects the source-like component,
- \(\mathcal N\) normalizes a closure-neutral reference branch to unit charge.

Because the field carries orientation sign \(\chi\), this gives the leading structure
\[
q_{toy}\propto q_*\chi(1-\delta).
\]

So the torus-surface lift preserves both:
- sign from orientation branch,
- magnitude from closure complement.

---

## 9) Minimal geometrical picture for the coherent region

A simple concrete torus picture is this:

- the carrier supports a family of near-closed phase tracks,
- most of the support follows a coherent band around that track,
- a smaller band of support fails to close cleanly and behaves as defect residue.

Then:
- coherent band area fraction \(\sim 1-\delta\),
- defect band area fraction \(\sim \delta\).

This is the surface-level analog of “completed segment plus leftover remainder.”

---

## 10) Order-3 check on the torus-surface model

Using the same trial assignments
\[
\delta_u=\frac13,
\qquad
\delta_d=\frac23,
\]
we get coherent-region weights
\[
1-\delta_u=\frac23,
\qquad
1-\delta_d=\frac13.
\]

With sign choices
\[
\chi_u=+1,
\qquad
\chi_d=-1,
\]
this yields
\[
q_u\propto +\frac23 q_*,
\qquad
q_d\propto -\frac13 q_*.
\]

So the torus-surface projector reproduces the same desired quark-like charge pattern.

---

## 11) Why this is more than a rephrased 1D picture

The gain from the torus-surface model is that it now matches the actual carrier logic:
- the fundamental object is a field on \(T^2\),
- the projector acts on the surface field itself,
- coherent vs defect content is interpreted as a region/weight decomposition on the carrier.

So this is a more faithful precursor to the full universal projector than the 1D orbit reduction.

---

## 12) What a more physical projector would likely replace

In a fuller derivation, the ad hoc weight \(W_\delta\) should be replaced by something generated from the field itself, for example:
- local phase-coherence measure,
- local closure-mismatch penalty,
- spectral selection rule,
- or a source-extraction kernel built from \(\Xi\) and its derivatives.

So the long-term goal is not
\[
W_\delta\ \text{manual mask},
\]
but rather
\[
W[\Xi]\ \text{derived coherence functional}.
\]

Still, the present toy model shows what such a derived kernel would need to do qualitatively.

---

## 13) Relation to composite closure

The torus-surface projector also fits naturally with the composite-closure picture.

If an isolated branch has defect \(\delta\neq0\), then only part of its support is coherently projectable on its own.
A composite that restores closure can be interpreted as one in which the missing coherent portions are supplied jointly across sectors, allowing the asymptotic observable to become closure-neutral.

So the surface-projector intuition is compatible with the additive closure algebra.

---

## 14) What this note does not prove

This note still does **not** provide:
- the final universal projector kernel \(\mathcal P_\mu\),
- a derivation of \(W[\Xi]\) from an action principle,
- the chirality modulation factor \(g(c)\),
- the role of color-phase in reshaping the coherent region,
- the exact spacetime dependence of the projected fields.

So this is still a toy derivation — just one step closer to the actual carrier geometry.

---

## 15) Working conclusion

A toy projector can be written directly on the torus surface so that:
- it acts on the actual carrier field \(\Xi(\theta_f,\theta_b,\tau)\),
- it preserves orientation sign,
- it retains the coherent torus region and suppresses the defect region,
- and it yields a projected source weight scaling as
\[
1-\delta.
\]

This is the torus-surface version of the closure-complement argument and is the best current toy bridge from internal geometry to quark-like effective charge structure.

---

## 16) Next tasks

1. Replace the manual coherence region \(\Omega_{coh}\) by a derived local coherence functional built from \(\Xi\) and phase gradients.
2. Add color-phase dependence to see whether it rescales or reshapes the coherent region.
3. Document the full derivation chain in one index note for easier repo navigation.
4. If useful, add a tiny numerical sketch showing how weighted torus-region area tracks projected source weight across different \(\delta\).
