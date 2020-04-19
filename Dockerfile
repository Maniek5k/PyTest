FROM python:3.8
ARG APP_DIR=/usr/src/pytest-selenium
WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p $APP_DIR
RUN apt-get install -y libglib2.0-0=2.50.3-2 \
    libnss3=2:3.26.2-1.1+deb9u1 \
    libgconf-2-4=3.2.6-4+b1 \
    libfontconfig1=2.11.0-6.7+b1
RUN webdrivermanager chrome --linkpath AUTO
ADD tests/ $APP_DIR/tests/
ADD pages/ ${APP_DIR}/pages/
ADD conftest.py $APP_DIR
CMD PYTHONPATH=$PYTHONPATH:/usr/src/pytest \
    pytest /usr/src/pytest-selenium/tests