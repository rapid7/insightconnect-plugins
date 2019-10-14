FROM komand/python-3-37-slim-plugin:3

LABEL organization=rapid7
LABEL sdk=python
LABEL type=plugin

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
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
USER root

ENTRYPOINT ["/usr/local/bin/icon_microsoft_office365_email"]
