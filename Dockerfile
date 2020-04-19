FROM python:3.6
ARG APP_DIR=/usr/src/pytest
WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p $APP_DIR
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN	sudo apt install ./google-chrome-stable_current_amd64.deb
RUN	webdrivermanager chrome --linkpath AUTO
RUN	python3 -V
RUN	chromedriver --version
RUN	google-chrome-stable --version
CMD PYTHONPATH=$PYTHONPATH:/usr/src/pytest \
    pytest tests/