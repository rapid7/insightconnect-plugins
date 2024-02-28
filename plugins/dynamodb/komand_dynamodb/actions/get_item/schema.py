# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return a set of attributes for the item with the given primary key"


class Input:
    CONSISTENT_READ = "consistent_read"
    EXPRESSION_ATTRIBUTE_NAMES = "expression_attribute_names"
    KEY = "key"
    PROJECTION_EXPRESSION = "projection_expression"
    RETURN_CONSUMED_CAPACITY = "return_consumed_capacity"
    TABLE_NAME = "table_name"


class Output:
    ITEM = "item"


class GetItemInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "consistent_read": {
      "type": "boolean",
      "title": "Consistent Read",
      "description": "Determines the read consistency model; If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads",
      "order": 3
    },
    "expression_attribute_names": {
      "type": "object",
      "title": "Expression Attribute Names",
      "description": "One or more substitution tokens for attribute names in an expression",
      "order": 6
    },
    "key": {
      "type": "object",
      "title": "Key",
      "description": "A map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve",
      "order": 2
    },
    "projection_expression": {
      "type": "string",
      "title": "Projection Expression",
      "description": "A string that identifies one or more attributes to retrieve from the specified table or index",
      "order": 5
    },
    "return_consumed_capacity": {
      "type": "string",
      "title": "Return Consumed Capacity",
      "description": "Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response",
      "default": "TOTAL",
      "enum": [
        "NONE",
        "INDEXES",
        "TOTAL"
      ],
      "order": 4
    },
    "table_name": {
      "type": "string",
      "title": "Table Name",
      "description": "The table name to search",
      "order": 1
    }
  },
  "required": [
    "key",
    "table_name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetItemOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "item": {
      "type": "object",
      "title": "Item",
      "description": "Output item",
      "order": 1
    }
  },
  "required": [
    "item"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
