# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='sleep-rapid7-plugin',
      version='1.0.2',
      description='Sleep allows Rapid7 InsightConnect users to suspend workflow execution for a specified period of time. Popular uses are to avoid rate limiting by a service or to wait for processing by a service to complete',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_sleep']
      )
