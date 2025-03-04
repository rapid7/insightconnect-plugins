FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.2.5

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

# Add any package dependencies here
ENV DEBIAN_FRONTEND noninteractive
# Kerberos dependencies
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    gcc python-dev libkrb5-dev \
    git \
    gnupg \
    krb5-user \
    libssl1.1 \
    ntp adcli sssd \
    samba-common \
    software-properties-common \
    sudo \
    realmd \
    wget

# Local PowerShell dependencies
RUN echo "deb http://security.ubuntu.com/ubuntu bionic-security main" | sudo tee -a /etc/apt/sources.list.d/bionic.list && \
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32 && sudo apt-get update && apt-cache policy libssl1.0-dev && \
    sudo apt-get install -y libssl1.0-dev && \
    wget http://mirrors.kernel.org/ubuntu/pool/main/i/icu/libicu52_52.1-3ubuntu0.8_amd64.deb && \
    sudo apt install -y ./libicu52_52.1-3ubuntu0.8_amd64.deb && \
    rm ./libicu52_52.1-3ubuntu0.8_amd64.deb && \
    wget https://github.com/PowerShell/PowerShell/releases/download/v7.4.6/powershell_7.4.6-1.deb_amd64.deb && \
    sudo apt install -y ./powershell_7.4.6-1.deb_amd64.deb && \
    rm ./powershell_7.4.6-1.deb_amd64.deb

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ADD . /python/src

RUN pip install .

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/icon_powershell"]
