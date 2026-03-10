from __future__ import annotations

from torus_cycle_renderer.particles import Electron, Photon, WPlus, WMinus, ZBoson, UQuark, DQuark, Gluon, AbstractParticle


PARTICLES = {
    "electron": Electron,
    "photon": Photon,
    "wplus": WPlus,
    "w+": WPlus,
    "wminus": WMinus,
    "w-": WMinus,
    "zboson": ZBoson,
    "z0": ZBoson,
    "z": ZBoson,
    "uquark": UQuark,
    "u": UQuark,
    "dquark": DQuark,
    "d": DQuark,
    "gluon": Gluon,
    "g": Gluon,
}


def build_scene(name: str, spin_state: str = "++", loop_anchor_mode: str = "evolving") -> AbstractParticle:
    key = name.strip().lower()
    if key not in PARTICLES:
        raise ValueError(f"Unknown particle '{name}'. Available: {', '.join(PARTICLES)}")

    cls = PARTICLES[key]
    if key == "electron":
        return cls(spin_state=spin_state, loop_anchor_mode=loop_anchor_mode)
    return cls()
