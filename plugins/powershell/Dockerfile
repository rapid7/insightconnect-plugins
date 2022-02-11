FROM komand/python-3-37-plugin:3.2
LABEL organization=komand
LABEL sdk=python
LABEL type=plugin

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

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
    libffi6 libffi-dev \
    libssl1.1 \
    ntp adcli sssd \
    samba-common \
    software-properties-common \
    sudo \
    realmd \
    wget

# Local PowerShell dependencies
RUN echo "deb http://security.ubuntu.com/ubuntu bionic-security main" | sudo tee -a /etc/apt/sources.list.d/bionic.list && \
    apt-cache policy libssl1.0-dev && \
    sudo apt-get install libssl1.0-dev && \
    wget http://mirrors.kernel.org/ubuntu/pool/main/i/icu/libicu52_52.1-3ubuntu0.8_amd64.deb && \
    sudo apt install -y ./libicu52_52.1-3ubuntu0.8_amd64.deb && \
    rm ./libicu52_52.1-3ubuntu0.8_amd64.deb && \
    wget https://github.com/PowerShell/PowerShell/releases/download/v7.1.5/powershell_7.1.5-1.debian.9_amd64.deb && \
    sudo apt install -y ./powershell_7.1.5-1.debian.9_amd64.deb && \
    rm ./powershell_7.1.5-1.debian.9_amd64.deb


# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/komand_powershell"]