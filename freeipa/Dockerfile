FROM komand/python-3-37-slim-plugin:3

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
RUN apk add git
RUN pip install git+https://github.com/komand/python-freeipa-json

# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

USER nobody

ENTRYPOINT ["/usr/local/bin/komand_freeipa"]