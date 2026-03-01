from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory

import imageio.v3 as iio

from torus_cycle_renderer.particles import AbstractParticle
from .renderer import TorusRenderer, RenderConfig


@dataclass(frozen=True)
class AnimationConfig:
    frames: int = 120
    cycle_time: float = 2 * 3.141592653589793
    fps: int = 30
    format: str = "gif"  # gif | mp4


class CycleAnimator:
    """Factory-style animation builder: render frames, then stitch outputs."""

    def __init__(self, render: RenderConfig | None = None, animation: AnimationConfig | None = None):
        self.render_config = render or RenderConfig()
        self.animation_config = animation or AnimationConfig()
        self.renderer = TorusRenderer(self.render_config)

    def _frame_times(self) -> list[float]:
        a = self.animation_config
        if a.frames < 2:
            return [0.0]
        step = a.cycle_time / a.frames
        return [k * step for k in range(a.frames)]

    def build(self, particle: AbstractParticle, output_path: str) -> None:
        a = self.animation_config
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        with TemporaryDirectory() as td:
            tmp = Path(td)
            frame_paths: list[Path] = []
            for idx, t in enumerate(self._frame_times()):
                fp = tmp / f"frame_{idx:04d}.png"
                self.renderer.render(particle=particle, time=t, output_path=str(fp))
                frame_paths.append(fp)

            frames = [iio.imread(fp) for fp in frame_paths]

            fmt = a.format.lower()
            if fmt == "gif":
                duration_ms = int(1000 / max(a.fps, 1))
                iio.imwrite(out, frames, duration=duration_ms, loop=0)
            elif fmt == "mp4":
                iio.imwrite(out, frames, fps=a.fps)
            else:
                raise ValueError(f"Unsupported animation format: {a.format}")
