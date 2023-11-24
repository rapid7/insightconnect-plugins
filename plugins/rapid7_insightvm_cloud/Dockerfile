FROM rapid7/insightconnect-python-3-plugin:5
# Refer to the following documentation for available SDK parent images: https://komand.github.io/python/sdk.html#version

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/icon_rapid7_insightvm_cloud"]