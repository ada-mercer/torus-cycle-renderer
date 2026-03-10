# EM Far-Field and Multipole Consequences of the Torus Projector

Status: derivation scaffold / first consequence analysis

This note takes the constrained projector family from
- `CONSTRAINED_TORUS_TO_EM_PROJECTOR_ANSATZ.md`

and derives the first far-field / multipole consequences.

The purpose is to move from
- “a projector exists”

to
- “here is what such a projector must imply for observed EM behavior.”

---

## 1) Starting projector family

Use the constrained family
\[
A_\mu(x)
=
q_*\chi
\int d\tau\int_{T^2} dudv\,Rr\,
G(x;X(u,v,\tau))\,
\mathcal W[\Xi](u,v,\tau)
\,\mathcal V_\mu[\Xi](u,v,\tau).
\]

In the quasi-static scalar channel,
\[
A_0(\mathbf x)
\sim
q_*\chi
\int_{T^2} dudv\,Rr\,
\frac{\mathcal W[\Xi](u,v)}{|\mathbf x-\mathbf X(u,v)|}.
\]

---

## 2) Far-field expansion

For observation point \(\mathbf x\) far from the support of the effective source map \(\mathbf X\), expand
\[
\frac{1}{|\mathbf x-\mathbf X|}
=
\frac{1}{r}
+
\frac{\hat{\mathbf r}\cdot\mathbf X}{r^2}
+
\frac{3(\hat{\mathbf r}\cdot\mathbf X)^2-\mathbf X^2}{2r^3}
+
\cdots
\]
where
\[
r:=|\mathbf x|,
\qquad \hat{\mathbf r}:=\mathbf x/r.
\]

Substituting into the scalar projector gives the far-field expansion of the projected potential.

---

## 3) Projected monopole term

The leading term is
\[
A_0^{(0)}(\mathbf x)
\sim
\frac{q_*\chi}{r}
\int_{T^2} dudv\,Rr\,\mathcal W[\Xi](u,v).
\]

Define the integrated source weight
\[
Q_{eff}[\Xi]
:=
q_*\chi
\int_{T^2} dudv\,Rr\,\mathcal W[\Xi](u,v).
\]

Then
\[
\boxed{
A_0^{(0)}(\mathbf x)
\sim
\frac{Q_{eff}[\Xi]}{r}.
}
\]

So the effective observed electric charge is the monopole moment of the projector-weighted internal source.

This is the cleanest quantitative emergence statement now available.

---

## 4) Connection to the coherence fraction

If the source-weight functional is normalized so that
\[
\int_{T^2} dudv\,Rr\,\mathcal W[\Xi](u,v)=\mathfrak C[\Xi],
\]
then
\[
\boxed{
Q_{eff}[\Xi]=q_*\chi\,\mathfrak C[\Xi].
}
\]

For defect-bearing coarse-grained branches with
\[
\mathfrak C[\Xi]\approx 1-\delta,
\]
this gives
\[
Q_{eff}\approx q_*\chi(1-\delta).
\]

Thus the earlier effective-charge ansatz appears as the far-field monopole consequence of the constrained projector family.

This is the strongest current bridge from the torus field to observed charge magnitude.

---

## 5) Projected dipole term

The next term in the far-field expansion is
\[
A_0^{(1)}(\mathbf x)
\sim
\frac{q_*\chi}{r^2}
\hat{\mathbf r}\cdot
\int_{T^2} dudv\,Rr\,
\mathcal W[\Xi](u,v)\,\mathbf X(u,v).
\]

Define the projected electric dipole moment
\[
\mathbf p_{eff}[\Xi]
:=
q_*\chi
\int_{T^2} dudv\,Rr\,
\mathcal W[\Xi](u,v)\,\mathbf X(u,v).
\]

Then
\[
\boxed{
A_0^{(1)}(\mathbf x)
\sim
\frac{\hat{\mathbf r}\cdot\mathbf p_{eff}[\Xi]}{r^2}.
}
\]

So asymmetry in the weighted internal source map naturally produces dipole-like projected behavior.

---

## 6) Neutral branches and monopole cancellation

A branch is electromagnetically neutral at monopole order when
\[
Q_{eff}[\Xi]=0.
\]

