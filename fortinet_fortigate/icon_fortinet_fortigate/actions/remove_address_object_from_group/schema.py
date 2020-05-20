# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = ""


class Input:
    ADDRESS_OBJECT = "address_object"
    GROUP = "group"
    

class Output:
    RESULT_OBJECT = "result_object"
    SUCCESS = "success"
    

class RemoveAddressObjectFromGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_object": {
      "type": "string",
      "title": "Address Object",
      "description": "Address object",
      "order": 2
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Group name",
      "order": 1
    }
  },
  "required": [
    "address_object",
    "group"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveAddressObjectFromGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result_object": {
      "type": "object",
      "title": "Result Object",
      "description": "An object containing the results of the action",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was the operation successful",
      "order": 1
    }
  },
  "required": [
    "result_object",
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
