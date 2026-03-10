# Transport-Current Image Ansatz

Status: derivation scaffold / next EM projector step

This note provides the next step after the constrained torus-to-EM projector family:

- the source-weight channel \(\mathcal W[\Xi]\) already controls effective charge / monopole content;
- the remaining missing ingredient is the projected transport-current image
\[
\mathcal V_i[\Xi].
\]

The purpose of this note is to derive the first usable ansatz for \(\mathcal V_i[\Xi]\) from the torus field itself rather than leaving it as a placeholder.

---

## 1) Starting point

The constrained projector family currently reads
\[
A_\mu(x)
=
q_*\chi
\int d\tau\int_{T^2} dudv\,Rr\,
G(x;X(u,v,\tau))\,
\mathcal W[\Xi](u,v,\tau)
\,\mathcal V_\mu[\Xi](u,v,\tau).
\]

For the scalar channel we set
\[
\mathcal V_0 \equiv 1.
\]

We now seek the spatial transport/current image
\[
\mathcal V_i[\Xi].
\]

---

## 2) Guiding principle

The spatial current image should represent the external image of **internal phase transport** on the torus carrier.

So the natural raw ingredients are:
- amplitude \(A(u,v,\tau)\),
- phase \(\Phi(u,v,\tau)\),
- torus phase gradients
\[
\partial_u\Phi,
\qquad
\partial_v\Phi,
\]
- and the carrier transport directions associated with the major/minor cycles.

Thus \(\mathcal V_i[\Xi]\) should be built from internal phase flow, not chosen independently.

---

## 3) Internal torus current density

Write the field as
\[
\Xi(u,v,\tau)=A(u,v,\tau)e^{i\Phi(u,v,\tau)}.
\]

The natural torus current densities are the phase-gradient currents
\[
J_u^{int} := A^2\,\frac{1}{R}\partial_u\Phi,
\qquad
J_v^{int} := A^2\,\frac{1}{r}\partial_v\Phi.
\]

Interpretation:
- \(J_u^{int}\): internal bosic-direction transport density,
- \(J_v^{int}\): internal fermic-direction transport density.

This is the standard phase-current structure one expects from complex wave transport on a compact carrier.

---

## 4) Directional projection map

To project torus currents into external space, introduce the external image of the torus-cycle tangent directions:
\[
\mathbf e_u(u,v),
\qquad
\mathbf e_v(u,v).
\]

At the reduced correspondence level, these are the projected unit directions associated with motion along the major and minor carrier cycles.

Then define the first transport-current image as
\[
\boxed{
\mathbfcal V[\Xi](u,v,\tau)
:=
\alpha_u J_u^{int}\,\mathbf e_u(u,v)
+
\alpha_v J_v^{int}\,\mathbf e_v(u,v)
}
\]
with projection coefficients \(\alpha_u,\alpha_v\).

This is the first explicit current-image ansatz.

---

## 5) Coherence-weighted version

Because the projector already uses a source-weight functional \(\mathcal W[\Xi]\), it is natural to separate:
- current direction/content,
- source coherence weight.

So define the raw current image
\[
\mathbfcal V_{raw}[\Xi]
=
\alpha_u J_u^{int}\,\mathbf e_u
+
\alpha_v J_v^{int}\,\mathbf e_v,
\]
and use the projector combination
\[
\mathcal W[\Xi] \, \mathbfcal V_{raw}[\Xi].
\]

This says:
- phase transport supplies the current direction and magnitude skeleton,
- coherent projectability decides how much of it survives into the EM channel.

That is the cleanest current separation of roles.

---

## 6) Reduced branch-level form for exact single modes

For a single exact mode
\[
\Xi \sim A_0 e^{i(\nu_p u + \nu_{pf} v - \omega\tau + \phi_0)},
\]
we have
\[
\partial_u\Phi = \nu_p,
\qquad
\partial_v\Phi = \nu_{pf}.
\]

Then
\[
J_u^{int}=A_0^2\frac{\nu_p}{R},
\qquad
J_v^{int}=A_0^2\frac{\nu_{pf}}{r}.
\]

So the projected transport image becomes
\[
\boxed{
\mathbfcal V[\Xi]
=
A_0^2\left(
\alpha_u\frac{\nu_p}{R}\mathbf e_u
+
\alpha_v\frac{\nu_{pf}}{r}\mathbf e_v
\right).
}
\]

