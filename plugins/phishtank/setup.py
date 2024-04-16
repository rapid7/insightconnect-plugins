# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="phishtank-rapid7-plugin",
      version="2.0.1",
      description="Phishtank is a community-driven anti-phishing site where users submit suspected phishes and other users 'vote' if it is a phish or not. This plugin utilizes the Phishtank API to look up URLs in the PhishTank database",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_phishtank']
      )
