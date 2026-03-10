from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
import math
from typing import TYPE_CHECKING

import numpy as np

from torus_cycle_renderer.math import phase_locked_tangent_loop

if TYPE_CHECKING:
    from torus_cycle_renderer.particles.base import AbstractParticle


def phase_lock_cycle_multiplier(coeff_v: float, *, max_denom: int = 16) -> int:
    """Return integer multiplier for full return of phase-locked loop anchor.

    For an anchor relation coeff_u*u + coeff_v*v - omega*t + phase0 = 0,
    full return of v-anchor generally needs omega*T/(2π*coeff_v) to be integer.
    This helper returns a compact integer multiplier m so that T_full = m*T_base.
    """
    c = abs(float(coeff_v))
    if c < 1e-12:
        return 1
    frac = Fraction(c).limit_denominator(max(1, int(max_denom)))
    return max(1, int(frac.numerator))


@dataclass(frozen=True)
class LoopGeometry:
    u: np.ndarray
    v: np.ndarray
    reference_uv: tuple[float, float]
    metadata: dict[str, float | int | str] = field(default_factory=dict)


@dataclass(frozen=True)
class PhaseLockedLoopConfig:
    omega: float
    coeff_u: float
    coeff_v: float
    phase_offset: float
    p_value: float
    pf_value: float
    major_radius: float
    minor_radius: float
    min_fermic_cycles: int = 1
    sign_u: int = +1
    sign_v: int = +1
    pf_orbit_relative: bool = False
    pf_orbit_sign: int = +1
    pf_orbit_scale: float = 1.0
    pf_orbit_period: float | None = None


class ParticleLoop:
    """Loop geometry builder anchored at a reference torus coordinate.

    This class centralizes loop construction and frame-to-frame transport logic.
    """

    def __init__(self, particle: AbstractParticle, reference_uv: tuple[float, float] = (0.0, 0.0)):
        self.particle = particle
        self.reference_uv = (float(reference_uv[0]), float(reference_uv[1]))

    def from_particle_default(self, t: float, points: int = 900) -> LoopGeometry:
        """Fallback adapter: use particle.resonant_loop while exposing LoopGeometry."""
        u, v = self.particle.resonant_loop(t=t, points=points)
        return LoopGeometry(
            u=u,
            v=v,
            reference_uv=self.reference_uv,
            metadata={"model": "legacy-resonant-loop"},
        )

    def phase_locked(self, t: float, points: int, config: PhaseLockedLoopConfig) -> LoopGeometry:
        """Build a closed phase-locked loop and optionally transport anchor with p_f."""
        u_ref, v_ref = self.reference_uv

        u, v = phase_locked_tangent_loop(
            points=points,
            t=t,
            omega=float(config.omega),
            coeff_u=float(config.coeff_u),
            coeff_v=float(config.coeff_v),
            phase_offset=float(config.phase_offset),
            p_value=float(config.p_value),
            pf_value=float(config.pf_value),
            major_radius=float(config.major_radius),
            minor_radius=float(config.minor_radius),
            min_fermic_cycles=max(1, int(config.min_fermic_cycles)),
            sign_u=int(np.sign(config.sign_u) or 1),
            sign_v=int(np.sign(config.sign_v) or 1),
            u_start=float(u_ref),
        )

        # Keep reference latitude available as an explicit shift (useful for k_v=0 branches).
        v = v + float(v_ref)

        if config.pf_orbit_relative:
            period = float(config.pf_orbit_period or self.particle.cycle_time())
            period = max(period, 1e-9)
            drift = (2.0 * math.pi) * int(np.sign(config.pf_orbit_sign) or 1) * float(config.pf_orbit_scale) * (t / period)
            v = v + drift

        return LoopGeometry(
            u=u,
            v=v,
            reference_uv=self.reference_uv,
            metadata={
                "model": "phase-locked-tangent",
                "pf_orbit_relative": int(bool(config.pf_orbit_relative)),
            },
        )

    def transport_winding(
        self,
        *,
        t: float,
        points: int,
        k_u: int,
        k_v: int,
        v_anchor: float,
        u_sign: int = +1,
        v_sign: int = +1,
        pf_orbit_relative: bool = False,
        pf_orbit_sign: int = +1,
        pf_orbit_scale: float = 1.0,
        pf_orbit_period: float | None = None,
    ) -> LoopGeometry:
        """Build a direct winding loop from integer turns around torus coordinates."""
        s = np.linspace(0.0, 1.0, points, endpoint=True)
        u_ref, v_ref = self.reference_uv

        u = float(u_ref) + 2.0 * math.pi * int(np.sign(u_sign) or 1) * int(k_u) * s
        v = float(v_anchor) + float(v_ref) + 2.0 * math.pi * int(np.sign(v_sign) or 1) * int(k_v) * s

        if pf_orbit_relative:
            period = float(pf_orbit_period or self.particle.cycle_time())
            period = max(period, 1e-9)
            drift = (2.0 * math.pi) * int(np.sign(pf_orbit_sign) or 1) * float(pf_orbit_scale) * (t / period)
            v = v + drift

        return LoopGeometry(
            u=u,
            v=v,
            reference_uv=self.reference_uv,
            metadata={
                "model": "transport-winding",
                "pf_orbit_relative": int(bool(pf_orbit_relative)),
            },
        )
