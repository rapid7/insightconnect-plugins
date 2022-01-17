# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add Notes to Offense"


class Input:
    FIELDS = "fields"
    NOTE_TEXT = "note_text"
    OFFENSE_ID = "offense_id"


class Output:
    DATA = "data"


class AddNotesToOffenseInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "string",
      "title": "Fields",
      "description": "Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas",
      "order": 3
    },
    "note_text": {
      "type": "string",
      "title": "Note Text",
      "description": "The Note Text to add to offense",
      "order": 2
    },
    "offense_id": {
      "type": "integer",
      "title": "Offense Id",
      "description": "The ID of the offense in which you want to add note",
      "order": 1
    }
  },
  "required": [
    "note_text",
    "offense_id"
  ]
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddNotesToOffenseOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/note",
      "title": "Newly Added Offense Notes",
      "description": "JSON Data of the newly added Offense Notes ",
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
          "description": "Created Time",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "Id",
          "description": "Id",
          "order": 1
        },
        "note_text": {
          "type": "string",
          "title": "Note text",
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