From the projector form, this occurs if either:
- \(\chi=0\)-type effective neutrality is realized (in a composite or branch-balanced sense), or
- the weighted source integral cancels,
\[
\int_{T^2} dudv\,Rr\,\mathcal W[\Xi]=0,
\]
which is possible only for sign-balanced or internally canceling constructions.

So the projector immediately predicts:
- charged branches require nonzero monopole weight,
- neutral branches must have vanishing weighted monopole content.

This matches the intended distinction between charged matter branches and neutral branches such as the renderer's neutral weak path.

---

## 7) Photon-like/radiative branch consequence

A purely radiative branch should not project a static monopole source.
So for a photon-like branch one expects
\[
Q_{eff}[\Xi_{\gamma}] = 0,
\qquad
\mathbf p_{eff}[\Xi_{\gamma}] = 0
]
at static source order, while time-varying/transverse current structure remains nonzero.

Thus the projector naturally separates:
- charge-bearing matter branches,
- neutral/radiative branches,

by the vanishing or nonvanishing of the low-order projected multipoles.

---

## 8) Vector potential and current moment

For the spatial potential,
\[
\mathbf A(\mathbf x)
\sim
q_*\chi
\int d\tau\int_{T^2} dudv\,Rr\,
\frac{\mathcal W[\Xi]\,\mathbf V_{int}[\Xi]}{|\mathbf x-\mathbf X|}.
\]

In the far field, the leading current moment is
\[
\mathbf J_{eff}[\Xi]
:=
q_*\chi
\int d\tau\int_{T^2} dudv\,Rr\,
\mathcal W[\Xi]\,\mathbf V_{int}[\Xi].
\]

This provides the first route by which internal transport on the torus projects into spacetime current/magnetic behavior.

A more explicit current-image ansatz is now developed in:
- `docs/TRANSPORT_CURRENT_IMAGE_ANSATZ.md`

So the projector family yields not just charge, but current-like multipoles as well.

---

## 9) First branch-level consequences

### Electron-like branch
Expected:
- nonzero monopole term,
- possible dipole substructure from asymmetry,
- current structure tied to internal transport.

### Positron-like branch
Same magnitude structure, opposite sign through \(\chi\).

### Photon-like branch
Vanishing static monopole term, dominant transport/transverse structure.

### Neutral weak branch
Vanishing monopole at leading order by branch neutrality, nontrivial higher moments possible.

### Charged weak branches
Nonzero sign-definite monopole term at branch level, consistent with charged weak sign assignment.

These are exactly the kinds of branch separations the EM theory was aiming to support.

---

## 10) What is now genuinely derived

The following is now derivable from the constrained projector family:

### D1. Effective observed charge as projected monopole weight
\[
Q_{eff}[\Xi]=q_*\chi\int_{T^2} dudv\,Rr\,\mathcal W[\Xi].
\]

### D2. Coherence-based charge law as far-field limit
If \(\mathcal W\) integrates to \(\mathfrak C[\Xi]\), then
\[
Q_{eff}=q_*\chi\,\mathfrak C[\Xi].
\]

### D3. First electric dipole moment from weighted source asymmetry
\[
\mathbf p_{eff}[\Xi]=q_*\chi\int_{T^2} dudv\,Rr\,\mathcal W[\Xi]\mathbf X(u,v).
\]

This is real progress beyond architecture-level discussion.

---

## 11) What remains ansatz-level

The following are still not uniquely fixed:
- the exact support map \(\mathbf X(u,v,\tau)\),
- the exact source-weight normalization \(\mathcal W[\Xi]\),
- the exact current-direction functional \(\mathbf V_{int}[\Xi]\),
- the full radiative field derivation at non-static order,
- final branch calibration to observed charge units.

So the far-field consequences are now constrained and partially derived, but not yet numerically closed.

---

## 12) Working conclusion

The constrained torus-to-EM projector family now implies a concrete far-field picture:
- effective charge is the projected monopole moment of the weighted internal source,
- dipole behavior comes from weighted source asymmetry,
- transport/current structure projects into the vector-potential channel,
- neutral and radiative branches are distinguished by vanishing low-order monopoles.

This is the first point at which the EM emergence program yields clear branch-level consequences beyond purely architectural consistency.
