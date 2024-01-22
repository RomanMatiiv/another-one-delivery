ruff-check:
	ruff check . --config pyproject.toml

ruff-fix:
	ruff . --config pyproject.toml --fix

mypy-check:
	mypy . --config-file pyproject.toml

lint: ruff-check mypy-check

lint-fix: ruff-fix