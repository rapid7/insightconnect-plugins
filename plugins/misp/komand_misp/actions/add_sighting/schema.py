# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a sighting to attribute"


class Input:
    ATTRIBUTE = "attribute"
    DATE = "date"
    SOURCE = "source"
    TIME = "Time"
    TYPE = "type"


class Output:
    SIGHTING = "sighting"


class AddSightingInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Time": {
      "type": "string",
      "title": "Time",
      "description": "The time of the sighting to be added to the attribute (if none is provided it will default to now)",
      "order": 5
    },
    "attribute": {
      "type": "integer",
      "title": "Attribute",
      "description": "The ID of the attribute to add the sighting to",
      "order": 1
    },
    "date": {
      "type": "string",
      "title": "Date",
      "description": "The date of the sighting to be added to the attribute (if none is provided it will default to now)",
      "order": 4
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "The source of the sighting to be added to the attribute",
      "order": 3
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "The type of sighting to be added to the attribute",
      "enum": [
        "Sighting",
        "False-positive",
        "Expiration"
      ],
      "order": 2
    }
  },
  "required": [
    "attribute",
    "type"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddSightingOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sighting": {
      "type": "object",
      "title": "Sighting",
      "description": "Whether any of the sightings provided were added",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
