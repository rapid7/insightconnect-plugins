# Include other Makefiles for improved functionality
INCLUDE_DIR = ../../tools/Makefiles
MAKEFILES := $(wildcard $(INCLUDE_DIR)/*.mk)
# We can't guarantee customers will have the include files
# - prefix to ignore Makefiles when not present
# https://www.gnu.org/software/make/manual/html_node/Include.html
-include $(MAKEFILES)

ifneq ($(MAKEFILES),)
  $(info [$(YELLOW)*$(NORMAL)] Use ``make menu`` for available targets)
  $(info [$(YELLOW)*$(NORMAL)] Including available Makefiles: $(MAKEFILES))
  $(info --)
else
  $(warning Makefile includes directory not present: $(INCLUDE_DIR))
endif

VERSION?=$(shell grep '^version: ' plugin.spec.yaml | sed 's/version: //')
NAME?=$(shell grep '^name: ' plugin.spec.yaml | sed 's/name: //')
VENDOR?=$(shell grep '^vendor: ' plugin.spec.yaml | sed 's/vendor: //')
CWD?=$(shell basename $(PWD))
_NAME?=$(shell echo $(NAME) | awk '{ print toupper(substr($$0,1,1)) tolower(substr($$0,2)) }')
PKG=$(VENDOR)-$(NAME)-$(VERSION).tar.gz

# Vendor name to use when building a tarball for TESTING in an InsightConnect (SOAR)
# instance. `rapid7` is a reserved vendor name and its tarball is rejected on upload,
# so test builds must use a non-reserved placeholder. The committed spec keeps
# `vendor: rapid7` (the merge-ready value); `test-export` rewrites it only during the
# build and restores it afterwards. Override with: make test-export TEST_VENDOR=myname
TEST_VENDOR?=rapid7lab

# Set default target explicitly. Make's default behavior is the first target in the Makefile.
# We don't want that behavior due to includes which are read first
.DEFAULT_GOAL := default # Make >= v3.80 (make -version)


default: image tarball

tarball:
	$(info [$(YELLOW)*$(NORMAL)] Creating plugin tarball)
	rm -rf build
	rm -rf $(PKG)
	tar -cvzf $(PKG) --exclude=$(PKG) --exclude=tests --exclude=run.sh *

image:
	$(info [$(YELLOW)*$(NORMAL)] Building plugin image)
	docker build --pull -t $(VENDOR)/$(NAME):$(VERSION) .
	docker tag $(VENDOR)/$(NAME):$(VERSION) $(VENDOR)/$(NAME):latest

regenerate:
	$(info [$(YELLOW)*$(NORMAL)] Refreshing schema from plugin.spec.yaml)
	insight-plugin refresh

export: image
	$(info [$(YELLOW)*$(NORMAL)] Exporting docker image)
	@printf "\n ---> Exporting Docker image to ./$(VENDOR)_$(NAME)_$(VERSION).tar\n"
	@docker save $(VENDOR)/$(NAME):$(VERSION) | gzip > $(VENDOR)_$(NAME)_$(VERSION).tar

# Build and export a tarball for TESTING in an InsightConnect instance.
# Temporarily rewrites `vendor:` in plugin.spec.yaml to $(TEST_VENDOR) (because
# `rapid7` is a reserved vendor name and its tarball is rejected on upload), builds
# and saves the image under that vendor, then restores the original spec. The spec is
# restored even if the build fails.
# Produces: ./$(TEST_VENDOR)_$(NAME)_$(VERSION).tar
test-export:
	$(info [$(YELLOW)*$(NORMAL)] Building TEST tarball with vendor '$(TEST_VENDOR)')
	@if [ "$(TEST_VENDOR)" = "rapid7" ]; then \
		echo "ERROR: TEST_VENDOR must not be 'rapid7' (reserved vendor name, rejected on upload)"; \
		exit 1; \
	fi
	@cp plugin.spec.yaml plugin.spec.yaml.bak
	@trap 'mv plugin.spec.yaml.bak plugin.spec.yaml' EXIT; \
	sed -i.sed_tmp 's/^vendor: rapid7$$/vendor: $(TEST_VENDOR)/' plugin.spec.yaml && rm -f plugin.spec.yaml.sed_tmp; \
	docker build --pull -t $(TEST_VENDOR)/$(NAME):$(VERSION) . && \
	docker tag $(TEST_VENDOR)/$(NAME):$(VERSION) $(TEST_VENDOR)/$(NAME):latest && \
	printf "\n ---> Exporting TEST Docker image to ./$(TEST_VENDOR)_$(NAME)_$(VERSION).tar\n" && \
	docker save $(TEST_VENDOR)/$(NAME):$(VERSION) | gzip > $(TEST_VENDOR)_$(NAME)_$(VERSION).tar

# Make will not run a target if a file of the same name exists unless setting phony targets
# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.PHONY: default tarball image regenerate test-export
