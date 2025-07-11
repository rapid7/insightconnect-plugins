# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="cylance_protect-rapid7-plugin",
    version="1.5.5",
    description="The [BlackBerry CylancePROTECT](https://www.cylance.com/en-us/platform/products/cylance-protect.html) plugin allows you to automate response operations for CylancePROTECT and CylanceOPTICS",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={"console_scripts": ["icon_cylance_protect = bin.icon_cylance_protect:main"]},
)
