FROM komand/python-3-37-slim-plugin
# Refer to the following documentation for available SDK parent images: https://komand.github.io/python/sdk.html#version

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
RUN apk add --no-cache libmagic

# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_thehive"]
