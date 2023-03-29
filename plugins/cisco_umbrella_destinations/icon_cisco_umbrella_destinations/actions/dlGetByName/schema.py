# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get destination list by name"


class Input:
    NAME = "name"
    

class Output:
    SUCCESS = "success"
    

class DlGetByNameInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Title for the destination list",
      "order": 1
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DlGetByNameOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "array",
      "title": "Success",
      "description": "Successful returned value",
      "items": {
        "$ref": "#/definitions/destinationList"
      },
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "destinationList": {
      "type": "object",
      "title": "destinationList",
      "properties": {
        "access": {
          "type": "string",
          "title": "Access",
          "description": "Allow or block access to domain",
          "order": 2
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "The unix UTC timestamp in milliseconds for creation of the destination list",
          "order": 6
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique ID of the destination list",
          "order": 1
        },
        "isGlobal": {
          "type": "boolean",
          "title": "Is Global",
          "description": "Boolean value indicating global state",
          "order": 3
        },
        "isMspDefault": {
          "type": "boolean",
          "title": "Is MSP Default",
          "description": "Whether or not MSP is default",
          "order": 8
        },
        "markedForDeletion": {
          "type": "boolean",
          "title": "Marked for Deletion",
          "description": "Whether or not destination list is marked for deletion",
          "order": 9
        },
        "modifiedAt": {
          "type": "integer",
          "title": "Modified At",
          "description": "The unix UTC timestamp in milliseconds for modification of the destination list",
          "order": 7
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Title for the destination list",
          "order": 4
        },
        "thirdpartyCategoryId": {
          "type": "integer",
          "title": "Third Party Category ID",
          "description": "ID, if any, for third parties",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
