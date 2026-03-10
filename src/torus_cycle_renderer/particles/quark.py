from __future__ import annotations

import math
from abc import abstractmethod

import numpy as np

from .base import AbstractParticle
from .families import FermionParticle, SpinState
from torus_cycle_renderer.loops import LoopGeometry, ParticleLoop, PhaseLockedLoopConfig, phase_lock_cycle_multiplier


SPIN_SIGN = {
    SpinState.PP: +1,
    SpinState.PM: +1,
    SpinState.MP: -1,
    SpinState.MM: -1,
}


class Quark(FermionParticle, AbstractParticle):
    """Shared base class for quark-like prototype branches.

    This layer holds the common mechanics used by the current defect-bearing
    quark branches while leaving branch-specific defaults and deformation
    textures to concrete subclasses such as `UQuark` and `DQuark`.
    """

    @property
    def spin_sign(self) -> int:
        return SPIN_SIGN[self.spin_state]

    @property
    def winding(self) -> tuple[int, int]:
        return self.state.transport_winding

    def _effective_omega(self) -> float:
        p = self.params
        m1u, m1v = self.state.resonant_mode
        omega_sq = (
            self.state.mass_gap**2
            + (m1u**2) / (p.major_radius**2)
            + (m1v**2) / (p.minor_radius**2)
        )
        return math.sqrt(max(omega_sq, 1e-12))

    def _defect_phase(self) -> float:
        return 2.0 * math.pi * self.state.closure_defect + self.state.color_phase

    def _phase_pair(self, u: np.ndarray, v: np.ndarray, t: float) -> tuple[np.ndarray, np.ndarray]:
        m1u, m1v = self.state.resonant_mode
        m2u, m2v = self.state.secondary_mode
        omega = self._effective_omega()
        defect_phase = self._defect_phase()

        phi1 = m1u * u + self.spin_sign * m1v * v - omega * t + defect_phase
        phi2 = m2u * u - self.spin_sign * m2v * v - omega * t + self.secondary_phase_offset()
        return phi1, phi2

    @abstractmethod
    def secondary_phase_offset(self) -> float:
        """Branch-specific phase offset for the secondary quark mode."""

    @abstractmethod
    def texture_terms(self, phi1: np.ndarray, phi2: np.ndarray) -> np.ndarray:
        """Branch-specific higher-harmonic texture contribution."""

    def deformation(self, u: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        p = self.params
        theta = self.state.mixing_angle
        phi1, phi2 = self._phase_pair(u, v, t)

        mixed = np.cos(theta) * np.cos(phi1) + np.sin(theta) * np.cos(phi2)
        texture = self.texture_terms(phi1, phi2)
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
        omega = self._effective_omega()

        config_kwargs = dict(
            omega=omega,
            coeff_u=float(m1u),
            coeff_v=float(self.spin_sign * m1v),
            phase_offset=float(self._defect_phase()),
            p_value=self.params.p_value,
            pf_value=self.params.pf_value,
            major_radius=self.params.major_radius,
            minor_radius=self.params.minor_radius,
            min_fermic_cycles=int(self.params.fermic_cycles),
        )

        if hasattr(self.state, "pf_orbit_relative"):
            config_kwargs.update(
                pf_orbit_relative=bool(self.state.pf_orbit_relative),
                pf_orbit_sign=+1,
                pf_orbit_scale=1.0,
                pf_orbit_period=self.loop_cycle_time(),
            )

        return ParticleLoop(self, reference_uv=reference_uv).phase_locked(
            t=t,
            points=points,
            config=PhaseLockedLoopConfig(**config_kwargs),
        )

    def cycle_time(self) -> float:
        return (2.0 * math.pi) / max(self._effective_omega(), 1e-9)

    def loop_cycle_time(self) -> float:
        _m1u, m1v = self.state.resonant_mode
        return self.cycle_time() * phase_lock_cycle_multiplier(self.spin_sign * m1v)

    def closure_residual(self, weak_cycles: int = 1) -> float:
        """Return fractional closure residual modulo 1 for the current hypothesis."""
        phase_units = self.state.closure_defect - weak_cycles * self.state.weak_assist_phase
        return abs(phase_units - round(phase_units))
