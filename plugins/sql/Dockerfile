FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.3.3 AS builder

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt
ADD . /python/src



RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.3.3

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

COPY --from=builder /python/src /python/src
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

ENV TDSVER=8.0
RUN apt-get update && apt-get install -y libxslt-dev libxml2-dev unixodbc unixodbc-dev freetds-dev tdsodbc default-libmysqlclient-dev libpq-dev
RUN pip install --upgrade pip
RUN sed -i.bak 's/# TDS protocol version/tds version = 8.0/' /etc/freetds/freetds.conf
RUN sed -i.bak '/tds version = 8.0/a\ \tclient charset = UTF-8' /etc/freetds/freetds.conf


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/python/src:${PYTHONPATH}"

RUN rm -rf /root/.cache;

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["python", "/python/src/bin/komand_sql"]
