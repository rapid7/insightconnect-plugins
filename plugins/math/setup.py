# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="math-rapid7-plugin",
    version="1.2.5",
    description="This plugin allows basic arithmetic functions to be performed",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={"console_scripts": ["komand_math = bin.komand_math:main"]},
)
