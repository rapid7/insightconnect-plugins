# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add an attribute to an event"


class Input:
    CATEGORY = "category"
    COMMENT = "comment"
    EVENT = "event"
    TYPE_VALUE = "type_value"
    VALUE = "value"


class Output:
    ATTRIBUTE = "attribute"


class AddAttributeInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "category": {
      "type": "string",
      "title": "Category",
      "description": "The attribute category e.g. external analysis, network activity",
      "order": 3
    },
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Optional comment to add to attribute",
      "order": 5
    },
    "event": {
      "type": "string",
      "title": "Event ID",
      "description": "ID of event to append to",
      "order": 1
    },
    "type_value": {
      "type": "string",
      "title": "Type Value",
      "description": "The Type of attribute e.g. URL, SHA256",
      "order": 2
    },
    "value": {
      "type": "string",
      "title": "Value",
      "description": "The Value of the attribute e.g. for a URL",
      "order": 4
    }
  },
  "required": [
    "category",
    "event",
    "type_value",
    "value"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddAttributeOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attribute": {
      "$ref": "#/definitions/attribute",
      "title": "Attribute",
      "description": "A summary of the added attribute",
      "order": 1
    }
  },
  "definitions": {
    "attribute": {
      "type": "object",
      "title": "attribute",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "order": 1
        },
        "event_id": {
          "type": "string",
          "title": "Event ID",
          "order": 2
        },
        "category": {
          "type": "string",
          "title": "Category",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 4
        },
        "value1": {
          "type": "string",
          "title": "Value1",
          "order": 5
        },
        "value2": {
          "type": "string",
          "title": "Value2",
          "order": 6
        },
        "to_ids": {
          "type": "boolean",
          "title": "To IDs",
          "order": 7
        },
        "uuid": {
          "type": "string",
          "title": "UUID",
          "order": 8
        },
        "timestamp": {
          "type": "string",
          "title": "TimeStamp",
          "order": 9
        },
        "distribution": {
          "type": "string",
          "title": "Distribution",
          "order": 10
        },
        "sharing_group_id": {
          "type": "string",
          "title": "Sharing Group ID",
          "order": 11
        },
        "comment": {
          "type": "string",
          "title": "Comment",
          "order": 12
        },
        "deleted": {
          "type": "boolean",
          "title": "Deleted",
          "order": 13
        },
        "disable_correlation": {
          "type": "boolean",
          "title": "Disable Correlation",
          "order": 14
        },
        "value": {
          "type": "string",
          "title": "Value",
          "order": 15
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
