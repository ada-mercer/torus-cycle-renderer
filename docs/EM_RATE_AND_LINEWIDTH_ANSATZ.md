# EM Rate and Line-Width Ansatz

Status: derivation scaffold / first quantitative extension

Purpose: provide the first quantitative extension of the EM projector and selection-rule program by introducing:
- an effective transition-rate ansatz,
- an effective line-width/broadening ansatz,
- a minimal interpretation of observed intensity and spectral width.

This note does **not** claim a final derivation of spectroscopic rates. It gives the first controlled heuristic layer after the selection score.

---

## 1) Starting point: the reduced transition score

From `EM_SELECTION_RULES_FROM_RESONANT_ATTRACTORS.md`, define the reduced transition score
\[
S_{m\to n}
=
\mathcal A_{mn}
\cdot
\mathcal R_{mn}
\cdot
\mathfrak C_{mn}
\cdot
\mathcal C_{mn},
\]
with:
- \(\mathcal A_{mn}=|\mathcal M_{m\to n}|\): transport overlap magnitude,
- \(\mathcal R_{mn}\): resonance-gap matching factor,
- \(\mathfrak C_{mn}\): coherence factor,
- \(\mathcal C_{mn}\in\{0,1\}\): closure-admissibility factor.

This score says which transitions are favored. The next question is:

> how does this favoredness translate into rate and width?

---

## 2) First rate ansatz

The simplest first rule is that the transition rate should increase with the selection score.

So define the reduced rate ansatz
\[
\boxed{
\Gamma_{m\to n}^{(eff)}
=
\Gamma_0\,S_{m\to n}^{\,2}
}
\]
where:
- \(\Gamma_0\) is a base coupling/radiative scale,
- the square reflects the usual amplitude-to-rate structure.

Expanding,
\[
\Gamma_{m\to n}^{(eff)}
=
\Gamma_0
\,\mathcal A_{mn}^2
\,\mathcal R_{mn}^2
\,\mathfrak C_{mn}^2
\,\mathcal C_{mn}.
\]

This is the first quantitative transition-rate ansatz.

---

## 3) Why the square is natural

The score \(S_{m\to n}\) behaves like a reduced transition amplitude.

So the simplest rate law is
\[
\text{rate} \propto |\text{amplitude}|^2.
\]

This is the weakest possible quantitative assumption while remaining compatible with common wave-interference logic.

Thus the rate ansatz above is not arbitrary: it is the first natural map from selection amplitude to observed transition strength.

---

## 4) Resonance factor and line profile

Use the reduced resonance factor
\[
\mathcal R_{mn}
=
\frac{1}{1+\left(\frac{\omega_{drive}-\Delta\omega_{mn}}{\Gamma_{mn}}\right)^2},
\]
with
\[
\Delta\omega_{mn}=\omega_n-\omega_m.
\]

This is a Lorentzian-type line factor centered on the resonant gap.

Interpretation:
- \(\omega_{drive}\): projected driving frequency,
- \(\Gamma_{mn}\): effective broadening / line width.

So the same formalism already implies a first line-shape model.

---

## 5) First line-width ansatz

We now need a first model for \(\Gamma_{mn}\).

The most natural first decomposition is:
\[
\boxed{
\Gamma_{mn}
=
\Gamma_{int,mn} + \Gamma_{coh,mn} + \Gamma_{ext,mn}
}
\]
where:
- \(\Gamma_{int,mn}\): intrinsic resonant-state relaxation width,
- \(\Gamma_{coh,mn}\): coherence-limited broadening,
- \(\Gamma_{ext,mn}\): environmental / external driving broadening.

This is the first line-width ansatz.

---

## 6) Coherence-limited broadening

Because coherence plays a central role in the projector chain, the line width should narrow when coherence is high and broaden when coherence is poor.

The simplest first coherence-width law is
\[
\boxed{
\Gamma_{coh,mn}
=
\gamma_c\,(1-\mathfrak C_{mn})
}
\]
with \(\gamma_c>0\).

