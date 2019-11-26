# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a single note for this project"


class Input:
    ID = "id"
    PROJECT_NAME = "project_name"
    

class Output:
    NOTE = "note"
    

class GetNoteInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Note ID",
      "description": "Note ID",
      "order": 2
    },
    "project_name": {
      "type": "string",
      "title": "Project Name",
      "description": "Project name",
      "order": 1
    }
  },
  "required": [
    "id",
    "project_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetNoteOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "note": {
      "$ref": "#/definitions/Note",
      "title": "Note",
      "description": "Project note",
      "order": 1
    }
  },
  "required": [
    "note"
  ],
  "definitions": {
    "Note": {
      "type": "object",
      "title": "Note",
      "properties": {
        "body": {
          "type": "string",
          "title": "Description",
          "description": "Note description",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Note ID",
          "order": 1
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Note title",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
