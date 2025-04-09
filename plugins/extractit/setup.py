# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="extractit-rapid7-plugin",
    version="3.0.12",
    description="The ExtractIt plugin is a collection of data extraction actions. This plugin allows users to extract various pieces of information from blocks of text. The pieces of information this plugin can extract include IPs, URLs, file paths, dates, domains, hashes, MAC addresses, and email addresses",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={"console_scripts": ["icon_extractit = bin.icon_extractit:main"]},
)
