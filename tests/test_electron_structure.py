from __future__ import annotations

import math

import numpy as np

from torus_cycle_renderer.particles.electron import Electron


TAU = 2.0 * math.pi


def _mod_2pi(x: float) -> float:
    return float(np.mod(x, TAU))


def test_resonant_loop_closes_and_spin_flips_bosic_chirality() -> None:
    """Loop closes modulo 2π and spin flip reverses major-angle handedness."""
    expected_du_sign = {
        "++": +1,
        "+-": +1,
        "-+": -1,
        "--": -1,
    }

    for spin_state, sign in expected_du_sign.items():
        e = Electron(spin_state=spin_state, loop_anchor_mode="evolving")
        u, v = e.resonant_loop(t=0.0, points=901)

        du = float(u[-1] - u[0])
        dv = float(v[-1] - v[0])

        # Geometric closure modulo 2π on both angles.
        assert np.isclose(_mod_2pi(du), 0.0, atol=1e-10)
        assert np.isclose(_mod_2pi(dv), 0.0, atol=1e-10)

        # Spin branch flips bosic handedness (u-direction only).
        assert np.sign(du) == sign
        # Fermic orientation remains fixed in this matter-branch convention.
        assert dv > 0.0


def test_phase_closure_is_integer_multiple_of_2pi() -> None:
    """Single-loop phase advance should close on an integer 2π multiple."""
    for spin_state in ["++", "+-", "-+", "--"]:
        e = Electron(spin_state=spin_state, loop_anchor_mode="evolving")
        mode_p, mode_pf = e.state.resonant_mode
        phase0 = {
            "++": 0.0,
            "+-": 0.5 * math.pi,
            "-+": -0.5 * math.pi,
            "--": math.pi,
        }[spin_state]

        u, v = e.resonant_loop(t=0.0, points=901)

        phi_start = mode_p * u[0] + mode_pf * v[0] + phase0
        phi_end = mode_p * u[-1] + mode_pf * v[-1] + phase0
        dphi = float(phi_end - phi_start)

        turns = dphi / TAU
        assert np.isclose(turns, round(turns), atol=1e-10)


def test_cycle_time_matches_anchor_law() -> None:
    """cycle_time() should follow static/evolving formula in code docs."""
    e_static = Electron(spin_state="++", loop_anchor_mode="static")
    e_evolving = Electron(spin_state="++", loop_anchor_mode="evolving")

    omega = e_static._effective_omega()
    scale = e_static._time_scale()
    base = TAU / (omega * scale)

    # Static anchor law.
    assert np.isclose(e_static.cycle_time(), base, rtol=1e-12, atol=1e-12)

    # Evolving anchor law.
    mode_pf = abs(e_evolving.state.resonant_mode[1])
    assert np.isclose(e_evolving.cycle_time(), mode_pf * base, rtol=1e-12, atol=1e-12)
