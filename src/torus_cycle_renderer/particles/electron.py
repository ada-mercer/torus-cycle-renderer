from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
import numpy as np

from .base import AbstractParticle, ParticleParams
from .families import FermionParticle, SpinState


@dataclass(frozen=True)
class ElectronState:
    """Single-mode electron state (no superpositions)."""

    spin_state: SpinState = SpinState.PP
    winding: tuple[int, int] = (1, 1)
    resonant_mode: tuple[int, int] = (1, 3)  # (nu_f, nu_b) single mode (no superposition)
    # Optional explicit transport winding (k_f, k_b). If None, inferred from pf/p ratio.
    transport_winding: tuple[int, int] | None = None
    # Loop anchor mode:
    # - "evolving": start point follows phase lock over time.
    # - "static": start point fixed from t=0 lock, shape still rotates through field.
    loop_anchor_mode: str = "evolving"
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

    def __init__(
        self,
        spin_state: str = "++",
        loop_anchor_mode: str = "evolving",
        state: ElectronState | None = None,
    ):
        base = state or ElectronState()
        if loop_anchor_mode not in {"evolving", "static"}:
            raise ValueError("loop_anchor_mode must be 'evolving' or 'static'")

        self.state = ElectronState(
            spin_state=SpinState(spin_state),
            winding=base.winding,
            resonant_mode=base.resonant_mode,
            transport_winding=base.transport_winding,
            loop_anchor_mode=loop_anchor_mode,
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
        return f"electron[{self.spin_state.value}] mode=({nu_f},{nu_b}) anchor={self.state.loop_anchor_mode}"

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

    def _time_scale(self) -> float:
        p = self.params
        return p.visual_time_scale * (max(p.p_value, 1e-9) / max(p.pf_value, 1e-9))

    def _transport_winding(self) -> tuple[int, int]:
        """Closed-loop winding (k_f, k_b) approximating m ∝ p_f e_f + p e_b."""
        if self.state.transport_winding is not None:
            return self.state.transport_winding

        ratio = max(self.state.pf_value, 1e-9) / max(self.state.p_value, 1e-9)
        frac = Fraction(ratio).limit_denominator(8)
        k_f = max(1, int(frac.numerator))
        k_b = max(1, int(frac.denominator))
        return (k_f, k_b)

    def deformation(self, u: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        p = self.params
        omega = self._effective_omega()
        t_eff = t * self._time_scale()
        phase0 = SPIN_PHASE_SHIFT[self.spin_state]
        nu_f, nu_b = self.state.resonant_mode
        phase = nu_f * u + nu_b * v - omega * t_eff + phase0
        return p.deform_amp * np.cos(phase)

    def resonant_loop(self, t: float, points: int = 900) -> tuple[np.ndarray, np.ndarray]:
        """Closed resonant transport loop in torus coordinates.

        Construction:
        - Tangent transport direction: m ~ p_f e_f + p e_b -> winding (k_f, k_b).
        - Loop: u = u0 + 2π k_f s, v = v0 + 2π k_b s, s in [0,1].
        - Start phase lock at (u0,v0): nu_f u0 + nu_b v0 - omega t_eff + phase0 = 0.

        This guarantees geometric closure (same point at s=0 and s=1 modulo 2π).
        """
        nu_f, nu_b = self.state.resonant_mode
        omega = self._effective_omega()
        t_eff = t * self._time_scale()
        phase0 = SPIN_PHASE_SHIFT[self.spin_state]

        k_f, k_b = self._transport_winding()
        s = np.linspace(0.0, 1.0, points, endpoint=True)

        u0 = 0.0
        if nu_b != 0:
            if self.state.loop_anchor_mode == "static":
                v0 = (-phase0 - nu_f * u0) / nu_b
            else:
                v0 = (omega * t_eff - phase0 - nu_f * u0) / nu_b
        else:
            v0 = 0.0

        u = u0 + 2.0 * np.pi * k_f * s
        v = v0 + 2.0 * np.pi * k_b * s
        return u, v

    def cycle_time(self) -> float:
        """Time for one complete resonant-cycle phase return at loop start."""
        omega = self._effective_omega()
        scale = self._time_scale()
        return (2.0 * math.pi) / max(omega * scale, 1e-9)
