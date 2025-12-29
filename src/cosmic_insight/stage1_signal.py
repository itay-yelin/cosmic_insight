from __future__ import annotations

from .config import Stage1Config
from .types import Stage1Input, Stage1Output
from .utils import moving_average


def smooth_signal(mood_samples: list[float], window: int = 3) -> list[float]:
    return moving_average(mood_samples, window=window)


def detect_change_points(smoothed: list[float], threshold: float) -> list[int]:
    change_points: list[int] = []
    for i in range(1, len(smoothed)):
        if abs(smoothed[i] - smoothed[i - 1]) > threshold:
            change_points.append(i)
    return change_points



def process_stage1(payload: Stage1Input, cfg: Stage1Config | None = None) -> Stage1Output:
    cfg = cfg or Stage1Config()
    smoothed = smooth_signal(payload.mood_samples, window=cfg.window)
    change_points = detect_change_points(smoothed, threshold=cfg.change_threshold)
    return Stage1Output(smoothed=[round(x, 3) for x in smoothed], change_points=change_points)
