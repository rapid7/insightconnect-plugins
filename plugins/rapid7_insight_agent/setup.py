# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="rapid7_insight_agent-rapid7-plugin",
      version="1.0.3",
      description="Using the Insight Agent plugin from InsightConnect, you can quarantine, unquarantine and monitor potentially malicious IPs, addresses, hostnames, and devices across your organization",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_rapid7_insight_agent']
      )
