from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import numpy as np
import plotly.graph_objects as go
from matplotlib.colors import to_rgb

from torus_cycle_renderer.math import torus_surface, torus_frame
from torus_cycle_renderer.particles import AbstractParticle
from .geometry_export import export_scene_npz, export_torus_obj, export_loop_obj


@dataclass(frozen=True)
class PlotlyRenderConfig:
    width: int = 1280
    height: int = 720
    background: str = "#0e1117"
    loop_lift: float = 0.04
    mesh_opacity: float = 0.1
    gridline_stride_u: int = 5
    gridline_stride_v: int = 4
    gridline_width: float = 0.6
    gridline_alpha: float = 0.035


class PlotlyTorusRenderer:
    def __init__(self, config: PlotlyRenderConfig | None = None):
        self.config = config or PlotlyRenderConfig()

    def _triangulate_grid(self, nv: int, nu: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        ii, jj, kk = [], [], []

        def vid(i: int, j: int) -> int:
            return i * nu + j

        for i in range(nv):
            i2 = (i + 1) % nv
            for j in range(nu):
                j2 = (j + 1) % nu
                a = vid(i, j)
                b = vid(i, j2)
                c = vid(i2, j2)
                d = vid(i2, j)
                ii.extend([a, a])
                jj.extend([b, c])
                kk.extend([c, d])

        return np.asarray(ii), np.asarray(jj), np.asarray(kk)

    def _gridline_highlight_rgba(self, base_color: str, alpha: float) -> str:
        _ = to_rgb(base_color)  # keep signature compatible; explicit blue requested.
        # Blue-toned gridlines with high transparency.
        return f"rgba(95, 145, 235, {alpha:.3f})"

    def render(self, particle: AbstractParticle, time: float, output_path: str, export_geometry: bool = False) -> None:
        p = particle.params
        cfg = self.config

        u, v = torus_frame()
        deform = particle.deformation(u, v, time)
        x, y, z = torus_surface(u, v, p.major_radius, p.minor_radius, deformation=deform)

        lu, lv = particle.resonant_loop(time)
        ldef = particle.deformation(lu, lv, time)
        lx, ly, lz = torus_surface(lu, lv, p.major_radius, p.minor_radius, deformation=ldef + cfg.loop_lift)

        nv, nu = x.shape
        i, j, k = self._triangulate_grid(nv, nu)

        mesh = go.Mesh3d(
            x=x.ravel(),
            y=y.ravel(),
            z=z.ravel(),
            i=i,
            j=j,
            k=k,
            color=p.color,
            opacity=cfg.mesh_opacity,
            flatshading=False,
            lighting=dict(ambient=0.4, diffuse=0.7, specular=0.25, roughness=0.6, fresnel=0.1),
            lightposition=dict(x=120, y=200, z=180),
            name="torus",
        )

        loop = go.Scatter3d(
            x=lx,
            y=ly,
            z=lz,
            mode="lines",
            line=dict(color=p.loop_color, width=7),
            name="loop",
        )

        grid_traces: list[go.Scatter3d] = []
        gridline_color = self._gridline_highlight_rgba(p.color, cfg.gridline_alpha)

        # u-lines (vary v index, sweep u)
        for iv in range(0, nv, max(cfg.gridline_stride_v, 1)):
            grid_traces.append(
                go.Scatter3d(
                    x=x[iv, :],
                    y=y[iv, :],
                    z=z[iv, :],
                    mode="lines",
                    line=dict(color=gridline_color, width=cfg.gridline_width),
                    hoverinfo="skip",
                    showlegend=False,
                )
            )

        # v-lines (vary u index, sweep v)
        for iu in range(0, nu, max(cfg.gridline_stride_u, 1)):
            grid_traces.append(
                go.Scatter3d(
                    x=x[:, iu],
                    y=y[:, iu],
                    z=z[:, iu],
                    mode="lines",
                    line=dict(color=gridline_color, width=cfg.gridline_width),
                    hoverinfo="skip",
                    showlegend=False,
                )
            )

        fig = go.Figure(data=[mesh, *grid_traces, loop])
        fig.update_layout(
            width=cfg.width,
            height=cfg.height,
            margin=dict(l=0, r=0, t=40, b=0),
            title=f"{particle.name}: deformed torus + resonant loop",
            scene=dict(
                bgcolor=cfg.background,
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                aspectmode="data",
                camera=dict(eye=dict(x=1.45, y=1.3, z=0.8)),
            ),
            paper_bgcolor=cfg.background,
        )

        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        if out.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            # Requires kaleido for static image export.
            fig.write_image(str(out))
        else:
            fig.write_html(str(out), include_plotlyjs="cdn")

        if export_geometry:
            stem = out.with_suffix("")
            export_scene_npz(str(stem) + "_geom.npz", x, y, z, lx, ly, lz)
            export_torus_obj(str(stem) + "_torus.obj", x, y, z)
            export_loop_obj(str(stem) + "_loop.obj", lx, ly, lz)
