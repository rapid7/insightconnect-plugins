FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.3.6 AS builder

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt
ADD . /python/src



RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.3.6

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

COPY --from=builder /python/src /python/src
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends gcc git libkrb5-dev krb5-user libffi-dev libssl-dev && rm -rf /var/lib/apt/lists/*


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/python/src:${PYTHONPATH}"

RUN rm -rf /root/.cache;

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["python", "/python/src/bin/komand_active_directory_ldap"]
