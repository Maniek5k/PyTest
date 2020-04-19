FROM python:3.8
ARG APP_DIR=/usr/src/pytest-selenium
WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p $APP_DIR
ADD tests/ $APP_DIR/tests/
ADD pages/ ${APP_DIR}/pages/
ADD conftest.py $APP_DIR/tests/
CMD PYTHONPATH=$PYTHONPATH:/usr/src/pytest \
    pytest /usr/src/pytest-selenium/tests