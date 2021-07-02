.PHONY: clean install tests tests_setup

clean:
	rm --force --recursive .pytest_cache
	rm --force --recursive tests/baseline
	rm --force --recursive **/__pycache__

install:
	pip install . --upgrade

tests_setup: install
	mkdir --parents tests/baseline
	pytest --mpl-generate-path tests/baseline/

tests: install
	pytest --mpl