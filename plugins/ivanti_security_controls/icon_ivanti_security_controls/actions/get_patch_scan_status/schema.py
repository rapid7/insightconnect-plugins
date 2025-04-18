# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get patch scan status"


class Input:
    SCAN_ID = "scan_id"


class Output:
    PATCH_SCAN_STATUS_DETAILS = "patch_scan_status_details"


class GetPatchScanStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_id": {
      "type": "string",
      "title": "Scan ID",
      "description": "Scan ID",
      "order": 1
    }
  },
  "required": [
    "scan_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPatchScanStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "patch_scan_status_details": {
      "$ref": "#/definitions/patch_scan_status_details",
      "title": "Patch Scan Status Details",
      "description": "Patch scan status details",
      "order": 1
    }
  },
  "required": [
    "patch_scan_status_details"
  ],
  "definitions": {
    "patch_scan_status_details": {
      "type": "object",
      "title": "patch_scan_status_details",
      "properties": {
        "consoleName": {
          "type": "string",
          "title": "Console Name",
          "description": "Console Name",
          "order": 1
        },
        "definitionDate": {
          "type": "string",
          "title": "Definition Date",
          "description": "Definition Date",
          "order": 2
        },
        "definitionVersion": {
          "type": "string",
          "title": "Definition Version",
          "description": "Definition version",
          "order": 3
        },
        "expectedResultTotal": {
          "type": "integer",
          "title": "Expected Result Total",
          "description": "Expected result total count",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Scan ID",
          "description": "Scan ID",
          "order": 5
        },
        "isComplete": {
          "type": "boolean",
          "title": "Is Complete",
          "description": "Is Complete",
          "order": 6
        },
        "links": {
          "type": "object",
          "title": "Links",
          "description": "Scan links",
          "order": 7
        },
        "name": {
          "type": "string",
          "title": "Scan Name",
          "description": "Scan name",
          "order": 8
        },
        "receivedResultCount": {
          "type": "integer",
          "title": "Received Result Count",
          "description": "Received result count",
          "order": 9
        },
        "scanType": {
          "type": "string",
          "title": "Scan Type",
          "description": "Scan Type",
          "order": 10
        },
        "startedOn": {
          "type": "string",
          "title": "Scan Start Time",
          "description": "Scan start time",
          "order": 11
        },
        "updatedOn": {
          "type": "string",
          "title": "Update Time",
          "description": "Update time",
          "order": 12
        },
        "user": {
          "type": "string",
          "title": "Username",
          "description": "Username",
          "order": 13
        }
      },
      "required": [
        "consoleName",
        "expectedResultTotal",
        "id",
        "isComplete",
        "links",
        "name",
        "receivedResultCount",
        "scanType",
        "startedOn",
        "updatedOn",
        "user"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
