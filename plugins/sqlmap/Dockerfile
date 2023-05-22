FROM rapid7/insightconnect-python-3-38-plugin:4

LABEL organization=rapid7
LABEL sdk=python

RUN apt-get update && \
    apt-get -y install wget

ENV SQLMAP_VERSION master

WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

RUN wget https://github.com/sqlmapproject/sqlmap/archive/$SQLMAP_VERSION.tar.gz && \
    tar -xf master.tar.gz

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

RUN	python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody

ENTRYPOINT ["/usr/local/bin/icon_sqlmap"]