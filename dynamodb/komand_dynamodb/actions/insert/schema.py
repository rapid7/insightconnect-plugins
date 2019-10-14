# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CONDITION_EXPRESSION = "condition_expression"
    DATA = "data"
    TABLE = "table"
    

class Output:
    SUCCESS = "success"
    

class InsertInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "condition_expression": {
      "type": "string",
      "title": "Condition Expression",
      "description": "An optional expression that can be used to reject inserts based on evaluating existing data",
      "order": 3
    },
    "data": {
      "type": "object",
      "title": "Data",
      "description": "The object data to store",
      "order": 2
    },
    "table": {
      "type": "string",
      "title": "Table",
      "description": "The table name to store into",
      "order": 1
    }
  },
  "required": [
    "table",
    "data"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class InsertOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
