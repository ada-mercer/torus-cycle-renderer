from __future__ import annotations

import numpy as np

from torus_cycle_renderer.particles.electron import Electron, ElectronState
from torus_cycle_renderer.particles.u_quark import UQuark, UQuarkState


def _mod_2pi(arr: np.ndarray) -> np.ndarray:
    return np.mod(arr, 2.0 * np.pi)


def test_uquark_loop_cycle_time_extends_base_cycle() -> None:
    q = UQuark()
    assert q.loop_cycle_time() >= q.cycle_time()


def test_pf_orbit_full_cycle_returns_loop_state_mod_2pi() -> None:
    e = Electron(state=ElectronState(pf_orbit_relative=True), loop_anchor_mode="evolving")
    t_full = e.loop_cycle_time()

    u0, v0 = e.resonant_loop(t=0.0, points=600)
    u1, v1 = e.resonant_loop(t=t_full, points=600)

    assert np.allclose(_mod_2pi(u0), _mod_2pi(u1), atol=1e-9)
    assert np.allclose(_mod_2pi(v0), _mod_2pi(v1), atol=1e-9)


def test_uquark_pf_orbit_full_cycle_returns_loop_state_mod_2pi() -> None:
    q = UQuark(state=UQuarkState(pf_orbit_relative=True))
    t_full = q.loop_cycle_time()

    u0, v0 = q.resonant_loop(t=0.0, points=600)
    u1, v1 = q.resonant_loop(t=t_full, points=600)

    assert np.allclose(_mod_2pi(u0), _mod_2pi(u1), atol=1e-9)
    assert np.allclose(_mod_2pi(v0), _mod_2pi(v1), atol=1e-9)
