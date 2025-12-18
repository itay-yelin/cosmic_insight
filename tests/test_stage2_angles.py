from cosmic_insight.stage2_angles import process_stage2


def test_stage2_returns_matches_list() -> None:
    payload = {
        "user_angles": {"Mars": 120.0},
        "events": [{"time": 1, "planets": ["Mars", "Jupiter"], "target_angle": 125.0}],
    }
    out = process_stage2(payload)  # type: ignore[arg-type]
    assert "matches" in out
    assert isinstance(out["matches"], list)
    assert len(out["matches"]) == 1
