# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get Offense Notes by ID"


class Input:
    FIELDS = "fields"
    FILTER = "filter"
    NOTE_ID = "note_id"
    OFFENSE_ID = "offense_id"


class Output:
    DATA = "data"


class GetOffenseNoteByIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "string",
      "title": "Fields",
      "description": "Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, create_time, username, note_text. More information about the fields can be found in plugin documentation",
      "order": 4
    },
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Restrict the elements in a list based on the contents of various fields",
      "order": 3
    },
    "note_id": {
      "type": "integer",
      "title": "Note ID",
      "description": "The ID of the offense note to get",
      "order": 2
    },
    "offense_id": {
      "type": "integer",
      "title": "Offense ID",
      "description": "The ID of the offense to get notes for",
      "order": 1
    }
  },
  "required": [
    "note_id",
    "offense_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetOffenseNoteByIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/note",
      "title": "Offense Notes by ID",
      "description": "JSON data of the Offense Notes for given ID",
      "order": 1
    }
  },
  "definitions": {
    "note": {
      "type": "object",
      "title": "note",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "create_time": {
          "type": "integer",
          "title": "Created Time",
          "description": "Created time",
          "order": 2
        },
        "note_text": {
          "type": "string",
          "title": "Note Text",
          "description": "Note text",
          "order": 3
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "Username",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
