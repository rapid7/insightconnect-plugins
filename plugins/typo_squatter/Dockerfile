FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:5.6.1

LABEL organization=rapid7
LABEL sdk=python

RUN apt-get update && apt-get install libgeoip-dev libfuzzy-dev python3-dnspython python3-geoip python3-whois python3-requests python3-ssdeep python3-cffi gcc -y

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/komand_typo_squatter"]
