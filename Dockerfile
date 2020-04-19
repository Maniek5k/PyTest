FROM python:3.8
ARG APP_DIR=/usr/src/pytest-selenium
WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p $APP_DIR
RUN apt-get install libnss3-dev
RUN webdrivermanager chrome --linkpath AUTO
RUN python3 -V
RUN chromedriver --version
RUN google-chrome-stable --version
ADD tests/ $APP_DIR/tests/
ADD pages/ ${APP_DIR}/pages/
ADD conftest.py $APP_DIR
CMD PYTHONPATH=$PYTHONPATH:/usr/src/pytest \
    pytest /usr/src/pytest-selenium/tests