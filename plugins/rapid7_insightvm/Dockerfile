FROM --platform=linux/amd64 rapid7/insightconnect-python-3-plugin:6.2.5

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

RUN apk add --no-cache --virtual .build-deps make gcc libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN pip install .

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/komand_rapid7_insightvm"]
