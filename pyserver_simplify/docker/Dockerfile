FROM python:3.10-slim-buster

ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8 \
  PATH="${PATH}:/root/.poetry/bin"

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  curl \
  && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

CMD mkdir -p /workspace
WORKDIR /workspace


# FROM python:latest

# # set the working directory
# WORKDIR /app

# # install dependencies
# COPY ./requirements.txt /app
# RUN pip install --no-cache-dir --upgrade -r requirements.txt

# # copy the scripts to the folder
# COPY . /app

# # start the server
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]