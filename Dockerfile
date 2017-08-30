# Dockerfile to create env: build using `datmo env build`
# [1] Base environment to start from:
# Find more at https://hub.docker.com/u/datmo/
FROM datmo/xgboost:cpu

RUN mkdir /code
COPY ./model.dat ./python_api.py ./request.py /code/

WORKDIR /code

CMD python /code/python_api.py
