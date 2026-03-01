from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy.sparse import diags, eye, kron, csc_matrix
from scipy.sparse.linalg import eigs


@dataclass(frozen=True)
class SteadyStateSolution:
    u_axis: np.ndarray
    v_axis: np.ndarray
    mode: np.ndarray  # shape (Nv, Nu), complex
    omega: float


def _d1_periodic(n: int, h: float) -> csc_matrix:
    data = [
        -0.5 * np.ones(n),
        0.5 * np.ones(n),
        np.array([-0.5]),
        np.array([0.5]),
    ]
    offsets = [-1, 1, n - 1, -(n - 1)]
    return diags(data, offsets, shape=(n, n), format="csc") / h


def solve_steady_state(
    n_f: int,
    n_b: int,
    r_f: float,
    r_b: float,
    c_int: float,
    omega0: float,
    nu: int = 72,
    nv: int = 56,
    mode_index: int = 0,
) -> SteadyStateSolution:
    """Numerically solve H psi = omega^2 psi for torus internal operator."""
    u_axis = np.linspace(0.0, 2 * np.pi, nu, endpoint=False)
    v_axis = np.linspace(0.0, 2 * np.pi, nv, endpoint=False)
    du = 2 * np.pi / nu
    dv = 2 * np.pi / nv

    Iu = eye(nu, format="csc", dtype=complex)
    Iv = eye(nv, format="csc", dtype=complex)

    Du0 = _d1_periodic(nu, du).astype(complex)
    Dv0 = _d1_periodic(nv, dv).astype(complex)

    Du = Du0 + 1j * n_f * Iu
    Dv = Dv0 + 1j * n_b * Iv

    Duu = Du @ Du
    Dvv = Dv @ Dv

    Delta_n = kron(Iv, Duu, format="csc") / (r_f**2) + kron(Dvv, Iu, format="csc") / (r_b**2)
    H = (-c_int**2) * Delta_n + (omega0**2) * eye(nu * nv, format="csc", dtype=complex)

    k = max(6, mode_index + 3)
    vals, vecs = eigs(H, k=k, which="SR")
    order = np.argsort(vals.real)
    eigval = float(vals.real[order[mode_index]])
    vec = vecs[:, order[mode_index]]

    mode = vec.reshape((nv, nu))
    mode /= np.max(np.abs(mode)) + 1e-12

    omega = float(np.sqrt(max(eigval, 1e-12)))
    return SteadyStateSolution(u_axis=u_axis, v_axis=v_axis, mode=mode, omega=omega)


def wrapped_phase_distance(phi: np.ndarray, target: float) -> np.ndarray:
    return np.abs(np.angle(np.exp(1j * (phi - target))))
