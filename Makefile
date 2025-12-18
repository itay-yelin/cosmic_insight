.PHONY: fmt lint type test cov run1 run2 run3 runall clean

fmt:
	ruff format .

lint:
	ruff check .

type:
	mypy src

test:
	pytest

cov:
	pytest --cov=cosmic_insight --cov-report=term-missing

run1:
	python -m cosmic_insight.cli --stage 1 --input data/sample_stage1.json --out out/stage1_out.json

run2:
	python -m cosmic_insight.cli --stage 2 --input data/sample_stage2.json --out out/stage2_out.json

run3:
	python -m cosmic_insight.cli --stage 3 --input data/sample_stage3.json --out out/stage3_out.json

runall:
	python -m cosmic_insight.cli --stage all --input data --out out

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache dist build *.egg-info
