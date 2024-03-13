FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:5.4.4

LABEL organization=rapid7
LABEL sdk=python

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

WORKDIR /python/src
# Add any package dependencies here
RUN apt-get update && apt-get install -y pandoc wkhtmltopdf --no-install-recommends
# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

USER nobody

ENTRYPOINT ["/usr/local/bin/icon_markdown"]
