# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='rapid7_insightappsec-rapid7-plugin',
      version='1.0.0',
      description='This plugin allows for the creation, configuration, and starting of scans. The plugin can also retrieve scan results and logging related to the execution of the scan',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_rapid7_insightappsec']
      )
