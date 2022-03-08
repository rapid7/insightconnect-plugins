# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get the confidence index for a user"


class Input:
    FROMTIME = "fromTime"
    USERNAME = "username"
    

class Output:
    CONFIDENCES = "confidences"
    USERID = "userId"
    

class GetSingleUserConfidenceIndexInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fromTime": {
      "type": "integer",
      "title": "From Time",
      "description": "Numeric value representing the time in epoch timestamp from the beginning of which confidence score values are taken until now",
      "order": 2
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Username of an existing user",
      "order": 1
    }
  },
  "required": [
    "fromTime",
    "username"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSingleUserConfidenceIndexOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "confidences": {
      "type": "array",
      "title": "Confidences",
      "description": "Contains User Confidence Index with starting score and confidence score",
      "items": {
        "$ref": "#/definitions/confidence"
      },
      "order": 2
    },
    "userId": {
      "type": "string",
      "title": "User ID",
      "description": "Identifier of user",
      "order": 1
    }
  },
  "required": [
    "confidences",
    "userId"
  ],
  "definitions": {
    "confidence": {
      "type": "object",
      "title": "confidence",
      "properties": {
        "confidenceScore": {
          "type": "integer",
          "title": "Confidence Score",
          "description": "Numeric value representing user's confidence score",
          "order": 2
        },
        "start": {
          "type": "integer",
          "title": "Start",
          "description": "Numeric value representing epoch timestamp",
          "order": 1
        }
      },
      "required": [
        "confidenceScore",
        "start"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
