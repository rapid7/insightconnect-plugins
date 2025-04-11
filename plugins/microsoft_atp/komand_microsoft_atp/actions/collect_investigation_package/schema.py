# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Collects investigation package from a machine"


class Input:
    COMMENT = "comment"
    MACHINE = "machine"


class Output:
    COLLECT_INVESTIGATION_PACKAGE_RESPONSE = "collect_investigation_package_response"


class CollectInvestigationPackageInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment to associate with the action",
      "default": "Investigation package collected via InsightConnect",
      "order": 2
    },
    "machine": {
      "type": "string",
      "title": "Machine",
      "description": "Machine IP address, hostname, or machine ID",
      "order": 1
    }
  },
  "required": [
    "machine"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CollectInvestigationPackageOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "collect_investigation_package_response": {
      "$ref": "#/definitions/machine_action",
      "title": "Collect Investigation Package Response",
      "description": "A response that includes information about the action taken",
      "order": 1
    }
  },
  "required": [
    "collect_investigation_package_response"
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
          "description": "Last update date time UTC",
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
