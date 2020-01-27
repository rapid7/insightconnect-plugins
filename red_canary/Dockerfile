FROM komand/python-3-37-slim-plugin:3
# Refer to the following documentation for available SDK parent images: https://komand.github.io/python/sdk.html#version

LABEL organization=komand
LABEL sdk=python
LABEL type=plugin

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

WORKDIR /python/src
# Add any package dependencies here

RUN apk add --no-cache gcc libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/komand_red_canary"]
