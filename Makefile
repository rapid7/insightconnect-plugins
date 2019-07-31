PLATFORM := $(shell uname)

update-tools:
	@echo "Updating tools for $(PLATFORM) platform..."
ifeq ($(PLATFORM), Darwin)
	brew tap rapid7/icon-plugin-homebrew https://github.com/rapid7/icon-plugin-homebrew
	brew upgrade icon-plugin
else
	@echo "Linux selected"
endif