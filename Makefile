.PHONY: tests

install:
	pip install .

tests/baseline/test_funcion_juego.png: install
	mkdir --parents tests/baseline
	pytest --mpl-generate-path tests/baseline/

tests: set_tests
	pytest