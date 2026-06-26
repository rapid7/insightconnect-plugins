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

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends gcc git libkrb5-dev krb5-user libffi-dev libssl-dev && rm -rf /var/lib/apt/lists/*


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/workspace:${PYTHONPATH}"

RUN rm -rf /root/.cache;

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["python", "/workspace/bin/komand_active_directory_ldap"]
