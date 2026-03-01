# Electron Steady-State Example

This document gives a complete practical mapping from electron state definition to rendered outputs.

---

## 1) Electron state object

`ElectronState` encodes the physical/render-driving state (single-mode, no superpositions):

- `spin_state` in `{++, +-, -+, --}`
- `winding`
- `resonant_mode = (mode_p, mode_pf)`
- `transport_winding` (optional explicit winding pair)
- `loop_anchor_mode` in `{static, evolving}`
- channel scales `pf_value`, `p_value`
- base geometry and deformation scales

Important convention:
- `mode_p` multiplies `u/theta` (bosic axis)
- `mode_pf` multiplies `v/phi` (fermic axis)

---

## 2) Mode phase law

For one mode:
\[
\varphi(u,v,t)= mode_p\,u + mode_{pf}\,v - \omega t_{eff} + \phi_s,
\]
with
\[
t_{eff}=t\cdot s_t, \quad s_t = p/p_f \;\text{(current model policy)}.
\]

Surface deformation uses:
\[
\delta r(u,v,t) \propto \cos\varphi(u,v,t).
\]

---

## 3) Resonant loop

Transport loop is parameterized by \(s\in[0,1]\):
\[
u(s)=u_0 + 2\pi\,\chi_p\,k_p\,s,
\qquad
v(s)=v_0 + 2\pi\,k_{pf}\,s,
\]
where:
- \(k_{pf},k_p\) come from a rational approximation of \(p_f/p\)
- \(\chi_p\in\{+1,-1\}\) is spin-driven bosic chirality

### Spin rule in code
- up-like states: \(\chi_p=+1\)
- down-like states: \(\chi_p=-1\)
- fermic winding sign remains fixed

---

## 4) Anchor modes

### Static anchor
\[
v_0=\frac{-\phi_s-mode_p u_0}{mode_{pf}}.
\]
Start point fixed in time.

### Evolving anchor
\[
v_0(t)=\frac{\omega t_{eff}-\phi_s-mode_p u_0}{mode_{pf}}.
\]
Start point follows phase lock over time.

---

## 5) Cycle period used by renderer

`Electron.cycle_time()` implements anchor-aware closure:

- static:
\[
T_{static}=\frac{2\pi}{\omega s_t}
\]
- evolving:
\[
T_{evolving}=|mode_{pf}|\,T_{static}
\]

This period is consumed by `render-cycle` when `--cycle-time` is not explicitly set.

---

## 6) Commands

### Spin up (Plotly GIF)
```bash
render-cycle --backend plotly --particle electron --spin-state ++ --loop-anchor-mode evolving --duration 3.2 --fps 14 --format gif --output output/electron_spin_up.gif
```

### Spin down (Plotly GIF)
```bash
render-cycle --backend plotly --particle electron --spin-state=-- --loop-anchor-mode evolving --duration 3.2 --fps 14 --format gif --output output/electron_spin_down.gif
```

(`--spin-state=--` uses `=` to avoid CLI parsing ambiguity.)

---

## 7) Why up/down may still look similar without cues

On symmetric geometry and fixed camera, opposite chirality can look deceptively similar in stills.
Use GIFs and/or add a directional marker for immediate handedness visibility.
