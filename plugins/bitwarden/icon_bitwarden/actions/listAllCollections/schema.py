# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return a list of your organization's collections. Collection objects listed in this call do not include information about their associated groups"


class Input:
    pass


class Output:
    COLLECTIONS = "collections"


class ListAllCollectionsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAllCollectionsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "collections": {
      "type": "array",
      "title": "Collections",
      "description": "List of collections",
      "items": {
        "$ref": "#/definitions/collectionObject"
      },
      "order": 1
    }
  },
  "definitions": {
    "collectionObject": {
      "type": "object",
      "title": "collectionObject",
      "properties": {
        "externalId": {
          "type": "string",
          "title": "External ID",
          "description": "External identifier for reference or linking this collection to another system",
          "order": 1
        },
        "object": {
          "type": "string",
          "title": "Object",
          "description": "String representing the object's type. Objects of the same type share the same properties",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The collection's unique identifier",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
