FROM komand/python-pypy3-plugin:2
# Refer to the following documentation for available SDK parent images: https://komand.github.io/python/sdk.html#version

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
RUN apt-get update -y && apt-get install -y tcptraceroute=1.5beta7+debian-4

# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_traceroute"]