from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

from .io_json import load_model, save_json
from .stage1_signal import process_stage1
from .stage2_angles import process_stage2
from .stage3_correlation import process_stage3
from .types import Stage1Input, Stage2Input, Stage3Input

StageName = Literal["1", "2", "3", "all"]


def run_stage(stage: StageName, payload: Any) -> Any:
    if stage == "1":
        return process_stage1(payload)
    if stage == "2":
        return process_stage2(payload)
    if stage == "3":
        return process_stage3(payload)
    raise ValueError(f"Unknown stage: {stage}")


def run_all(input_dir: str | Path, out_dir: str | Path) -> None:
    in_dir = Path(input_dir)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    stage1 = load_model(in_dir / "sample_stage1.json", Stage1Input)
    stage2 = load_model(in_dir / "sample_stage2.json", Stage2Input)
    stage3 = load_model(in_dir / "sample_stage3.json", Stage3Input)

    save_json(out / "stage1_out.json", process_stage1(stage1))
    save_json(out / "stage2_out.json", process_stage2(stage2))
    save_json(out / "stage3_out.json", process_stage3(stage3))
