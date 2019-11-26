# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='echotrail-echotrail-plugin',
      version='1.0.2',
      description='EchoTrail Insights is a database of executable behavioral analytics, searchable by filename or SHA256 or MD5 hash. Users can lookup filenames and hashes using the EchoTrail Insights plugin for Rapid7 InsightConnect',
      author='echotrail',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_echotrail']
      )
