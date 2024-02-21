# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves reputation score of specified domain name"


class Input:
    DOMAIN = "domain"
    INCLUDE_REASONS = "include_reasons"


class Output:
    RESPONSE = "response"


class ReputationInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "description": "Input domain for which the risk score is desired",
      "order": 1
    },
    "include_reasons": {
      "type": "boolean",
      "description": "Return a list of reasons for the risk score determination",
      "default": false,
      "order": 2
    }
  },
  "required": [
    "domain"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReputationOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/reputation_response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "reputation_response": {
      "type": "object",
      "title": "reputation_response",
      "properties": {
        "domain": {
          "type": "string",
          "order": 1
        },
        "risk_score": {
          "type": "integer",
          "order": 2
        },
        "reasons": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
