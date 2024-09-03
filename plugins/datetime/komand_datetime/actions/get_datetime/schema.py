# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Gets the current Datetime in a specified format"


class Input:
    FORMAT_STRING = "format_string"
    USE_RFC3339_FORMAT = "use_rfc3339_format"


class Output:
    DATETIME = "datetime"
    EPOCH_TIMESTAMP = "epoch_timestamp"


class GetDatetimeInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "format_string": {
      "type": "string",
      "description": "Format string for the output",
      "default": "%d %b %Y %H:%M:%S",
      "order": 1
    },
    "use_rfc3339_format": {
      "type": "boolean",
      "title": "Use RFC3339 Format",
      "description": "Use RFC3339 format (eg. 2017-10-24T18:27:36.23Z). This is the most compatible date format for timestamp manipulation. Enabling this will override the format string input",
      "order": 2
    }
  },
  "required": [
    "format_string",
    "use_rfc3339_format"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetDatetimeOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "datetime": {
      "type": "string",
      "title": "Datetime",
      "description": "Datetime",
      "order": 1
    },
    "epoch_timestamp": {
      "type": "integer",
      "title": "Epoch Timestamp",
      "description": "Epoch timestamp",
      "order": 2
    }
  },
  "required": [
    "datetime",
    "epoch_timestamp"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
