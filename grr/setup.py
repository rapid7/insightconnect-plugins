# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='grr-rapid7-plugin',
      version='2.0.1',
      description='The GRR plugin allows you to organize and start hunts using GRR',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_grr']
      )
