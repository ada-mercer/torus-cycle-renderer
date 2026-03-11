from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from .base import ParticleParams
from .families import SpinState
from .quark import Quark


@dataclass(frozen=True)
class DQuarkState:
    """Prototype down-quark correspondence state (foundation branch)."""

    spin_state: SpinState = SpinState.PP
    color_phase: float = 2.0 * math.pi / 3.0
    resonant_mode: tuple[int, int] = (1, 3)
    secondary_mode: tuple[int, int] = (3, 1)
    transport_winding: tuple[int, int] = (5, 3)
    phase_speed: float = 1.85
    major_radius: float = 2.0
    minor_radius: float = 0.62
    deform_amp: float = 0.108
    mixing_angle: float = 0.48
    mass_gap: float = 1.0
    # Down-like closure-defect hypothesis.
    closure_defect: float = 2.0 / 3.0
    # Weak-assist compensation per coupled weak cycle.
    weak_assist_phase: float = 1.0 / 3.0


class DQuark(Quark):
    """Prototype down-quark correspondence particle.

    Foundation assumptions:
    - down branch carries fractional closure-defect phase,
    - weak-channel cycles compensate defect in low-order resonance locks,
    - current spin-state handling remains an observable/probe-level handedness choice,
      not a full quark sign ontology.
    """

    def __init__(self, state: DQuarkState | None = None):
        base = state or DQuarkState()
        self.state = DQuarkState(
            spin_state=SpinState(base.spin_state),
            color_phase=float(base.color_phase),
            resonant_mode=base.resonant_mode,
            secondary_mode=base.secondary_mode,
            transport_winding=base.transport_winding,
            phase_speed=base.phase_speed,
            major_radius=base.major_radius,
            minor_radius=base.minor_radius,
            deform_amp=base.deform_amp,
            mixing_angle=float(base.mixing_angle),
            mass_gap=max(base.mass_gap, 1e-6),
            closure_defect=float(base.closure_defect),
            weak_assist_phase=float(base.weak_assist_phase),
        )
        self.spin_state = self.state.spin_state
        self.validate_policy(stage="init")

    @property
    def name(self) -> str:
        m1u, m1v = self.state.resonant_mode
        return f"d-quark[{self.spin_state.value}] mode=({m1u},{m1v})"

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
            pf_value=0.84,
            p_value=0.42,
            resonance_coupling=0.40,
            resonance_detuning=0.06,
            loop_lift=0.08,
            fermic_cycles=2,
        )

    def secondary_phase_offset(self) -> float:
        return 0.25

    def texture_terms(self, phi1: np.ndarray, phi2: np.ndarray) -> np.ndarray:
        return 0.15 * np.cos(2.0 * phi1) + 0.13 * np.sin(2.0 * phi2)
