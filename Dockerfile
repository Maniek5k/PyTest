FROM python:3.6
ARG APP_DIR=/usr/src/pytest
WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p $APP_DIR
CMD pytest tests/