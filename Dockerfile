# Dockerfile to create env: build using `datmo env build`
# [1] Base environment to start from:
# Find more at https://hub.docker.com/u/datmo/
FROM datmo/xgboost:cpu
RUN pip install kombu==4.0.0
RUN pip install Celery==4.0.0
RUN pip install redis==2.10.6
RUN apt-get update
RUN apt-get install -y supervisor

RUN mkdir /code
COPY . /code/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /code

CMD ["/usr/bin/supervisord"]
