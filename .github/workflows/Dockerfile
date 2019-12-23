FROM python:3.8.1-alpine3.10

RUN python3 -m pip install --upgrade pip setuptools && \
    python3 -m pip install github-status-checker

ENTRYPOINT ["github-status"]