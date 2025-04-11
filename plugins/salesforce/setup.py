# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(
    name="salesforce-rapid7-plugin",
    version="2.1.13",
    description="[Salesforce](https://www.salesforce.com) is a CRM solution that brings together all customer information in a single, integrated platform that enables building a customer-centered business from marketing right through to sales, customer service and business analysis. The Salesforce plugin allows you to search, update, and manage salesforce records. This plugin utilizes the [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm)",
    author="rapid7",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=["insightconnect-plugin-runtime"],  # Add third-party dependencies to requirements.txt, not here!
    scripts=["bin/komand_salesforce"],
)
