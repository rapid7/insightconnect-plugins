# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="redhat_advisory-rapid7-plugin",
      version="1.0.3",
      description="This plugin will trigger workflows on new Red Hat Security Advisories",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_redhat_advisory']
      )
