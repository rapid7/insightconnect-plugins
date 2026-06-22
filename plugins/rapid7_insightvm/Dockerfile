FROM --platform=linux/amd64 rapid7/insightconnect-python-3-plugin:6.5.1 AS builder

WORKDIR /workspace

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /workspace/requirements.txt
ADD . /workspace



RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-plugin:6.5.1

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /workspace

COPY --from=builder /workspace /workspace
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

RUN apk add --no-cache --virtual .build-deps make gcc libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/workspace:${PYTHONPATH}"

RUN rm -rf /root/.cache;
RUN mkdir -p /workspace/tmp && chown -R root /workspace/tmp

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["python", "/workspace/bin/komand_rapid7_insightvm"]
