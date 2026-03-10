from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import numpy as np
import plotly.graph_objects as go
from matplotlib.colors import to_rgb

from torus_cycle_renderer.particles import AbstractParticle
from .geometry_export import export_scene_npz, export_torus_obj, export_loop_obj
from .scene_data import sample_scene_geometry


@dataclass(frozen=True)
class PlotlyRenderConfig:
    width: int = 1280
    height: int = 720
    background: str = "#0e1117"
    elev: float = 22.0
    azim: float = 36.0
    camera_radius: float = 2.1
    loop_lift: float = 0.04
    mesh_opacity: float = 0.45
    gridline_stride_u: int = 5
    gridline_stride_v: int = 4
    gridline_width: float = 0.6
    gridline_alpha: float = 0.10
    loop_points: int = 900

    # Visual styling (renderer-owned)
    torus_color: str = "#3a86ff"
    loop_color: str = "#ff006e"
    time_scale: float = 1.0


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

    def _camera_eye(self) -> dict[str, float]:
        cfg = self.config
        az = np.deg2rad(cfg.azim)
        alt = np.deg2rad(cfg.elev)
        r = cfg.camera_radius
        return dict(
            x=float(r * np.cos(alt) * np.cos(az)),
            y=float(r * np.cos(alt) * np.sin(az)),
            z=float(r * np.sin(alt)),
        )

    def render(self, particle: AbstractParticle, time: float, output_path: str, export_geometry: bool = False) -> None:
        cfg = self.config
        scene = sample_scene_geometry(
            particle,
            time,
            time_scale=cfg.time_scale,
            loop_points=cfg.loop_points,
            loop_lift_override=cfg.loop_lift,
        )

        nv, nu = scene.x.shape
        i, j, k = self._triangulate_grid(nv, nu)

        mesh = go.Mesh3d(
            x=scene.x.ravel(),
            y=scene.y.ravel(),
            z=scene.z.ravel(),
            i=i,
            j=j,
            k=k,
            color=cfg.torus_color,
            opacity=cfg.mesh_opacity,
            flatshading=False,
            lighting=dict(ambient=0.4, diffuse=0.7, specular=0.25, roughness=0.6, fresnel=0.1),
            lightposition=dict(x=120, y=200, z=180),
            name="torus",
        )

        loop = go.Scatter3d(
            x=scene.lx,
            y=scene.ly,
            z=scene.lz,
            mode="lines",
            line=dict(color=cfg.loop_color, width=7),
            name="loop",
        )

        grid_traces: list[go.Scatter3d] = []
        gridline_color = self._gridline_highlight_rgba(cfg.torus_color, cfg.gridline_alpha)

        # u-lines (vary v index, sweep u)
        for iv in range(0, nv, max(cfg.gridline_stride_v, 1)):
            grid_traces.append(
                go.Scatter3d(
                    x=scene.x[iv, :],
                    y=scene.y[iv, :],
                    z=scene.z[iv, :],
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
                    x=scene.x[:, iu],
                    y=scene.y[:, iu],
                    z=scene.z[:, iu],
                    mode="lines",
                    line=dict(color=gridline_color, width=cfg.gridline_width),
                    hoverinfo="skip",
                    showlegend=False,
                )
            )

        legend_text = f"channels: p={scene.p_value:.3f}, p_f={scene.pf_value:.3f}, p/p_f={scene.ratio_label}"

        fig = go.Figure(data=[mesh, *grid_traces, loop])
        fig.update_layout(
            width=cfg.width,
            height=cfg.height,
            margin=dict(l=0, r=0, t=40, b=0),
            title=f"{scene.particle_name}: deformed torus + resonant loop",
            scene=dict(
                bgcolor=cfg.background,
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                aspectmode="data",
                camera=dict(eye=self._camera_eye()),
            ),
            paper_bgcolor=cfg.background,
            annotations=[
                dict(
                    x=0.015,
                    y=0.98,
                    xref="paper",
                    yref="paper",
                    text=legend_text,
                    showarrow=False,
                    font=dict(color="white", size=12),
                    bgcolor="rgba(0,0,0,0.45)",
                    bordercolor="rgba(255,255,255,0.22)",
                    borderwidth=1,
                    borderpad=4,
                    align="left",
                ),
                dict(
                    x=0.015,
                    y=0.935,
                    xref="paper",
                    yref="paper",
                    text=scene.particle_subtitle,
                    showarrow=False,
                    font=dict(color="#c9d1d9", size=11),
                    bgcolor="rgba(0,0,0,0.0)",
                    borderwidth=0,
                    align="left",
                ),
            ],
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
            export_scene_npz(str(stem) + "_geom.npz", scene.x, scene.y, scene.z, scene.lx, scene.ly, scene.lz)
            export_torus_obj(str(stem) + "_torus.obj", scene.x, scene.y, scene.z)
            export_loop_obj(str(stem) + "_loop.obj", scene.lx, scene.ly, scene.lz)
