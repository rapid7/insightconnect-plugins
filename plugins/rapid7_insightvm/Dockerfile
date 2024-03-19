FROM --platform=linux/amd64 rapid7/insightconnect-python-3-plugin:5.4.4

LABEL organization=rapid7
LABEL sdk=python

RUN apk add --no-cache --virtual .build-deps make gcc libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/komand_rapid7_insightvm"]
