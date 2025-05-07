.PHONY: test format lint install

install:
    pip install -r requirements.txt
    pre-commint install

test:
    PYTHONPATH=. pytest

format:
    ruff check . --fix

lint:
    ruff check .
