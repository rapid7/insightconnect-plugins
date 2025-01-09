# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="dig-rapid7-plugin",
      version="2.0.4",
      description="The DNS plugin is used for forward and reverse DNS lookups. This plugin uses [Dig](https://linux.die.net/man/1/dig), or Domain Information Groper, which is a network administration command-line tool for querying Domain Name System (DNS) name servers",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_dig']
      )
