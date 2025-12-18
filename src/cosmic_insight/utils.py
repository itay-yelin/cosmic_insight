from __future__ import annotations


def clamp(x: float, lo: float, hi: float) -> float:
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


def moving_average(values: list[float], window: int) -> list[float]:
    if window <= 0:
        raise ValueError("window must be positive")
    if not values:
        return []

    out: list[float] = []
    half = window // 2

    for i in range(len(values)):
        start = max(0, i - half)
        end = min(len(values), i + half + 1)
        out.append(sum(values[start:end]) / float(end - start))
    return out
