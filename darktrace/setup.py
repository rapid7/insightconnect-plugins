# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="darktrace-rapid7-plugin",
      version="1.0.0",
      description="This plugin utilizes DarkTrace to  detects novel attacks and insider threats at an early stage",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_darktrace']
      )
