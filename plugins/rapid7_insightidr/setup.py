# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="rapid7_insightidr-rapid7-plugin",
      version="8.2.0",
      description="This plugin allows you to add indicators to a threat and see the status of investigations",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_rapid7_insightidr']
      )
