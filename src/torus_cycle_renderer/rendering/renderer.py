from __future__ import annotations

from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np

from torus_cycle_renderer.math import torus_surface, torus_frame
from torus_cycle_renderer.particles import AbstractParticle


@dataclass(frozen=True)
class RenderConfig:
    width: int = 1280
    height: int = 720
    dpi: int = 100
    elev: float = 22.0
    azim: float = 36.0

    # Surface / wireframe
    face_alpha: float = 0.45
    surface_edge_linewidth: float = 0.10
    surface_edge_alpha: float = 0.30
    wireframe_linewidth: float = 0.36
    wireframe_alpha: float = 0.28
    wireframe_stride: int = 5

    # Loop
    loop_linewidth: float = 2.6
    loop_lift: float = 0.05

    # Visual styling (renderer-owned)
    torus_color: str = "#3a86ff"
    loop_color: str = "#ff006e"
    time_scale: float = 1.0

    # Lighting / shadow
    light_azdeg: float = 35.0
    light_altdeg: float = 45.0
    ambient: float = 0.35
    diffuse: float = 0.65
    shadow_alpha: float = 0.14

    background: str = "#0e1117"


def _normalize(v: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    return v / np.clip(n, eps, None)


class TorusRenderer:
    def __init__(self, config: RenderConfig | None = None):
        self.config = config or RenderConfig()

    def _surface_normals(self, x: np.ndarray, y: np.ndarray, z: np.ndarray) -> np.ndarray:
        p = np.stack([x, y, z], axis=-1)
        du = np.roll(p, -1, axis=1) - np.roll(p, 1, axis=1)
        dv = np.roll(p, -1, axis=0) - np.roll(p, 1, axis=0)
        n = np.cross(du, dv)
        return _normalize(n)

    def _surface_facecolors(self, x: np.ndarray, y: np.ndarray, z: np.ndarray, base_color: str) -> np.ndarray:
        cfg = self.config
        base = np.array(to_rgb(base_color))[None, None, :]

        normals = self._surface_normals(x, y, z)

        az = np.deg2rad(cfg.light_azdeg)
        alt = np.deg2rad(cfg.light_altdeg)
        ldir = np.array([
            np.cos(alt) * np.cos(az),
            np.cos(alt) * np.sin(az),
            np.sin(alt),
        ])

        lambert = np.clip(np.sum(normals * ldir[None, None, :], axis=-1), 0.0, 1.0)
        intensity = np.clip(cfg.ambient + cfg.diffuse * lambert, 0.0, 1.0)

        rgb = np.clip(base * intensity[..., None], 0.0, 1.0)
        alpha = np.full((*rgb.shape[:2], 1), cfg.face_alpha)
        return np.concatenate([rgb, alpha], axis=-1)

    def _line_collection(self, x: np.ndarray, y: np.ndarray, z: np.ndarray, color: str, lw: float) -> Line3DCollection:
        pts = np.column_stack([x, y, z])
        segs = np.stack([pts[:-1], pts[1:]], axis=1)
        coll = Line3DCollection(segs, colors=color, linewidths=lw, alpha=0.98)
        return coll

    def render(self, particle: AbstractParticle, time: float, output_path: str) -> None:
        p = particle.params
        cfg = self.config

        figsize = (cfg.width / cfg.dpi, cfg.height / cfg.dpi)
        fig = plt.figure(figsize=figsize, dpi=cfg.dpi)
        ax = fig.add_subplot(111, projection="3d", computed_zorder=True)

        fig.patch.set_facecolor(cfg.background)
        ax.set_facecolor(cfg.background)

        t_vis = time * cfg.time_scale

        u, v = torus_frame()
        deform = particle.deformation(u, v, t_vis)
        x, y, z = torus_surface(u, v, p.major_radius, p.minor_radius, deformation=deform)

        # Soft shadow on ground plane for depth cue.
        z_floor = np.min(z) - 0.12 * (p.major_radius + p.minor_radius)
        ax.plot_surface(
            x,
            y,
            np.full_like(z, z_floor),
            rstride=2,
            cstride=2,
            linewidth=0,
            antialiased=False,
            color="black",
            alpha=cfg.shadow_alpha,
            shade=False,
        )

        facecolors = self._surface_facecolors(x, y, z, cfg.torus_color)
        ax.plot_surface(
            x,
            y,
            z,
            rstride=1,
            cstride=1,
            linewidth=cfg.surface_edge_linewidth,
            edgecolor=(1, 1, 1, cfg.surface_edge_alpha),
            antialiased=True,
            facecolors=facecolors,
            shade=False,
        )

        # Secondary wireframe layer for shape readability.
        ax.plot_wireframe(
            x,
            y,
            z,
            rstride=cfg.wireframe_stride,
            cstride=cfg.wireframe_stride,
            color=(1, 1, 1, cfg.wireframe_alpha),
            linewidth=cfg.wireframe_linewidth,
        )

        lu, lv = particle.resonant_loop(t_vis)
        ldef = particle.deformation(lu, lv, t_vis)
        lx, ly, lz = torus_surface(
            lu,
            lv,
            p.major_radius,
            p.minor_radius,
            deformation=ldef + cfg.loop_lift,
        )

        # Segment collections give better depth sorting than one monolithic line artist.
        # Add a soft under-stroke + core stroke for readability over mesh.
        loop_glow = self._line_collection(lx, ly, lz, cfg.loop_color, cfg.loop_linewidth * 1.8)
        loop_glow.set_alpha(0.25)
        ax.add_collection3d(loop_glow)

        loop_collection = self._line_collection(lx, ly, lz, cfg.loop_color, cfg.loop_linewidth)
        loop_collection.set_alpha(0.98)
        ax.add_collection3d(loop_collection)

        extent = p.major_radius + p.minor_radius + p.deform_amp + 0.2
        ax.set_xlim(-extent, extent)
        ax.set_ylim(-extent, extent)
        ax.set_zlim(z_floor, extent * 0.75)
        ax.set_box_aspect((1, 1, 0.6))

        ax.view_init(elev=cfg.elev, azim=cfg.azim)
        ax.set_axis_off()
        ax.set_title(f"{particle.name}: deformed torus + resonant loop", color="white", pad=14)

        plt.tight_layout(pad=0)
        fig.savefig(output_path, bbox_inches="tight", pad_inches=0)
        plt.close(fig)
