from cosmic_insight.cli import main

if __name__ == "__main__":
    raise SystemExit(
        main(["--stage", "3", "--input", "data/sample_stage3.json", "--out", "out/stage3_out.json"])
    )
