# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="palo_alto_pan_os-rapid7-plugin",
      version="6.1.7",
      description="[PAN-OS](https://www.paloaltonetworks.com/documentation/80/pan-os) is the software that runs all Palo Alto Networks next-generation firewalls. This plugin utilizes the [PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api) to provide programmatic management of the Palo Alto Firewall appliance(s). It supports managing firewalls individually or centralized via [Panorama](https://www.paloaltonetworks.com/network-security/panorama)",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_palo_alto_pan_os']
      )
