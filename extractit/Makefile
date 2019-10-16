VERSION?=$(shell grep '^version: ' plugin.spec.yaml | sed 's/version: //')
NAME?=$(shell grep '^name: ' plugin.spec.yaml | sed 's/name: //')
ENCODING:=$(shell base64 icon.png 2>/dev/null | sed 's|/|\\/|g' | tr -d '\n')
VENDOR?=$(shell grep '^vendor: ' plugin.spec.yaml | sed 's/vendor: //')
CWD?=$(shell basename $(PWD))
_NAME?=$(shell echo $(NAME) | awk '{ print toupper(substr($$0,1,1)) tolower(substr($$0,2)) }')

PKG=$(VENDOR)-$(NAME)-$(VERSION).tar.gz

DST?=/komand/plugins/bin

REPO=github.com/rapid7/komand-plugins/extractit
ifndef REPO
	REPO=$(NAME)
endif

all: validate icon image tarball runner

plugin: install

build:
	@echo "Using repo $(REPO)"
	test -d $(GOPATH)/src/$(REPO) || ln -s $(PWD) $(GOPATH)/src/$(REPO) 
	mkdir -p bin
	go build -o bin/$(NAME) $(GOPATH)/src/$(REPO)/cmd/main.go

install: build
	cp -r bin/$(NAME) $(DST)

icon:
	@test -f icon.png && \
	sed -i.bu "/^icon/s/\(icon: \).*/\1\"data:image\/png;base64,$(ENCODING)\"/" plugin.spec.yaml || true
	@rm -f *.bu || true

tarball:
	rm -rf build
	rm -rf $(PKG)
	tar -cvzf $(PKG) --exclude=$(PKG) --exclude=tests --exclude=run.sh *
 
image:
	docker build --pull -t $(VENDOR)/$(NAME):$(VERSION) .
	docker tag $(VENDOR)/$(NAME):$(VERSION) $(VENDOR)/$(NAME):latest

regenerate:
	@echo Generating new plugin skeleton
	@echo Overlaying plugin skeleton to the current directory
	@which icon-plugin 1>/dev/null && icon-plugin generate go plugin.spec.yaml --path $(CWD) --repo "github.com/rapid7/komand-plugins/extractit"

runner:
	@ln -f -s ../tools/run.sh run.sh

help:
	@test -x ../tools/help.py && ../tools/help.py ./plugin.spec.yaml || true
	@test -f ../tools/help_md_gen.py && python ../tools/help_md_gen.py ./plugin.spec.yaml || true

validate:
	@test -x ../tools/check_spec.py && ../tools/check_spec.py ./plugin.spec.yaml || true
	@test -d ../0_ci && make -C ../ install-ci &> /dev/null && komand-plugin-ci validate . || true
	@test -x ../tools/mdl.sh && ../tools/mdl.sh || true
	@test -x ../tools/flake8.sh && ../tools/flake8.sh || true
	@test -x ../tools/bandit.sh && ../tools/bandit.sh || true

deps:
	go get -u honnef.co/go/tools/cmd/gosimple
	go get -u honnef.co/go/tools/cmd/staticcheck
	go get -u honnef.co/go/tools/cmd/unused
	go get -u github.com/golang/dep/cmd/dep

check:
	staticcheck $$(go list ./... | grep -v /vendor/)
	gosimple $$(go list ./... | grep -v /vendor/)
	unused $$(go list ./... | grep -v /vendor/)

export: image
	@printf "\n ---> Exporting Docker image to ./$(NAME).img\n"
	@docker save $(VENDOR)/$(NAME):$(VERSION) | gzip > $(NAME)_$(VERSION).img

.PHONY: all build package image plugin regenerate deps check