FROM python:3.6-alpine

ENV FLASK_APP flasky.py
ENV FLASK_CONFIG docker


WORKDIR /home/flasky

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN venv/bin/pip config set install.trusted-host mirrors.aliyun.com
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY flasky.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]