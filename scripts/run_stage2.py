from cosmic_insight.cli import main

if __name__ == "__main__":
    raise SystemExit(
        main(["--stage", "2", "--input", "data/sample_stage2.json", "--out", "out/stage2_out.json"])
    )
