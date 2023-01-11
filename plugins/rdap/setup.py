# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="rdap-rapid7-plugin",
      version="1.0.0",
      description="The Registration Data Access Protocol (RDAP) is the successor to WHOIS. Like WHOIS, RDAP provides access to information about Internet resources (domain names, autonomous system numbers, and IP addresses)",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_rdap']
      )
