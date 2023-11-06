# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="velociraptor_legacy-jbauvinet-plugin",
    version="1.0.0",
    description="Velociraptor is a unique, advanced open-source endpoint monitoring, digital forensic and cyber response platform. It provides you with the ability to more effectively respond to a wide range of digital forensic and cyber incident response investigations and data breaches",
    author="jbauvinet",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=[
        "insightconnect-plugin-runtime"
    ],  # Add third-party dependencies to requirements.txt, not here!
    scripts=["bin/icon_velociraptor_legacy"],
)
