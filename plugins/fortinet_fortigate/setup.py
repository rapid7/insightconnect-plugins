# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="fortinet_fortigate-rapid7-plugin",
    version="6.0.3",
    description="[FortiGate Next Generation Firewalls (NGFWs)](https://www.fortinet.com/) enable security-driven networking and consolidate industry-leading security capabilities such as intrusion prevention system (IPS), web filtering, secure sockets layer (SSL) inspection, and automated threat protection",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={"console_scripts": ["icon_fortinet_fortigate = bin.icon_fortinet_fortigate:main"]},
)
