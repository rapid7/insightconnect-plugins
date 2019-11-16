# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get key's hash"


class Input:
    KEY = "key"
    

class Output:
    FOUND = "found"
    VALUES = "values"
    

class HashGetInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
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


class HashGetOutput(komand.Output):
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
      "type": "object",
      "title": "Values",
      "description": "Values",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
