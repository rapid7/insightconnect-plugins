FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.2.3

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/icon_rapid7_insightvm_cloud"]
