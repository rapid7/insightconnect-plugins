# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="sed-rapid7-plugin",
      version="2.0.3",
      description="The Sed plugin allows you to run the GNU stream editor on strings and files",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_sed']
      )
