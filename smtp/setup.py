# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='smtp-rapid7-plugin',
      version='2.0.5',
      description='Simple Mail Transfer Protocol (SMTP) is an Internet standard for electronic mail (email) transmission. Users of this plugin will be able to automatically send email through their Rapid7 InsightConnect workflows',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_smtp']
      )
