from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from .base import AbstractParticle, ParticleParams
from .families import WeakBosonParticle
from torus_cycle_renderer.loops import LoopGeometry, ParticleLoop, PhaseLockedLoopConfig, phase_lock_cycle_multiplier


@dataclass(frozen=True)
class ZBosonState:
    """Neutral weak-boson correspondence state.

    Uses a minimal two-branch neutral mix (B3/B0-like) to avoid a too-simple
    single-wave appearance while keeping a compact renderer model.
    """

    helicity: int = +1
    resonant_mode: tuple[int, int] = (2, 2)  # primary (mode_u, mode_v)
    secondary_mode: tuple[int, int] = (3, 1)  # neutral companion branch
    transport_winding: tuple[int, int] = (3, 2)  # (k_u, k_v)
    phase_speed: float = 1.7
    major_radius: float = 2.0
    minor_radius: float = 0.62
    deform_amp: float = 0.10
    # Neutral mixing angle between primary/secondary branches.
    mixing_angle: float = 0.58
    # Massive neutral branch lock.
    mass_gap: float = 1.75


class ZBoson(WeakBosonParticle, AbstractParticle):
    """Neutral weak-boson (Z-like) correspondence particle.

    Neutral branch policy:
    - massive weak channel (positive mass gap),
    - no charged-conjugate orientation sign in loop definition,
    - same general projection framework as other particle classes.
    """

    def __init__(self, state: ZBosonState | None = None):
        base = state or ZBosonState()
        helicity = +1 if base.helicity >= 0 else -1
        self.state = ZBosonState(
            helicity=helicity,
            resonant_mode=base.resonant_mode,
            secondary_mode=base.secondary_mode,
            transport_winding=base.transport_winding,
            phase_speed=base.phase_speed,
            major_radius=base.major_radius,
            minor_radius=base.minor_radius,
            deform_amp=base.deform_amp,
            mixing_angle=float(base.mixing_angle),
            mass_gap=max(base.mass_gap, 1e-6),
        )
        self.validate_policy(stage="init")

    @property
    def name(self) -> str:
        mu, mv = self.state.resonant_mode
        h = "+" if self.state.helicity > 0 else "-"
        return f"Z0[h={h}] mode=({mu},{mv})"

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
            # Neutral weak branch uses mixed channels with p/p_f < 1 preferred.
            pf_value=0.95,
            p_value=0.475,
            resonance_coupling=0.32,
            resonance_detuning=0.045,
            loop_lift=0.09,
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
        m1u, m1v = self.state.resonant_mode
        m2u, m2v = self.state.secondary_mode
        h = self.state.helicity
        theta = self.state.mixing_angle

        phase_1 = m1u * u + h * m1v * v - omega * t
        phase_2 = m2u * u - h * m2v * v - omega * t + 0.65

        # Neutral-channel blend: two companion branches + gentle texture.
        mixed = np.cos(theta) * np.cos(phase_1) + np.sin(theta) * np.cos(phase_2)
        texture = 0.14 * np.cos(2.0 * phase_1) + 0.10 * np.sin(2.0 * phase_2)
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
        """Closed, channel-tangent neutral loop with phase anchor on primary mode."""
        m1u, m1v = self.state.resonant_mode
        omega = self._effective_omega()
        h = self.state.helicity
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
        omega = self._effective_omega()
        return (2.0 * math.pi) / max(omega, 1e-9)

    def loop_cycle_time(self) -> float:
        _m1u, m1v = self.state.resonant_mode
        return self.cycle_time() * phase_lock_cycle_multiplier(self.state.helicity * m1v)
