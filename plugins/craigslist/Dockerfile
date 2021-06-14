FROM komand/python-2-plugin:2
LABEL organization=komand
LABEL sdk=python
LABEL type=plugin

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

RUN pip install python-craigslist
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

WORKDIR /python/src
# Add any package dependencies here

# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_craigslist"]
