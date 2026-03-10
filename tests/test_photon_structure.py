from __future__ import annotations

import numpy as np

from torus_cycle_renderer.particles.photon import Photon


def test_photon_has_zero_fermic_channel() -> None:
    p = Photon().params
    assert p.pf_value == 0.0


def test_photon_loop_has_no_phi_transport_component() -> None:
    ph = Photon()
    _u, v = ph.resonant_loop(t=0.7, points=600)
    assert np.allclose(v, v[0], atol=1e-12)
