#!/usr/bin/env bash

platform=$(uname)

if [[ "${platform}" == "Darwin" ]]; then
	echo "[*] Executing update/installation for MacOS!"
	echo "[*] Installing/updating jq via homebrew"
	brew reinstall jq > /dev/null; true

elif [[ "${platform}" == "Linux" ]] && [[ -f /etc/debian_version ]]; then
	echo "[*] Executing update/installation for Debian Linux!"
	echo "[*] Installing/updating jq..."
	sudo apt-get -qq install -y jq

elif [[ "${platform}" == "Linux" ]] && [[ -f /etc/redhat-release ]]; then
	echo "[*] Executing update/installation for Red Hat Linux!"
	echo "[*] Installing/updating jq..."
	sudo yum install -q -y jq

else
	echo "[!] Unsupported OS found! Unable to install insight-plugin and jq!"
fi

echo "[*] Installing/updating insight-plugin via PyPi..."
sudo -H python3 -m pip install --user --upgrade insight-plugin > /dev/null; true

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
