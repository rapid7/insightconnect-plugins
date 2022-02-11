FROM komand/python-3-37-plugin:3
LABEL organization=komand
LABEL sdk=python
LABEL type=plugin

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

WORKDIR /python/src
# Add any package dependencies here
RUN apt-get update && \
	apt-get install --no-install-recommends --no-install-suggests -y libxslt-dev libxml2-dev gcc g++ && \
	apt-get clean -y

ENV PYTHONUSERBASE=/var/cache/python_dependencies \
		PYTHONPATH=/var/cache/python_dependencies

# End package dependencies
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi
RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER nobody

ENTRYPOINT ["/usr/local/bin/komand_python_3_script"]