# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='urlscan-rapid7-plugin',
      version='2.1.2',
      description='The URLScan plugin uses URLScan to analyze urls for malicious indicators',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_urlscan']
      )
