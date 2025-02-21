# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extract data via regex from a string"


class Input:
    ASCII = "ascii"
    DOTALL = "dotall"
    IGNORECASE = "ignorecase"
    IN_REGEX = "in_regex"
    IN_STRING = "in_string"
    MULTILINE = "multiline"


class Output:
    MATCHES = "matches"


class DataExtractionInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ascii": {
      "type": "boolean",
      "title": "ASCII",
      "description": "Make \\w \\W \\b \\B follow ASCII rules",
      "default": false,
      "order": 6
    },
    "dotall": {
      "type": "boolean",
      "title": "Dot All",
      "description": "Make . match newline",
      "default": false,
      "order": 5
    },
    "ignorecase": {
      "type": "boolean",
      "title": "Ignore Case",
      "description": "Make regex non-case sensitive",
      "default": false,
      "order": 3
    },
    "in_regex": {
      "type": "string",
      "title": "Regex",
      "description": "Regex to use for data extraction",
      "order": 2
    },
    "in_string": {
      "type": "string",
      "title": "Input String",
      "description": "Input string",
      "order": 1
    },
    "multiline": {
      "type": "boolean",
      "title": "Multiline",
      "description": "Make begin/end consider each line",
      "default": false,
      "order": 4
    }
  },
  "required": [
    "in_regex",
    "in_string"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DataExtractionOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "matches": {
      "type": "array",
      "title": "Matches",
      "description": "An array of string arrays matching the output of Python re.findall()",
      "order": 1
    }
  },
  "required": [
    "matches"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
