# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="rapid7_surface_command-rapid7-plugin",
    version="1.0.0",
    description="Surface Command gives you full visibilty over your assets and identies across multiple technology platforms",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={"console_scripts": ["icon_rapid7_surface_command = bin.icon_rapid7_surface_command:main"]},
)
