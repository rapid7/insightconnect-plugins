# Include other Makefiles for improved functionality
INCLUDE_DIR = ../tools/Makefiles
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
	$(info [$(YELLOW)*$(NORMAL)] Regenerating schema from plugin.spec.yaml)
	icon-plugin generate python --regenerate

export: image
	$(info [$(YELLOW)*$(NORMAL)] Exporting docker image)
	@printf "\n ---> Exporting Docker image to ./$(VENDOR)_$(NAME)_$(VERSION).tar\n"
	@docker save $(VENDOR)/$(NAME):$(VERSION) | gzip > $(VENDOR)_$(NAME)_$(VERSION).tar

# Make will not run a target if a file of the same name exists unless setting phony targets
# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.PHONY: default tarball image regenerate
