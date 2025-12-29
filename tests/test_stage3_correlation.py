from cosmic_insight.stage3_correlation import process_stage3
from cosmic_insight.types import Stage3Input


def test_stage3_returns_structure() -> None:
    payload = Stage3Input(
        mood_data=[[0.0, 1.0], [1.0, 0.0], [0.0, 1.0]],
        event_angles=[[0.0], [1.0], [0.0]],
    )
    out = process_stage3(payload)
    link = out.strongest_link
    assert isinstance(link.mood_column, int)
    assert isinstance(link.angle_column, int)
    assert isinstance(link.correlation, float)
    assert isinstance(link.p_value, float)
