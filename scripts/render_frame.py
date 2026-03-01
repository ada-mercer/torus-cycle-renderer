#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from torus_cycle_renderer.rendering import TorusRenderer, RenderConfig
from torus_cycle_renderer.scenes import build_scene


def main() -> None:
    parser = argparse.ArgumentParser(description="Render one torus-cycle frame")
    parser.add_argument("--particle", default="electron", choices=["electron", "photon"])
    parser.add_argument("--time", type=float, default=0.0)
    parser.add_argument("--spin-state", default="++", choices=["++", "+-", "-+", "--"])
    parser.add_argument("--loop-anchor-mode", default="evolving", choices=["evolving", "static"])
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--output", default="output/frame.png")
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    particle = build_scene(
        args.particle,
        spin_state=args.spin_state,
        loop_anchor_mode=args.loop_anchor_mode,
    )
    renderer = TorusRenderer(RenderConfig(width=args.width, height=args.height, dpi=args.dpi))
    renderer.render(particle=particle, time=args.time, output_path=args.output)
    print(f"Rendered: {args.output}")


if __name__ == "__main__":
    main()
