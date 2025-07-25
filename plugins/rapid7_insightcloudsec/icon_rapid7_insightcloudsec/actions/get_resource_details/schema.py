# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get all of the details about a resource based on provided resource ID"


class Input:
    RESOURCEID = "resourceId"


class Output:
    RESOURCEDETAILS = "resourceDetails"


class GetResourceDetailsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "resourceId": {
      "type": "string",
      "title": "Resource ID",
      "description": "ID of the resource",
      "order": 1
    }
  },
  "required": [
    "resourceId"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetResourceDetailsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "resourceDetails": {
      "$ref": "#/definitions/resourceDetails",
      "title": "Resource Details",
      "description": "Information about the resource for the provided ID",
      "order": 1
    }
  },
  "definitions": {
    "resourceDetails": {
      "type": "object",
      "title": "resourceDetails",
      "properties": {
        "dependencies": {
          "type": "object",
          "title": "Dependencies",
          "description": "Dependencies for the provided resource ID",
          "order": 1
        },
        "details": {
          "type": "object",
          "title": "Details",
          "description": "Details for the provided resource ID",
          "order": 2
        },
        "relatedResources": {
          "type": "object",
          "title": "Related Resources",
          "description": "Related resources with the provided resource ID",
          "order": 3
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
