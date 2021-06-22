.PHONY: clean install tests

clean:
	rm --force --recursive tests/baseline
	rm --force --recursive tests/__pycache__

install:
	pip install .

tests/baseline/test_funcion_juego.png: install
	mkdir --parents tests/baseline
	pytest --mpl-generate-path tests/baseline/

tests: tests/baseline/test_funcion_juego.png
	pytest