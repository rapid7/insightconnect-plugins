PLUGIN_NAME = teamdynamix
PLUGIN_VERSION = 1.0.0

.PHONY: all image build test export

all: image

image:
	docker build -t teamdynamix:1.0.0 .

build:
	docker build -t $(PLUGIN_NAME):$(PLUGIN_VERSION) .

test:
	insight-plugin samples
	@echo "Fill in tests/ directory then run: insight-plugin run tests/<action>.json"

export:
	insight-plugin export

lint:
	pylint icon_teamdynamix --disable=C0114,C0115,C0116
