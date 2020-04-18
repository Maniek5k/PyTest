.PHONY: test

deps:
	pip install -r test_requirements.txt
	wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	sudo apt install ./google-chrome-stable_current_amd64.deb
	webdrivermanager chrome --linkpath AUTO
	python3 -V
	chromedriver --version
	google-chrome-stable --version
lint:
	flake8 hello_world test
test:
	PYTHONPATH=. py.test --verbose -s