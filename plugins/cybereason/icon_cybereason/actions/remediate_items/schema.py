# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Remediate a specific process, file or registry key if remediation is possible"


class Input:
    ACTIONS_BY_MACHINE = "actions_by_machine"
    INITIATOR_USER_NAME = "initiator_user_name"
    MALOP_ID = "malop_id"
    

class Output:
    RESPONSE = "response"
    

class RemediateItemsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "actions_by_machine": {
      "$ref": "#/definitions/remediate_items",
      "title": "Actions by Machine",
      "description": "Actions by machine",
      "order": 2
    },
    "initiator_user_name": {
      "type": "string",
      "title": "Initiator User Name",
      "description": "Initiator user name",
      "order": 1
    },
    "malop_id": {
      "type": "string",
      "title": "Malop ID",
      "description": "Malop ID to associate with the remediation actions",
      "order": 3
    }
  },
  "required": [
    "actions_by_machine",
    "initiator_user_name"
  ],
  "definitions": {
    "error": {
      "type": "object",
      "title": "error",
      "properties": {
        "errorType": {
          "type": "string",
          "title": "Error Type",
          "description": "The type of error",
          "order": 2
        },
        "message": {
          "type": "string",
          "title": "Message",
          "description": "A description of the error",
          "order": 1
        }
      }
    },
    "remediate_items": {
      "type": "object",
      "title": "remediate_items",
      "properties": {
        "end": {
          "type": "integer",
          "title": "End",
          "description": "The time (in epoch) that the remediation operation ended",
          "order": 4
        },
        "error": {
          "type": "array",
          "title": "Error",
          "description": "An object containing details of the error",
          "items": {
            "$ref": "#/definitions/error"
          },
          "order": 7
        },
        "initiatingUser": {
          "type": "string",
          "title": "Initiating User",
          "description": "The Cybereason user name of the user initiating the remediation",
          "order": 5
        },
        "malopId": {
          "type": "string",
          "title": "Malop ID",
          "description": "The numerical identifier of the Malop assigned by Cybereason",
          "order": 1
        },
        "remediationID": {
          "type": "string",
          "title": "Remediation ID",
          "description": "The numerical identifier of the Malop assigned by Cybereason",
          "order": 2
        },
        "start": {
          "type": "integer",
          "title": "Start",
          "description": "The time (in epoch) that the remediation operation began",
          "order": 3
        },
        "statusLog": {
          "type": "array",
          "title": "Status Log",
          "description": "An object containing information about the remediation",
          "items": {
            "$ref": "#/definitions/statusLog"
          },
          "order": 6
        }
      },
      "definitions": {
        "error": {
          "type": "object",
          "title": "error",
          "properties": {
            "errorType": {
              "type": "string",
              "title": "Error Type",
              "description": "The type of error",
              "order": 2
            },
            "message": {
              "type": "string",
              "title": "Message",
              "description": "A description of the error",
              "order": 1
            }
          }
        },
        "statusLog": {
          "type": "object",
          "title": "statusLog",
          "properties": {
            "actionType": {
              "type": "string",
              "title": "Action Type",
              "description": "The type of action you attempted to perform",
              "order": 4
            },
            "machineId": {
              "type": "string",
              "title": "Machine ID",
              "description": "The unique ID for the machine or machines on which the remediation was performed",
              "order": 1
            },
            "status": {
              "type": "string",
              "title": "Status",
              "description": "The status of the remediation request",
              "order": 3
            },
            "targetID": {
              "type": "string",
              "title": "Target ID",
              "description": "Reports a null value",
              "order": 2
            },
            "timestamp": {
              "type": "integer",
              "title": "Timestamp",
              "description": "The time (in epoch) of the status report for the remediation request",
              "order": 5
            }
          }
        }
      }
    },
    "statusLog": {
      "type": "object",
      "title": "statusLog",
      "properties": {
        "actionType": {
          "type": "string",
          "title": "Action Type",
          "description": "The type of action you attempted to perform",
          "order": 4
        },
        "machineId": {
          "type": "string",
          "title": "Machine ID",
          "description": "The unique ID for the machine or machines on which the remediation was performed",
          "order": 1
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the remediation request",
          "order": 3
        },
        "targetID": {
          "type": "string",
          "title": "Target ID",
          "description": "Reports a null value",
          "order": 2
        },
        "timestamp": {
          "type": "integer",
          "title": "Timestamp",
          "description": "The time (in epoch) of the status report for the remediation request",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemediateItemsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "type": "object",
      "title": "Malop Response",
      "description": "Malop response",
      "order": 1
    }
  },
  "required": [
    "response"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
