# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='ossec-rapid7-plugin',
      version='1.0.2',
      description='OSSEC is a free, open-source host-based intrusion detection system. Using the OSSEC plugin for InsightConnect, users can parse OSSEC alerts into JSON format',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_ossec']
      )
