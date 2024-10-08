# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="ipstack-rapid7-plugin",
      version="3.0.2",
      description="IPStack (https://ipstack.com) offers one of the leading IP to geolocation APIs and global IP database services worldwide. This plugin uses the [ipstack API](https://ipstack.com/documentation) to get geolocation data for a provided IP address",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_ipstack']
      )
