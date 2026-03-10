# EM Calibration Strategy

Status: derivation scaffold / calibration layer

Purpose: provide the first practical strategy for calibrating the quantitative parameters introduced in
- `EM_RATE_AND_LINEWIDTH_ANSATZ.md`

without pretending that the EM projector program is already uniquely normalized.

The goal is to identify:
- which parameters are structural,
- which are calibration scales,
- how they may be fixed in stages,
- and which relative predictions can be made before absolute normalization is known.

---

## 1) Parameters introduced so far

The current reduced transition-rate chain contains the following free scales:

### A. Global transition scale
\[
\Gamma_0
\]
which sets the overall transition-rate scale.

### B. Coherence broadening scale
\[
\gamma_c
\]
through
\[
\Gamma_{coh,mn}=\gamma_c(1-\mathfrak C_{mn}).
\]

### C. Intrinsic/attractor width scale(s)
\[
\Gamma_{int,mn}
\]
or more microscopically the attractor-basin width measures
\[
\sigma_{mn}^{(attr)}.
\]

### D. External/environmental broadening scale(s)
\[
\Gamma_{ext,mn}.
\]

### E. Projector transport normalizations
\[
\alpha_u,
\qquad
\alpha_v.
\]

### F. Source-weight normalization
The absolute normalization of
\[
\mathcal W[\Xi]
\]
and therefore of
\[
Q_{eff}[\Xi]
]
and
\[
I_{m\to n}^{(eff)}.
\]

---

## 2) Calibration principle: separate shape from scale

The main strategy is:

\[
\boxed{
\text{first calibrate dimensionless relative structure, then calibrate absolute scales.}
}
\]

This means separating:
- **dimensionless relative predictions**, which can already be compared internally,
- **absolute dimensional scales**, which should be fixed only after the relative structure is stable.

This is the safest route.

---

## 3) Stage 1 calibration: relative branch structure only

At the first stage, ignore absolute units and compare only relative quantities such as:

### Relative transition strength
\[
\frac{\Gamma_{m\to n}^{(eff)}}{\Gamma_{p\to q}^{(eff)}}
=
\frac{S_{m\to n}^2}{S_{p\to q}^2}
\]
when using the same global scale \(\Gamma_0\).

### Relative coherence width
\[
\frac{\Gamma_{coh,mn}}{\Gamma_{coh,pq}}
=
\frac{1-\mathfrak C_{mn}}{1-\mathfrak C_{pq}}.
\]

### Relative transport intensity
\[
\frac{I_{m\to n}^{(eff)}}{I_{p\to q}^{(eff)}}
\sim
\frac{S_{m\to n}^2
\int \mathcal W[\Xi_m]|\mathbfcal V[\Xi_m]|^2}{S_{p\to q}^2
\int \mathcal W[\Xi_p]|\mathbfcal V[\Xi_p]|^2}.
\]

These ratios are independent of the absolute global scale and therefore are the cleanest first outputs.

---

## 4) Stage 2 calibration: charge normalization first

Before calibrating rates, the charge normalization should be fixed.

The monopole law is
\[
Q_{eff}[\Xi]=q_*\chi\int_{T^2} dudv\,Rr\,\mathcal W[\Xi].
\]

The most natural first calibration choice is:

### Charge normalization lock
Choose the electron-like branch as the unit-charge calibration state, so that
\[
Q_{eff}[\Xi_e]=-e,
\qquad
Q_{eff}[\Xi_{e^+}]=+e.
\]

This fixes the combination
\[
q_*\int_{T^2} dudv\,Rr\,\mathcal W[\Xi_e].
\]

This is the correct first absolute normalization because charge is the most robust observable presently in the chain.

---

## 5) Stage 3 calibration: transport-current normalization

Once the charge scale is fixed, the current-image normalization can be addressed.

The transport image is
\[
\mathbfcal V[\Xi]
=
\alpha_u A^2\frac{\partial_u\Phi}{R}\mathbf e_u
+
\alpha_v A^2\frac{\partial_v\Phi}{r}\mathbf e_v.
\]

A practical first strategy is to calibrate only the **ratio**
\[
\rho_\alpha := \frac{\alpha_v}{\alpha_u}
\]
first.

Why?
- \(\rho_\alpha\) determines the relative strength of fermic vs bosic transport contribution,
- this is more physically meaningful and easier to compare across branches than fixing both \(\alpha_u\) and \(\alpha_v\) absolutely.

So Stage 3 should first fit
\[
\rho_\alpha
\]
from relative branch behavior before fixing the overall transport scale.

