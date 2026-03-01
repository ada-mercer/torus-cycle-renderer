from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def coupled_phase_trajectory(
    t: float,
    points: int,
    base_u: float,
    base_v: float,
    coupling: float,
    detuning: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate a resonant loop via a tiny coupled-phase ODE.

    State y = [theta_u, theta_v]. Dynamics:
      d theta_u / ds = base_u + coupling * sin(theta_v - theta_u)
      d theta_v / ds = base_v + coupling * sin(theta_u - theta_v) + detuning

    This gives richer loop structure than static Lissajous lines while staying lightweight.
    """

    def rhs(_s: float, y: np.ndarray) -> np.ndarray:
        tu, tv = y
        dtu = base_u + coupling * np.sin(tv - tu)
        dtv = base_v + coupling * np.sin(tu - tv) + detuning
        return np.array([dtu, dtv], dtype=float)

    s_grid = np.linspace(0.0, 2 * np.pi, points)
    y0 = np.array([0.15 * t, -0.10 * t], dtype=float)

    sol = solve_ivp(
        rhs,
        t_span=(s_grid[0], s_grid[-1]),
        y0=y0,
        t_eval=s_grid,
        method="RK45",
        rtol=1e-7,
        atol=1e-9,
    )

    if not sol.success:
        raise RuntimeError(f"Resonance ODE integration failed: {sol.message}")

    u = np.mod(sol.y[0], 2 * np.pi)
    v = np.mod(sol.y[1], 2 * np.pi)
    return u, v
