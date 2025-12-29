from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

from pydantic import BaseModel


class Stage1Input(BaseModel):
    user_id: str
    mood_samples: list[float]
    timestamps: list[int]


class Stage1Output(BaseModel):
    smoothed: list[float]
    change_points: list[int]


class Event(BaseModel):
    time: int
    planets: list[str]
    target_angle: float


class Stage2Input(BaseModel):
    user_angles: dict[str, float]
    events: list[Event]


class Match(BaseModel):
    time: int
    planets: list[str]
    score: float


class Stage2Output(BaseModel):
    matches: list[Match]


class Stage3Input(BaseModel):
    mood_data: list[list[float]]
    event_angles: list[list[float]]


class StrongestLink(BaseModel):
    mood_column: int
    angle_column: int
    correlation: float
    p_value: float


class Stage3Output(BaseModel):
    strongest_link: StrongestLink


@dataclass(frozen=True)
class PipelineResult:
    stage: Literal["1", "2", "3", "all"]
    payload: dict[str, Any]
