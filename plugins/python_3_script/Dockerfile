FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.1.0

LABEL organization=rapid7
LABEL sdk=python

RUN apt-get update && apt-get install libxslt-dev libxml2-dev gcc g++ -y

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

ENV PYTHONUSERBASE=/var/cache/python_dependencies
ENV PYTHONPATH=/var/cache/python_dependencies

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/icon_python_3_script"]
