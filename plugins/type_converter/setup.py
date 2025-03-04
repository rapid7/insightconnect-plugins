# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="type_converter-rapid7-plugin",
      version="1.8.4",
      description="Type Converter is a utility plugin for converting data types within a Rapid7 InsightConnect workflow. This is useful for enabling input interoperability between certain plugins",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_type_converter']
      )
