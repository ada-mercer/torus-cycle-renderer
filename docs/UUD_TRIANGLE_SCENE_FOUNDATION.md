# UUD Triangle Scene Foundation

Status: prototype scene note

This note defines how to read the `uud` triangle scene rendered by:
- `scripts/render_uud_triangle.py`

## 1) What the scene is

A first baryon-like composite visualization using:
- three local quark torus nodes,
- `u`, `u`, `d`,
- arranged at the vertices of an equilateral triangle,
- with a cyclic band overlay joining the nodes.

## 2) What the scene is **not**

It is **not** a claim that three isolated free quark toruses already form a closed proton state by themselves.

Instead, the scene should be read as a **quark-only effective render** in which:
- explicit gluon toruses are omitted,
- but their coupled-closure role is integrated out into effective edge phase lags / exchange channels.

## 3) Mathematical reading

Working defect assignments:
\[
\delta_A=\frac13,
\qquad
\delta_B=\frac13,
\qquad
\delta_C=\frac23.
\]

So the three isolated quark defects alone do not close:
\[
\delta_A+\delta_B+\delta_C = \frac43.
\]

The scene therefore uses integrated-out edge compensation terms
\[
\gamma_{AB},\gamma_{BC},\gamma_{CA}
\]
with first symmetric prototype choice
\[
\gamma_{AB}=\gamma_{BC}=\gamma_{CA}=\frac29,
\]
so that
\[
\delta_A+\delta_B+\delta_C+\gamma_{AB}+\gamma_{BC}+\gamma_{CA}=2.
\]

This is the closure logic the scene is visualizing.

## 4) Source/drain / port interpretation

Each quark torus is treated as a coupled node with:
- one incoming port,
- one outgoing port,
- zero net node injection.

So the cyclic band should be read as passing through the nodes rather than being emitted by isolated source particles.

## 5) Practical interpretation

This scene is best treated as:
- a coupled-closure visualization,
- a renderer-level prototype,
- an honest first step toward baryon-like composite scenes,
- not yet a final composite-field solver.
