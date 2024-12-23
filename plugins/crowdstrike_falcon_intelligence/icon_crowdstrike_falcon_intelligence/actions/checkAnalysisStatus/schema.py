# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes"


class Input:
    IDS = "ids"


class Output:
    SUBMISSIONS = "submissions"


class CheckAnalysisStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ids": {
      "type": "array",
      "title": "IDs",
      "description": "List of submitted malware samples ids. Find a submission ID from the response when submitting a malware sample or search with `Get Submissions IDs` action",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "ids"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckAnalysisStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "submissions": {
      "type": "array",
      "title": "Submissions",
      "description": "List of submissions",
      "items": {
        "$ref": "#/definitions/submission"
      },
      "order": 1
    }
  },
  "required": [
    "submissions"
  ],
  "definitions": {
    "submission": {
      "type": "object",
      "title": "submission",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "cid": {
          "type": "string",
          "title": "Cid",
          "description": "Cid",
          "order": 2
        },
        "userId": {
          "type": "string",
          "title": "User ID",
          "description": "User ID",
          "order": 3
        },
        "userName": {
          "type": "string",
          "title": "User Name",
          "description": "User name",
          "order": 4
        },
        "userUuid": {
          "type": "string",
          "title": "User UUID",
          "description": "User UUID",
          "order": 5
        },
        "origin": {
          "type": "string",
          "title": "Origin",
          "description": "Origin",
          "order": 6
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 7
        },
        "createdTimestamp": {
          "type": "string",
          "title": "Created Timestamp",
          "description": "Created timestamp",
          "order": 8
        },
        "sandbox": {
          "type": "array",
          "title": "Sandbox",
          "description": "Sandbox",
          "items": {
            "$ref": "#/definitions/sandboxShort"
          },
          "order": 9
        },
        "userTags": {
          "type": "array",
          "title": "User Tags",
          "description": "User tags",
          "items": {
            "type": "string"
          },
          "order": 10
        }
      }
    },
    "sandboxShort": {
      "type": "object",
      "title": "sandboxShort",
      "properties": {
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "SHA256",
          "order": 1
        },
        "submitUrl": {
          "type": "string",
          "title": "Submit URL",
          "description": "Submit URL",
          "order": 2
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 3
        },
        "actionScript": {
          "type": "string",
          "title": "Action Script",
          "description": "Action script",
          "order": 4
        },
        "systemDate": {
          "type": "string",
          "title": "System Date",
          "description": "System date",
          "order": 5
        },
        "systemTime": {
          "type": "string",
          "title": "System Time",
          "description": "System time",
          "order": 6
        },
        "networkSettings": {
          "type": "string",
          "title": "Network Settings",
          "description": "Network settings",
          "order": 7
        },
        "environmentId": {
          "type": "integer",
          "title": "Environment ID",
          "description": "Environment ID",
          "order": 8
        },
        "environmentDescription": {
          "type": "string",
          "title": "Environment Description",
          "description": "Environment description",
          "order": 9
        },
        "fileType": {
          "type": "string",
          "title": "File Type",
          "description": "File type",
          "order": 10
        },
        "submitName": {
          "type": "string",
          "title": "Submit Name",
          "description": "Submit name",
          "order": 11
        },
        "submissionType": {
          "type": "string",
          "title": "Submission Type",
          "description": "Submission type",
          "order": 12
        },
        "verdict": {
          "type": "string",
          "title": "Verdict",
          "description": "Verdict",
          "order": 13
        },
        "sampleFlags": {
          "type": "array",
          "title": "Sample Flags",
          "description": "Sample flags",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "errorMessage": {
          "type": "string",
          "title": "Error Message",
          "description": "Error message",
          "order": 15
        },
        "errorType": {
          "type": "string",
          "title": "Error Type",
          "description": "Error type",
          "order": 16
        },
        "errorOrigin": {
          "type": "string",
          "title": "Error Origin",
          "description": "Error origin",
          "order": 17
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
