from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stage1Config:
    window: int = 3
    change_threshold: float = 0.15


@dataclass(frozen=True)
class Stage2Config:
    tolerance_deg: float = 10.0


@dataclass(frozen=True)
class Stage3Config:
    # Placeholder for future options (e.g., Pearson vs Spearman).
    method: str = "pearson"
