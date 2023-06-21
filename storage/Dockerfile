# alpine wasn't adding curl
from python:3.10-slim-buster
# args for user creation
ARG HOST_UID
ARG HOST_GID
# add curl for docker container requests
# and kafka lib
RUN apt-get update -y
RUN apt-get install -y librdkafka-dev curl libcurl4-openssl-dev libssl-dev
# add gcc for pycurl
RUN apt-get -y install gcc
# load forms
RUN getent group $HOST_GID || groupadd -g $HOST_GID apigroup
RUN useradd -u $HOST_UID -g $HOST_GID -m -s /bin/bash --create-home api
RUN echo "api ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN mkdir -p /home/fastapi/app/api
WORKDIR /home/fastapi/app/api
COPY requirements.txt .
COPY start.sh .
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R $HOST_UID:$HOST_GID /home/fastapi
USER api
RUN mkdir /home/api/staticfiles
RUN chmod +x start.sh
