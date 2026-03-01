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
    face_alpha: float = 0.44
    surface_edge_linewidth: float = 0.10
    surface_edge_alpha: float = 0.30
    wireframe_linewidth: float = 0.36
    wireframe_alpha: float = 0.28
    wireframe_stride: int = 5

    # Loop
    loop_linewidth: float = 2.6
    loop_lift: float = 0.04
    loop_back_alpha: float = 0.18
    loop_front_alpha: float = 0.98

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

    def _split_loop_by_camera_hemisphere(
        self,
        lx: np.ndarray,
        ly: np.ndarray,
        lz: np.ndarray,
        center: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray]:
        """Approximate front/back segmentation against camera direction.

        This is a robust practical fix for Matplotlib's painterly 3D ordering:
        back hemisphere segments are drawn before the torus, front segments after.
        """
        cfg = self.config
        az = np.deg2rad(cfg.azim)
        el = np.deg2rad(cfg.elev)
        view_dir = np.array([
            np.cos(el) * np.cos(az),
            np.cos(el) * np.sin(az),
            np.sin(el),
        ])

        pts = np.column_stack([lx, ly, lz])
        mids = 0.5 * (pts[:-1] + pts[1:])
        rel = mids - center[None, :]
        front_mask = (rel @ view_dir) >= 0.0
        return front_mask, ~front_mask

    def render(self, particle: AbstractParticle, time: float, output_path: str) -> None:
        p = particle.params
        cfg = self.config

        figsize = (cfg.width / cfg.dpi, cfg.height / cfg.dpi)
        fig = plt.figure(figsize=figsize, dpi=cfg.dpi)
        ax = fig.add_subplot(111, projection="3d", computed_zorder=True)

        fig.patch.set_facecolor(cfg.background)
        ax.set_facecolor(cfg.background)

        u, v = torus_frame()
        deform = particle.deformation(u, v, time)
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

        lu, lv = particle.resonant_loop(time)
        ldef = particle.deformation(lu, lv, time)
        lx, ly, lz = torus_surface(
            lu,
            lv,
            p.major_radius,
            p.minor_radius,
            deformation=ldef + cfg.loop_lift,
        )

        center = np.array([np.mean(x), np.mean(y), np.mean(z)])
        front_mask, back_mask = self._split_loop_by_camera_hemisphere(lx, ly, lz, center)

        # Draw back loop segments first (so torus naturally occludes them).
        pts = np.column_stack([lx, ly, lz])
        segs = np.stack([pts[:-1], pts[1:]], axis=1)
        if np.any(back_mask):
            back_coll = Line3DCollection(
                segs[back_mask],
                colors=p.loop_color,
                linewidths=cfg.loop_linewidth * 0.95,
                alpha=cfg.loop_back_alpha,
            )
            ax.add_collection3d(back_coll)

        facecolors = self._surface_facecolors(x, y, z, p.color)
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

        # Draw front loop segments after torus.
        if np.any(front_mask):
            front_glow = Line3DCollection(
                segs[front_mask],
                colors=p.loop_color,
                linewidths=cfg.loop_linewidth * 1.8,
                alpha=0.20,
            )
            ax.add_collection3d(front_glow)

            front_coll = Line3DCollection(
                segs[front_mask],
                colors=p.loop_color,
                linewidths=cfg.loop_linewidth,
                alpha=cfg.loop_front_alpha,
            )
            ax.add_collection3d(front_coll)

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
