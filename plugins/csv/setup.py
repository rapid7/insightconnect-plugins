# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="csv-rapid7-plugin",
      version="2.0.3",
      description="[Comma Separated Value](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV) is a common format to express data.This plugin allows one to extract fields from CSV strings and files.Using the CSV plugin, users can automate conversions between JSON and CSV to help enable service interoperabilityas well as filter data within a CSV file",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_csv']
      )
