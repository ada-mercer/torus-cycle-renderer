#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from torus_cycle_renderer.rendering import (
    TorusRenderer,
    RenderConfig,
    PlotlyTorusRenderer,
    PlotlyRenderConfig,
)
from torus_cycle_renderer.scenes import build_scene
from torus_cycle_renderer.math import torus_surface, torus_frame
from torus_cycle_renderer.rendering.geometry_export import (
    export_scene_npz,
    export_torus_obj,
    export_loop_obj,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render one torus-cycle frame")
    parser.add_argument("--particle", default="electron", choices=["electron", "photon"])
    parser.add_argument("--time", type=float, default=0.0)
    parser.add_argument("--spin-state", default="++", choices=["++", "+-", "-+", "--"])
    parser.add_argument("--loop-anchor-mode", default="evolving", choices=["evolving", "static"])
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--backend", default="matplotlib", choices=["matplotlib", "plotly"])
    parser.add_argument("--export-geometry", action="store_true")
    parser.add_argument("--output", default="output/frame.png")
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    particle = build_scene(
        args.particle,
        spin_state=args.spin_state,
        loop_anchor_mode=args.loop_anchor_mode,
    )

    if args.backend == "matplotlib":
        renderer = TorusRenderer(RenderConfig(width=args.width, height=args.height, dpi=args.dpi))
        renderer.render(particle=particle, time=args.time, output_path=args.output)

        if args.export_geometry:
            p = particle.params
            u, v = torus_frame()
            deform = particle.deformation(u, v, args.time)
            x, y, z = torus_surface(u, v, p.major_radius, p.minor_radius, deformation=deform)
            lu, lv = particle.resonant_loop(args.time)
            ldef = particle.deformation(lu, lv, args.time)
            lx, ly, lz = torus_surface(lu, lv, p.major_radius, p.minor_radius, deformation=ldef + 0.04)
            stem = Path(args.output).with_suffix("")
            export_scene_npz(str(stem) + "_geom.npz", x, y, z, lx, ly, lz)
            export_torus_obj(str(stem) + "_torus.obj", x, y, z)
            export_loop_obj(str(stem) + "_loop.obj", lx, ly, lz)
    else:
        # Plotly backend gives stronger depth-accurate multi-object rendering.
        renderer = PlotlyTorusRenderer(PlotlyRenderConfig(width=args.width, height=args.height))
        renderer.render(
            particle=particle,
            time=args.time,
            output_path=args.output,
            export_geometry=args.export_geometry,
        )

    print(f"Rendered ({args.backend}): {args.output}")


if __name__ == "__main__":
    main()
