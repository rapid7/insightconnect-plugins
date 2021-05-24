# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="rapid7_vulndb-rapid7-plugin",
      version="2.1.0",
      description="The Vulnerability & Exploit Database plugin allows you to search and compare potential threats with a curated repository of vetted computer software exploits and exploitable vulnerabilities vulnerabilities",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_rapid7_vulndb']
      )
