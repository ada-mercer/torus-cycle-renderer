from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from .base import AbstractParticle, ParticleParams
from .families import WeakBosonParticle
from torus_cycle_renderer.loops import LoopGeometry, ParticleLoop, PhaseLockedLoopConfig, phase_lock_cycle_multiplier


@dataclass(frozen=True)
class WMinusState:
    """Single-mode W- weak-boson correspondence state."""

    helicity: int = +1
    resonant_mode: tuple[int, int] = (2, 1)  # (mode_u, mode_v)
    transport_winding: tuple[int, int] = (3, 1)  # (k_u, k_v)
    phase_speed: float = 1.8
    major_radius: float = 2.0
    minor_radius: float = 0.62
    deform_amp: float = 0.095
    mass_gap: float = 1.6


class WMinus(WeakBosonParticle, AbstractParticle):
    """W- weak-boson correspondence particle for torus rendering.

    Constructed as the charged-conjugate branch of W+ at renderer level:
    same mass gap and mode magnitudes, opposite charged-channel orientation.
    """

    def __init__(self, state: WMinusState | None = None):
        base = state or WMinusState()
        helicity = +1 if base.helicity >= 0 else -1
        self.state = WMinusState(
            helicity=helicity,
            resonant_mode=base.resonant_mode,
            transport_winding=base.transport_winding,
            phase_speed=base.phase_speed,
            major_radius=base.major_radius,
            minor_radius=base.minor_radius,
            deform_amp=base.deform_amp,
            mass_gap=max(base.mass_gap, 1e-6),
        )
        self.validate_policy(stage="init")

    @property
    def name(self) -> str:
        mu, mv = self.state.resonant_mode
        h = "+" if self.state.helicity > 0 else "-"
        return f"W-[h={h}] mode=({mu},{mv})"

    @property
    def params(self) -> ParticleParams:
        mode_u, mode_v = self.state.resonant_mode
        k_u, k_v = self.state.transport_winding
        return ParticleParams(
            major_radius=self.state.major_radius,
            minor_radius=self.state.minor_radius,
            deform_amp=self.state.deform_amp,
            deform_mode_u=mode_u,
            deform_mode_v=mode_v,
            loop_turn_u=k_u,
            loop_turn_v=k_v,
            phase_speed=self.state.phase_speed,
            pf_value=1.00,
            p_value=0.50,
            resonance_coupling=0.35,
            resonance_detuning=0.05,
            fermic_cycles=2,
        )

    def _effective_omega(self) -> float:
        p = self.params
        mode_u, mode_v = self.state.resonant_mode
        omega_sq = (
            self.state.mass_gap**2
            + (mode_u**2) / (p.major_radius**2)
            + (mode_v**2) / (p.minor_radius**2)
        )
        return math.sqrt(max(omega_sq, 1e-12))

    def deformation(self, u: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        p = self.params
        omega = self._effective_omega()
        mode_u, mode_v = self.state.resonant_mode
        h = self.state.helicity

        # Conjugate charged branch: opposite phase orientation relative to W+.
        phase = mode_u * u - h * mode_v * v - omega * t
        texture = 0.22 * np.sin(2.0 * phase - 0.4 * h)
        return p.deform_amp * (np.cos(phase) + texture)

    def resonant_loop(self, t: float, points: int = 900) -> tuple[np.ndarray, np.ndarray]:
        loop = self.loop_geometry(t=t, points=points)
        return loop.u, loop.v

    def loop_geometry(
        self,
        t: float,
        points: int = 900,
        reference_uv: tuple[float, float] = (0.0, 0.0),
    ) -> LoopGeometry:
        mode_u, mode_v = self.state.resonant_mode
        omega = self._effective_omega()
        h = self.state.helicity
        return ParticleLoop(self, reference_uv=reference_uv).phase_locked(
            t=t,
            points=points,
            config=PhaseLockedLoopConfig(
                omega=omega,
                coeff_u=float(mode_u),
                coeff_v=float(-h * mode_v),
                phase_offset=0.0,
                p_value=self.params.p_value,
                pf_value=self.params.pf_value,
                major_radius=self.params.major_radius,
                minor_radius=self.params.minor_radius,
                min_fermic_cycles=int(self.params.fermic_cycles),
                sign_u=+1,
                sign_v=-1,
            ),
        )

    def cycle_time(self) -> float:
        omega = self._effective_omega()
        return (2.0 * math.pi) / max(omega, 1e-9)

    def loop_cycle_time(self) -> float:
        _mode_u, mode_v = self.state.resonant_mode
        return self.cycle_time() * phase_lock_cycle_multiplier(-self.state.helicity * mode_v)
