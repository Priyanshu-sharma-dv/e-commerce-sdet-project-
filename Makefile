.PHONY: install test smoke regression coverage lint typecheck all

install:
	python -m pip install -r requirements.txt
	playwright install chromium

test:
	pytest -v

smoke:
	pytest -m smoke -v

regression:
	pytest -m regression -n auto -v

coverage:
	pytest --cov=app --cov=api_clients --cov=database --cov-report=term-missing --cov-report=xml -v

lint:
	ruff check .

typecheck:
	pyright

all: lint typecheck coverage
