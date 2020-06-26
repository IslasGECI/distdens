mutants:
	mutmut run --paths-to-mutate distdens 

.PHONY: clean mutants tests

tests:
	pytest --cov=distdens --cov-report=term --verbose

clean:
	rm --force --recursive $$(find . -name "__pycache__")
	rm --force --recursive .pytest_cache
	rm --force .mutmut-cache
