FROM komand/python-3-37-slim-plugin:3
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

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# End package dependencies
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_microsoft_atp"]