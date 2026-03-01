from __future__ import annotations

from dataclasses import dataclass
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
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
    face_alpha: float = 0.42
    surface_edge_linewidth: float = 0.0
    loop_linewidth: float = 2.2
    loop_lift: float = 0.03
    background: str = "#0e1117"


class TorusRenderer:
    def __init__(self, config: RenderConfig | None = None):
        self.config = config or RenderConfig()

    def render(self, particle: AbstractParticle, time: float, output_path: str) -> None:
        p = particle.params
        cfg = self.config

        figsize = (cfg.width / cfg.dpi, cfg.height / cfg.dpi)
        fig = plt.figure(figsize=figsize, dpi=cfg.dpi)
        ax = fig.add_subplot(111, projection="3d")

        fig.patch.set_facecolor(cfg.background)
        ax.set_facecolor(cfg.background)

        u, v = torus_frame()
        deform = particle.deformation(u, v, time)
        x, y, z = torus_surface(u, v, p.major_radius, p.minor_radius, deformation=deform)

        ax.plot_surface(
            x,
            y,
            z,
            rstride=1,
            cstride=1,
            linewidth=cfg.surface_edge_linewidth,
            edgecolor=(1, 1, 1, 0.12),
            antialiased=True,
            alpha=cfg.face_alpha,
            color=p.color,
            shade=False,
        )

        lu, lv = particle.resonant_loop(time)
        ldef = particle.deformation(lu, lv, time)
        # Slight outward lift keeps loop visible through transparency while staying surface-locked.
        lx, ly, lz = torus_surface(
            lu,
            lv,
            p.major_radius,
            p.minor_radius,
            deformation=ldef + cfg.loop_lift,
        )
        ax.plot(lx, ly, lz, color=p.loop_color, linewidth=cfg.loop_linewidth, alpha=0.98)

        extent = p.major_radius + p.minor_radius + p.deform_amp + 0.2
        ax.set_xlim(-extent, extent)
        ax.set_ylim(-extent, extent)
        ax.set_zlim(-extent * 0.75, extent * 0.75)
        ax.set_box_aspect((1, 1, 0.6))

        ax.view_init(elev=cfg.elev, azim=cfg.azim)
        ax.set_axis_off()
        ax.set_title(f"{particle.name}: deformed torus + resonant loop", color="white", pad=14)

        plt.tight_layout(pad=0)
        fig.savefig(output_path, bbox_inches="tight", pad_inches=0)
        plt.close(fig)
