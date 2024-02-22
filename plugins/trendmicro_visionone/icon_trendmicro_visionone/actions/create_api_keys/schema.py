# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Generates API keys that allow third-party applications to access the Trend Vision One APIs"


class Input:
    API_KEYS_OBJECTS = "api_keys_objects"


class Output:
    API_KEYS_RESP = "api_keys_resp"


class CreateApiKeysInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_keys_objects": {
      "type": "array",
      "title": "API Keys Objects",
      "description": "List of JSON objects containing data for API keys creation",
      "items": {
        "$ref": "#/definitions/api_keys_objects"
      },
      "order": 1
    }
  },
  "required": [
    "api_keys_objects"
  ],
  "definitions": {
    "api_keys_objects": {
      "type": "object",
      "title": "api_keys_objects",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The unique name of an API key",
          "order": 1
        },
        "role": {
          "type": "string",
          "title": "Role",
          "description": "The user role assigned to the API key",
          "order": 2
        },
        "months_to_expiration": {
          "type": "integer",
          "title": "Months to Expiration",
          "description": "The duration of validity for the API key (in months, 0 for no expiration)",
          "enum": [
            1,
            3,
            6,
            12,
            0
          ],
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "A brief note about the API key",
          "order": 4
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of an API key",
          "enum": [
            "enabled",
            "disabled"
          ],
          "order": 5
        }
      },
      "required": [
        "name",
        "role"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateApiKeysOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_keys_resp": {
      "type": "array",
      "title": "API Keys Response",
      "description": "List of API keys responses",
      "items": {
        "$ref": "#/definitions/api_keys_resp"
      },
      "order": 1
    }
  },
  "required": [
    "api_keys_resp"
  ],
  "definitions": {
    "api_keys_resp": {
      "type": "object",
      "title": "api_keys_resp",
      "properties": {
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "The Status Code of the submitted API keys task",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The unique identifier of the API key",
          "order": 2
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "The API key",
          "order": 3
        },
        "expired_date_time": {
          "type": "string",
          "title": "Expired Date Time",
          "description": "Timestamp in ISO 8601 format indicating the expiration date of the API key",
          "order": 4
        }
      },
      "required": [
        "expired_date_time",
        "id",
        "status",
        "value"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
