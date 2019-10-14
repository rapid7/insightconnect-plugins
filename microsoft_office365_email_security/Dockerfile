FROM komand/python-3-37-plugin:3
# Refer to the following documentation for available SDK parent images: https://komand.github.io/python/sdk.html#version

LABEL organization=rapid7
LABEL sdk=python

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt


# End package dependencies

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src
ADD ./icon_microsoft_office365_email_security/powershell /powershell

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

# User to run plugin code. The two supported users are: root, nobody
USER root

# Install Powershell Core
# Install system components
RUN apt-get -y update
RUN apt-get install -y curl gnupg apt-transport-https --no-install-recommends

# Import the public repository GPG keys
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Register the Microsoft Product feed
RUN sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch main" > /etc/apt/sources.list.d/microsoft.list'

# Update the list of products
# Install PowerShell
RUN apt-get -y update \
    && apt-get install -y powershell --no-install-recommends

# Need this to run New-PSSession
RUN ln -s /usr/lib/x86_64-linux-gnu/libssl.so.1.0.2 /opt/microsoft/powershell/6/libssl.so.1.0.0 \
    && ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.2 /opt/microsoft/powershell/6/libcrypto.so.1.0.0

ENTRYPOINT ["/usr/local/bin/icon_microsoft_office365_email_security"]
