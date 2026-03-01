from __future__ import annotations

import numpy as np


def torus_surface(
    u: np.ndarray,
    v: np.ndarray,
    major_radius: float,
    minor_radius: float,
    deformation: np.ndarray | float = 0.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    r = minor_radius + deformation
    x = (major_radius + r * np.cos(v)) * np.cos(u)
    y = (major_radius + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    return x, y, z


def torus_frame(
    u_res: int = 320,
    v_res: int = 180,
) -> tuple[np.ndarray, np.ndarray]:
    u = np.linspace(0.0, 2 * np.pi, u_res)
    v = np.linspace(0.0, 2 * np.pi, v_res)
    return np.meshgrid(u, v)
