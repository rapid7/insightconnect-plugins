FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.0.1

LABEL organization=rapid7
LABEL sdk=python
LABEL type=plugin

RUN apt-get update && apt-get install -y pandoc texlive lmodern --no-install-recommends

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN python setup.py build && python setup.py install

# root is required for the conversion to work. If USER set to nobody, actions/tests will fail
USER root

ENTRYPOINT ["/usr/local/bin/icon_html"]
