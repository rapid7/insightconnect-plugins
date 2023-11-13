FROM rapid7/insightconnect-python-3-38-plugin:5

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN apt-get update && apt-get install -y python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 libpangocairo-1.0-0
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN	python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/komand_pdf_generator"]
