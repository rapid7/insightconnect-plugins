# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="jq-rapid7-plugin",
    version="3.0.0",
    description="[jq](https://stedolan.github.io/jq/) is a command-line tool used for slicing, filtering, mapping, and transforming structured JSON data. The jq plugin passes the given list of flags to the jq command, which then runs the given filter expression on the given JSON input. For flexibility, the output is returned as a string",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={"console_scripts": ["icon_jq = bin.icon_jq:main"]},
)
