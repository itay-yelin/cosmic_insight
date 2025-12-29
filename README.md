# CosmicInsight - Skeleton

This repository contains a minimal, production-style Python project layout for the CosmicInsight take-home task.

## Quickstart

### 1) Create venv and install
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

python -m pip install -U pip
pip install -e .[dev]
```

### 2) Run tests
```bash
pytest -q
```

### 3) Run stages from CLI
```bash
python -m cosmic_insight.cli --stage 1 --input data/sample_stage1.json --out out/stage1_out.json
python -m cosmic_insight.cli --stage 2 --input data/sample_stage2.json --out out/stage2_out.json
python -m cosmic_insight.cli --stage 3 --input data/sample_stage3.json --out out/stage3_out.json
```

## Developer tools

```bash
make fmt
make lint
make type
make test
```

## Assumptions
- Mood samples are normalized to [0,1]
- Timestamps are monotonic
- Angle units are degrees