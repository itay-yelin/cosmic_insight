from cosmic_insight.stage2_angles import process_stage2
from cosmic_insight.types import Event, Stage2Input


def test_stage2_returns_matches_list() -> None:
    payload = Stage2Input(
        user_angles={"Mars": 120.0},
        events=[Event(time=1, planets=["Mars", "Jupiter"], target_angle=125.0)],
    )
    out = process_stage2(payload)
    assert out.matches is not None
    assert isinstance(out.matches, list)
    assert len(out.matches) == 1
