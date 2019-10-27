FROM komand/go-plugin-2:2
# The supported go parent images are:
# - komand/go-plugin-2
#

LABEL organization=komand
LABEL sdk=go
LABEL type=plugin

# Add source code
RUN mkdir -p /komand/plugins/bin
ADD . /go/src/github.com/rapid7/komand-plugins/extractit
WORKDIR /go/src/github.com/rapid7/komand-plugins/extractit

ADD ./plugin.spec.yaml /plugin.spec.yaml

# Build plugin
RUN make plugin

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/komand/plugins/bin/extractit"]
