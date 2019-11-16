# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='subnet-rapid7-plugin',
      version='1.0.1',
      description='The Subnet plugin takes input as a network in CIDR notation and returns useful information, such as the number of hosts, the ID, host address range, and broadcast address',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_subnet']
      )
