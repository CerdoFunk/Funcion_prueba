.PHONY: tests

install:
	pip install .

set_tests: install
	mkdir --parents tests/baseline
	pytest --mpl-generate-path tests/baseline/

tests:
	pytest