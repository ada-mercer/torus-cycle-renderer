from __future__ import annotations

from .base import AbstractParticle, ParticleParams
from .families import BosonParticle


class Photon(BosonParticle, AbstractParticle):
    @property
    def name(self) -> str:
        return "photon"

    @property
    def params(self) -> ParticleParams:
        return ParticleParams(
            major_radius=2.0,
            minor_radius=0.58,
            deform_amp=0.09,
            deform_mode_u=1,
            deform_mode_v=4,
            loop_turn_u=4,
            loop_turn_v=4,
            phase_speed=2.4,
            color="#ffd166",
            loop_color="#ef476f",
        )
