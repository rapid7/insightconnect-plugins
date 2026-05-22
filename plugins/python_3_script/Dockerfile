FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.5.1 AS builder

WORKDIR /workspace

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /workspace/requirements.txt
ADD . /workspace


RUN apt-get update && apt-get install libxslt-dev libxml2-dev gcc g++ -y


RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.5.1

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /workspace

COPY --from=builder /workspace /workspace
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

ENV PYTHONUSERBASE=/var/cache/python_dependencies
ENV PYTHONPATH=/var/cache/python_dependencies


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/workspace:${PYTHONPATH}"

RUN rm -rf /root/.cache;
RUN mkdir -p /workspace/cache && chown -R root /workspace/cache

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["python", "/workspace/bin/icon_python_3_script"]
