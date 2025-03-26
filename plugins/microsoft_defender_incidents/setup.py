# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="microsoft_defender_incidents-rapid7-plugin",
    version="2.0.1",
    description="Manage security incidents with Microsoft Defender 365",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={
        "console_scripts": ["icon_microsoft_defender_incidents = bin.icon_microsoft_defender_incidents:main"]
    },
)
