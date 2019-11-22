.PHONY: clean mutation tests

clean:
	rm --recursive $$(find . -name "__pycache__")

mutation:
	mutmut run --paths-to-mutate distdens

tests:
	pytest --cov=distdens --cov-report=term --verbose
