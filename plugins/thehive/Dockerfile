FROM rapid7/insightconnect-python-3-38-plugin:5

LABEL organization=rapid7
LABEL sdk=python

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN	python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
# Needed for ssl
USER root

ENTRYPOINT ["/usr/local/bin/komand_thehive"]
