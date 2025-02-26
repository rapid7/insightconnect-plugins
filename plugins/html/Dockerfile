FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.2.5

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

RUN apt-get update && apt-get install -y texlive lmodern --no-install-recommends
# root is required for the conversion to work. If USER set to nobody, actions/tests will fail

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN pip install .

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/icon_html"]
