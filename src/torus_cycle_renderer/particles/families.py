from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum

import numpy as np

from .base import AbstractParticle, ParticleParams
from torus_cycle_renderer.math.steady_state import solve_steady_state, wrapped_phase_distance


class PolicyViolation(ValueError):
    """Raised when particle-family policy constraints are violated."""


class SpinState(str, Enum):
    PP = "++"
    PM = "+-"
    MP = "-+"
    MM = "--"


SPIN_PHASE_TARGET = {
    SpinState.PP: 0.0,
    SpinState.PM: 0.5 * np.pi,
    SpinState.MP: -0.5 * np.pi,
    SpinState.MM: np.pi,
}


@dataclass(frozen=True)
class SolverConfig:
    mode_index: int = 0
    nu: int = 72
    nv: int = 56


class ParticleFamily(AbstractParticle):
    family: str = "particle"

    def validate_policy(self, stage: str = "pre") -> None:
        p = self.params
        if p.major_radius <= 0 or p.minor_radius <= 0:
            raise PolicyViolation(f"{self.family}: radii must be > 0")
        if p.deform_amp < 0:
            raise PolicyViolation(f"{self.family}: deform_amp must be >= 0")


class FermionParticle(ParticleFamily):
    family = "fermion"
    # Conservative default: require nontrivial fermic content, but avoid over-constraining
    # before full calibration locks are implemented.
    pf_ratio_min: float = 0.01

    def validate_policy(self, stage: str = "pre") -> None:
        super().validate_policy(stage=stage)

        spin_state = getattr(self, "spin_state", None)
        if spin_state is None:
            raise PolicyViolation("fermion: spin_state must be set")

        winding = getattr(self, "winding", None)
        if winding is None:
            raise PolicyViolation("fermion: winding sector (n_f, n_b) must be defined")

        n_f, n_b = winding
        if not (isinstance(n_f, int) and isinstance(n_b, int)):
            raise PolicyViolation("fermion: winding values must be integers")


class BosonParticle(ParticleFamily):
    family = "boson"

    def validate_policy(self, stage: str = "pre") -> None:
        super().validate_policy(stage=stage)


class WeakBosonParticle(BosonParticle):
    family = "weak-boson"

    def validate_policy(self, stage: str = "pre") -> None:
        super().validate_policy(stage=stage)
        coupling = self.params.resonance_coupling
        if not (0.0 <= coupling <= 1.0):
            raise PolicyViolation("weak-boson: resonance_coupling must be in [0, 1]")


class SolverBackedParticle(ParticleFamily):
    def __init__(self, spin_state: str = "++", solver: SolverConfig | None = None):
        self.spin_state = SpinState(spin_state)
        self.solver = solver or SolverConfig()
        self._steady = None

    @property
    @abstractmethod
    def winding(self) -> tuple[int, int]:
        ...

    @property
    def mode_index(self) -> int:
        return self.solver.mode_index

    def _channel_intensities(self, mode: np.ndarray) -> tuple[float, float]:
        p = self.params
        n_f, n_b = self.winding

        du = 2 * np.pi / mode.shape[1]
        dv = 2 * np.pi / mode.shape[0]

        d_u = (np.roll(mode, -1, axis=1) - np.roll(mode, 1, axis=1)) / (2.0 * du)
        d_v = (np.roll(mode, -1, axis=0) - np.roll(mode, 1, axis=0)) / (2.0 * dv)

        D_f_mode = d_u + 1j * n_f * mode
        D_b_mode = d_v + 1j * n_b * mode

        i_f = float(np.mean((np.abs(D_f_mode) ** 2) / (p.major_radius**2)))
        i_b = float(np.mean((np.abs(D_b_mode) ** 2) / (p.minor_radius**2)))
        return i_f, i_b

    def _validate_solver_solution(self) -> None:
        steady = self._steady
        if steady is None:
            raise PolicyViolation("solver-backed: steady solution missing")

        i_f, i_b = self._channel_intensities(steady.mode)

        if isinstance(self, FermionParticle):
            total = i_f + i_b + 1e-12
            pf_ratio = i_f / total
            if pf_ratio < self.pf_ratio_min:
                raise PolicyViolation(
                    f"fermion: p_f dominance failed (ratio={pf_ratio:.3f} < {self.pf_ratio_min:.3f})"
                )

    def _ensure_solution(self) -> None:
        if self._steady is not None:
            return

        self.validate_policy(stage="pre-solve")

        p = self.params
        n_f, n_b = self.winding
        self._steady = solve_steady_state(
            n_f=n_f,
            n_b=n_b,
            r_f=p.major_radius,
            r_b=p.minor_radius,
            c_int=1.0,
            omega0=1.0,
            nu=self.solver.nu,
            nv=self.solver.nv,
            mode_index=self.mode_index,
        )

        self._validate_solver_solution()
        self.validate_policy(stage="post-solve")

    def _sample_mode(self, u: np.ndarray, v: np.ndarray) -> np.ndarray:
        self._ensure_solution()
        steady = self._steady
        assert steady is not None

        nu = len(steady.u_axis)
        nv = len(steady.v_axis)
        iu = np.mod((u / (2 * np.pi) * nu).astype(int), nu)
        iv = np.mod((v / (2 * np.pi) * nv).astype(int), nv)
        return steady.mode[iv, iu]

    def deformation(self, u: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        p = self.params
        self._ensure_solution()
        steady = self._steady
        assert steady is not None

        t_eff = t * p.visual_time_scale
        sampled = self._sample_mode(u, v)
        field_t = np.real(sampled * np.exp(-1j * steady.omega * t_eff))
        norm = np.max(np.abs(field_t)) + 1e-12
        return p.deform_amp * (field_t / norm)

    def resonant_loop(self, t: float, points: int = 900) -> tuple[np.ndarray, np.ndarray]:
        self._ensure_solution()
        steady = self._steady
        assert steady is not None

        p = self.params
        t_eff = t * p.visual_time_scale
        phase = np.angle(steady.mode * np.exp(-1j * steady.omega * t_eff))
        target = SPIN_PHASE_TARGET[self.spin_state]

        u = np.linspace(0.0, 2 * np.pi, points, endpoint=False)
        iu = np.mod((u / (2 * np.pi) * len(steady.u_axis)).astype(int), len(steady.u_axis))

        nv = len(steady.v_axis)
        penalty_weight = 0.20  # continuity regularizer to avoid jagged loop jumps
        v = np.empty_like(u)
        prev_iv: int | None = None

        idx = np.arange(nv)
        for j, iu_j in enumerate(iu):
            col = phase[:, iu_j]
            base_cost = wrapped_phase_distance(col, target)
            if prev_iv is None:
                iv = int(np.argmin(base_cost))
            else:
                cyclic_dist = np.minimum(np.abs(idx - prev_iv), nv - np.abs(idx - prev_iv)) / max(nv, 1)
                cost = base_cost + penalty_weight * cyclic_dist
                iv = int(np.argmin(cost))
            v[j] = steady.v_axis[iv]
            prev_iv = iv

        return u, v
