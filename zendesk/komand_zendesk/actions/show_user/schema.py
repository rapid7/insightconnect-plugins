# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve user information"


class Input:
    USER_ID = "user_id"
    

class Output:
    USER = "user"
    

class ShowUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "ID of user to show E.g. 361738647591",
      "order": 1
    }
  },
  "required": [
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ShowUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "type": "object",
      "title": "User Info",
      "description": "User meta data",
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
