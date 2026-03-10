from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from torus_cycle_renderer.math import torus_surface, torus_frame
from torus_cycle_renderer.particles import AbstractParticle


@dataclass(frozen=True)
class SceneGeometry:
    particle_name: str
    particle_subtitle: str
    p_value: float
    pf_value: float
    ratio_label: str
    major_radius: float
    minor_radius: float
    deform_amp: float
    loop_lift: float
    time_visible: float
    surface_u: np.ndarray
    surface_v: np.ndarray
    surface_deformation: np.ndarray
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    loop_u: np.ndarray
    loop_v: np.ndarray
    loop_deformation: np.ndarray
    lx: np.ndarray
    ly: np.ndarray
    lz: np.ndarray
    z_floor: float


def ratio_label(p_value: float, pf_value: float) -> str:
    if abs(pf_value) < 1e-12:
        return "∞"
    return f"{(p_value / pf_value):.3f}"


def particle_subtitle(particle: AbstractParticle) -> str:
    cls = particle.__class__.__name__
    if cls == "Electron":
        return "reference resonant branch"
    if cls in {"WPlus", "WMinus", "ZBoson"}:
        return "weak-channel resonant probe"
    if cls in {"UQuark", "DQuark"}:
        return "defect-bearing quark probe"
    if cls == "Gluon":
        return "color-transport prototype"
    if cls == "Photon":
        return "pure bosic probe branch"
    return "renderer correspondence branch"


def sample_scene_geometry(
    particle: AbstractParticle,
    time: float,
    *,
    time_scale: float = 1.0,
    loop_points: int = 900,
    loop_lift_override: float | None = None,
) -> SceneGeometry:
    p = particle.params
    t_vis = time * time_scale

    u, v = torus_frame()
    deform = particle.deformation(u, v, t_vis)
    x, y, z = torus_surface(u, v, p.major_radius, p.minor_radius, deformation=deform)

    loop = particle.loop_geometry(t=t_vis, points=max(64, int(loop_points)))
    lu, lv = loop.u, loop.v
    ldef = particle.deformation(lu, lv, t_vis)

    loop_lift = loop_lift_override if loop_lift_override is not None else getattr(p, "loop_lift", 0.04)
    lx, ly, lz = torus_surface(
        lu,
        lv,
        p.major_radius,
        p.minor_radius,
        deformation=ldef + loop_lift,
    )

    z_floor = float(np.min(z) - 0.12 * (p.major_radius + p.minor_radius))

    return SceneGeometry(
        particle_name=particle.name,
        particle_subtitle=particle_subtitle(particle),
        p_value=float(p.p_value),
        pf_value=float(p.pf_value),
        ratio_label=ratio_label(float(p.p_value), float(p.pf_value)),
        major_radius=float(p.major_radius),
        minor_radius=float(p.minor_radius),
        deform_amp=float(p.deform_amp),
        loop_lift=float(loop_lift),
        time_visible=float(t_vis),
        surface_u=u,
        surface_v=v,
        surface_deformation=deform,
        x=x,
        y=y,
        z=z,
        loop_u=lu,
        loop_v=lv,
        loop_deformation=ldef,
        lx=lx,
        ly=ly,
        lz=lz,
        z_floor=z_floor,
    )
