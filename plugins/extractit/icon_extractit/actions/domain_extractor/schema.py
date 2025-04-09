# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extracts all domain names from a string or file"


class Input:
    FILE = "file"
    STR = "str"
    SUBDOMAIN = "subdomain"


class Output:
    DOMAINS = "domains"


class DomainExtractorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "File",
      "description": "Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODF, TXT, ZIP",
      "order": 2
    },
    "str": {
      "type": "string",
      "title": "String",
      "description": "Input string",
      "order": 1
    },
    "subdomain": {
      "type": "boolean",
      "title": "Subdomain",
      "description": "Include subdomain in result",
      "order": 3
    }
  },
  "required": [
    "subdomain"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainExtractorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domains": {
      "type": "array",
      "title": "Domain Names",
      "description": "List of extracted Domain names",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
