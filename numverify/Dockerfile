FROM komand/go-plugin-2:2
LABEL organization=komand
LABEL sdk=go
LABEL type=plugin

RUN mkdir -p /komand/plugins/bin
ADD . /go/src/github.com/rapid7/komand-plugins/numverify
WORKDIR /go/src/github.com/rapid7/komand-plugins/numverify

ADD ./plugin.spec.yaml /plugin.spec.yaml

RUN make plugin

ENTRYPOINT ["/komand/plugins/bin/numverify"]
