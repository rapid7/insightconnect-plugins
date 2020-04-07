FROM komand/python-3-37-slim-plugin:3
# The three supported python parent images are:
# - komand/python-2-plugin
# - komand/python-3-plugin
# - komand/python-pypy3-plugin
#
# Update the tag to a full semver version

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

RUN apk add --no-cache gcc libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

# End package dependencies
RUN pip install wheel && pip install wheels/*.whl && \
		python setup.py build && python setup.py install

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENTRYPOINT ["/usr/local/bin/komand_cymon"]