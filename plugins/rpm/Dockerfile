FROM komand/python-3-plugin:2
# The three supported python parent images are:
# - komand/python-2-plugin
# - komand/python-3-plugin
# - komand/python-pypy3-plugin
#
LABEL organization=komand

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
RUN apt-get clean
RUN apt-get update -y
RUN apt-get upgrade -y --fix-missing
RUN apt-get update && apt-get install -y apt-utils rpm yum yum-utils
# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src
ADD ./repos/* /etc/yum.repos.d/
RUN mkdir /rpm-gpg
ADD ./rpm-gpg/* /rpm-gpg/

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/komand_rpm"]