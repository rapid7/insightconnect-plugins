# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Promote an ordinary user to admin"


class Input:
    USER = "user"
    

class Output:
    STATUS = "status"
    

class PromoteInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "type": "string",
      "title": "User",
      "description": "User to promote",
      "order": 1
    }
  },
  "required": [
    "user"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PromoteOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
