# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a comment to an incident"


class Input:
    BODY = "body"
    INCIDENT_ID = "incident_id"
    IS_PRIVATE = "is_private"
    

class Output:
    COMMENT = "comment"
    

class CommentIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "body": {
      "type": "string",
      "title": "Body",
      "description": "The contents of the comment",
      "order": 2
    },
    "incident_id": {
      "type": "integer",
      "title": "Incident ID",
      "description": "ID of an incident to add the comment to",
      "order": 1
    },
    "is_private": {
      "type": "boolean",
      "title": "Is Private",
      "description": "Is the comment private or public?",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "body",
    "incident_id",
    "is_private"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CommentIncidentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "$ref": "#/definitions/samanage_comment",
      "title": "Comment",
      "description": "Newly created comment",
      "order": 1
    }
  },
  "required": [
    "comment"
  ],
  "definitions": {
    "samanage_comment": {
      "type": "object",
      "title": "samanage_comment",
      "properties": {
        "body": {
          "type": "string",
          "title": "Body",
          "description": "The contents of the comment",
          "order": 1
        },
        "is_private": {
          "type": "boolean",
          "title": "Is Private",
          "description": "Is the comment private or public?",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
