all: check coverage mutants

repo = distdens
codecov_token = eae768b1-8c32-40a8-89fd-6b7589f9efa8

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

.PHONY: \
	all \
	check \
	clean \
	coverage \
	format \
	install \
	linter \
	mutants \
	tests

check:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 setup.py
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 setup.py
	flake8 --max-line-length 100 tests

clean:
	rm --force .mutmut-cache
	rm --recursive --force ${repo}.egg-info
	rm --recursive --force ${repo}/__pycache__
	rm --recursive --force test/__pycache__

coverage: install
	pytest --cov=${repo} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length 100 ${repo}
	black --line-length 100 tests
	black --line-length 100 setup.py

install:
	pip install --editable .

linter:
	$(call lint, ${repo})
	$(call lint, tests)

mutants: install
	mutmut run --paths-to-mutate ${repo}

tests: install
	pytest --verbose
