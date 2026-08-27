FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.6.0 AS builder

WORKDIR /workspace

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /workspace/requirements.txt
ADD . /workspace



RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.6.0

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /workspace

COPY --from=builder /workspace /workspace
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR=/etc/ssl/certs
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/workspace:${PYTHONPATH}"

RUN rm -rf /root/.cache;
RUN mkdir -p /workspace/cache && chown -R root /workspace/cache

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["python", "/workspace/bin/komand_netmiko"]
