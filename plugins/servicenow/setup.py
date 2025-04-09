# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="servicenow-rapid7-plugin",
    version="8.1.1",
    description="[ServiceNow](https://www.servicenow.com/) is a tool for managing incidents and configuration management. This plugin allows users to manage all aspects of incidents including creation, search, and updates. Additionally, incident changes can be monitored and processed for use in a Rapid7 InsightConnect workflow.Note: This plugin affects only the underlying tables in a ServiceNow instance, not its UI. Hence, this plugin will work seamlessly with Virtual Task Boards",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    entry_points={"console_scripts": ["icon_servicenow = bin.icon_servicenow:main"]},
)
