# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="rapid7_insightvm-rapid7-plugin",
      version="6.1.1",
      description="InsightVM is a powerful vulnerability management tool which finds, prioritizes, and remediates vulnerabilities. This plugin uses an orchestrator to get top remediations, scan results and start scans",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_rapid7_insightvm']
      )
