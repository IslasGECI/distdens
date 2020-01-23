.PHONY: clean mutation tests

mutation:
	mutmut run --paths-to-mutate distdens

tests:
	pytest --cov=distdens --cov-report=term --verbose

clean:
	rm --force --recursive $$(find . -name "__pycache__")
	rm --force .mutmut-cache
