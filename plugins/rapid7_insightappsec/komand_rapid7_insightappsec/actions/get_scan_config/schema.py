# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a scan configuration"


class Input:
    SCAN_CONFIG_ID = "scan_config_id"


class Output:
    APP_ID = "app_id"
    ATTACK_TEMPLATE_ID = "attack_template_id"
    CONFIG_DESCRIPTION = "config_description"
    CONFIG_NAME = "config_name"
    ERRORS = "errors"
    ID = "id"
    LINKS = "links"


class GetScanConfigInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_config_id": {
      "type": "string",
      "title": "Scan Config ID",
      "description": "Scan configuration UUID",
      "order": 1
    }
  },
  "required": [
    "scan_config_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetScanConfigOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "App UUID",
      "order": 4
    },
    "attack_template_id": {
      "type": "string",
      "title": "Attack Template ID",
      "description": "Attack template UUID",
      "order": 5
    },
    "config_description": {
      "type": "string",
      "title": "Description",
      "description": "The description of the scan configuration",
      "order": 3
    },
    "config_name": {
      "type": "string",
      "title": "Name",
      "description": "The name of the scan configuration",
      "order": 2
    },
    "errors": {
      "type": "array",
      "title": "Errors",
      "description": "A list of errors that detail any current validation failures",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "id": {
      "type": "string",
      "title": "UUID",
      "description": "The UUID of the scan configuration",
      "order": 1
    },
    "links": {
      "type": "array",
      "title": "Links",
      "description": "A list of links",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 7
    }
  },
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "description": "Href",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "rel",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
