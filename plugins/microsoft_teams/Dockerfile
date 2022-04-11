FROM rapid7/insightconnect-python-3-38-slim-plugin:4
# Refer to the following documentation for available SDK parent images: https://docs.rapid7.com/insightconnect/sdk-guide/#sdk-guide

LABEL organization=rapid7
LABEL sdk=python

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt

# Need gcc for maya
RUN apk add --no-cache --virtual .build-deps \
                                        make \
                                        gcc \
                                        libc-dev \
                                        libffi-dev \
                                        openssl-dev \
                                        libxml2-dev \
                                        libxslt-dev
# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
# Need root for CA bundle  
USER root

ENTRYPOINT ["/usr/local/bin/icon_microsoft_teams"]
