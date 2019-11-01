# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Creates a new Checkmarx Scan"


class Input:
    COMMENT = "comment"
    FORCESCAN = "forceScan"
    ISINCREMENTAL = "isIncremental"
    ISPUBLIC = "isPublic"
    PROJECTID = "projectId"
    

class Output:
    ID = "id"
    LINK = "link"
    

class CreateScanInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Specifies the scan comment",
      "order": 5
    },
    "forceScan": {
      "type": "boolean",
      "title": "Force Scan",
      "description": "Specifies whether the code should be scanned or not, regardless of whether changes were made to the code since the last scan",
      "order": 4
    },
    "isIncremental": {
      "type": "boolean",
      "title": "Is Incremental",
      "description": "Specifies whether the requested scan is incremental or full scan",
      "order": 2
    },
    "isPublic": {
      "type": "boolean",
      "title": "Is Public",
      "description": "Specifies whether the requested scan is public or private",
      "order": 3
    },
    "projectId": {
      "type": "integer",
      "title": "Project ID",
      "description": "Unique ID of the project to be scanned",
      "order": 1
    }
  },
  "required": [
    "comment",
    "forceScan",
    "isIncremental",
    "isPublic",
    "projectId"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateScanOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of the created scan",
      "order": 1
    },
    "link": {
      "$ref": "#/definitions/link",
      "title": "Link",
      "description": "Metadata about the scan",
      "order": 2
    }
  },
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Relation of the link",
          "order": 1
        },
        "uri": {
          "type": "string",
          "title": "URI",
          "description": "Relative URL of the project",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
