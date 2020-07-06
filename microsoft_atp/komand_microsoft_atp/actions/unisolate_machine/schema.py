# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Restore network connectivity to a machine"


class Input:
    COMMENT = "comment"
    MACHINE_ID = "machine_id"
    

class Output:
    MACHINE_ISOLATION_RESPONSE = "machine_isolation_response"
    

class UnisolateMachineInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment to associate with the unisolate action",
      "order": 2
    },
    "machine_id": {
      "type": "string",
      "title": "Machine ID",
      "description": "Machine ID",
      "order": 1
    }
  },
  "required": [
    "comment",
    "machine_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UnisolateMachineOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine_isolation_response": {
      "$ref": "#/definitions/machine_action",
      "title": "Machine Action Response",
      "description": "A response that includes the result of the action, and supplemental information about the action taken",
      "order": 1
    }
  },
  "required": [
    "machine_isolation_response"
  ],
  "definitions": {
    "machine_action": {
      "type": "object",
      "title": "machine_action",
      "properties": {
        "creationDateTimeUtc": {
          "type": "string",
          "title": "Creation Date Time UTC",
          "description": "Creation date time UTC",
          "order": 1
        },
        "errorHResult": {
          "type": "integer",
          "title": "Error HResult",
          "description": "Error HResult",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 3
        },
        "lastUpdateDateTimeUtc": {
          "type": "string",
          "title": "Last Update Date Time UTC",
          "description": "Last update date time utc",
          "order": 4
        },
        "machineId": {
          "type": "string",
          "title": "Machine ID",
          "description": "Machine ID",
          "order": 5
        },
        "requestor": {
          "type": "string",
          "title": "Requestor",
          "description": "Requestor",
          "order": 6
        },
        "requestorComment": {
          "type": "string",
          "title": "Requestor Comment",
          "description": "Requestor comment",
          "order": 7
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 8
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