Interpretation:
- perfect coherence \((\mathfrak C_{mn}=1)\) gives minimal coherence broadening,
- weak coherence broadens the transition.

This is the first explicit role for coherence in line width.

---

## 7) Attractor-basin contribution to line width

In the attractor picture, the target state is not a single infinitely sharp point but a basin with finite capture width.

So another natural broadening term is
\[
\Gamma_{attr,mn}
:=
\gamma_a\,\sigma_{mn}^{(attr)},
\]
where \(\sigma_{mn}^{(attr)}\) measures the effective width of the target attractor basin.

This contributes to \(\Gamma_{int,mn}\) or can be written separately. The important conceptual point is:
- sharper attractors imply narrower lines,
- broader attractor basins imply broader lines.

Thus the attractor picture naturally explains why not all resonant transitions are infinitely sharp.

---

## 8) First intensity ansatz

Observed transition intensity should scale with both:
- the rate,
- the amount of transferable projected current content.

So define a first reduced intensity law
\[
\boxed{
I_{m\to n}^{(eff)}
\,\propto\,
\Gamma_{m\to n}^{(eff)}
\int d\tau\int_{T^2} dudv\,Rr\,
\mathcal W[\Xi_m]\,|\mathbfcal V[\Xi_m]|^2
}
\]

This says:
- strong projected transport content plus strong selection overlap gives bright lines,
- weak transport or weak selection gives faint lines.

---

## 9) Branch-level interpretation

### Matter-like transitions
Expected to show:
- nonzero monopole/current structure,
- discrete favored lines governed by the selection score,
- widths controlled by coherence and attractor sharpness.

### Photon-like/radiative branch
Acts as the continuous transport-driving channel; the observed line structure is selected by the target state's resonance and coherence properties.

So the radiative branch itself need not be fundamentally discrete in transfer, while the line structure of the interaction still becomes discrete and width-limited.

---

## 10) Minimal working set of formulas

The current recommended reduced formulas are:

### Transition score
\[
S_{m\to n}
=
\mathcal A_{mn}
\cdot
\mathcal R_{mn}
\cdot
\mathfrak C_{mn}
\cdot
\mathcal C_{mn}.
\]

### Effective rate
\[
\Gamma_{m\to n}^{(eff)}
=
\Gamma_0 S_{m\to n}^2.
\]

### Resonance factor
\[
\mathcal R_{mn}
=
\frac{1}{1+\left(\frac{\omega_{drive}-\Delta\omega_{mn}}{\Gamma_{mn}}\right)^2}.
\]

### Width decomposition
\[
\Gamma_{mn}
=
\Gamma_{int,mn}+
\gamma_c(1-\mathfrak C_{mn})+
\Gamma_{ext,mn}.
\]

### Effective intensity
\[
I_{m\to n}^{(eff)}
\propto
\Gamma_{m\to n}^{(eff)}
\int d\tau\int_{T^2} dudv\,Rr\,
\mathcal W[\Xi_m]|\mathbfcal V[\Xi_m]|^2.
\]

These are the first quantitative reduced formulas in the current EM chain.

---

## 11) Exact / constrained / open status

### Strongly motivated
- rates should increase with selection overlap,
- widths should broaden when coherence is poor,
- attractor sharpness should affect line width,
- transport content should affect intensity.

### Constrained but not unique
- exact power on the selection score,
- exact decomposition of the line width,
- exact normalization of intensity.

### Still open
- full radiative power law,
- exact spectroscopic calibration,
- final comparison with observed line strengths and widths.

---

## 12) Working conclusion

The EM projector program now admits a first quantitative extension:
- the selection score determines favored transitions,
- the square of that score gives a first rate ansatz,
- coherence and attractor width control line broadening,
- projected transport content controls line intensity.

This is not yet full spectroscopy, but it is the first consistent route from the torus-wave/projector program to rate-like and line-width-like observables.

The next practical step, namely how to calibrate the free scales without overfitting, is now documented in:
- `docs/EM_CALIBRATION_STRATEGY.md`
