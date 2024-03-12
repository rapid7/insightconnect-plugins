# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Quarantine (isolate) endpoint an endpoint"


class Input:
    AGENT = "agent"
    QUARANTINE_STATE = "quarantine_state"
    WHITELIST = "whitelist"


class Output:
    SUCCESS = "success"
    WHITELISTED = "whitelisted"


class QuarantineInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent to perform quarantine action on. This must be either a MAC address or hostname",
      "order": 1
    },
    "quarantine_state": {
      "type": "boolean",
      "title": "Quarantine State",
      "description": "True to quarantine host, false to unquarantine host",
      "default": true,
      "order": 3
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "MAC addresses for machines to avoid quarantining. Both hyphenated and colon-delimited formats are acceptable",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "agent",
    "quarantine_state"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QuarantineOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not the quarantine/unquarantine was successful",
      "order": 1
    },
    "whitelisted": {
      "type": "boolean",
      "title": "Whitelisted",
      "description": "Whether or not the quarantine/unquarantine failed due to whitelisting",
      "order": 2
    }
  },
  "required": [
    "success",
    "whitelisted"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
