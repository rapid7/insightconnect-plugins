# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="sentinelone-rapid7-plugin",
      version="9.1.2",
      description="The SentinelOne plugin allows you to manage and mitigate all your security operations through SentinelOne",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_sentinelone']
      )
