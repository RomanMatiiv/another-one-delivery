ruff-check:
	ruff check . --select ALL --config pyproject.toml

ruff-fix:
	ruff . --select ALL --config pyproject.toml --fix

mypy-check:
	mypy . --config-file pyproject.toml

lint: ruff-check mypy-check

lint-fix: ruff-fix

test:
	pytest -cov -v -o log_cli=true
