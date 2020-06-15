FROM rapid7/insightconnect-python-3-38-plugin:4
LABEL organization=komand
LABEL sdk=python
LABEL type=plugin

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

ADD ./whois.conf /etc/whois.conf
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

WORKDIR /python/src
# Add any package dependencies here
RUN apt-get update && apt-get install -y whois git
RUN pip install git+https://github.com/komand/python-whois.git@0.6.13

# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_whois"]
