.PHONY: test

USERNAME=maniek5k
SERVICE_NAME=pytest
MY_DOCKER_NAME=$(SERVICE_NAME)
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

deps:
	pip install -r requirements.txt
	# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	# sudo apt install ./google-chrome-stable_current_amd64.deb
	webdrivermanager chrome --linkpath AUTO
	python3 -V
	chromedriver --version
	google-chrome-stable --version
lint:
	flake8 hello_world test
test:
	PYTHONPATH=. py.test --verbose -s

docker_build:
	docker build -t $(MY_DOCKER_NAME) .

docker_run: docker_build
	docker run \
		--name $(SERVICE_NAME)-dev \
		-d $(MY_DOCKER_NAME)

docker_run_local:
	docker run \
		$(USERNAME)/$(SERVICE_NAME)

docker_stop_local:
	docker stop $(USERNAME)/$(SERVICE_NAME)

docker_stop:
	docker stop $(SERVICE_NAME)-dev

docker_push: docker_build
	docker login --username $(USERNAME) --password ${DOCKER_PASSWORD} docker.io; \
	docker tag $(MY_DOCKER_NAME) $(TAG); \
	docker push $(TAG); \
	docker logout;