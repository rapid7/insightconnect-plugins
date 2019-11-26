# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Move a Github Issue between ZenHub Pipelines"


class Input:
    ISSUE_NUMBER = "issue_number"
    PIPELINE_ID = "pipeline_id"
    POSITION = "position"
    REPO_ID = "repo_id"
    

class Output:
    STATUS_CODE = "status_code"
    

class MoveIssueBetweenPipelinesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "issue_number": {
      "type": "integer",
      "title": "Issue Number",
      "description": "GitHub Issue Number",
      "order": 2
    },
    "pipeline_id": {
      "type": "string",
      "title": "Pipeline ID",
      "description": "ZenHub Pipeline ID",
      "order": 3
    },
    "position": {
      "type": "integer",
      "title": "Position",
      "description": "New Position in the ZenHub Pipeline (-1: bottom, 0: top, n: nth index)",
      "order": 4
    },
    "repo_id": {
      "type": "integer",
      "title": "Repository ID",
      "description": "GitHub Repository ID e.g. 24237263",
      "order": 1
    }
  },
  "required": [
    "issue_number",
    "pipeline_id",
    "position",
    "repo_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MoveIssueBetweenPipelinesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status_code": {
      "type": "integer",
      "title": "Status",
      "description": "HTTP status code",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
