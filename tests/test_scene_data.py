from __future__ import annotations

import numpy as np

from torus_cycle_renderer.particles import Electron, UQuark
from torus_cycle_renderer.rendering import sample_scene_geometry, particle_subtitle, frame_times


def test_scene_geometry_sampler_returns_consistent_shapes() -> None:
    e = Electron(spin_state="++", loop_anchor_mode="evolving")
    scene = sample_scene_geometry(e, time=0.4, time_scale=1.0, loop_points=256)

    assert scene.x.shape == scene.y.shape == scene.z.shape
    assert scene.surface_u.shape == scene.surface_v.shape == scene.x.shape
    assert scene.lx.shape == scene.ly.shape == scene.lz.shape
    assert len(scene.lx) == 256
    assert np.isfinite(scene.z_floor)
    assert scene.ratio_label != ""


def test_particle_subtitle_tracks_branch_kind() -> None:
    assert particle_subtitle(Electron(spin_state="++", loop_anchor_mode="evolving")) == "reference resonant branch"
    assert particle_subtitle(UQuark()) == "defect-bearing quark probe"


def test_frame_times_excludes_terminal_duplicate_frame() -> None:
    times = frame_times(4, 2.0)
    assert times == [0.0, 0.5, 1.0, 1.5]
