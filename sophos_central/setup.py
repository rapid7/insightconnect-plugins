# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="sophos_central-rapid7-plugin",
      version="1.0.0",
      description="Sophos Central is a unified console for managing Sophos products. Using the Sophos Central plugin for Rapid7 InsightConnect, users can get alerts, endpoints, and SIEM events",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_sophos_central']
      )
