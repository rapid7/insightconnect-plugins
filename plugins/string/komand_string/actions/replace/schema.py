# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Replace parts of a string"


class Input:
    IN_STRING = "in_string"
    REPLACEMENT_VALUE = "replacement_value"
    STRING_PART_TO_FIND = "string_part_to_find"


class Output:
    RESULT_STRING = "result_string"


class ReplaceInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "in_string": {
      "type": "string",
      "title": "In String",
      "description": "The string to replace parts of",
      "order": 1
    },
    "replacement_value": {
      "type": "string",
      "title": "Replacement Value",
      "description": "The string that will replace the parts that are found. If left blank the characters to find will be deleted",
      "order": 3
    },
    "string_part_to_find": {
      "type": "string",
      "title": "String Part to Find",
      "description": "The string part to look for. All instances of this string will be replaced",
      "order": 2
    }
  },
  "required": [
    "in_string",
    "string_part_to_find"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReplaceOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result_string": {
      "type": "string",
      "title": "Result String",
      "description": "The string after replacement",
      "order": 1
    }
  },
  "required": [
    "result_string"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
