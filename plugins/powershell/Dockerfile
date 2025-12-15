FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.4.1 AS builder

WORKDIR /python/src

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD ./requirements.txt /python/src/requirements.txt
ADD . /python/src



RUN pip install .
RUN pip uninstall -y setuptools

FROM --platform=linux/amd64 rapid7/insightconnect-python-3-slim-plugin:6.4.1

LABEL organization=rapid7
LABEL sdk=python

WORKDIR /python/src

COPY --from=builder /python/src /python/src
COPY --from=builder /plugin.spec.yaml /plugin.spec.yaml

# Add any package dependencies here
ENV DEBIAN_FRONTEND noninteractive
# Kerberos dependencies
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    gcc python-dev-is-python3 libkrb5-dev \
    git \
    gnupg \
    krb5-user \
    libssl3 \
    ntpsec adcli sssd \
    samba-common \
    sudo \
    realmd \
    wget

# Local PowerShell dependencies
RUN wget https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/powershell-7.5.4-linux-x64.tar.gz \
    && mkdir /opt/powershell \
    && tar -xzf powershell-7.5.4-linux-x64.tar.gz -C /opt/powershell \
    && ln -s /opt/powershell/pwsh /usr/bin/pwsh \
    && rm powershell-7.5.4-linux-x64.tar.gz


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

ENV PYTHONPATH="/python/src:${PYTHONPATH}"

RUN rm -rf /root/.cache;

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["python", "/python/src/bin/icon_powershell"]
