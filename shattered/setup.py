# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='shattered-rapid7-plugin',
      version='1.0.0',
      description='SHAttered is a free service for checking SHA-1 hash collisions. Using the SHAttered plugin for Rapid7 InsightConnect, users can quickly determine if a file is part of a collision attack',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_shattered']
      )
