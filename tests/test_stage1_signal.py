from cosmic_insight.stage1_signal import process_stage1
from cosmic_insight.types import Stage1Input


def test_stage1_has_expected_keys() -> None:
    payload = Stage1Input(
        user_id="U1",
        mood_samples=[0.4, 0.9, 0.2, 0.7, 0.3],
        timestamps=[1, 2, 3, 4, 5],
    )
    out = process_stage1(payload)
    assert out.smoothed is not None
    assert out.change_points is not None
    assert len(out.smoothed) == len(payload.mood_samples)
