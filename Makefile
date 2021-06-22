.PHONY: tests

set_tests:
	mkdir --parents tests/baseline
	pytest --mpl-generate-path tests/baseline/

tests:
	pytest