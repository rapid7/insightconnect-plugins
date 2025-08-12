FROM --platform=linux/amd64 rapid7/insightconnect-python-3-plugin:6.3.9 AS builder

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt
ADD . /python/src



RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-plugin:6.3.9

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

COPY --from=builder /python/src /python/src
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

RUN apk add --no-cache --virtual .build-deps make gcc libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/python/src:${PYTHONPATH}"

RUN rm -rf /root/.cache;

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["python", "/python/src/bin/komand_rapid7_insightvm"]
