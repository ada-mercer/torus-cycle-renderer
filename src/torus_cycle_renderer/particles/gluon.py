from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from .base import AbstractParticle, ParticleParams
from .families import BosonParticle
from torus_cycle_renderer.loops import LoopGeometry, ParticleLoop, PhaseLockedLoopConfig, phase_lock_cycle_multiplier


@dataclass(frozen=True)
class GluonState:
    """Prototype gluon correspondence state.

    Represents a color-adjoint-like transport branch with zero net EM charge
    expectation in the unified projector picture.
    """

    helicity: int = +1
    resonant_mode: tuple[int, int] = (3, 2)
    secondary_mode: tuple[int, int] = (2, 3)
    transport_winding: tuple[int, int] = (4, 4)
    phase_speed: float = 2.1
    major_radius: float = 2.0
    minor_radius: float = 0.62
    deform_amp: float = 0.10
    mixing_angle: float = 0.50
    # Effective in-hadron branch gap (not free-particle mass claim).
    effective_gap: float = 0.30


class Gluon(BosonParticle, AbstractParticle):
    """Prototype gluon renderer branch.

    Built as a dual-color-phase transport mode with no EM-charge annotation.
    """

    def __init__(self, state: GluonState | None = None):
        base = state or GluonState()
        helicity = +1 if base.helicity >= 0 else -1
        self.state = GluonState(
            helicity=helicity,
            resonant_mode=base.resonant_mode,
            secondary_mode=base.secondary_mode,
            transport_winding=base.transport_winding,
            phase_speed=base.phase_speed,
            major_radius=base.major_radius,
            minor_radius=base.minor_radius,
            deform_amp=base.deform_amp,
            mixing_angle=float(base.mixing_angle),
            effective_gap=max(base.effective_gap, 1e-6),
        )
        self.validate_policy(stage="init")

    @property
    def name(self) -> str:
        m1u, m1v = self.state.resonant_mode
        h = "+" if self.state.helicity > 0 else "-"
        return f"gluon[h={h}] mode=({m1u},{m1v})"

    @property
    def params(self) -> ParticleParams:
        m1u, m1v = self.state.resonant_mode
        ku, kv = self.state.transport_winding
        return ParticleParams(
            major_radius=self.state.major_radius,
            minor_radius=self.state.minor_radius,
            deform_amp=self.state.deform_amp,
            deform_mode_u=m1u,
            deform_mode_v=m1v,
            loop_turn_u=ku,
            loop_turn_v=kv,
            phase_speed=self.state.phase_speed,
            pf_value=1.20,
            p_value=0.60,
            resonance_coupling=0.44,
            resonance_detuning=0.07,
            loop_lift=0.09,
            fermic_cycles=2,
        )

    def _effective_omega(self) -> float:
        p = self.params
        m1u, m1v = self.state.resonant_mode
        omega_sq = (
            self.state.effective_gap**2
            + (m1u**2) / (p.major_radius**2)
            + (m1v**2) / (p.minor_radius**2)
        )
        return math.sqrt(max(omega_sq, 1e-12))

    def deformation(self, u: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        p = self.params
        m1u, m1v = self.state.resonant_mode
        m2u, m2v = self.state.secondary_mode
        h = self.state.helicity
        theta = self.state.mixing_angle
        omega = self._effective_omega()

        phi1 = m1u * u + h * m1v * v - omega * t
        phi2 = m2u * u - h * m2v * v - omega * t + 0.8

        mixed = np.cos(theta) * np.cos(phi1) + np.sin(theta) * np.sin(phi2)
        texture = 0.18 * np.sin(2.0 * phi1) + 0.14 * np.cos(2.0 * phi2)
        return p.deform_amp * (mixed + texture)

    def resonant_loop(self, t: float, points: int = 900) -> tuple[np.ndarray, np.ndarray]:
        loop = self.loop_geometry(t=t, points=points)
        return loop.u, loop.v

    def loop_geometry(
        self,
        t: float,
        points: int = 900,
        reference_uv: tuple[float, float] = (0.0, 0.0),
    ) -> LoopGeometry:
        m1u, m1v = self.state.resonant_mode
        h = self.state.helicity
        omega = self._effective_omega()

        return ParticleLoop(self, reference_uv=reference_uv).phase_locked(
            t=t,
            points=points,
            config=PhaseLockedLoopConfig(
                omega=omega,
                coeff_u=float(m1u),
                coeff_v=float(h * m1v),
                phase_offset=0.0,
                p_value=self.params.p_value,
                pf_value=self.params.pf_value,
                major_radius=self.params.major_radius,
                minor_radius=self.params.minor_radius,
                min_fermic_cycles=int(self.params.fermic_cycles),
            ),
        )

    def cycle_time(self) -> float:
        return (2.0 * math.pi) / max(self._effective_omega(), 1e-9)

    def loop_cycle_time(self) -> float:
        _m1u, m1v = self.state.resonant_mode
        return self.cycle_time() * phase_lock_cycle_multiplier(self.state.helicity * m1v)
