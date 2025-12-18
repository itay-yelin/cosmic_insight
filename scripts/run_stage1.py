from cosmic_insight.cli import main

if __name__ == "__main__":
    raise SystemExit(
        main(["--stage", "1", "--input", "data/sample_stage1.json", "--out", "out/stage1_out.json"])
    )
