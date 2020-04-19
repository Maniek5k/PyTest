FROM python:3.8
ARG APP_DIR=/usr/src/pytest-selenium
WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN apt-get update
RUN apt-get -y install libnss3
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN webdrivermanager chrome --linkpath AUTO
RUN apt-get -y install xvfb
RUN mkdir -p $APP_DIR
ADD tests/ $APP_DIR/tests/
ADD pages/ ${APP_DIR}/pages/
ADD conftest.py $APP_DIR
CMD PYTHONPATH=$PYTHONPATH:/usr/src/pytest \
    pytest /usr/src/pytest-selenium/tests