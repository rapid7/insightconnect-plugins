FROM rapid7/insightconnect-python-3-38-slim-plugin:4
# Refer to the following documentation for available SDK parent images: https://komand.github.io/python/sdk.html#version

LABEL organization=rapid7
LABEL sdk=python

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
# Uncomment the below line for building wheels
#RUN apk add --no-cache gcc libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev
# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN pip install wheel && pip install wheels/*.whl && \
		python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/icon_symantec_endpoint_security"]