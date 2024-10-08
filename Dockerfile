FROM python:3.10.6-buster

ARG GID=1000
ARG UID=1000

# Copy our program in, owned by the docker user
COPY --chown=docker:docker src /app
WORKDIR /app

ENV PYTHONPATH=$PYTHONPATH:/app
ENV APP_BASE=/app/

RUN apt-get update && \
    apt-get install -y libpcre3 \
                    libpcre3-dev \
                    socat && \
    apt-get clean

COPY requirements.txt requirements.txt
RUN pip3 --disable-pip-version-check install -r requirements.txt


# Add a docker user
RUN groupadd -o -g $GID docker
RUN useradd -o -m -u $UID -g $GID  -s /bin/bash docker

CMD ["python3", "src/app.py"]
