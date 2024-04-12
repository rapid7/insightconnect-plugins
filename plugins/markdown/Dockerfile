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
RUN apt-get update && apt-get install -y pandoc curl --no-install-recommends
# Curling the wkhtmltopdf package to fix corrupted lib5QtCore.5.so file that appeared
# when running on the front-end. Installing it this way resolves the issue.
RUN apt-get clean
RUN curl -L -o wkhtmltox_0.12.6.1-2.bullseye_amd64.deb 'https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.bullseye_amd64.deb'
RUN apt --fix-broken install
RUN apt install ./wkhtmltox_0.12.6.1-2.bullseye_amd64.deb -y
# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

USER nobody

ENTRYPOINT ["/usr/local/bin/icon_markdown"]
