FROM python:3.10-slim-buster

# Requirements for the Rapid7 plugin runtime
LABEL organization=nleech
LABEL program=bitdefender_gravityzone_comprehensive
LABEL version=2.0.0
LABEL vendor=nleech

ENV INST_PKG=bitdefender_gravityzone_comprehensive
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

WORKDIR /python/src
ADD ./setup.py /python/src/setup.py
ADD ./requirements.txt /python/src/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt && python setup.py install

ADD ./plugin.spec.yaml /python/src/plugin.spec.yaml
ADD ./bitdefender_gravityzone_comprehensive /python/src/bitdefender_gravityzone_comprehensive

# Run the plugin via the default engine module entry point
ENTRYPOINT ["python", "-m", "bitdefender_gravityzone_comprehensive"]