This is the exact reduced-mode current image for the single-mode branch.

---

## 7) Electron-like branch consequence

For the current electron branch, the deformation phase is of the form
\[
\Phi_e = mode_p\,u + mode_{pf}\,v - \omega t_{eff} + \phi_s.
\]

So the reduced transport-current image is
\[
\mathbfcal V_e
=
A_0^2\left(
\alpha_u\frac{mode_p}{R}\mathbf e_u
+
\alpha_v\frac{mode_{pf}}{r}\mathbf e_v
\right).
\]

This gives the first explicit mapping from the electron branch mode numbers to the projected EM current channel.

In words:
- the bosic mode number controls one projected current component,
- the fermic mode number controls the other projected component,
- the coherence/source weight determines how much of that current survives into the external EM field.

---

## 8) Photon-like branch consequence

For a pure bosic branch with vanishing fermic transport contribution at the renderer level, one has effectively
\[
J_v^{int} \approx 0.
\]

Then
\[
\mathbfcal V_\gamma
\approx
\alpha_u A_0^2\frac{\nu_p}{R}\mathbf e_u.
\]

So the photon-like branch naturally projects into a dominantly transport/current channel with no static monopole requirement.

This fits the intended separation between:
- matter-like charged branches with nonzero monopole content,
- radiative/pure-transport branches whose main nontrivial EM content is current/transverse structure.

---

## 9) Divergence-free current condition at reduced level

A reasonable consistency condition is that the projected current image should satisfy a continuity relation with the source-weight density.

At the reduced level this suggests
\[
\partial_\tau \rho_{int}^{eff} + \nabla\cdot\mathbf J_{int}^{eff}=0,
\]
with
\[
\rho_{int}^{eff} = q_*\chi\mathcal W[\Xi],
\qquad
\mathbf J_{int}^{eff}=q_*\chi\mathcal W[\Xi]\mathbfcal V[\Xi].
\]

This does not yet derive the full external continuity equation uniquely, but it imposes a strong consistency target on any further projector refinement.

---

## 10) Minimal normalized transport image

It is useful to separate magnitude from direction.

Define
\[
\mathbfcal V[\Xi] = \mathcal J[\Xi]\,\hat{\mathbf v}[\Xi],
\]
where
\[
\mathcal J[\Xi]
:=
\sqrt{
\left(\alpha_u J_u^{int}\right)^2+
\left(\alpha_v J_v^{int}\right)^2
},
\]
and
\[
\hat{\mathbf v}[\Xi]
:=
\frac{\alpha_u J_u^{int}\mathbf e_u+
\alpha_v J_v^{int}\mathbf e_v}{\mathcal J[\Xi]+\varepsilon}.
\]

Then the projector uses
\[
\mathcal W[\Xi]\mathcal J[\Xi]\hat{\mathbf v}[\Xi].
\]

This is often the cleaner practical form.

---

## 11) Exact / constrained / open status

### Derived / strongly motivated
- the current image should be built from phase gradients on the torus,
- the major/minor channels should contribute through \(\partial_u\Phi\) and \(\partial_v\Phi\),
- the single-mode branches give exact reduced current images of the form above.

### Constrained but not unique
- the exact projection coefficients \(\alpha_u,\alpha_v\),
- the exact external image directions \(\mathbf e_u,\mathbf e_v\),
- the exact normalization of \(\mathcal J[\Xi]\).

### Still open
- full radiative-field closure from this current image,
- exact support map coupling between \(\mathbfcal V\) and \(X(u,v,\tau)\),
- unique branch calibration to observed current/magnetic moments.

---

## 12) Working conclusion

The next missing piece of the torus-to-EM projector is now no longer undefined.

A first explicit candidate for the transport-current image is:
\[
\boxed{
\mathbfcal V[\Xi](u,v,\tau)
=
\alpha_u A^2\frac{\partial_u\Phi}{R}\mathbf e_u
+
\alpha_v A^2\frac{\partial_v\Phi}{r}\mathbf e_v
}
\]

with the projector using the coherence-weighted combination
\[
\mathcal W[\Xi]\,\mathbfcal V[\Xi].
\]

This is the first explicit transport-current ansatz that is consistent with:
- the torus-wave backbone,
- the source-weight/coherence picture,
- and the branch-level distinction between matter-like and transport-dominated EM behavior.
