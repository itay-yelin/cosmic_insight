from cosmic_insight.pipeline import run_stage


def test_run_stage_dispatch() -> None:
    stage1_payload = {"user_id": "U1", "mood_samples": [0.1, 0.2], "timestamps": [1, 2]}
    out = run_stage("1", stage1_payload)
    assert "smoothed" in out
