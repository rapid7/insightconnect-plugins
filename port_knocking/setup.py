# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='port_knocking-rapid7-plugin',
      version='1.0.0',
      description='The Pork Knocking plugin knocks the specified ports on a host and optionally supports a payload',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_port_knocking']
      )
