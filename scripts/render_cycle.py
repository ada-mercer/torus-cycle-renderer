#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from tempfile import TemporaryDirectory

import imageio.v3 as iio

from torus_cycle_renderer.rendering import (
    TorusRenderer,
    RenderConfig,
    CycleAnimator,
    AnimationConfig,
    PlotlyTorusRenderer,
    PlotlyRenderConfig,
)
from torus_cycle_renderer.scenes import build_scene


def _frame_times(frames: int, cycle_time: float) -> list[float]:
    if frames < 2:
        return [0.0]
    step = cycle_time / frames
    return [k * step for k in range(frames)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a full torus-cycle animation")
    parser.add_argument("--backend", default="matplotlib", choices=["matplotlib", "plotly"])
    parser.add_argument("--particle", default="electron", choices=["electron", "photon"])
    parser.add_argument("--spin-state", default="++", choices=["++", "+-", "-+", "--"])
    parser.add_argument("--loop-anchor-mode", default="evolving", choices=["evolving", "static"])
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--frames", type=int, default=None)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--duration", type=float, default=4.0, help="Output duration in seconds (target 3-5s)")
    parser.add_argument(
        "--cycle-time",
        type=float,
        default=None,
        help="Physics-time span covered by the animation. Default: one full particle cycle.",
    )
    parser.add_argument("--format", default="gif", choices=["gif", "mp4"])
    parser.add_argument("--output", default="output/cycle.gif")
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    particle = build_scene(
        args.particle,
        spin_state=args.spin_state,
        loop_anchor_mode=args.loop_anchor_mode,
    )

    frames = args.frames if args.frames is not None else max(2, int(round(args.duration * args.fps)))
    cycle_time = args.cycle_time if args.cycle_time is not None else float(particle.cycle_time())

    if args.backend == "matplotlib":
        render_cfg = RenderConfig(width=args.width, height=args.height, dpi=args.dpi)
        anim_cfg = AnimationConfig(
            frames=frames,
            cycle_time=cycle_time,
            fps=args.fps,
            format=args.format,
        )
        animator = CycleAnimator(render=render_cfg, animation=anim_cfg)
        animator.build(particle=particle, output_path=args.output)
    else:
        # Plotly path: render per-frame PNG with WebGL pipeline, then stitch via imageio.
        pr = PlotlyTorusRenderer(PlotlyRenderConfig(width=args.width, height=args.height))
        times = _frame_times(frames, cycle_time)

        with TemporaryDirectory() as td:
            tmp = Path(td)
            frame_paths: list[Path] = []
            for idx, t in enumerate(times):
                fp = tmp / f"plotly_{idx:04d}.png"
                try:
                    pr.render(particle=particle, time=t, output_path=str(fp), export_geometry=False)
                except Exception as e:
                    raise RuntimeError(
                        "Plotly image export failed. Plotly GIF/MP4 needs kaleido + Chromium system deps. "
                        "Try backend=matplotlib for immediate GIF output, or install Chromium libs for kaleido. "
                        f"Original error: {e}"
                    ) from e
                frame_paths.append(fp)

            imgs = [iio.imread(fp) for fp in frame_paths]
            if args.format == "gif":
                duration_ms = int(1000 / max(args.fps, 1))
                iio.imwrite(args.output, imgs, duration=duration_ms, loop=0)
            else:
                iio.imwrite(args.output, imgs, fps=args.fps)

    print(f"Rendered cycle ({args.backend}): {args.output}")


if __name__ == "__main__":
    main()
