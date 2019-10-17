.PHONY: all setup plugin test

export BASE?=$(PWD)/..
export DST?=$(GOPATH)/src/github.com/komand/plugin-sdk-go


setup:
	test -d $(DST) || ln -s $(BASE) $(DST)

all: setup plugin

plugin:
	cd $(DST)/plugin && go get -v ./...
	cd $(DST)/plugin && go build .

test:
	cd $(DST)/plugin && go list ./... | grep -v /vendor/ | xargs -P4 -L1 go test -v
	cd $(DST)/test/cache/ && go run main.go
