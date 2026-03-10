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
    PyVistaTorusRenderer,
    PyVistaRenderConfig,
    CycleAnimator,
    AnimationConfig,
    frame_times,
    sample_scene_geometry,
)
from torus_cycle_renderer.scenes import build_scene
from torus_cycle_renderer.rendering.geometry_export import export_scene_npz, export_torus_obj, export_loop_obj


def render_frame_main() -> None:
    parser = argparse.ArgumentParser(description="Render one torus-cycle frame")
    parser.add_argument("--particle", default="electron", choices=["electron", "photon", "wplus", "w+", "wminus", "w-", "zboson", "z0", "z", "uquark", "u", "dquark", "d", "gluon", "g"])
    parser.add_argument("--time", type=float, default=0.0)
    parser.add_argument("--spin-state", default="++", choices=["++", "+-", "-+", "--"])
    parser.add_argument("--loop-anchor-mode", default="evolving", choices=["evolving", "static"])
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--elev", type=float, default=22.0)
    parser.add_argument("--azim", type=float, default=36.0)
    parser.add_argument("--camera-radius", type=float, default=2.1)
    parser.add_argument("--backend", default="matplotlib", choices=["matplotlib", "plotly", "pyvista"])
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
                elev=args.elev,
                azim=args.azim,
                torus_color=args.torus_color,
                loop_color=args.loop_color,
                time_scale=args.time_scale,
            )
        )
        renderer.render(particle=particle, time=args.time, output_path=args.output)

        if args.export_geometry:
            _export_geometry(args.output, particle, args.time, time_scale=args.time_scale, loop_lift=renderer.config.loop_lift)
    elif args.backend == "plotly":
        renderer = PlotlyTorusRenderer(
            PlotlyRenderConfig(
                width=args.width,
                height=args.height,
                elev=args.elev,
                azim=args.azim,
                torus_color=args.torus_color,
                loop_color=args.loop_color,
                time_scale=args.time_scale,
            )
        )
        renderer.render(particle=particle, time=args.time, output_path=args.output, export_geometry=args.export_geometry)
    else:
        renderer = PyVistaTorusRenderer(
            PyVistaRenderConfig(
                width=args.width,
                height=args.height,
                elev=args.elev,
                azim=args.azim,
                camera_radius=args.camera_radius,
                torus_color=args.torus_color,
                loop_color=args.loop_color,
                time_scale=args.time_scale,
            )
        )
        renderer.render(particle=particle, time=args.time, output_path=args.output, export_geometry=args.export_geometry)

    print(f"Rendered ({args.backend}): {args.output}")


def _export_geometry(output_path: str, particle, time: float, *, time_scale: float, loop_lift: float | None = None) -> None:
    scene = sample_scene_geometry(
        particle,
        time,
        time_scale=time_scale,
        loop_lift_override=loop_lift,
    )
    stem = Path(output_path).with_suffix("")
    export_scene_npz(str(stem) + "_geom.npz", scene.x, scene.y, scene.z, scene.lx, scene.ly, scene.lz)
    export_torus_obj(str(stem) + "_torus.obj", scene.x, scene.y, scene.z)
    export_loop_obj(str(stem) + "_loop.obj", scene.lx, scene.ly, scene.lz)


def render_cycle_main() -> None:
    parser = argparse.ArgumentParser(description="Render a full torus-cycle animation")
    parser.add_argument("--backend", default="matplotlib", choices=["matplotlib", "plotly", "pyvista"])
    parser.add_argument("--particle", default="electron", choices=["electron", "photon", "wplus", "w+", "wminus", "w-", "zboson", "z0", "z", "uquark", "u", "dquark", "d", "gluon", "g"])
    parser.add_argument("--spin-state", default="++", choices=["++", "+-", "-+", "--"])
    parser.add_argument("--loop-anchor-mode", default="evolving", choices=["evolving", "static"])
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--elev", type=float, default=22.0)
    parser.add_argument("--azim", type=float, default=36.0)
    parser.add_argument("--camera-radius", type=float, default=2.1)
    parser.add_argument("--torus-color", default="#3a86ff")
    parser.add_argument("--loop-color", default="#ff006e")
    parser.add_argument("--time-scale", type=float, default=1.0)
    parser.add_argument("--frames", type=int, default=None)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--duration", type=float, default=4.0)
    parser.add_argument("--cycles", type=float, default=None, help="Render an integer/fractional number of full particle cycles")
    parser.add_argument("--cycle-time", type=float, default=None)
    parser.add_argument("--full-loop-cycle", action="store_true", help="Use particle.loop_cycle_time() for full loop-state return")
    parser.add_argument("--frame-workers", type=int, default=1, help="Parallel workers for frame rendering")
    parser.add_argument("--format", default="gif", choices=["gif", "mp4"])
    parser.add_argument("--output", default="output/cycle.gif")
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    particle = build_scene(args.particle, spin_state=args.spin_state, loop_anchor_mode=args.loop_anchor_mode)

    base_cycle_time = float(particle.loop_cycle_time() if args.full_loop_cycle else particle.cycle_time())
    cycle_time = args.cycle_time if args.cycle_time is not None else (base_cycle_time / max(args.time_scale, 1e-9))

    effective_duration = args.duration
    if args.cycles is not None:
        effective_duration = float(args.cycles) * float(cycle_time)

    frames = args.frames if args.frames is not None else max(2, int(round(effective_duration * args.fps)))
    # Ensure exact cycle closure when --cycles is provided.
    if args.cycles is not None:
        cycle_time = effective_duration

    if args.backend == "matplotlib":
        render_cfg = RenderConfig(
            width=args.width,
            height=args.height,
            dpi=args.dpi,
            elev=args.elev,
            azim=args.azim,
            torus_color=args.torus_color,
            loop_color=args.loop_color,
            time_scale=args.time_scale,
        )
        anim_cfg = AnimationConfig(
            frames=frames,
            cycle_time=cycle_time,
            fps=args.fps,
            format=args.format,
            frame_workers=max(1, int(args.frame_workers)),
        )
        CycleAnimator(render=render_cfg, animation=anim_cfg).build(particle=particle, output_path=args.output)
    else:
        if args.backend == "plotly":
            image_renderer = PlotlyTorusRenderer(
                PlotlyRenderConfig(
                    width=args.width,
                    height=args.height,
                    elev=args.elev,
                    azim=args.azim,
                    torus_color=args.torus_color,
                    loop_color=args.loop_color,
                    time_scale=args.time_scale,
                )
            )
            frame_prefix = "plotly"
        else:
            image_renderer = PyVistaTorusRenderer(
                PyVistaRenderConfig(
                    width=args.width,
                    height=args.height,
                    elev=args.elev,
                    azim=args.azim,
                    camera_radius=args.camera_radius,
                    torus_color=args.torus_color,
                    loop_color=args.loop_color,
                    time_scale=args.time_scale,
                )
            )
            frame_prefix = "pyvista"

        times = frame_times(frames, cycle_time)
        with TemporaryDirectory() as td:
            tmp = Path(td)
            frame_paths = []
            for idx, t in enumerate(times):
                fp = tmp / f"{frame_prefix}_{idx:04d}.png"
                image_renderer.render(particle=particle, time=t, output_path=str(fp), export_geometry=False)
                frame_paths.append(fp)
            imgs = [iio.imread(fp) for fp in frame_paths]
            if args.format == "gif":
                iio.imwrite(args.output, imgs, duration=int(1000 / max(args.fps, 1)), loop=0)
            else:
                iio.imwrite(args.output, imgs, fps=args.fps)

    print(f"Rendered cycle ({args.backend}): {args.output}")
