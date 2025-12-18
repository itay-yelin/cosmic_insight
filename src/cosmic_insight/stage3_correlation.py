from __future__ import annotations

import numpy as np
from scipy.stats import pearsonr

from .config import Stage3Config
from .types import Stage3Input, Stage3Output


def strongest_correlation(mood: np.ndarray, angles: np.ndarray) -> tuple[int, int, float, float]:
    if mood.ndim != 2 or angles.ndim != 2:
        raise ValueError("mood and angles must be 2D arrays")
    if mood.shape[0] != angles.shape[0]:
        raise ValueError("mood and angles must have the same number of rows (samples)")

    best_i = 0
    best_j = 0
    best_corr = 0.0
    best_p = 1.0

    for i in range(mood.shape[1]):
        for j in range(angles.shape[1]):
            corr, p = pearsonr(mood[:, i], angles[:, j])
            if abs(corr) > abs(best_corr):
                best_i, best_j, best_corr, best_p = int(i), int(j), float(corr), float(p)

    return best_i, best_j, best_corr, best_p


def process_stage3(payload: Stage3Input, cfg: Stage3Config | None = None) -> Stage3Output:
    _ = cfg or Stage3Config()
    mood = np.asarray(payload["mood_data"], dtype=float)
    angles = np.asarray(payload["event_angles"], dtype=float)
    i, j, corr, p = strongest_correlation(mood, angles)
    return {
        "strongest_link": {
            "mood_column": i,
            "angle_column": j,
            "correlation": round(corr, 3),
            "p_value": round(p, 6),
        }
    }
