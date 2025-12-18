from cosmic_insight.stage1_signal import process_stage1


def test_stage1_has_expected_keys() -> None:
    payload = {
        "user_id": "U1",
        "mood_samples": [0.4, 0.9, 0.2, 0.7, 0.3],
        "timestamps": [1, 2, 3, 4, 5],
    }
    out = process_stage1(payload)  # type: ignore[arg-type]
    assert "smoothed" in out
    assert "change_points" in out
    assert len(out["smoothed"]) == len(payload["mood_samples"])
