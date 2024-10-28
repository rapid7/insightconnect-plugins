# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="cloudflare-rapid7-plugin",
      version="1.0.1",
      description="Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable. This plugin allows you to list accounts, zones, zone access rules and lists and create or delete access rules for specific zones",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_cloudflare']
      )
