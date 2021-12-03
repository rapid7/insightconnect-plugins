FROM rapid7/insightconnect-python-3-38-slim-plugin:4
LABEL organization=komand

WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

USER nobody

ENTRYPOINT ["/usr/local/bin/icon_ipstack"]