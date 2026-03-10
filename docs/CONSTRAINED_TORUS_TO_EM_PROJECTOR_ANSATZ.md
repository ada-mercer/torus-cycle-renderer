# Constrained Torus-to-EM Projector Ansatz

Status: derivation scaffold / constrained projector family

Purpose: move the EM emergence story from a purely architectural statement
\[
\Xi \to A_\mu \to F_{\mu\nu} \to J^\mu
\]
to a constrained family of explicit projector ansätze from the torus carrier field \(\Xi\).

This note does **not** claim the unique final projector. It derives the strongest current constraint set on what the projector is allowed to look like.

---

## 1) Input field and target output

From `FULL_WAVE_EQUATION_DERIVATION.md`, the internal carrier field is
\[
\Xi(u,v,\tau)
=
A(u,v,\tau)e^{i\Phi(u,v,\tau)},
\qquad (u,v)\in T^2.
\]

We seek a spacetime gauge potential
\[
A_\mu(x)
=
\mathcal P_\mu[\Xi](x)
\]
from which
\[
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu
]
and a source current \(J^\mu\) emerge consistently.

---

## 2) General linear kernel form

The most general first linear ansatz is
\[
\boxed{
A_\mu(x)
=
\int d\tau\int_{T^2} dudv\,Rr\,
K_\mu(x;u,v,\tau)\,\Xi(u,v,\tau)
+
\text{c.c.}
}
\]

where:
- \(K_\mu\) is a projection kernel,
- `c.c.` is added as needed to produce a real spacetime potential.

This is the broadest natural starting family.

---

## 3) First-principles constraints on the kernel

A useful projector family must satisfy the following.

### P1. Linearity at first pass
The first projector family should be linear in \(\Xi\), so that mode decomposition on the torus remains meaningful and tractable.

### P2. Reality of the spacetime potential
The resulting \(A_\mu(x)\) must be real. Hence either:
- the kernel couples to \(\Re\Xi\), or
- the projector uses a complex kernel plus conjugate completion.

### P3. Orientation-sign inheritance
The EM sign branch is already encoded by the orientation variable \(\chi\). Therefore the projector must satisfy
\[
\mathcal P_\mu[\chi\Xi] = \chi\,\mathcal P_\mu[\Xi].
\]

So sign must pass linearly from the internal branch to the projected EM field.

### P4. Neutral-mode cancellation
Modes with neutral total orientation or neutral branch pairing should project to zero net monopole source. The kernel must therefore annihilate neutral sign-balanced combinations at monopole order.

### P5. Translation to far-field locality
The projected field at spacetime point \(x\) should depend on the internal source through a retarded or effective-causal kernel, so the kernel must be of Green-function type rather than arbitrary nonlocal weighting.

### P6. Gauge redundancy at potential level, gauge invariance at field level
The kernel need not uniquely fix \(A_\mu\), but different allowed kernels must produce the same physical content up to
\[
A_\mu \to A_\mu + \partial_\mu\Lambda.
\]

### P7. Rotational covariance in the external projection
The kernel must not privilege an arbitrary external spatial direction except through the projected multipole structure of the internal source.

---

## 4) Minimal Green-kernel projector family

The smallest useful restricted family is obtained by writing
\[
K_\mu(x;u,v,\tau) = G(x;X(u,v,\tau))\,W_\mu(u,v,\tau),
\]
where:
- \(G\) is a retarded or quasi-static Green kernel in spacetime,
- \(X(u,v,\tau)\) is the effective spacetime emission/support map,
- \(W_\mu\) is an internal current-weight functional on the torus.

Then
\[
\boxed{
A_\mu(x)
=
\int d\tau\int_{T^2} dudv\,Rr\,
G(x;X(u,v,\tau))\,W_\mu(u,v,\tau)\,\Xi(u,v,\tau)
+
\text{c.c.}
}
\]

This is the first constrained projector family.

---

## 5) Static/quasi-static reduction

In the quasi-static limit, the time structure reduces and the scalar potential should take Coulomb-like form. Therefore the scalar part of the projector must reduce to
\[
A_0(\mathbf x)
\sim
\int_{T^2} dudv\,Rr\,
\frac{\rho_{int}(u,v)}{|\mathbf x-\mathbf X(u,v)|},
\]
where \(\rho_{int}\) is the projected internal charge density functional.

Thus the quasi-static kernel forces the family toward a Green-function structure with Coulomb asymptotics.

---

## 6) Internal source moments

The key new object is the projected internal source density. The simplest scalar family is
\[
\rho_{int}(u,v,\tau) = q_*\,\chi\,\mathcal W[\Xi](u,v,\tau),
\]
where:
- \(q_*\) is the base charge scale,
- \(\chi\) carries sign,
- \(\mathcal W[\Xi]\ge 0\) is a source-weight functional.

