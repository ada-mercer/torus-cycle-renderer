from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
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
    frame_workers: int = 1


@dataclass(frozen=True)
class RenderJob:
    particle: AbstractParticle
    output_path: str
    render: RenderConfig
    animation: AnimationConfig


def _render_single_frame(
    particle: AbstractParticle,
    render_cfg: RenderConfig,
    time_point: float,
    frame_path: str,
) -> None:
    TorusRenderer(render_cfg).render(particle=particle, time=time_point, output_path=frame_path)


def _run_render_job(job: RenderJob) -> str:
    CycleAnimator(render=job.render, animation=job.animation).build(job.particle, job.output_path)
    return job.output_path


def frame_times(frames: int, cycle_time: float) -> list[float]:
    if frames < 2:
        return [0.0]
    step = cycle_time / frames
    return [k * step for k in range(frames)]


class CycleAnimator:
    """Factory-style animation builder: render frames, then stitch outputs."""

    def __init__(self, render: RenderConfig | None = None, animation: AnimationConfig | None = None):
        self.render_config = render or RenderConfig()
        self.animation_config = animation or AnimationConfig()
        self.renderer = TorusRenderer(self.render_config)

    def _frame_times(self) -> list[float]:
        a = self.animation_config
        return frame_times(a.frames, a.cycle_time)

    def _render_frames(self, particle: AbstractParticle, frame_paths: list[Path], times: list[float]) -> None:
        workers = max(1, int(self.animation_config.frame_workers))
        if workers <= 1:
            for fp, t in zip(frame_paths, times, strict=True):
                self.renderer.render(particle=particle, time=t, output_path=str(fp))
            return

        with ProcessPoolExecutor(max_workers=workers) as pool:
            futures = [
                pool.submit(_render_single_frame, particle, self.render_config, t, str(fp))
                for fp, t in zip(frame_paths, times, strict=True)
            ]
            for f in futures:
                f.result()

    def build(self, particle: AbstractParticle, output_path: str) -> None:
        a = self.animation_config
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        with TemporaryDirectory() as td:
            tmp = Path(td)
            times = self._frame_times()
            frame_paths = [tmp / f"frame_{idx:04d}.png" for idx in range(len(times))]
            self._render_frames(particle=particle, frame_paths=frame_paths, times=times)

            frames = [iio.imread(fp) for fp in frame_paths]

            fmt = a.format.lower()
            if fmt == "gif":
                duration_ms = int(1000 / max(a.fps, 1))
                iio.imwrite(out, frames, duration=duration_ms, loop=0)
            elif fmt == "mp4":
                iio.imwrite(out, frames, fps=a.fps)
            else:
                raise ValueError(f"Unsupported animation format: {a.format}")

    @staticmethod
    def build_many(jobs: list[RenderJob], max_workers: int = 1) -> list[str]:
        """Render multiple animations, optionally in parallel across jobs."""
        workers = max(1, int(max_workers))
        if workers <= 1:
            return [_run_render_job(job) for job in jobs]

        with ProcessPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(_run_render_job, job) for job in jobs]
            return [f.result() for f in futures]
