from __future__ import annotations

import argparse

from .io_json import load_json, save_json
from .pipeline import run_all, run_stage


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="CosmicInsight CLI")
    p.add_argument("--stage", required=True, choices=["1", "2", "3", "all"])
    p.add_argument(
        "--input", required=True, help="Input JSON file path (or data dir for --stage all)"
    )
    p.add_argument(
        "--out", required=True, help="Output JSON file path (or output dir for --stage all)"
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.stage == "all":
        run_all(args.input, args.out)
        return 0

    payload = load_json(args.input)
    result = run_stage(args.stage, payload)
    save_json(args.out, result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
