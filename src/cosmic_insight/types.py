from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal, TypedDict


class Stage1Input(TypedDict):
    user_id: str
    mood_samples: list[float]
    timestamps: list[int]


class Stage1Output(TypedDict):
    smoothed: list[float]
    change_points: list[int]


class Event(TypedDict):
    time: int
    planets: list[str]
    target_angle: float


class Stage2Input(TypedDict):
    user_angles: dict[str, float]
    events: list[Event]


class Match(TypedDict):
    time: int
    planets: list[str]
    score: float


class Stage2Output(TypedDict):
    matches: list[Match]


class Stage3Input(TypedDict):
    mood_data: list[list[float]]
    event_angles: list[list[float]]


class StrongestLink(TypedDict):
    mood_column: int
    angle_column: int
    correlation: float
    p_value: float


class Stage3Output(TypedDict):
    strongest_link: StrongestLink


@dataclass(frozen=True)
class PipelineResult:
    stage: Literal["1", "2", "3", "all"]
    payload: dict[str, Any]
