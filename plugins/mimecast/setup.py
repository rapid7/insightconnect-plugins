# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="mimecast-rapid7-plugin",
      version="5.3.19",
      description="[Mimecast](https://www.mimecast.com) is a set of cloud services designed to provide next generation protection against advanced email-borne threats such as malicious URLs, malware, impersonation attacks, as well as internally generated threats, with a focus on email security. This plugin utilizes the [Mimecast API](https://www.mimecast.com/developer/documentation)",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_mimecast']
      )
