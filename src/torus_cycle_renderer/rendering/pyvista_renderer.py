from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import ctypes.util
import os

import numpy as np

from torus_cycle_renderer.particles import AbstractParticle

from .geometry_export import export_loop_obj, export_scene_npz, export_torus_obj
from .scene_data import sample_scene_geometry

try:  # Optional dependency.
    import pyvista as pv
except Exception:  # pragma: no cover - exercised only when dependency missing.
    pv = None


@dataclass(frozen=True)
class PyVistaRenderConfig:
    width: int = 1280
    height: int = 720
    background: str = "#0e1117"
    elev: float = 22.0
    azim: float = 36.0
    camera_radius: float = 4.8
    camera_zoom: float = 0.58
    loop_lift: float = 0.04
    loop_points: int = 900
    mesh_opacity: float = 0.06
    gridline_stride_u: int = 5
    gridline_stride_v: int = 4
    gridline_width: float = 1.0
    gridline_opacity: float = 0.22
    loop_line_width: float = 4.0
    torus_color: str = "#3a86ff"
    loop_color: str = "#ff006e"
    time_scale: float = 1.0


class PyVistaTorusRenderer:
    def __init__(self, config: PyVistaRenderConfig | None = None):
        self.config = config or PyVistaRenderConfig()
        if pv is None:
            raise ImportError(
                "PyVista backend requested, but `pyvista` is not installed. "
                "Install it with `pip install pyvista` or the project extra if configured."
            )

    def _has_headless_runtime(self) -> bool:
        if os.environ.get("DISPLAY"):
            return True
        return bool(ctypes.util.find_library("EGL") or ctypes.util.find_library("OSMesa"))

    def _ensure_runtime_support(self) -> None:
        if self._has_headless_runtime():
            return
        raise RuntimeError(
            "PyVista/VTK offscreen rendering is unavailable on this host. "
            "No DISPLAY is set and neither EGL nor OSMesa could be found. "
            "Install a headless runtime (for example xvfb, EGL, or OSMesa) before using the PyVista backend."
        )

    def _camera_position(self, scene) -> list[tuple[float, float, float]]:
        cfg = self.config
        extent = scene.major_radius + scene.minor_radius + scene.deform_amp + 0.2
        radius = cfg.camera_radius * extent
        az = np.deg2rad(cfg.azim)
        alt = np.deg2rad(cfg.elev)
        pos = (
            float(radius * np.cos(alt) * np.cos(az)),
            float(radius * np.cos(alt) * np.sin(az)),
            float(radius * np.sin(alt)),
        )
        focal = (0.0, 0.0, 0.0)
        viewup = (0.0, 0.0, 1.0)
        return [pos, focal, viewup]

    def _surface_mesh(self, scene):
        assert pv is not None
        grid = pv.StructuredGrid(scene.x, scene.y, scene.z)
        return grid.extract_surface(algorithm="dataset_surface")

    def _gridline_polylines(self, scene):
        assert pv is not None
        traces = []

        def make_line(x: np.ndarray, y: np.ndarray, z: np.ndarray):
            pts = np.column_stack([x, y, z])
            poly = pv.PolyData()
            poly.points = pts
            poly.lines = np.hstack(([len(pts)], np.arange(len(pts), dtype=np.int32)))
            return poly

        for iv in range(0, scene.x.shape[0], max(self.config.gridline_stride_v, 1)):
            traces.append(make_line(scene.x[iv, :], scene.y[iv, :], scene.z[iv, :]))
        for iu in range(0, scene.x.shape[1], max(self.config.gridline_stride_u, 1)):
            traces.append(make_line(scene.x[:, iu], scene.y[:, iu], scene.z[:, iu]))
        return traces

    def _loop_polyline(self, scene):
        assert pv is not None
        pts = np.column_stack([scene.lx, scene.ly, scene.lz])
        poly = pv.PolyData()
        poly.points = pts
        poly.lines = np.hstack(([len(pts)], np.arange(len(pts), dtype=np.int32)))
        return poly

    def _add_lights(self, plotter, scene) -> None:
        assert pv is not None
        extent = scene.major_radius + scene.minor_radius + scene.deform_amp
        key = pv.Light(
            position=(2.6 * extent, 1.8 * extent, 2.2 * extent),
            focal_point=(0.0, 0.0, 0.0),
            color="white",
            intensity=0.55,
            positional=True,
        )
        fill = pv.Light(
            position=(-2.0 * extent, 1.2 * extent, 0.8 * extent),
            focal_point=(0.0, 0.0, 0.0),
            color=(1.0, 1.0, 1.0),
            intensity=0.10,
            positional=True,
        )
        plotter.add_light(key)
        plotter.add_light(fill)

    def _title_text(self, scene) -> str:
        return scene.particle_name.split(" mode=")[0]

    def render(self, particle: AbstractParticle, time: float, output_path: str, export_geometry: bool = False) -> None:
        assert pv is not None
        self._ensure_runtime_support()
        cfg = self.config
        scene = sample_scene_geometry(
            particle,
            time,
            time_scale=cfg.time_scale,
            loop_points=cfg.loop_points,
            loop_lift_override=cfg.loop_lift,
        )

        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            raise ValueError("PyVista renderer currently supports static image outputs only; use CLI cycle mode for GIF/MP4 stitching.")

        plotter = pv.Plotter(off_screen=True, window_size=(cfg.width, cfg.height))
        plotter.set_background(cfg.background)
        try:
            plotter.ren_win.SetAlphaBitPlanes(1)
            plotter.ren_win.SetMultiSamples(0)
        except Exception:
            pass
        try:
            plotter.enable_depth_peeling(number_of_peels=8, occlusion_ratio=0.0)
        except Exception:
            pass

        surface = self._surface_mesh(scene)
        gridlines = self._gridline_polylines(scene)
        loop = self._loop_polyline(scene)

        self._add_lights(plotter, scene)
        plotter.add_mesh(
            surface,
            color=cfg.torus_color,
            opacity=cfg.mesh_opacity,
            lighting=True,
            smooth_shading=True,
            ambient=0.10,
            diffuse=0.78,
            specular=0.06,
            specular_power=8.0,
            use_transparency=True,
            show_edges=False,
        )
        for gridline in gridlines:
            plotter.add_mesh(
                gridline,
                color=(1.0, 1.0, 1.0),
                opacity=cfg.gridline_opacity,
                line_width=cfg.gridline_width,
            )
        loop_actor = plotter.add_mesh(
            loop,
            color=cfg.loop_color,
            opacity=0.98,
            line_width=cfg.loop_line_width,
            render_lines_as_tubes=True,
            lighting=False,
        )
        try:
            loop_actor.mapper.resolve = "polygon_offset"
        except Exception:
            pass

        plotter.camera_position = self._camera_position(scene)
        if abs(cfg.camera_zoom - 1.0) > 1e-9:
            plotter.camera.zoom(cfg.camera_zoom)
        plotter.camera.reset_clipping_range()
        plotter.add_text(self._title_text(scene), position=(12, cfg.height - 34), font_size=14, color="white")
        plotter.add_text(scene.particle_subtitle, position=(12, cfg.height - 58), font_size=9, color="#c9d1d9")
        plotter.add_text(
            f"p={scene.p_value:.3f}, p_f={scene.pf_value:.3f}, p/p_f={scene.ratio_label}",
            position=(12, cfg.height - 78),
            font_size=9,
            color="white",
        )

        plotter.screenshot(str(out))
        plotter.close()

        if export_geometry:
            stem = out.with_suffix("")
            export_scene_npz(str(stem) + "_geom.npz", scene.x, scene.y, scene.z, scene.lx, scene.ly, scene.lz)
            export_torus_obj(str(stem) + "_torus.obj", scene.x, scene.y, scene.z)
            export_loop_obj(str(stem) + "_loop.obj", scene.lx, scene.ly, scene.lz)
