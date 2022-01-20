# GENERATED BY KOMAND SDK - DO NOT EDIT
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
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "string",
      "title": "Fields",
      "description": "Specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas",
      "order": 4
    },
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Restrict the elements in a list based on the contents of various fields",
      "order": 3
    },
    "offense_id": {
      "type": "integer",
      "title": "Offense Id",
      "description": "The ID of the offense to get notes for",
      "order": 1
    },
    "range": {
      "type": "string",
      "title": "Range",
      "description": "Restrict the number of returned elements to a range, eg. 0-10, with 0 being the first index",
      "order": 2
    }
  },
  "required": [
    "offense_id"
  ]
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetOffenseNoteOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        """
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
        "create_time": {
          "type": "integer",
          "title": "Created Time",
          "description": "Created time",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
