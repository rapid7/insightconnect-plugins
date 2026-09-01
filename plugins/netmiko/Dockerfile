FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.3.4 AS builder

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt
ADD . /python/src



RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.3.4

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

COPY --from=builder /python/src /python/src
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR=/etc/ssl/certs
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/python/src:${PYTHONPATH}"

RUN rm -rf /root/.cache;

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["python", "/python/src/bin/komand_netmiko"]
