#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from pathlib import Path
from tempfile import TemporaryDirectory

import imageio.v3 as iio
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import numpy as np

from torus_cycle_renderer.math import torus_surface
from torus_cycle_renderer.particles import UQuark, UQuarkState, DQuark, DQuarkState, SpinState
from torus_cycle_renderer.rendering.scene_data import sample_scene_geometry


EDGE_GAMMAS = {
    "AB": 2.0 / 9.0,
    "BC": 2.0 / 9.0,
    "CA": 2.0 / 9.0,
}

NODE_COLORS = {
    "A": ("#4cc9f0", "#f72585"),
    "B": ("#4cc9f0", "#ff4d6d"),
    "C": ("#90be6d", "#f94144"),
}

PORT_IN_COLOR = "#ffd166"
PORT_OUT_COLOR = "#06d6a0"
BAND_COLOR = "#ffffff"
BACKGROUND = "#0e1117"


def _normalize(v: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    n = np.linalg.norm(v)
    if n < eps:
        return np.zeros_like(v)
    return v / n


def _surface_normals(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> np.ndarray:
    p = np.stack([x, y, z], axis=-1)
    du = np.roll(p, -1, axis=1) - np.roll(p, 1, axis=1)
    dv = np.roll(p, -1, axis=0) - np.roll(p, 1, axis=0)
    n = np.cross(du, dv)
    nn = np.linalg.norm(n, axis=-1, keepdims=True)
    return n / np.clip(nn, 1e-12, None)


def _surface_facecolors(x: np.ndarray, y: np.ndarray, z: np.ndarray, base_color: str, alpha: float = 0.42) -> np.ndarray:
    base = np.array(to_rgb(base_color))[None, None, :]
    normals = _surface_normals(x, y, z)

    az = np.deg2rad(35.0)
    alt = np.deg2rad(45.0)
    ldir = np.array([
        np.cos(alt) * np.cos(az),
        np.cos(alt) * np.sin(az),
        np.sin(alt),
    ])
    lambert = np.clip(np.sum(normals * ldir[None, None, :], axis=-1), 0.0, 1.0)
    intensity = np.clip(0.35 + 0.65 * lambert, 0.0, 1.0)
    rgb = np.clip(base * intensity[..., None], 0.0, 1.0)
    a = np.full((*rgb.shape[:2], 1), alpha)
    return np.concatenate([rgb, a], axis=-1)


def _rotation_z(theta: float) -> np.ndarray:
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def _transform_xyz(x: np.ndarray, y: np.ndarray, z: np.ndarray, center: np.ndarray, rot: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    pts = np.stack([x, y, z], axis=-1)
    pts = pts @ rot.T
    pts = pts + center[None, None, :] if pts.ndim == 3 else pts + center[None, :]
    return pts[..., 0], pts[..., 1], pts[..., 2]


def _bezier_curve(p0: np.ndarray, p1: np.ndarray, p2: np.ndarray, p3: np.ndarray, n: int = 140) -> np.ndarray:
    t = np.linspace(0.0, 1.0, n)
    omt = 1.0 - t
    return (
        (omt**3)[:, None] * p0[None, :]
        + 3.0 * (omt**2 * t)[:, None] * p1[None, :]
        + 3.0 * (omt * t**2)[:, None] * p2[None, :]
        + (t**3)[:, None] * p3[None, :]
    )


class TriangleNode:
    def __init__(self, label: str, particle, center: np.ndarray, rot_angle: float):
        self.label = label
        self.particle = particle
        self.center = center
        self.rot = _rotation_z(rot_angle)


def build_nodes() -> list[TriangleNode]:
    radius = 5.2
    angles = {
        "A": math.pi / 2.0,
        "B": math.pi / 2.0 + 2.0 * math.pi / 3.0,
        "C": math.pi / 2.0 + 4.0 * math.pi / 3.0,
    }
    centers = {
        k: np.array([radius * math.cos(a), radius * math.sin(a), 0.0])
        for k, a in angles.items()
    }

    # Distinct color-phase branches across the triangle.
    qa = UQuark(UQuarkState(spin_state=SpinState.PP, color_phase=0.0))
    qb = UQuark(UQuarkState(spin_state=SpinState.PP, color_phase=2.0 * math.pi / 3.0))
    qc = DQuark(DQuarkState(spin_state=SpinState.PP, color_phase=4.0 * math.pi / 3.0))

    nodes = []
    for label, particle in [("A", qa), ("B", qb), ("C", qc)]:
        c = centers[label]
        outward = _normalize(c)
        rot_angle = math.atan2(outward[1], outward[0])
        nodes.append(TriangleNode(label, particle, c, rot_angle))
    return nodes


def _port_angles_for_node(node: TriangleNode, centers: dict[str, np.ndarray], order: list[str]) -> tuple[float, float]:
    idx = order.index(node.label)
    prev_label = order[(idx - 1) % len(order)]
    next_label = order[(idx + 1) % len(order)]
    c = centers[node.label]
    v_prev = centers[prev_label] - c
    v_next = centers[next_label] - c
    # Local u angles are defined before rigid rotation; undo the node rotation.
    rot_inv = node.rot.T
    lp = rot_inv @ _normalize(v_prev)
    ln = rot_inv @ _normalize(v_next)
    u_in = math.atan2(lp[1], lp[0])
    u_out = math.atan2(ln[1], ln[0])
    return u_in, u_out


def _port_point(node: TriangleNode, t: float, u_angle: float, v_angle: float = 0.0, outward_lift: float = 0.10) -> np.ndarray:
    p = node.particle.params
    u = np.array([[u_angle]])
    v = np.array([[v_angle]])
    deform = node.particle.deformation(u, v, t)
    x, y, z = torus_surface(u, v, p.major_radius, p.minor_radius, deformation=deform)
    pt = np.array([float(x[0, 0]), float(y[0, 0]), float(z[0, 0])])
    pt = node.rot @ pt + node.center

    radial = _normalize(np.array([pt[0] - node.center[0], pt[1] - node.center[1], 0.0]))
    return pt + outward_lift * radial


def render_triangle_frame(time: float, output: Path, width: int, height: int, dpi: int) -> None:
    nodes = build_nodes()
    centers = {n.label: n.center for n in nodes}
    order = ["A", "B", "C"]

    fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    ax = fig.add_subplot(111, projection="3d", computed_zorder=True)
    fig.patch.set_facecolor(BACKGROUND)
    ax.set_facecolor(BACKGROUND)

    global_min = np.array([np.inf, np.inf, np.inf])
    global_max = np.array([-np.inf, -np.inf, -np.inf])

    port_points: dict[str, dict[str, np.ndarray]] = {}

    # Draw torus nodes.
    for node in nodes:
        torus_color, loop_color = NODE_COLORS[node.label]
        scene = sample_scene_geometry(node.particle, time, time_scale=1.0, loop_points=800, loop_lift_override=0.06)

        x, y, z = _transform_xyz(scene.x, scene.y, scene.z, node.center, node.rot)
        lx, ly, lz = _transform_xyz(scene.lx, scene.ly, scene.lz, node.center, node.rot)
        global_min = np.minimum(global_min, np.array([x.min(), y.min(), z.min()]))
        global_max = np.maximum(global_max, np.array([x.max(), y.max(), z.max()]))

        facecolors = _surface_facecolors(x, y, z, torus_color, alpha=0.44)
        ax.plot_surface(
            x,
            y,
            z,
            rstride=1,
            cstride=1,
            linewidth=0.08,
            edgecolor=(1, 1, 1, 0.20),
            antialiased=True,
            facecolors=facecolors,
            shade=False,
            zorder=1,
        )
        ax.plot_wireframe(
            x,
            y,
            z,
            rstride=6,
            cstride=6,
            color=(1, 1, 1, 0.16),
            linewidth=0.30,
            zorder=2,
        )
        ax.plot(lx, ly, lz, color=loop_color, linewidth=2.2, alpha=0.95, zorder=4)

        ax.text(
            node.center[0],
            node.center[1],
            node.center[2] + node.particle.params.major_radius + 1.0,
            f"{node.label}: {node.particle.name.split('[')[0]}",
            color="white",
            fontsize=10,
            ha="center",
            va="bottom",
            zorder=10,
        )

        u_in, u_out = _port_angles_for_node(node, centers, order)
        p_in = _port_point(node, time, u_in)
        p_out = _port_point(node, time, u_out)
        port_points[node.label] = {"in": p_in, "out": p_out}

        ax.scatter(*p_in, color=PORT_IN_COLOR, s=34, depthshade=False, zorder=8)
        ax.scatter(*p_out, color=PORT_OUT_COLOR, s=34, depthshade=False, zorder=8)

    # Draw cyclic edge bands with integrated-out gluon phase labels.
    edges = [("A", "B", "AB"), ("B", "C", "BC"), ("C", "A", "CA")]
    for src, dst, edge_key in edges:
        p0 = port_points[src]["out"]
        p3 = port_points[dst]["in"]
        edge_vec = p3 - p0
        edge_dir = _normalize(edge_vec)
        mid = 0.5 * (p0 + p3)
        lift = np.array([0.0, 0.0, 1.35])
        p1 = p0 + 0.42 * np.linalg.norm(edge_vec) * edge_dir + lift
        p2 = p3 - 0.42 * np.linalg.norm(edge_vec) * edge_dir + lift
        curve = _bezier_curve(p0, p1, p2, p3, n=180)

        ax.plot(curve[:, 0], curve[:, 1], curve[:, 2], color=BAND_COLOR, linewidth=2.9, alpha=0.88, zorder=6)
        ax.plot(curve[:, 0], curve[:, 1], curve[:, 2], color="#7bdff2", linewidth=5.5, alpha=0.12, zorder=5)

        mid_idx = len(curve) // 2
        mp = curve[mid_idx]
        ax.text(
            mp[0], mp[1], mp[2] + 0.22,
            f"γ{edge_key}={EDGE_GAMMAS[edge_key]:.3f}",
            color="#c9d1d9",
            fontsize=8,
            ha="center",
            va="bottom",
            zorder=10,
        )

    # Overlay theory summary.
    text = (
        "uud triangle · quark-only render\n"
        "explicit gluons integrated out into edge phase lags\n"
        "δ = (1/3, 1/3, 2/3),  γ = (2/9, 2/9, 2/9),  net node injection = 0"
    )
    ax.text2D(
        0.02,
        0.965,
        text,
        transform=ax.transAxes,
        color="white",
        fontsize=9,
        va="top",
        ha="left",
        bbox=dict(boxstyle="round,pad=0.40", facecolor=(0, 0, 0, 0.45), edgecolor=(1, 1, 1, 0.18)),
    )

    extent = max(np.max(np.abs(global_min[:2])), np.max(np.abs(global_max[:2]))) + 2.0
    ax.set_xlim(-extent, extent)
    ax.set_ylim(-extent, extent)
    ax.set_zlim(global_min[2] - 1.2, global_max[2] + 2.8)
    ax.set_box_aspect((1.0, 1.0, 0.58))
    ax.view_init(elev=24.0, azim=34.0)
    ax.set_axis_off()

    output.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout(pad=0)
    fig.savefig(output, bbox_inches="tight", pad_inches=0)
    plt.close(fig)


def build_cycle(output: Path, duration: float, fps: int, width: int, height: int, dpi: int) -> None:
    frames = max(2, int(round(duration * fps)))
    with TemporaryDirectory() as td:
        td_path = Path(td)
        imgs = []
        for i in range(frames):
            t = duration * i / frames
            fp = td_path / f"frame_{i:04d}.png"
            render_triangle_frame(t=t, output=fp, width=width, height=height, dpi=dpi)
            imgs.append(iio.imread(fp))
        iio.imwrite(output, imgs, duration=1000 / fps, loop=0)


def main() -> None:
    ap = argparse.ArgumentParser(description="Render a proton-like uud triangle with integrated-out edge coupling")
    ap.add_argument("--mode", choices=["frame", "cycle"], default="frame")
    ap.add_argument("--time", type=float, default=0.42)
    ap.add_argument("--duration", type=float, default=1.8)
    ap.add_argument("--fps", type=int, default=12)
    ap.add_argument("--width", type=int, default=1400)
    ap.add_argument("--height", type=int, default=980)
    ap.add_argument("--dpi", type=int, default=110)
    ap.add_argument("--output", default="output/uud_triangle.png")
    args = ap.parse_args()

    output = Path(args.output)
    if args.mode == "frame":
        render_triangle_frame(args.time, output, args.width, args.height, args.dpi)
        print(f"Rendered uud triangle frame: {output}")
        return

    build_cycle(output, args.duration, args.fps, args.width, args.height, args.dpi)
    print(f"Rendered uud triangle cycle: {output}")


if __name__ == "__main__":
    main()
