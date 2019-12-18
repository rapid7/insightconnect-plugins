# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='haveibeenpwned-rapid7-plugin',
      version='4.0.2',
      description='Determine if a user, domain, or password has been leaked via data available in the Have I Been Pwned database',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_haveibeenpwned']
      )
