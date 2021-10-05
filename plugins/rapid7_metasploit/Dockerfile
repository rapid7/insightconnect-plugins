FROM rapid7/insightconnect-python-3-38-slim-plugin:4

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
                                        libxslt-dev \
                                        git
# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN pip install --upgrade pip
RUN pip install -U setuptools
RUN pip install -r requirements.txt

# Install plugin
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_rapid7_metasploit"]
