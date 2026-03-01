from __future__ import annotations

from torus_cycle_renderer.particles import Electron, Photon, AbstractParticle


PARTICLES = {
    "electron": Electron,
    "photon": Photon,
}


def build_scene(name: str, spin_state: str = "++") -> AbstractParticle:
    key = name.strip().lower()
    if key not in PARTICLES:
        raise ValueError(f"Unknown particle '{name}'. Available: {', '.join(PARTICLES)}")

    cls = PARTICLES[key]
    if key == "electron":
        return cls(spin_state=spin_state)
    return cls()
