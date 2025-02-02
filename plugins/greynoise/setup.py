# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="greynoise-greynoise-plugin",
      version="2.0.0",
      description="GreyNoise helps analysts recognize events not worth their attention. Indicators in GreyNoise are likely associated with opportunistic internet scanning or common business services, not targeted threats. This context helps analysts focus on what matters most",
      author="greynoise",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_greynoise']
      )
