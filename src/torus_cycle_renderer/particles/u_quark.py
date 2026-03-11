from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from .base import ParticleParams
from .families import SpinState
from .quark import Quark


@dataclass(frozen=True)
class UQuarkState:
    """Prototype up-quark correspondence state.

    This model is intentionally marked as foundation/prototype:
    it encodes a closure-defect + weak-assist hypothesis for investigating
    quark-like resonance locking in the renderer.
    """

    spin_state: SpinState = SpinState.PP
    # Color-phase branch (0, 2π/3, 4π/3 in simple cycle model).
    # Renderer interpretation: this is a color/coherence modifier, not a standalone EM-sign label.
    color_phase: float = 0.0
    resonant_mode: tuple[int, int] = (1, 3)
    secondary_mode: tuple[int, int] = (2, 2)
    transport_winding: tuple[int, int] = (4, 3)
    phase_speed: float = 1.9
    major_radius: float = 2.0
    minor_radius: float = 0.62
    deform_amp: float = 0.105
    mixing_angle: float = 0.52
    mass_gap: float = 1.0
    # Fractional closure-defect hypothesis (up-like branch).
    closure_defect: float = 1.0 / 3.0
    # Weak-assist phase compensation per coupled weak cycle.
    weak_assist_phase: float = 2.0 / 3.0
    # If true, move loop reference along fermic/minor direction over one cycle.
    pf_orbit_relative: bool = False


class UQuark(Quark):
    """Prototype up-quark correspondence particle.

    Foundation assumptions:
    - quark branch carries a fractional closure-defect phase,
    - weak-channel cycles can compensate defect in low-order resonances,
    - current spin-state handling remains an observable/probe-level handedness choice,
      not a full quark sign ontology.
    """

    def __init__(self, state: UQuarkState | None = None):
        base = state or UQuarkState()
        self.state = UQuarkState(
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
            pf_orbit_relative=bool(base.pf_orbit_relative),
        )
        self.spin_state = self.state.spin_state
        self.validate_policy(stage="init")

    @property
    def name(self) -> str:
        m1u, m1v = self.state.resonant_mode
        return f"u-quark[{self.spin_state.value}] mode=({m1u},{m1v})"

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
            resonance_coupling=0.38,
            resonance_detuning=0.06,
            loop_lift=0.08,
            fermic_cycles=2,
        )

    def secondary_phase_offset(self) -> float:
        return 0.45

    def texture_terms(self, phi1: np.ndarray, phi2: np.ndarray) -> np.ndarray:
        return 0.16 * np.sin(2.0 * phi1) + 0.12 * np.cos(2.0 * phi2)