---

## 6) Stage 4 calibration: line-width decomposition

The line width currently decomposes as
\[
\Gamma_{mn} = \Gamma_{int,mn} + \gamma_c(1-\mathfrak C_{mn}) + \Gamma_{ext,mn}.
\]

A good staged strategy is:

### Step 4A. Fix a baseline intrinsic width scale
Choose one reference class of transitions and define a baseline intrinsic width
\[
\Gamma_{int}^{(0)}.
\]

### Step 4B. Fit coherence broadening only as a relative correction
Use
\[
\Gamma_{coh,mn}=\gamma_c(1-\mathfrak C_{mn})
\]
to determine how much width tracks loss of coherence relative to the baseline.

### Step 4C. Treat environmental broadening as external, not structural
Do not fold \(\Gamma_{ext,mn}\) into the theory calibration until the internal structure is stable.

This avoids contaminating the structural fit with environment-specific effects.

---

## 7) Stage 5 calibration: overall transition-rate scale

Only after charge and relative transport/current structure are fixed should the global rate scale \(\Gamma_0\) be calibrated.

The effective rate law is
\[
\Gamma_{m\to n}^{(eff)} = \Gamma_0 S_{m\to n}^2.
\]

So the correct procedure is:
- first stabilize the score structure \(S_{m\to n}\),
- then fit a single global scale \(\Gamma_0\) to one reference transition family,
- then compare all other predicted relative rates.

This prevents the scale fit from hiding structural errors in the score itself.

---

## 8) First practical calibration ladder

The recommended order is:

### Calibration Ladder
1. **Fix charge normalization** using the electron-like unit-charge branch.
2. **Fit the relative transport ratio** \(\rho_\alpha=\alpha_v/\alpha_u\).
3. **Compare relative transition scores** across branches and transitions.
4. **Fix baseline intrinsic width** \(\Gamma_{int}^{(0)}\).
5. **Fit coherence broadening scale** \(\gamma_c\).
6. **Fit global transition-rate scale** \(\Gamma_0\).
7. **Only afterward** include external/environmental width corrections.

This is the safest current calibration strategy.

---

## 9) Dimensionless reduced observables

Before absolute calibration, the most trustworthy predictions are dimensionless ratios.

Define:

### Reduced transition score ratio
\[
\mathcal R^{(S)}_{mn;pq}
:=
\frac{S_{m\to n}}{S_{p\to q}}.
\]

### Reduced rate ratio
\[
\mathcal R^{(\Gamma)}_{mn;pq}
:=
\frac{\Gamma_{m\to n}^{(eff)}}{\Gamma_{p\to q}^{(eff)}}
=
\left(\frac{S_{m\to n}}{S_{p\to q}}\right)^2.
\]

### Reduced intensity ratio
\[
\mathcal R^{(I)}_{mn;pq}
:=
\frac{I_{m\to n}^{(eff)}}{I_{p\to q}^{(eff)}}.
\]

These are the quantities to compare first against any candidate phenomenology.

---

## 10) Branch-specific calibration reading

### Electron-like branch
Use for:
- charge normalization,
- baseline transport-current ratio,
- baseline stable resonant-state reference.

### Photon-like branch
Use for:
- transport-only/radiative calibration,
- line-shape and current-channel tests,
- but not as the first charge-normalization anchor.

### Weak branches
Use later for:
- sign/neutrality cross-checks,
- branch-modified rate comparison,
- not as the first absolute anchor.

### Quark/gluon branches
Use only after the coupled closure and projector chains are more mature.
They are not yet the right place to anchor quantitative EM calibration.

---

## 11) Exact / constrained / open status

### Strongly justified
- charge should be calibrated before rates,
- relative branch/rate/intensity structure should be trusted before absolute scales,
- coherence broadening should be treated as a separate contribution.

### Constrained but not unique
- exact order of fitting \(\Gamma_0\), \(\gamma_c\), and \(\rho_\alpha\),
- exact mapping from branch observables to calibration data.

### Still open
- final absolute numerical calibration,
- spectroscopic dataset matching,
- branch-by-branch quantitative validation beyond the electron-like anchor.

---

## 12) Working conclusion

The correct current strategy is not to fit everything at once.
Instead:
- normalize charge first,
- fix relative transport structure next,
- compare dimensionless transition ratios,
- and only then calibrate widths and rates.

This staged procedure is the most honest and testable way to move the EM projector program from structural theory toward quantitative phenomenology.
