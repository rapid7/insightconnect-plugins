FROM komand/python-3-37-slim-plugin

LABEL organization=rapid7
LABEL sdk=python

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt

# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

# Install jq
RUN apk add --no-cache jq

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/icon_jq"]