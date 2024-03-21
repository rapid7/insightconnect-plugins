# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get Offense Notes"


class Input:
    FIELDS = "fields"
    FILTER = "filter"
    OFFENSE_ID = "offense_id"
    RANGE = "range"


class Output:
    DATA = "data"


class GetOffenseNoteInput(insightconnect_plugin_runtime.Input):
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
      "description": "Restrict the elements in a list based on the contents of various fields. E.g. id=55 and username = admin",
      "order": 3
    },
    "offense_id": {
      "type": "integer",
      "title": "Offense ID",
      "description": "The ID of the offense to get notes for",
      "order": 1
    },
    "range": {
      "type": "string",
      "title": "Range",
      "description": "Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records",
      "default": "1-50",
      "order": 2
    }
  },
  "required": [
    "offense_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetOffenseNoteOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Offense Notes",
      "description": "JSON data of the Offense Notes",
      "items": {
        "$ref": "#/definitions/note"
      },
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
