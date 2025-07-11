# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="anomali_threatstream-rapid7-plugin",
    version="4.0.0",
    description="[Anomali ThreatStream](https://www.anomali.com/) is an operational threat intelligence stream, automating collection and integration that enables security teams to analyze and respond to threats. The Anomali ThreatStream InsightConnect plugin allows you lookup hashes, IP addresses, URLs, observables. It also allows importing observables",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={"console_scripts": ["komand_anomali_threatstream = bin.komand_anomali_threatstream:main"]},
)
