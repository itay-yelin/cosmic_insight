from __future__ import annotations

import json
from pathlib import Path
from typing import Any, TypeVar, cast

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def load_json(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)
        if not isinstance(data, dict):
            raise TypeError(f"Expected dict, got {type(data)}")
        return cast(dict[str, Any], data)


def load_model(path: str | Path, model: type[T]) -> T:
    p = Path(path)
    # pydantic's model_validate_json reads from string/bytes, not file object directly efficiently enough?
    # actually it takes str | bytes. Reading file content is fine.
    with p.open("r", encoding="utf-8") as f:
        # validate_json is safer ensuring we parse JSON correctly according to models
        return model.model_validate_json(f.read())


def save_json(path: str | Path, obj: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    
    if isinstance(obj, BaseModel):
        obj = obj.model_dump(mode="json")
        
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
