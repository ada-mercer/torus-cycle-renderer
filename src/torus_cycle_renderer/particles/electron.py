from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from .base import AbstractParticle, ParticleParams
from .families import FermionParticle, SpinState


@dataclass(frozen=True)
class ElectronState:
    """Single-mode electron state (no superpositions)."""

    spin_state: SpinState = SpinState.PP
    winding: tuple[int, int] = (1, 1)
    resonant_mode: tuple[int, int] = (1, 3)  # (nu_f, nu_b) single closed mode
    pf_value: float = 1.0
    p_value: float = 1.0 / 3.0
    phase_speed: float = 1.2
    visual_time_scale: float = 0.5
    major_radius: float = 2.1
    minor_radius: float = 0.72
    deform_amp: float = 0.12


SPIN_PHASE_SHIFT = {
    SpinState.PP: 0.0,
    SpinState.PM: 0.5 * math.pi,
    SpinState.MP: -0.5 * math.pi,
    SpinState.MM: math.pi,
}


class Electron(FermionParticle, AbstractParticle):
    """Electron rendered from a single resonant mode state (no superpositions)."""

    def __init__(self, spin_state: str = "++", state: ElectronState | None = None):
        base = state or ElectronState()
        self.state = ElectronState(
            spin_state=SpinState(spin_state),
            winding=base.winding,
            resonant_mode=base.resonant_mode,
            pf_value=base.pf_value,
            p_value=base.p_value,
            phase_speed=base.phase_speed,
            visual_time_scale=base.visual_time_scale,
            major_radius=base.major_radius,
            minor_radius=base.minor_radius,
            deform_amp=base.deform_amp,
        )
        self.spin_state = self.state.spin_state
        self.validate_policy(stage="init")

    @property
    def name(self) -> str:
        nu_f, nu_b = self.state.resonant_mode
        return f"electron[{self.spin_state.value}] mode=({nu_f},{nu_b})"

    @property
    def winding(self) -> tuple[int, int]:
        return self.state.winding

    @property
    def params(self) -> ParticleParams:
        nu_f, nu_b = self.state.resonant_mode
        return ParticleParams(
            major_radius=self.state.major_radius,
            minor_radius=self.state.minor_radius,
            deform_amp=self.state.deform_amp,
            deform_mode_u=nu_f,
            deform_mode_v=nu_b,
            loop_turn_u=nu_f,
            loop_turn_v=nu_b,
            phase_speed=self.state.phase_speed,
            pf_value=self.state.pf_value,
            p_value=self.state.p_value,
            visual_time_scale=self.state.visual_time_scale,
            color="#3a86ff",
            loop_color="#ff006e",
        )

    def _effective_omega(self) -> float:
        p = self.params
        nu_f, nu_b = self.state.resonant_mode
        # Baseline linear torus spectrum for one single mode.
        omega_sq = 1.0 + (nu_f**2) / (p.major_radius**2) + (nu_b**2) / (p.minor_radius**2)
        return math.sqrt(max(omega_sq, 1e-12))

    def deformation(self, u: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        p = self.params
        omega = self._effective_omega()
        # Presentation pacing uses p/pf to keep the cycle readable.
        t_eff = t * p.visual_time_scale * (max(p.p_value, 1e-6) / max(p.pf_value, 1e-6))
        phase0 = SPIN_PHASE_SHIFT[self.spin_state]
        nu_f, nu_b = self.state.resonant_mode
        phase = nu_f * u + nu_b * v - omega * t_eff + phase0
        return p.deform_amp * np.cos(phase)

    def resonant_loop(self, t: float, points: int = 900) -> tuple[np.ndarray, np.ndarray]:
        """Closed single-branch resonant cycle from one mode equation.

        Constraint: nu_f*u + nu_b*v - omega*t + phase0 = const.
        Use continuous branch values (no modulo) to avoid visual jump artifacts.
        """
        p = self.params
        nu_f, nu_b = self.state.resonant_mode
        omega = self._effective_omega()
        t_eff = t * p.visual_time_scale * (max(p.p_value, 1e-6) / max(p.pf_value, 1e-6))
        phase0 = SPIN_PHASE_SHIFT[self.spin_state]

        u = np.linspace(0.0, 2 * np.pi, points, endpoint=True)

        if nu_b == 0:
            # Degenerate case: solve for constant u branch and sweep v.
            u0 = (omega * t_eff - phase0) / max(nu_f, 1e-6)
            u = np.full(points, u0)
            v = np.linspace(0.0, 2 * np.pi, points, endpoint=True)
            return u, v

        v = (omega * t_eff - phase0 - nu_f * u) / nu_b
        return u, v

    def cycle_time(self) -> float:
        """Time for one complete phase advance of the single resonant mode."""
        p = self.params
        omega = self._effective_omega()
        scale = p.visual_time_scale * (max(p.p_value, 1e-6) / max(p.pf_value, 1e-6))
        return (2.0 * math.pi) / max(omega * scale, 1e-9)
