# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve details about an action taken on a machine"


class Input:
    ACTION_ID = "action_id"
    

class Output:
    MACHINE_ACTION_RESPONSE = "machine_action_response"
    

class GetMachineActionInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action_id": {
      "type": "string",
      "title": "Action ID",
      "description": "Action ID",
      "order": 1
    }
  },
  "required": [
    "action_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetMachineActionOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine_action_response": {
      "$ref": "#/definitions/machine_action",
      "title": "Machine Action Response",
      "description": "A response that includes the result of the action, and supplemental information about the action taken",
      "order": 1
    }
  },
  "required": [
    "machine_action_response"
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
