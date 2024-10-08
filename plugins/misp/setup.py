# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="misp-rapid7-plugin",
      version="6.0.0",
      description="[MISP](http://www.misp-project.org/) is an open source threat sharing platform. Gather, store and then find correlations of indicators of compromise. Quality of data is determined by the open source community. This plugin utilizes the [MISP API](https://circl.lu/doc/misp/automation/index.html) and leverages the [pymisp](https://github.com/CIRCL/PyMISP) library",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_misp']
      )
