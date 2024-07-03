# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="rapid7_vulndb-rapid7-plugin",
      version="2.1.2",
      description="Make searching the Rapid7 vulnerability and exploit data fast, easy and efficient with the InsightConnect plugin. Leverage this curated repository of vetted computer software exploits and exploitable vulnerabilities to ensure your security operations are always aware of the latest threats that could be used against your environment vulnerabilities",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_rapid7_vulndb']
      )
