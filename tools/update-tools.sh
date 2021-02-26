#!/usr/bin/env bash

platform=$(uname)

if [[ "${platform}" == "Darwin" ]]; then
	echo "[*] Executing update/installation for MacOS!"
	echo "[*] Installing/updating icon-plugin via homebrew..."
	brew tap rapid7/icon-plugin-homebrew https://github.com/rapid7/icon-plugin-homebrew > /dev/null
	brew reinstall icon-plugin > /dev/null; true

	echo "[*] Installing/updating jq via homebrew"
	brew reinstall jq > /dev/null; true

elif [[ "${platform}" == "Linux" ]] && [[ -f /etc/debian_version ]]; then
	echo "[*] Executing update/installation for Debian Linux!"
	curl -s https://packagecloud.io/install/repositories/rapid7/insightconnect_plugin_tooling/script.deb.sh | sudo bash
	sudo apt-get update
	sudo apt-get -qq install -y icon-plugin

	echo "[*] Installing/updating jq..."
	sudo apt-get -qq install -y jq

elif [[ "${platform}" == "Linux" ]] && [[ -f /etc/redhat-release ]]; then
	echo "[*] Executing update/installation for Red Hat Linux!"
	curl -s https://packagecloud.io/install/repositories/rapid7/insightconnect_plugin_tooling/script.rpm.sh | sudo bash
	sudo yum install -q -y icon-plugin

	echo "[*] Installing/updating jq..."
	sudo yum install -q -y jq
else
	echo "[!] Unsupported OS found! Unable to install icon-plugin and jq!"
fi

echo "[*] Installing InsightConnect validator tooling..."
sudo -H python3 -m pip install --user --upgrade insightconnect-integrations-validators > /dev/null; true

echo "[*] Installing PyYAML..."
sudo -H python3 -m pip install --user --upgrade pyyaml > /dev/null; true

echo "[*] Installing pre-commit..."
sudo -H python3 -m pip install --user --upgrade pre-commit > /dev/null; true

echo "[*] Installing mdl..."
sudo gem install mdl > /dev/null; true

echo "[*] Installing js-yaml..."
sudo npm install -g js-yaml > /dev/null; true

echo "[*] Complete! Tooling installed & updated!"
