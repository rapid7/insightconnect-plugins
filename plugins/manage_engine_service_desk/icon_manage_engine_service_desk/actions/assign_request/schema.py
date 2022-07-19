# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This Operation allows you to assign a request to a technician or group. At least one input parameter (except Request ID) is required - Group or Technician. In every parameter containing `ID` and `Name` fields please provide only one of them"


class Input:
    GROUP = "group"
    REQUEST_ID = "request_id"
    TECHNICIAN = "technician"
    

class Output:
    REQUEST_ID = "request_id"
    STATUS = "status"
    STATUS_CODE = "status_code"
    

class AssignRequestInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group": {
      "$ref": "#/definitions/group",
      "title": "Group",
      "description": "The group to which the request belongs",
      "order": 2
    },
    "request_id": {
      "type": "integer",
      "title": "Request ID",
      "description": "The request id that should be assigned",
      "order": 1
    },
    "technician": {
      "$ref": "#/definitions/technician",
      "title": "Technician",
      "description": "The technician that was assigned to the request",
      "order": 3
    }
  },
  "required": [
    "request_id"
  ],
  "definitions": {
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Group's id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Group's name",
          "order": 2
        }
      }
    },
    "technician": {
      "type": "object",
      "title": "technician",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Technician ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Technician Name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AssignRequestOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "request_id": {
      "type": "integer",
      "title": "Request ID",
      "description": "The id of the assigned request",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status of the request",
      "order": 2
    },
    "status_code": {
      "type": "integer",
      "title": "Status Code",
      "description": "Status code of the request",
      "order": 3
    }
  },
  "required": [
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
