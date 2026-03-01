#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from torus_cycle_renderer.rendering import (
    TorusRenderer,
    RenderConfig,
    CycleAnimator,
    AnimationConfig,
)
from torus_cycle_renderer.scenes import build_scene


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a full torus-cycle animation")
    parser.add_argument("--particle", default="electron", choices=["electron", "photon"])
    parser.add_argument("--spin-state", default="++", choices=["++", "+-", "-+", "--"])
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--frames", type=int, default=120)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--cycle-time", type=float, default=6.283185307179586)
    parser.add_argument("--format", default="gif", choices=["gif", "mp4"])
    parser.add_argument("--output", default="output/cycle.gif")
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    particle = build_scene(args.particle, spin_state=args.spin_state)

    render_cfg = RenderConfig(width=args.width, height=args.height, dpi=args.dpi)
    anim_cfg = AnimationConfig(
        frames=args.frames,
        cycle_time=args.cycle_time,
        fps=args.fps,
        format=args.format,
    )

    animator = CycleAnimator(render=render_cfg, animation=anim_cfg)
    animator.build(particle=particle, output_path=args.output)
    print(f"Rendered cycle: {args.output}")


if __name__ == "__main__":
    main()
