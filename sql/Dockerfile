FROM komand/python-3-plugin
# The three supported python parent images are:
# - komand/python-2-plugin
# - komand/python-3-plugin
# - komand/python-pypy3-plugin
#
# Update the tag to a full semver version

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt

# End package dependencies
ENV TDSVER=8.0
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y libxslt-dev libxml2-dev unixodbc unixodbc-dev freetds-dev tdsodbc
RUN sed -i.bak 's/# TDS protocol version/tds version = 8.0/' /etc/freetds/freetds.conf
RUN sed -i.bak '/tds version = 8.0/a\ \tclient charset = UTF-8' /etc/freetds/freetds.conf

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install


ENTRYPOINT ["/usr/local/bin/komand_sql"]
