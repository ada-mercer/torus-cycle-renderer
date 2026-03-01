from __future__ import annotations

import argparse
from pathlib import Path
from tempfile import TemporaryDirectory

import imageio.v3 as iio

from torus_cycle_renderer.rendering import (
    TorusRenderer,
    RenderConfig,
    PlotlyTorusRenderer,
    PlotlyRenderConfig,
    CycleAnimator,
    AnimationConfig,
)
from torus_cycle_renderer.scenes import build_scene
from torus_cycle_renderer.math import torus_surface, torus_frame
from torus_cycle_renderer.rendering.geometry_export import (
    export_scene_npz,
    export_torus_obj,
    export_loop_obj,
)


def render_frame_main() -> None:
    parser = argparse.ArgumentParser(description="Render one torus-cycle frame")
    parser.add_argument("--particle", default="electron", choices=["electron", "photon"])
    parser.add_argument("--time", type=float, default=0.0)
    parser.add_argument("--spin-state", default="++", choices=["++", "+-", "-+", "--"])
    parser.add_argument("--loop-anchor-mode", default="evolving", choices=["evolving", "static"])
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--backend", default="matplotlib", choices=["matplotlib", "plotly"])
    parser.add_argument("--torus-color", default="#3a86ff")
    parser.add_argument("--loop-color", default="#ff006e")
    parser.add_argument("--time-scale", type=float, default=1.0)
    parser.add_argument("--export-geometry", action="store_true")
    parser.add_argument("--output", default="output/frame.png")
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    particle = build_scene(args.particle, spin_state=args.spin_state, loop_anchor_mode=args.loop_anchor_mode)

    if args.backend == "matplotlib":
        renderer = TorusRenderer(
            RenderConfig(
                width=args.width,
                height=args.height,
                dpi=args.dpi,
                torus_color=args.torus_color,
                loop_color=args.loop_color,
                time_scale=args.time_scale,
            )
        )
        renderer.render(particle=particle, time=args.time, output_path=args.output)

        if args.export_geometry:
            p = particle.params
            t_vis = args.time * args.time_scale
            u, v = torus_frame()
            deform = particle.deformation(u, v, t_vis)
            x, y, z = torus_surface(u, v, p.major_radius, p.minor_radius, deformation=deform)
            lu, lv = particle.resonant_loop(t_vis)
            ldef = particle.deformation(lu, lv, t_vis)
            lx, ly, lz = torus_surface(lu, lv, p.major_radius, p.minor_radius, deformation=ldef + 0.04)
            stem = Path(args.output).with_suffix("")
            export_scene_npz(str(stem) + "_geom.npz", x, y, z, lx, ly, lz)
            export_torus_obj(str(stem) + "_torus.obj", x, y, z)
            export_loop_obj(str(stem) + "_loop.obj", lx, ly, lz)
    else:
        renderer = PlotlyTorusRenderer(
            PlotlyRenderConfig(
                width=args.width,
                height=args.height,
                torus_color=args.torus_color,
                loop_color=args.loop_color,
                time_scale=args.time_scale,
            )
        )
        renderer.render(particle=particle, time=args.time, output_path=args.output, export_geometry=args.export_geometry)

    print(f"Rendered ({args.backend}): {args.output}")


def _frame_times(frames: int, cycle_time: float) -> list[float]:
    if frames < 2:
        return [0.0]
    step = cycle_time / frames
    return [k * step for k in range(frames)]


def render_cycle_main() -> None:
    parser = argparse.ArgumentParser(description="Render a full torus-cycle animation")
    parser.add_argument("--backend", default="matplotlib", choices=["matplotlib", "plotly"])
    parser.add_argument("--particle", default="electron", choices=["electron", "photon"])
    parser.add_argument("--spin-state", default="++", choices=["++", "+-", "-+", "--"])
    parser.add_argument("--loop-anchor-mode", default="evolving", choices=["evolving", "static"])
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--torus-color", default="#3a86ff")
    parser.add_argument("--loop-color", default="#ff006e")
    parser.add_argument("--time-scale", type=float, default=1.0)
    parser.add_argument("--frames", type=int, default=None)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--duration", type=float, default=4.0)
    parser.add_argument("--cycle-time", type=float, default=None)
    parser.add_argument("--format", default="gif", choices=["gif", "mp4"])
    parser.add_argument("--output", default="output/cycle.gif")
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    particle = build_scene(args.particle, spin_state=args.spin_state, loop_anchor_mode=args.loop_anchor_mode)

    frames = args.frames if args.frames is not None else max(2, int(round(args.duration * args.fps)))
    base_cycle_time = float(particle.cycle_time())
    cycle_time = args.cycle_time if args.cycle_time is not None else (base_cycle_time / max(args.time_scale, 1e-9))

    if args.backend == "matplotlib":
        render_cfg = RenderConfig(
            width=args.width,
            height=args.height,
            dpi=args.dpi,
            torus_color=args.torus_color,
            loop_color=args.loop_color,
            time_scale=args.time_scale,
        )
        anim_cfg = AnimationConfig(frames=frames, cycle_time=cycle_time, fps=args.fps, format=args.format)
        CycleAnimator(render=render_cfg, animation=anim_cfg).build(particle=particle, output_path=args.output)
    else:
        pr = PlotlyTorusRenderer(
            PlotlyRenderConfig(
                width=args.width,
                height=args.height,
                torus_color=args.torus_color,
                loop_color=args.loop_color,
                time_scale=args.time_scale,
            )
        )
        times = _frame_times(frames, cycle_time)
        with TemporaryDirectory() as td:
            tmp = Path(td)
            frame_paths = []
            for idx, t in enumerate(times):
                fp = tmp / f"plotly_{idx:04d}.png"
                pr.render(particle=particle, time=t, output_path=str(fp), export_geometry=False)
                frame_paths.append(fp)
            imgs = [iio.imread(fp) for fp in frame_paths]
            if args.format == "gif":
                iio.imwrite(args.output, imgs, duration=int(1000 / max(args.fps, 1)), loop=0)
            else:
                iio.imwrite(args.output, imgs, fps=args.fps)

    print(f"Rendered cycle ({args.backend}): {args.output}")
