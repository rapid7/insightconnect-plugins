# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="rapid7_insightvm_cloud-rapid7-plugin",
      version="3.3.0",
      description="InsightVM is a powerful vulnerability management tool which finds, prioritizes, and remediates vulnerabilities. This plugin uses the InsightVM Cloud Integrations API to view assets and start scans",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_rapid7_insightvm_cloud']
      )
