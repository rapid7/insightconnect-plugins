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

# Removed the below line as it was needed for dependency compilation. Dependencies are now vendored into the vendor/
# directory, thus making these package dependencies obsolete. If the wheel files ever need to be updated, this line
# can be uncommented to do so.
#RUN apk add --no-cache gcc libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

# End package dependencies
RUN pip install wheel && pip install vendor/*.whl && \
		python setup.py build && python setup.py install

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/komand_red_canary"]
