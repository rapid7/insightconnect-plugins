FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:5.3.1

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

# PLGN-701: POC how we can inject an env var into the container to specify a new date
# the intention will be in next version to remove this hard coded injection and then if a backfill is needed
# again we simply inject the value at the deployment level (TBD on how we would do this and persist if pod restarts etc)
ENV SPECIFIC_DATE='{"year": 2024, "month": 1, "day": 27, "hour": 0, "minute": 0, "second": 0}'

ENTRYPOINT ["/usr/local/bin/komand_proofpoint_tap"]
