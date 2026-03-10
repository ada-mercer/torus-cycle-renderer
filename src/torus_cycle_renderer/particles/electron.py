from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from .base import AbstractParticle, ParticleParams
from .families import FermionParticle, SpinState
from torus_cycle_renderer.math import tangent_winding_from_channels
from torus_cycle_renderer.loops import LoopGeometry, ParticleLoop


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
    # If true, move the loop reference along the fermic/minor coordinate over the cycle.
    pf_orbit_relative: bool = True
    pf_value: float = 1.0
    p_value: float = 0.50
    phase_speed: float = 1.2
    major_radius: float = 2.1
    minor_radius: float = 0.72
    deform_amp: float = 0.12


SPIN_PHASE_SHIFT = {
    SpinState.PP: 0.0,
    SpinState.PM: 0.5 * math.pi,
    SpinState.MP: -0.5 * math.pi,
    SpinState.MM: math.pi,
}

# Spin convention: spin flip reverses bosic transport handedness (p-sector),
# while fermic orientation (p_f-sector) remains fixed for matter branch.
SPIN_BOSIC_CHIRALITY = {
    SpinState.PP: +1,
    SpinState.PM: +1,
    SpinState.MP: -1,
    SpinState.MM: -1,
}


class Electron(FermionParticle, AbstractParticle):
    """Electron rendered from a single resonant mode state (no superpositions).

    Convention lock:
    - p (bosic) wraps the major angle u/theta.
    - p_f (fermic) wraps the minor angle v/phi.
    """

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
            pf_orbit_relative=bool(base.pf_orbit_relative),
            pf_value=base.pf_value,
            p_value=base.p_value,
            phase_speed=base.phase_speed,
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
        # resonant_mode stores (mode_p, mode_pf) to reflect p on theta(u), p_f on phi(v)
        mode_p, mode_pf = self.state.resonant_mode
        return ParticleParams(
            major_radius=self.state.major_radius,
            minor_radius=self.state.minor_radius,
            deform_amp=self.state.deform_amp,
            deform_mode_u=mode_p,
            deform_mode_v=mode_pf,
            loop_turn_u=mode_p,
            loop_turn_v=mode_pf,
            phase_speed=self.state.phase_speed,
            pf_value=self.state.pf_value,
            p_value=self.state.p_value,
            fermic_cycles=2,
        )

    def _effective_omega(self) -> float:
        p = self.params
        mode_p, mode_pf = self.state.resonant_mode
        # Baseline linear torus spectrum for one single mode.
        omega_sq = 1.0 + (mode_p**2) / (p.major_radius**2) + (mode_pf**2) / (p.minor_radius**2)
        return math.sqrt(max(omega_sq, 1e-12))

    def _time_scale(self) -> float:
        p = self.params
        return max(p.p_value, 1e-9) / max(p.pf_value, 1e-9)

    def _transport_winding(self) -> tuple[int, int]:
        """Return (k_pf, k_p) with short-loop preference under tangent constraint."""
        if self.state.transport_winding is not None:
            return self.state.transport_winding

        # Helper returns (k_u, k_v) with u~p and v~p_f.
        k_u, k_v = tangent_winding_from_channels(
            self.state.p_value,
            self.state.pf_value,
            major_radius=self.state.major_radius,
            minor_radius=self.state.minor_radius,
            min_k_v=max(1, int(self.params.fermic_cycles)),
        )
        # Electron convention in this file expects (k_pf, k_p).
        return (k_v, k_u)

    def deformation(self, u: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        p = self.params
        omega = self._effective_omega()
        t_eff = t * self._time_scale()
        phase0 = SPIN_PHASE_SHIFT[self.spin_state]
        mode_p, mode_pf = self.state.resonant_mode
        phase = mode_p * u + mode_pf * v - omega * t_eff + phase0
        return p.deform_amp * np.cos(phase)

    def resonant_loop(self, t: float, points: int = 900) -> tuple[np.ndarray, np.ndarray]:
        loop = self.loop_geometry(t=t, points=points)
        return loop.u, loop.v

    def loop_geometry(
        self,
        t: float,
        points: int = 900,
        reference_uv: tuple[float, float] = (0.0, 0.0),
    ) -> LoopGeometry:
        """Closed resonant transport loop with optional p_f-relative reference motion."""
        mode_p, mode_pf = self.state.resonant_mode
        omega = self._effective_omega()
        t_eff = t * self._time_scale()
        phase0 = SPIN_PHASE_SHIFT[self.spin_state]

        # _transport_winding returns (k_pf, k_p); swap into coordinate axes.
        k_pf, k_p = self._transport_winding()
        bosic_chirality = SPIN_BOSIC_CHIRALITY[self.spin_state]

        u0 = float(reference_uv[0])
        if mode_pf != 0:
            if self.state.loop_anchor_mode == "static":
                v_anchor = (-phase0 - mode_p * u0) / mode_pf
            else:
                v_anchor = (omega * t_eff - phase0 - mode_p * u0) / mode_pf
        else:
            v_anchor = 0.0

        move_with_pf = bool(self.state.pf_orbit_relative and self.state.loop_anchor_mode == "evolving")

        return ParticleLoop(self, reference_uv=reference_uv).transport_winding(
            t=t,
            points=points,
            k_u=k_p,
            k_v=k_pf,
            v_anchor=v_anchor,
            u_sign=bosic_chirality,
            v_sign=+1,
            pf_orbit_relative=move_with_pf,
            pf_orbit_sign=+1,
            pf_orbit_scale=1.0,
            pf_orbit_period=self.loop_cycle_time(),
        )

    def cycle_time(self) -> float:
        """Time for full return of electron loop and phase anchor."""
        omega = self._effective_omega()
        scale = self._time_scale()
        base = (2.0 * math.pi) / max(omega * scale, 1e-9)

        if self.state.loop_anchor_mode == "evolving":
            _mode_p, mode_pf = self.state.resonant_mode
            return max(abs(mode_pf), 1) * base
        return base

    def loop_cycle_time(self) -> float:
        return self.cycle_time()
