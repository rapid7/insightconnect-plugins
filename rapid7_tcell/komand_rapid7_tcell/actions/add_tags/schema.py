# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add all the tags posted in the body to the set of tags the app already has"


class Input:
    APP_ID = "app_id"
    TAGS = "tags"
    

class Output:
    SUCCESS = "success"
    

class AddTagsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "App ID",
      "order": 1
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "List of strings, choosing the new tags for the application",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "app_id",
    "tags"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddTagsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Successfully updated tags",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
