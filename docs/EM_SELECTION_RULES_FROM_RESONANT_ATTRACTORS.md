# EM Selection Rules from Resonant Attractors

Status: derivation scaffold / transition rule extension

Purpose: derive the first selection-rule formulation implied by the current EM projector chain together with the resonant-attractor picture.

This note answers the question:

> If projected transfer is continuous at first pass, what determines which transitions are actually allowed or strongly favored?

The answer proposed here is:
- the projector supplies continuous source/current transfer,
- the carrier provides a discrete ladder of resonant attractor states,
- selection rules arise from compatibility between projected transport and the target resonant-state structure.

---

## 1) Starting ingredients

From earlier notes we now have:

### A. Discrete torus mode ladder
\[
\omega_{rs}^2 = \Omega_0^2 + c_{int}^2\left(
\frac{(r+n_b)^2}{R^2}+
\frac{(s+n_f)^2}{r^2}
\right).
\]

### B. Projected source/current structure
\[
A_\mu(x)
=
q_*\chi
\int G(x;X)\,\mathcal W[\Xi] \, \mathcal V_\mu[\Xi].
\]

### C. Explicit transport-current image
\[
\mathbfcal V[\Xi]
=
\alpha_u A^2\frac{\partial_u\Phi}{R}\mathbf e_u
+
\alpha_v A^2\frac{\partial_v\Phi}{r}\mathbf e_v.
\]

### D. Attractor picture
Projected transfer can be continuous, but long-lived observable outcomes correspond to discrete resonant-state attractors.

---

## 2) Transition as overlap-driven capture

Let the system initially occupy resonant state \(\Xi_m\) and be driven toward another possible resonant state \(\Xi_n\) by the projected EM transport channel.

A transition amplitude must therefore depend on how well the projected source/current channel overlaps the difference between those resonant states.

Define the transition-driving functional
\[
\mathcal M_{m\to n}
:=
\int d\tau\int_{T^2} dudv\,Rr\,
\mathcal W[\Xi_m]\,
\mathbfcal V[\Xi_m]\cdot
\mathbfcal T_{m\to n}(u,v,\tau),
\]
where \(\mathbfcal T_{m\to n}\) is the internal transition profile connecting the two resonant states.

Then the first selection principle is:
\[
\boxed{
\text{Transition } m\to n \text{ is allowed/strong when } \mathcal M_{m\to n}\neq 0
}
\]
and suppressed when \(\mathcal M_{m\to n}\) vanishes or is very small.

---

## 3) Frequency matching condition

Because the resonant states have discrete internal frequencies, the transfer channel must also match the frequency gap at least approximately.

Define
\[
\Delta\omega_{mn}:=\omega_n-\omega_m.
\]

Then the next required condition is frequency compatibility:
\[
\boxed{
\omega_{drive}\approx \Delta\omega_{mn}
}
\]
up to the line width / damping / interaction broadening of the attractor basins.

So the first frequency selection rule is simply resonant matching of the gap.

---

## 4) Coherence selection rule

The projected transfer is weighted by the coherence functional \(\mathcal W[\Xi]\), so transitions should also be suppressed when the relevant transport channel is poorly projected.

Thus the next rule is:

\[
\boxed{
\text{A transition is suppressed if the source/transport coherence weight in the relevant channel is too small.}
}
\]

In reduced form, if
\[
\mathfrak C_{m\to n}
:=
\int d\tau\int_{T^2} dudv\,Rr\,
\mathcal W[\Xi_m]\,\mathcal W[\mathbfcal T_{m\to n}],
\]
then small \(\mathfrak C_{m\to n}\) implies weak effective coupling.

So the attractor picture naturally adds a coherence-based selection rule on top of simple frequency matching.

---

## 5) Sign/orientation rule

Because the EM projector inherits sign through \(\chi\), transitions must also respect the sign/orientation structure of the branch.

Thus the effective projected coupling changes sign under
\[
\chi\to -\chi.
\]

So the selection structure must distinguish:
- same-orientation transitions,
- opposite-orientation transitions,
- sign-canceling/neutral combinations.

This yields the first orientation selection rule:
\[
\boxed{
\text{Only sign-compatible projected channels contribute constructively to the transition amplitude.}
}
\]

---

## 6) Closure-compatibility rule

From the broader M1 program, the target state must itself be admissible as a resonant or coupled closure state.

Therefore even if:
- the frequency matches,
- the overlap is nonzero,
- the coherence weight is nonzero,

a transition should still be excluded if the target branch/state does not satisfy the relevant closure criterion.

So the next rule is:
\[
\boxed{
\text{Transitions into non-admissible closure states are dynamically suppressed or absent.}
}
\]

This ties the EM selection problem back to the closure program.

---

## 7) First reduced transition score

Collecting the above, define a reduced transition score
\[
S_{m\to n}
:=
\mathcal A_{mn}
\cdot
\mathcal R_{mn}
\cdot
\mathfrak C_{mn}
\cdot
\mathcal C_{mn},
\]
where:
- \(\mathcal A_{mn}:=|\mathcal M_{m\to n}|\) is the transport overlap magnitude,
- \(\mathcal R_{mn}\) is the resonance matching factor,
- \(\mathfrak C_{mn}\) is the coherence factor,
- \(\mathcal C_{mn}\in\{0,1\}\) is the closure-admissibility factor.

A simple resonance factor is
\[
\mathcal R_{mn}
=
\frac{1}{1+\left(\frac{\omega_{drive}-\Delta\omega_{mn}}{\Gamma_{mn}}\right)^2},
\]
with width \(\Gamma_{mn}\).

Then the reduced rule is:
\[
\boxed{
\text{Allowed/favored transitions maximize } S_{m\to n}.
}
\]

This is the cleanest current selection-rule formula.

---

## 8) Photon-like branch interpretation

For a radiative/pure-transport branch, the projector does not need to deliver a quantized packet ab initio.

Instead, the projected radiative current can continuously drive the target system, and the observed discrete transition is determined by which resonant attractor score \(S_{m\to n}\) dominates.

Thus the photon-like branch is best interpreted as:
- a continuous projected transport channel,
- whose observed discrete outcomes arise from the attractor/selection structure of the target state.

That is the key interpretive result.

---

## 9) Matter-branch interpretation

For matter-like branches, the same rule says:
- not every mathematically possible mode difference is realized,
- only those with sufficient resonance, overlap, coherence, and closure admissibility are favored.

So the observed selection rules are not arbitrary add-ons; they are consequences of:
- the projector,
- the mode ladder,
- the coherence structure,
- the closure constraints.

---

## 10) Exact / constrained / open status

### Strongly justified
- discrete resonant-state ladder exists,
- projected transport can be continuous,
- target-state resonance should matter for observed discrete outcomes.

### Constrained but not unique
- the exact overlap functional \(\mathcal M_{m\to n}\),
- the exact coherence factor \(\mathfrak C_{mn}\),
- the exact broadening/width factor \(\Gamma_{mn}\).

### Still open
- quantitative transition rates,
- exact selection intensities,
- final correspondence to observed spectroscopic rules.

---

## 11) Working conclusion

The first selection-rule statement implied by the current EM projector program is:

\[
\boxed{
\text{Transitions are favored when projected transport overlaps a closure-admissible target resonant attractor with matching frequency gap and sufficient coherence.}
}
\]

This gives a principled next step beyond the statement that transfer may be continuous while outcomes are discrete. It identifies the actual ingredients that select which discrete outcomes appear.

A first quantitative extension of this score into rate and line-width language is now developed in:
- `docs/EM_RATE_AND_LINEWIDTH_ANSATZ.md`
