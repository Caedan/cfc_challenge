install:
	poetry install

tests:
	poetry run pytest

format:
	poetry run black ./src ./tests

lint:
	poetry run ./bin/lint.sh