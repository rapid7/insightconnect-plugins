# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="confluence-rapid7-plugin",
      version="1.0.1",
      description="Confluence is an open and shared workspace for managing documents and files within an organization. Using the Confluence plugin for Rapid7 InsightConnect, users can view and update pages dynamically within automation workflows",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_confluence']
      )
