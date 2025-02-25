# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="datetime-rapid7-plugin",
      version="3.0.2",
      description="Timestamps, timezones, and Datetimes can be difficult to work with, especially when dealing with different locales on different systems. The Datetime InsightConnect plugin manipulates timestamps using Python's [Maya](https://pypi.org/project/maya/) library, which makes the simple things much easier while admitting that time is an illusion (timezones doubly so)",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_datetime']
      )
