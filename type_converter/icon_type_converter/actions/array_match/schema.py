# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Identify matched items present across two arrays"


class Input:
    ARRAY1 = "array1"
    ARRAY2 = "array2"
    DEDUPLICATES = "deduplicates"
    

class Output:
    COUNT = "count"
    MATCHES_ARRAY = "matches_array"
    

class ArrayMatchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "array1": {
      "type": "array",
      "title": "Array1",
      "description": "First array",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "array2": {
      "type": "array",
      "title": "Array2",
      "description": "Second array",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "deduplicates": {
      "type": "boolean",
      "title": "Deduplicates",
      "description": "Set to true to return first matches items, set to false to return all matches",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "array1",
    "array2"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ArrayMatchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Count of matches",
      "order": 2
    },
    "matches_array": {
      "type": "array",
      "title": "Matches Array",
      "description": "Array containing items found in both the first and second arrays",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "count",
    "matches_array"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