The previous quark/electron discussion suggests that \(\mathcal W[\Xi]\) should track the **coherently projectable** fraction of the internal state rather than raw closure defect.

So the projector family is already constrained to the form
\[
\boxed{
A_0(\mathbf x)
\sim
q_*\chi
\int_{T^2} dudv\,Rr\,
\frac{\mathcal W[\Xi](u,v)}{|\mathbf x-\mathbf X(u,v)|}
}
\]
up to normalization and retardation details.

---

## 7) Minimal vector-current family

For the spatial components, the analogous first family is
\[
\mathbf A(\mathbf x)
\sim
\int d\tau\int_{T^2} dudv\,Rr\,
\frac{\mathbf J_{int}(u,v,\tau)}{|\mathbf x-\mathbf X(u,v,\tau)|},
\]
with
\[
\mathbf J_{int} = q_*\chi\,\mathcal W[\Xi]\,\mathbf V_{int}[\Xi].
\]

This introduces a projected internal velocity/current direction \(\mathbf V_{int}[\Xi]\), which is the external image of the internal transport structure.

Thus the projector family separates naturally into:
- source weight \(\mathcal W[\Xi]\),
- transport direction \(\mathbf V_{int}[\Xi]\),
- Green propagation kernel.

---

## 8) Source-weight constraint from previous derivation work

The earlier closure/projector notes already suggest that the observable source content should scale with the coherently completed portion of the internal state.

Therefore the source-weight functional is constrained by
\[
\mathcal W[\Xi] \propto \mathfrak C[\Xi],
\]
where \(\mathfrak C[\Xi]\) is the integrated coherence fraction from `LOCAL_COHERENCE_FUNCTIONAL_FOR_PROJECTOR_V1.md`.

At coarse-grained branch level this becomes
\[
\mathfrak C[\Xi]\approx 1-\delta
\]
for defect-bearing branches.

So the projector family must be compatible with
\[
\boxed{
\rho_{int} \sim q_*\chi\,\mathfrak C[\Xi].
}
\]

This is now the strongest current projector-side constraint.

---

## 9) Projector family ruled out by consistency

The following kinds of projector are now disfavored or ruled out:

### R1. Sign-blind projector
Any kernel that does not preserve the orientation sign \(\chi\) cannot reproduce electron/positron reversal cleanly.

### R2. Raw-defect projector
A projector whose source magnitude grows directly with unresolved defect is disfavored, because it would make less-complete branches appear as stronger coherent EM sources.

### R3. Purely local point-evaluation projector on the torus
Any projector that samples only a single carrier point without integrating or averaging is too sensitive to gauge/phase location and does not support robust far-field emergence.

### R4. Non-Green arbitrary nonlocal projector
A kernel with no retarded/Coulomb/propagator structure does not naturally recover Maxwell-like far-field behavior.

---

## 10) Recommended constrained ansatz family

The strongest current family is therefore:
\[
\boxed{
A_\mu(x)
=
q_*\chi
\int d\tau\int_{T^2} dudv\,Rr\,
G(x;X(u,v,\tau))\,
\mathcal W[\Xi](u,v,\tau)
\,\mathcal V_\mu[\Xi](u,v,\tau)
}
\]
with:
- \(\mathcal V_0\equiv 1\) for the scalar source channel,
- \(\mathcal V_i\) the projected transport/current components,
- \(\mathcal W[\Xi]\) the coherence/source-weight functional.

This is the best current constrained projector ansatz family.

The spatial transport-current image \(\mathcal V_i[\Xi]\) is now developed further in:
- `docs/TRANSPORT_CURRENT_IMAGE_ANSATZ.md`

---

## 11) What remains open

This note still does **not** uniquely derive:
- the exact support map \(X(u,v,\tau)\),
- the exact form of \(\mathcal V_i[\Xi]\),
- the unique normalization of \(\mathcal W[\Xi]\),
- the final gauge-fixing prescription at potential level,
- the full nonabelian extension for color sectors.

So the projector is now constrained, but not yet uniquely closed.

---

## 12) Working conclusion

The torus-to-EM emergence story can now be stated more strongly than before:

- the input field \(\Xi\) is fully specified by the torus-wave backbone,
- the projector must be linear at first pass,
- it must inherit sign through \(\chi\),
- it must use a Green/propagator structure for correct far-field behavior,
- and its source strength must be controlled by the coherently projectable fraction of the internal state.

This is the first constrained family of torus-to-EM projector ansätze that goes beyond architecture-level consistency while remaining honest about what is still undetermined.
