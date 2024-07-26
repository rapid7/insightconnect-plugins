# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="html-rapid7-plugin",
      version="1.2.6",
      description="Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. This plugin provides the ability to convert an HTML document into a variety of formats using [pypandoc](https://pypi.python.org/pypi/pypandoc). Supported formats are: DOCX, EPUB, Markdown, PDF, HTML5, Plain Text",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_html']
      )
