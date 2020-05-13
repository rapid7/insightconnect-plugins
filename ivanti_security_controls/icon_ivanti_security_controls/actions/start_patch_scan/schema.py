# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Start a patch scan"


class Input:
    CREDENTIAL_ID = "credential_id"
    DIAGNOSTIC_TRACE_ENABLED = "diagnostic_trace_enabled"
    HOSTNAMES = "hostnames"
    MACHINE_GROUP_IDS = "machine_group_ids"
    NAME = "name"
    RUN_AS_CREDENTIAL_ID = "run_as_credential_id"
    TEMPLATE_ID = "template_id"
    USE_MACHINE_CREDENTIAL = "use_machine_credential"
    

class Output:
    SCAN_DETAILS = "scan_details"
    

class StartPatchScanInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credential_id": {
      "type": "string",
      "title": "Credential ID",
      "description": "Credential ID",
      "order": 4
    },
    "diagnostic_trace_enabled": {
      "type": "boolean",
      "title": "Diagnostic Trace Enabled",
      "description": "An indication whether diagnostics tracing should be enabled during scan",
      "order": 3
    },
    "hostnames": {
      "type": "array",
      "title": "Hostnames",
      "description": "Hostnames - Either hostnames or machine group IDs must be specified",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "machine_group_ids": {
      "type": "array",
      "title": "Machine Group IDs",
      "description": "List of machine groups to scan. Either hostnames or machine group IDs must be specified",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name to be given to scan",
      "order": 5
    },
    "run_as_credential_id": {
      "type": "string",
      "title": "Run as Credential ID",
      "description": "Reference to a credential to use to start a scan. Overwrites RunAsDefault behavior",
      "order": 6
    },
    "template_id": {
      "type": "string",
      "title": "Patch Scan Template ID",
      "description": "Patch scan template ID",
      "order": 7
    },
    "use_machine_credential": {
      "type": "boolean",
      "title": "Use Machine Credential",
      "description": "An indication whether to use machine credentials. If No is specified, then either group-level credentials, default credentials or integrated Windows authentication credentials (in that order) will be used. This parameter is only used if an endpoint name is specified",
      "order": 8
    }
  },
  "required": [
    "template_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class StartPatchScanOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_details": {
      "$ref": "#/definitions/scan_details",
      "title": "Scan Details",
      "description": "Scan details",
      "order": 1
    }
  },
  "required": [
    "scan_details"
  ],
  "definitions": {
    "scan_details": {
      "type": "object",
      "title": "scan_details",
      "properties": {
        "id": {
          "type": "string",
          "title": "Scan ID",
          "description": "Scan ID",
          "order": 1
        },
        "isComplete": {
          "type": "boolean",
          "title": "Is Complete",
          "description": "Is complete",
          "order": 2
        },
        "links": {
          "type": "object",
          "title": "Scan Links",
          "description": "Scan links",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Scan Name",
          "description": "Scan name",
          "order": 4
        },
        "scanType": {
          "type": "string",
          "title": "Scan Type",
          "description": "Scan Type",
          "order": 5
        },
        "startedOn": {
          "type": "string",
          "title": "Scan Start Time",
          "description": "Scan start time",
          "order": 6
        },
        "updatedOn": {
          "type": "string",
          "title": "Update Time",
          "description": "Update Time",
          "order": 7
        },
        "user": {
          "type": "string",
          "title": "Username",
          "description": "Username",
          "order": 8
        }
      },
      "required": [
        "id",
        "isComplete",
        "links",
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
