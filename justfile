@_default:
    just --list --unsorted

# Run Python code styler.
style-python:
  poetry run black .

# Install Python package dependencies, as well as the package itself.
install:
  poetry install

# Check to validate the `poetry.lock` file with the `pyproject.toml` file.
check:
  poetry check
