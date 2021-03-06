# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Modify a user by ID"


class Input:
    STATUS = "status"
    USER_ID = "user_id"
    

class Output:
    USER = "user"
    

class ModifyUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "string",
      "title": "Status",
      "description": "New status",
      "enum": [
        "active",
        "disabled",
        "bypass"
      ],
      "order": 2
    },
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID, e.g. DUCUULF6HBMZ43IG9MBH",
      "order": 1
    }
  },
  "required": [
    "status",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ModifyUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "$ref": "#/definitions/user",
      "title": "User",
      "description": "User",
      "order": 1
    }
  },
  "definitions": {
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "desc": {
          "type": "string",
          "title": "Desc",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 1
        }
      }
    },
    "phone": {
      "type": "object",
      "title": "phone",
      "properties": {
        "activated": {
          "type": "boolean",
          "title": "Activated",
          "order": 8
        },
        "capabilities": {
          "type": "array",
          "title": "Capabilities",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "extension": {
          "type": "string",
          "title": "Extension",
          "order": 3
        },
        "number": {
          "type": "string",
          "title": "Number",
          "order": 2
        },
        "phone_id": {
          "type": "string",
          "title": "Phone ID",
          "order": 1
        },
        "platform": {
          "type": "string",
          "title": "Platform",
          "order": 7
        },
        "postdelay": {
          "type": "string",
          "title": "Postdelay",
          "order": 4
        },
        "predelay": {
          "type": "string",
          "title": "Predelay",
          "order": 5
        },
        "sms_passcodes_sent": {
          "type": "boolean",
          "title": "SMS Passcodes Sent",
          "order": 9
        }
      }
    },
    "token": {
      "type": "object",
      "title": "token",
      "properties": {
        "serial": {
          "type": "string",
          "title": "Serial",
          "description": "Serial",
          "order": 1
        },
        "token_id": {
          "type": "string",
          "title": "Token ID",
          "description": "Token ID",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "order": 4
        },
        "groups": {
          "type": "array",
          "title": "Groups",
          "items": {
            "$ref": "#/definitions/group"
          },
          "order": 6
        },
        "last_login": {
          "type": "integer",
          "title": "Last Login",
          "order": 7
        },
        "notes": {
          "type": "string",
          "title": "Notes",
          "order": 8
        },
        "phones": {
          "type": "array",
          "title": "Phones",
          "items": {
            "$ref": "#/definitions/phone"
          },
          "order": 9
        },
        "realname": {
          "type": "string",
          "title": "Realname",
          "order": 3
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 5
        },
        "tokens": {
          "type": "array",
          "title": "Tokens",
          "items": {
            "$ref": "#/definitions/token"
          },
          "order": 10
        },
        "user_id": {
          "type": "string",
          "title": "User ID",
          "order": 1
        },
        "username": {
          "type": "string",
          "title": "Username",
          "order": 2
        }
      },
      "required": [
        "user_id"
      ],
      "definitions": {
        "group": {
          "type": "object",
          "title": "group",
          "properties": {
            "desc": {
              "type": "string",
              "title": "Desc",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 1
            }
          }
        },
        "phone": {
          "type": "object",
          "title": "phone",
          "properties": {
            "activated": {
              "type": "boolean",
              "title": "Activated",
              "order": 8
            },
            "capabilities": {
              "type": "array",
              "title": "Capabilities",
              "items": {
                "type": "string"
              },
              "order": 6
            },
            "extension": {
              "type": "string",
              "title": "Extension",
              "order": 3
            },
            "number": {
              "type": "string",
              "title": "Number",
              "order": 2
            },
            "phone_id": {
              "type": "string",
              "title": "Phone ID",
              "order": 1
            },
            "platform": {
              "type": "string",
              "title": "Platform",
              "order": 7
            },
            "postdelay": {
              "type": "string",
              "title": "Postdelay",
              "order": 4
            },
            "predelay": {
              "type": "string",
              "title": "Predelay",
              "order": 5
            },
            "sms_passcodes_sent": {
              "type": "boolean",
              "title": "SMS Passcodes Sent",
              "order": 9
            }
          }
        },
        "token": {
          "type": "object",
          "title": "token",
          "properties": {
            "serial": {
              "type": "string",
              "title": "Serial",
              "description": "Serial",
              "order": 1
            },
            "token_id": {
              "type": "string",
              "title": "Token ID",
              "description": "Token ID",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 3
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
