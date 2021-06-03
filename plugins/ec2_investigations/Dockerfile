FROM komand/python-pypy3-plugin:2
# The three supported python parent images are:
# - komand/python-2-plugin
# - komand/python-3-plugin
# - komand/python-pypy3-plugin
#
# Update the tag to a full semver version

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt

RUN pip install paramiko
RUN pip install boto
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src
ADD ./komand_ec2_investigations/actions/known_hosts /root/.ssh/known_hosts
ADD ./komand_ec2_investigations/actions/mount.sh ./mount.sh
ADD ./komand_ec2_investigations/actions/clam_av_run.py ./clam_av_run.py

# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_ec2_investigations"]
