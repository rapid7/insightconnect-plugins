# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    USER_PRINCIPAL_NAME = "user_principal_name"
    

class Output:
    SUCCESS = "success"
    

class DeleteUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_principal_name": {
      "type": "string",
      "title": "User Principal Name",
      "description": "The user principal name to delete",
      "order": 1
    }
  },
  "required": [
    "user_principal_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Return true if it worked",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
