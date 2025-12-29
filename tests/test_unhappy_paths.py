import pytest
from pydantic import ValidationError

from cosmic_insight.stage1_signal import process_stage1
from cosmic_insight.stage3_correlation import process_stage3
from cosmic_insight.types import Stage1Input, Stage3Input


def test_stage1_empty_mood_samples() -> None:
    # Logic should handle empty list gracefully or raise logic error, 
    # but Pydantic allows empty list unless constrained.
    # Check if logic crashes.
    payload = Stage1Input(user_id="U1", mood_samples=[], timestamps=[])
    # utils.moving_average might crash or return empty.
    # Let's see behavior. logic says: for i in range(1, len(smoothed))...
    # If empty, loop doesn't run. Returns empty structures.
    out = process_stage1(payload)
    assert out.smoothed == []
    assert out.change_points == []


def test_stage3_mismatched_dimensions() -> None:
    # mood and angles must have same number of rows.
    payload = Stage3Input(
        mood_data=[[1.0], [2.0]],  # 2 rows
        event_angles=[[10.0], [20.0], [30.0]],  # 3 rows
    )
    with pytest.raises(ValueError, match="mood and angles must have the same number of rows"):
        process_stage3(payload)


def test_invalid_types_validation_error() -> None:
    # Pydantic validation error when types are wrong at model creation.
    with pytest.raises(ValidationError):
        Stage1Input(
            user_id="U1",
            mood_samples=["not-a-float"],  # type: ignore
            timestamps=[1, 2],
        )

def test_stage3_invalid_dims_in_array() -> None:
    # Check 1D array passed as 2D? Pydantic expects list[list[float]].
    # If we pass list[float], it might fail validation or become list containing floats, 
    # which fails 'list[list[float]]' check?
    # Actually Pydantic v2 might coerce.
    # But stage3 logic checks ndim != 2.
    
    # If we pass empty list of lists?
    payload = Stage3Input(mood_data=[], event_angles=[])
    # np.asarray([]) -> ndim=1 check?
    with pytest.raises(ValueError, match="mood and angles must be 2D arrays"):
         process_stage3(payload)
