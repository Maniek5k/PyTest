FROM python:3.8
ARG APP_DIR=/usr/src/pytest-selenium
WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt; \
    apt-get update; \
    apt-get -y install libnss3; \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb; \
    apt install -y ./google-chrome-stable_current_amd64.deb; \
    webdrivermanager chrome --linkpath AUTO \
    apt-get -y install xvfb; \
    mkdir -p $APP_DIR
ADD tests/ $APP_DIR/tests/; \
    pages/ ${APP_DIR}/pages/; \
    conftest.py $APP_DIR
CMD PYTHONPATH=$PYTHONPATH:/usr/src/pytest; \
    pytest /usr/src/pytest-selenium/tests
