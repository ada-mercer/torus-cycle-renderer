# Radiative Branch and Attractor Quantization

Status: derivation scaffold / radiative extension

Purpose: extend the EM projector chain from static/far-field source structure to radiative behavior, while keeping the following warning explicit:

> transfer need not be fundamentally quantized at the projector level;
> quantization may instead emerge because resonant particle states act as attractors of momentum/energy transfer.

This note therefore treats:
- continuous transport/current projection as primary,
- resonant-state locking as the origin of effective discrete transfer.

---

## 1) Starting point

From `TRANSPORT_CURRENT_IMAGE_ANSATZ.md`, the projected transport-current image is
\[
\mathbfcal V[\Xi](u,v,\tau)
=
\alpha_u A^2\frac{\partial_u\Phi}{R}\mathbf e_u
+
\alpha_v A^2\frac{\partial_v\Phi}{r}\mathbf e_v.
\]

The EM projector family then uses
\[
\mathbf A(\mathbf x,t)
\sim
q_*\chi
\int d\tau\int_{T^2} dudv\,Rr\,
G(x;X(u,v,\tau))
\mathcal W[\Xi](u,v,\tau)
\mathbfcal V[\Xi](u,v,\tau).
\]

So the projector naturally supports time-dependent radiative/current behavior.

---

## 2) Radiative branch principle

A branch is radiative when its projected source moments are time-dependent in a way that cannot be reduced to a static monopole source.

At the first reduced level this means:
- static monopole term vanishes or is subdominant,
- the time-dependent projected current image remains nonzero,
- the resulting far field is controlled by time derivatives of the transport moments.

So for a photon-like branch, the leading EM content is expected to be transport/radiation, not static charge.

---

## 3) Continuous transfer picture

The projector family by itself does **not** force transfer to occur in discrete packets.

Instead, the natural first picture is continuous:
- internal torus transport produces a continuous projected EM current,
- that current can exchange momentum/energy continuously with other systems,
- the field channel itself does not need to begin as intrinsically quantized.

In this sense, the primary projected transfer variable is continuous.

---

## 4) Resonant-state attractor principle

Quantization can then arise as a property of the *receiving and emitting states*, not necessarily as a primitive property of the transfer channel.

Let the interacting system possess a set of resonant carrier states
\[
\{\Xi_n\}
\]
with associated stable/attractive mode manifolds.

Then continuous projected transport may still relax preferentially into one of these resonant states.

This motivates the attractor principle:

\[
\boxed{
\text{continuous projected transfer}
\quad\to\quad
\text{capture by discrete resonant attractor states}
}
\]

So the effective observed discreteness arises because stable resonant states select what can persist.

---

## 5) Mode-energy ladder as the attractor set

From the full torus wave derivation, exact steady-state modes satisfy
\[
\omega_{rs}^2 = \Omega_0^2 + c_{int}^2\left(\frac{(r+n_b)^2}{R^2}+\frac{(s+n_f)^2}{r^2}\right).
\]

Thus the carrier already has a discrete steady-state spectrum.

If those states are dynamically attractive under interaction and damping/relaxation, then the observed transfer picture becomes:
- external interaction channel can exchange momentum continuously,
- but the system stabilizes only on the discrete mode ladder.

This gives a natural route to effective quantization without postulating fundamentally quantized transfer at the field-channel level.

---

## 6) Reduced mathematical form of attractor capture

Let \(Q(t)\) be a continuous projected transfer quantity (energy, momentum-like content, or source-weighted mode amplitude).

Let the resonant attractor values be
\[
Q_n,
\qquad n\in\mathbb Z_{\ge0}.
\]

Then a simple reduced dynamics is
\[
\dot Q = \mathcal I(t) - \Gamma\,\partial_Q U_{eff}(Q),
\]
where:
- \(\mathcal I(t)\): external continuous input/output,
- \(U_{eff}(Q)\): effective landscape with minima at \(Q_n\),
- \(\Gamma>0\): relaxation scale.

In this picture:
- transfer itself is continuous,
- stable observed states are discrete because the minima \(Q_n\) are discrete.

This is the cleanest reduced attractor model.

---

## 7) Photon-like branch consequence

For a pure transport/radiative branch such as the current photon correspondence branch:
- static monopole term should vanish,
- the relevant projected observable is the time-dependent current/multipole channel,
- interaction with matter-like states can still produce effectively discrete outcomes if the matter states have discrete resonant attractors.

So a photon-like branch does not need to be born fundamentally as a quantized lump in order for emission/absorption events to appear discrete.

Instead:
\[
\boxed{
\text{radiative transfer can be continuous at the projector level,}
\quad
\text{while matter-state resonance makes the net outcome appear quantized.}
}
\]

---

## 8) Matter-branch consequence

For matter-like branches, the projected monopole and current content both matter.

When such a branch interacts with a radiative branch, the allowed long-lived outcomes are governed by the resonant-state spectrum of the matter branch.

Thus the observed transfer rule is not:
- arbitrary continuous final state,

but rather:
- continuous interaction path,
- discrete stable endpoints.

That is exactly the attractor reading.

---

## 9) Selection rule interpretation

This gives a new interpretation of selection rules.

Instead of saying only:
- transitions are allowed because the field itself carries discrete quanta,

one may say:
- transitions are allowed when projected transport can connect one resonant attractor basin to another while respecting sign, coherence, and closure constraints.

So the selection structure becomes partly a property of:
- the mode ladder,
- the coherence weight,
- the transport-current image,
- and the interaction geometry.

---

## 10) Exact / constrained / open status

### Strongly justified
- the torus carrier has a discrete steady-state mode spectrum,
- the projected transport/current channel can be continuous at first pass,
- radiative behavior belongs naturally to time-dependent current/multipole structure.

### Constrained but not unique
- the exact effective landscape \(U_{eff}(Q)\),
- the exact dynamical capture rule into resonant states,
- the precise relation between projected energy transfer and internal mode amplitudes.

### Still open
- full quantitative emission/absorption law,
- exact radiative power formula from the torus projector,
- unique connection to observed quantum rates and spectra.

---

## 11) Working conclusion

The best current extension of the EM projector program is:

1. the projector transports source/current content continuously;
2. the torus carrier provides a discrete resonant-state ladder;
3. effective quantization of transfer emerges because these resonant states act as attractors of momentum/energy transfer.

This is the strongest honest formulation that incorporates the warning that transfer need not be fundamentally quantized at the projector level while still explaining why observed interactions may appear discrete.

The next step from this point is now developed in:
- `docs/EM_SELECTION_RULES_FROM_RESONANT_ATTRACTORS.md`
