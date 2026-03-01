from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum

import numpy as np

from .base import AbstractParticle, ParticleParams
from torus_cycle_renderer.math.steady_state import solve_steady_state, wrapped_phase_distance


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


class FermionParticle(ParticleFamily):
    family = "fermion"


class BosonParticle(ParticleFamily):
    family = "boson"


class WeakBosonParticle(BosonParticle):
    family = "weak-boson"


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

    def _ensure_solution(self) -> None:
        if self._steady is not None:
            return
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

        sampled = self._sample_mode(u, v)
        field_t = np.real(sampled * np.exp(-1j * steady.omega * t))
        norm = np.max(np.abs(field_t)) + 1e-12
        return p.deform_amp * (field_t / norm)

    def resonant_loop(self, t: float, points: int = 900) -> tuple[np.ndarray, np.ndarray]:
        self._ensure_solution()
        steady = self._steady
        assert steady is not None

        phase = np.angle(steady.mode * np.exp(-1j * steady.omega * t))
        target = SPIN_PHASE_TARGET[self.spin_state]

        u = np.linspace(0.0, 2 * np.pi, points, endpoint=False)
        iu = np.mod((u / (2 * np.pi) * len(steady.u_axis)).astype(int), len(steady.u_axis))

        v = np.empty_like(u)
        for j, iu_j in enumerate(iu):
            col = phase[:, iu_j]
            iv = int(np.argmin(wrapped_phase_distance(col, target)))
            v[j] = steady.v_axis[iv]
        return u, v
