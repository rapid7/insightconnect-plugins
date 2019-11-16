# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get all elements in a list"


class Input:
    COUNT = "count"
    KEY = "key"
    

class Output:
    FOUND = "found"
    VALUES = "values"
    

class ListGetInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Max results to return",
      "default": 1000,
      "order": 2
    },
    "key": {
      "type": "string",
      "title": "Key",
      "description": "Key to get",
      "order": 1
    }
  },
  "required": [
    "key"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListGetOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "True if found",
      "order": 1
    },
    "values": {
      "type": "array",
      "title": "Values",
      "description": "Values",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
