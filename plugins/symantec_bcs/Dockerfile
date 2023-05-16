FROM rapid7/insightconnect-python-3-38-plugin:5
# The three supported python parent images are:
# - komand/python-2-plugin
# - komand/python-3-plugin
# - komand/python-pypy3-plugin
#
# Update the tag to a full semver version

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
RUN apt-get update
RUN apt-get install -y libmagic-dev
RUN pip install python-magic

WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

RUN	python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/komand_symantec_bcs"]