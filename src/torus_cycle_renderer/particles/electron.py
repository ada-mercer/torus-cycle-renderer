from __future__ import annotations

from .base import AbstractParticle, ParticleParams


class Electron(AbstractParticle):
    @property
    def name(self) -> str:
        return "electron"

    @property
    def params(self) -> ParticleParams:
        return ParticleParams(
            major_radius=2.1,
            minor_radius=0.72,
            deform_amp=0.12,
            deform_mode_u=2,
            deform_mode_v=3,
            loop_turn_u=3,
            loop_turn_v=5,
            phase_speed=1.4,
            color="#3a86ff",
            loop_color="#ff006e",
        )
