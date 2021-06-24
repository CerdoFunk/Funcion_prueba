.PHONY: clean install tests tests_setup

clean:
	rm --force --recursive tests/baseline
	rm --force --recursive tests/__pycache__

install:
	pip install .

tests_setup: install
	mkdir --parents tests/baseline
	pytest --mpl-generate-path tests/baseline/

tests: 
	pytest --mpl