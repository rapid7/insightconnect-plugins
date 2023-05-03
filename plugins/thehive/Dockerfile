FROM rapid7/insightconnect-python-3-38-plugin:4

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

RUN	python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/komand_thehive"]