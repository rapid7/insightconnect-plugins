# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Submit a URL to PhishTank"


class Input:
    URL = "url"


class Output:
    IN_DATABASE = "in_database"
    PHISH_DETAIL_PAGE = "phish_detail_page"
    PHISH_ID = "phish_id"
    URL = "url"
    VALID = "valid"
    VERIFIED = "verified"
    VERIFIED_AT = "verified_at"


class CheckInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL to Submit",
      "order": 1
    }
  },
  "required": [
    "url"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "in_database": {
      "type": "boolean",
      "title": "In Database",
      "description": "If the URL is in the PhishTank database",
      "order": 2
    },
    "phish_detail_page": {
      "type": "string",
      "title": "Phish Detail Page",
      "description": "PhishTank detail URL for the phish, where you can view data about the phish, including a screenshot and the community votes",
      "order": 4
    },
    "phish_id": {
      "type": "string",
      "title": "Phish ID",
      "description": "The ID number by which PhishTank refers to a phish submission",
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Submitted URL",
      "order": 1
    },
    "valid": {
      "type": "boolean",
      "title": "Valid",
      "description": "Whether the phish is valid or not",
      "order": 7
    },
    "verified": {
      "type": "boolean",
      "title": "Verified",
      "description": "Whether or not this phish has been verified by the PhishTank community",
      "order": 5
    },
    "verified_at": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Verified At",
      "description": "The date and time at which the phish was verified as valid by the PhishTank community",
      "order": 6
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
