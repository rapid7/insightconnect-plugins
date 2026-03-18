FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.4.3 AS builder

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt
ADD . /python/src



RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.4.3

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

COPY --from=builder /python/src /python/src
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

RUN apt-get update && apt-get upgrade -y && apt-get install -y wget rpm dnf dnf-plugins-core && mkdir -p /etc/yum.repos.d
COPY --from=builder /python/src/repos /opt/rpm-plugin/repos


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/python/src:${PYTHONPATH}"

RUN rm -rf /root/.cache;

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["python", "/python/src/bin/komand_rpm"]
