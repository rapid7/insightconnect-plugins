FROM rapid7/insightconnect-python-3-38-plugin:latest

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt
RUN apt-get update -y && apt-get install -y libffi6 libffi-dev

# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

ENTRYPOINT ["/usr/local/bin/icon_carbon_black_response"]
