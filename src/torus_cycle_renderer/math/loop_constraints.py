from __future__ import annotations

from fractions import Fraction
import math
import numpy as np


def loop_length_estimate(
    k_u: int,
    k_v: int,
    major_radius: float,
    minor_radius: float,
    *,
    samples: int = 720,
) -> float:
    """Numerical estimate of carrier-loop length for integer windings.

    For
      u(s)=u0+2πk_u s,
      v(s)=v0+2πk_v s,
    on an undeformed torus, speed is
      |dX/ds| = 2π*sqrt(k_u^2 (R+r cos v)^2 + (r k_v)^2).

    Over one closed cycle this yields the integral below (independent of u0, v0).
    """
    R = float(major_radius)
    r = float(minor_radius)
    if k_v == 0:
        return 2.0 * math.pi * abs(k_u) * (R + r)

    theta = np.linspace(0.0, 2.0 * np.pi, max(24, int(samples)), endpoint=True)
    integrand = np.sqrt((k_u * (R + r * np.cos(theta))) ** 2 + (r * k_v) ** 2)
    return float(np.trapezoid(integrand, theta))


def tangent_winding_from_channels(
    p_value: float,
    pf_value: float,
    *,
    max_denom: int = 12,
    major_radius: float | None = None,
    minor_radius: float | None = None,
    max_turn: int = 4,
    rel_ratio_tol: float = 0.18,
    min_k_v: int = 1,
) -> tuple[int, int]:
    """Return short closed winding close to du/dv=p/p_f, favoring cleaner loops."""
    p_mag = max(abs(float(p_value)), 1e-12)
    pf_mag = abs(float(pf_value))

    if pf_mag < 1e-12:
        return (1, 0)

    target = p_mag / pf_mag

    # Prefer short loops if a close low-order ratio exists.
    R = float(major_radius) if major_radius is not None else 2.0
    r = float(minor_radius) if minor_radius is not None else 0.62
    candidates: list[tuple[float, float, int, int]] = []
    kv_min = max(1, int(min_k_v))
    for k_u in range(1, max(2, int(max_turn)) + 1):
        for k_v in range(kv_min, max(2, int(max_turn)) + 1):
            ratio = k_u / k_v
            rel_err = abs(ratio - target) / max(target, 1e-12)
            if rel_err <= rel_ratio_tol:
                L = loop_length_estimate(k_u, k_v, R, r, samples=360)
                candidates.append((L, rel_err, k_u, k_v))

    if candidates:
        candidates.sort(key=lambda x: (x[0], x[1]))
        _, _, k_u, k_v = candidates[0]
        return (int(k_u), int(k_v))

    frac = Fraction(target).limit_denominator(max(1, int(max_denom)))
    k_u = max(1, int(frac.numerator))
    k_v = max(1, int(frac.denominator))
    return (k_u, k_v)


def phase_locked_tangent_loop(
    *,
    points: int,
    t: float,
    omega: float,
    coeff_u: float,
    coeff_v: float,
    phase_offset: float,
    p_value: float,
    pf_value: float,
    major_radius: float = 2.0,
    minor_radius: float = 0.62,
    min_fermic_cycles: int = 1,
    sign_u: int = +1,
    sign_v: int = +1,
    u_start: float = 0.0,
    max_denom: int = 12,
) -> tuple[np.ndarray, np.ndarray]:
    """Build a loop that is (1) closed, (2) channel-tangent, (3) phase-anchored.

    Loop equations:
      u(s) = u0 + 2π sign_u k_u s
      v(s) = v0 + 2π sign_v k_v s

    with k_u:k_v chosen from p:p_f to enforce tangency to
      M_vec = p_f e_v + p e_u
    on the torus carrier surface.

    Start point is phase-locked to
      coeff_u*u + coeff_v*v - omega*t + phase_offset = 0
    whenever coeff_v != 0; otherwise v0=0.
    """
    s = np.linspace(0.0, 1.0, points, endpoint=True)
    k_u, k_v = tangent_winding_from_channels(
        p_value,
        pf_value,
        max_denom=max_denom,
        major_radius=major_radius,
        minor_radius=minor_radius,
        min_k_v=min_fermic_cycles,
    )

    u0 = float(u_start)
    if abs(coeff_v) > 1e-12:
        v0 = (omega * t - phase_offset - coeff_u * u0) / coeff_v
    else:
        v0 = 0.0

    u = u0 + 2.0 * np.pi * int(np.sign(sign_u) or 1) * k_u * s
    if k_v == 0:
        v = np.full_like(s, v0)
    else:
        v = v0 + 2.0 * np.pi * int(np.sign(sign_v) or 1) * k_v * s
    return u, v
