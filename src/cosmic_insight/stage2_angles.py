from __future__ import annotations

from .config import Stage2Config
from .types import Event, Match, Stage2Input, Stage2Output
from .utils import clamp


def score_match(delta_deg: float, tolerance_deg: float) -> float:
    # Linear score: 1.0 at perfect match, 0.0 at tolerance boundary.
    if delta_deg >= tolerance_deg:
        return 0.0
    score = 1.0 - (delta_deg / tolerance_deg)
    return float(clamp(score, 0.0, 1.0))


def match_events(
    user_angles: dict[str, float],
    events: list[Event],
    tolerance_deg: float,
) -> list[Match]:
    matches: list[Match] = []

    for e in events:
        for p in e["planets"]:
            if p not in user_angles:
                continue

            delta = abs(user_angles[p] - e["target_angle"])
            if delta <= tolerance_deg:
                matches.append(
                    {
                        "time": int(e["time"]),
                        "planets": list(e["planets"]),
                        "score": round(score_match(delta, tolerance_deg), 3),
                    }
                )
                break

    return matches


def process_stage2(payload: Stage2Input, cfg: Stage2Config | None = None) -> Stage2Output:
    cfg = cfg or Stage2Config()
    matches = match_events(
        payload["user_angles"], payload["events"], tolerance_deg=cfg.tolerance_deg
    )
    return {"matches": matches}
