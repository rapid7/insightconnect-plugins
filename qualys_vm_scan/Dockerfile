FROM komand/go-plugin-2:2
LABEL organization=komand
LABEL sdk=go
LABEL type=plugin

RUN mkdir -p /komand/plugins/bin
ADD . /go/src/github.com/rapid7/komand-plugins/qualys_vm_scan
WORKDIR /go/src/github.com/rapid7/komand-plugins/qualys_vm_scan

ADD ./plugin.spec.yaml /plugin.spec.yaml

RUN make plugin

ENTRYPOINT ["/komand/plugins/bin/qualys_vm_scan"]
