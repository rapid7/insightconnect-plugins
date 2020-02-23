FROM komand/python-3-37-plugin:3
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
ENV PKG phantomjs-2.1.1-linux-x86_64.tar.bz2
ENV DST /tmp/phantomjs
RUN mkdir $DST
COPY $PKG /tmp/phantomjs
RUN apt-get update && apt-get install -y bzip2 libxml2-dev libxmlsec1-dev gcc libfontconfig && rm -rf /var/lib/apt/lists/*
RUN tar -xj --strip-components=1 -f $PKG -C $DST
RUN mv $DST/bin/phantomjs /usr/local/bin
RUN rm -rf $DST
# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_rapid7_vulndb"]
