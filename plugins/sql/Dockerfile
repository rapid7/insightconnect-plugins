FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:5

LABEL organization=rapid7
LABEL sdk=python

ENV TDSVER=8.0
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y libxslt-dev libxml2-dev unixodbc unixodbc-dev freetds-dev tdsodbc default-libmysqlclient-dev libpq-dev
RUN sed -i.bak 's/# TDS protocol version/tds version = 8.0/' /etc/freetds/freetds.conf
RUN sed -i.bak '/tds version = 8.0/a\ \tclient charset = UTF-8' /etc/freetds/freetds.conf

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN	python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/komand_sql"]
