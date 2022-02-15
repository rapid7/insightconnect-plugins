FROM rapid7/insightconnect-python-3-38-plugin:4
# The three supported python parent images are:
# - komand/python-2-plugin
# - komand/python-3-plugin
# - komand/python-pypy3-plugin
#
# Update the tag to a full semver version

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
RUN apt-get update
RUN apt-get install -y libgeoip-dev libfuzzy-dev python3-dnspython python3-geoip python3-whois python3-requests python3-ssdeep python3-cffi gcc

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

ENTRYPOINT ["/usr/local/bin/komand_typo_squatter"]
