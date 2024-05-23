FROM --platform=linux/amd64 rapid7/insightconnect-python-3-plugin:5.4.9

LABEL organization=rapid7
LABEL sdk=python
LABEL type=plugin

ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR /etc/ssl/certs
ENV REQUESTS_CA_BUNDLE  /etc/ssl/certs/ca-certificates.crt

# Add any package dependencies here
ENV DEBIAN_FRONTEND noninteractive
# Kerberos dependencies
RUN apk update && apk add --no-cache \
    curl \
    gcc \
    python3-dev \
    krb5-dev \
    git \
    gnupg \
    krb5 \
    libffi-dev \
    libssl3 \
    openntpd \
    samba-common-tools \
    sudo \
    wget \
    ca-certificates \
    less \
    ncurses-terminfo-base \
    libgcc \
    libintl \
    libstdc++ \
    tzdata \
    userspace-rcu \
    zlib \
    icu-libs

# Kerberos dependancies Alpine
RUN apk add --upgrade krb5-libs

# Alipine Powershell dependencies

RUN apk -X https://dl-cdn.alpinelinux.org/alpine/edge/main add --no-cache \
    lttng-ust

    # Download the powershell '.tar.gz' archive
RUN curl -L https://github.com/PowerShell/PowerShell/releases/download/v7.4.2/powershell-7.4.2-linux-musl-x64.tar.gz -o /tmp/powershell.tar.gz && \
    # Create the target folder where powershell will be placed
    mkdir -p /opt/microsoft/powershell/7 && \
    # Expand powershell to the target folder
    tar zxf /tmp/powershell.tar.gz -C /opt/microsoft/powershell/7 && \
    # Set execute permissions
    chmod +x /opt/microsoft/powershell/7/pwsh && \
    # Create the symbolic link that points to pwsh
    ln -s /opt/microsoft/powershell/7/pwsh /usr/bin/pwsh

ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

WORKDIR /python/src

# End package dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER root

ENTRYPOINT ["/usr/local/bin/icon_powershell"]
