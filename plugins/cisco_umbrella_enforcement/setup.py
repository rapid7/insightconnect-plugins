# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="cisco_umbrella_enforcement-rapid7-plugin",
      version="1.0.2",
      description="This plugin utilizes Cisco Umbrella Enforcement to inherit the ability to send security events from platform/service/appliance within a customer environment to the Cisco security cloud for enforcement",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_cisco_umbrella_enforcement']
      )
