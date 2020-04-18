.PHONY: test

deps:
	pip install -r test_requirements.txt
lint:
	flake8 hello_world test
test:
	PYTHONPATH=. py.test --verbose -s