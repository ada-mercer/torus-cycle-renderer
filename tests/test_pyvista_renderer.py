from __future__ import annotations

import pytest

pyvista = pytest.importorskip("pyvista")

from torus_cycle_renderer.particles import Electron
from torus_cycle_renderer.rendering import PyVistaRenderConfig, PyVistaTorusRenderer, sample_scene_geometry


def test_pyvista_renderer_camera_helper() -> None:
    renderer = PyVistaTorusRenderer(PyVistaRenderConfig(width=320, height=240, elev=20.0, azim=30.0))
    particle = Electron(spin_state="++", loop_anchor_mode="evolving")
    scene = sample_scene_geometry(particle, time=0.25)
    pos, focal, viewup = renderer._camera_position(scene)

    assert len(pos) == 3
    assert focal == (0.0, 0.0, 0.0)
    assert viewup == (0.0, 0.0, 1.0)
    assert pos != focal
