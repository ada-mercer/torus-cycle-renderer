from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
import numpy as np

from torus_cycle_renderer.math import coupled_phase_trajectory
from torus_cycle_renderer.loops import LoopGeometry, ParticleLoop


@dataclass(frozen=True)
class ParticleParams:
    major_radius: float
    minor_radius: float
    deform_amp: float
    deform_mode_u: int
    deform_mode_v: int
    loop_turn_u: int
    loop_turn_v: int
    phase_speed: float
    # Internal channel controls (presentation-level until full calibration lock):
    # pf_value ~ fermic channel scale, p_value ~ bosic channel scale.
    pf_value: float = 1.0
    p_value: float = 0.33
    resonance_coupling: float = 0.22
    resonance_detuning: float = 0.03
    # Optional per-particle loop visibility tuning.
    loop_lift: float = 0.05
    # Preferred minimum number of fermic turns (v-cycle) for closed loops.
    fermic_cycles: int = 1


class AbstractParticle(ABC):
    """Abstract contract used by the renderer."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def params(self) -> ParticleParams:
        ...

    def deformation(self, u: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        p = self.params
        phase = p.deform_mode_u * u + p.deform_mode_v * v - p.phase_speed * t
        return p.deform_amp * np.cos(phase)

    def resonant_loop(self, t: float, points: int = 900) -> tuple[np.ndarray, np.ndarray]:
        p = self.params
        return coupled_phase_trajectory(
            t=t,
            points=points,
            base_u=float(p.loop_turn_u),
            base_v=float(p.loop_turn_v),
            coupling=p.resonance_coupling,
            detuning=p.resonance_detuning * p.phase_speed,
        )

    def loop_geometry(
        self,
        t: float,
        points: int = 900,
        reference_uv: tuple[float, float] = (0.0, 0.0),
    ) -> LoopGeometry:
        """Return loop geometry via a dedicated loop model object."""
        return ParticleLoop(self, reference_uv=reference_uv).from_particle_default(t=t, points=points)

    def cycle_time(self) -> float:
        """Base cycle from phase-speed scale only."""
        p = self.params
        return (2.0 * np.pi) / max(abs(p.phase_speed), 1e-9)

    def loop_cycle_time(self) -> float:
        """Time interval for full return to original loop state.

        Subclasses with extra closure constraints should override.
        """
        return self.cycle_time()
