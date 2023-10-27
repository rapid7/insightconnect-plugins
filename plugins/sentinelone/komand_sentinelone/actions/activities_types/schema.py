# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of activity types"


class Input:
    pass


class Output:
    ACTIVITYTYPES = "activityTypes"


class ActivitiesTypesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ActivitiesTypesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "activityTypes": {
      "type": "array",
      "title": "Activity Types",
      "description": "List of activity types",
      "items": {
        "$ref": "#/definitions/activityTypes"
      },
      "order": 1
    }
  },
  "required": [
    "activityTypes"
  ],
  "definitions": {
    "activityTypes": {
      "type": "object",
      "title": "activityTypes",
      "properties": {
        "id": {
          "type": "integer",
          "title": "Type ID",
          "description": "Activity type ID",
          "order": 1
        },
        "descriptionTemplate": {
          "type": "string",
          "title": "Description Template",
          "description": "Activity description template as seen in activity page",
          "order": 2
        },
        "action": {
          "type": "string",
          "title": "Action",
          "description": "Action described in the activity",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
