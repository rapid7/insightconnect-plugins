# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Show a user's information"


class Input:
    USERNAME = "username"
    

class Output:
    FOUND = "found"
    FULL_MESSAGE = "full_message"
    

class ShowUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "username": {
      "type": "string",
      "title": "Username",
      "description": "The login name of the user to search for",
      "order": 1
    }
  },
  "required": [
    "username"
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
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Boolean showing the status of the request",
      "order": 1
    },
    "full_message": {
      "$ref": "#/definitions/show_user_out",
      "title": "Full Message",
      "description": "All data returned by the request",
      "order": 2
    }
  },
  "definitions": {
    "show_user_out": {
      "type": "object",
      "title": "show_user_out",
      "properties": {
        "cn": {
          "type": "array",
          "title": "CN",
          "description": "CN",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "displayname": {
          "type": "array",
          "title": "Display Name",
          "description": "Display name",
          "items": {
            "type": "string"
          },
          "order": 16
        },
        "dn": {
          "type": "string",
          "title": "DN",
          "description": "DN",
          "order": 15
        },
        "gecos": {
          "type": "array",
          "title": "Gecos",
          "description": "Gecos",
          "items": {
            "type": "string"
          },
          "order": 24
        },
        "gidnumber": {
          "type": "array",
          "title": "GID Number",
          "description": "GID number",
          "items": {
            "type": "string"
          },
          "order": 23
        },
        "givenname": {
          "type": "array",
          "title": "Given Name",
          "description": "Given name",
          "items": {
            "type": "string"
          },
          "order": 20
        },
        "has_keytab": {
          "type": "boolean",
          "title": "Has Keytab",
          "description": "Has keytab",
          "order": 2
        },
        "has_password": {
          "type": "boolean",
          "title": "Has Password",
          "description": "Has password",
          "order": 7
        },
        "homedirectory": {
          "type": "array",
          "title": "Home Directory",
          "description": "Home directory",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "initials": {
          "type": "array",
          "title": "Initials",
          "description": "Initials",
          "items": {
            "type": "string"
          },
          "order": 26
        },
        "ipantsecurityidentifier": {
          "type": "array",
          "title": "Ipant Security Identifier",
          "description": "Ipant security identifier",
          "items": {
            "type": "string"
          },
          "order": 22
        },
        "ipasshpubkey": {
          "type": "array",
          "title": "IPA SSH Pub Key",
          "description": "IPA SSH pub key",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "ipauniqueid": {
          "type": "array",
          "title": "IPA Unique ID",
          "description": "IPA unique ID",
          "items": {
            "type": "string"
          },
          "order": 18
        },
        "krbcanonicalname": {
          "type": "array",
          "title": "Krb Canonical Name",
          "description": "krb canonical name",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "krbprincipalname": {
          "type": "array",
          "title": "Krb Principal Name",
          "description": "Krb principal name",
          "items": {
            "type": "string"
          },
          "order": 19
        },
        "loginshell": {
          "type": "array",
          "title": "Login Shell",
          "description": "Login shell",
          "items": {
            "type": "string"
          },
          "order": 11
        },
        "mail": {
          "type": "array",
          "title": "Mail",
          "description": "Mail",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "memberof_group": {
          "type": "array",
          "title": "Member of Group",
          "description": "Member of group",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "mepmanagedentry": {
          "type": "array",
          "title": "Mepmanagedentry",
          "description": "Mepmanagedentry",
          "items": {
            "type": "string"
          },
          "order": 17
        },
        "nsaccountlock": {
          "type": "boolean",
          "title": "NS Account Lock",
          "description": "NS account lock",
          "order": 9
        },
        "objectclass": {
          "type": "array",
          "title": "Object Class",
          "description": "Object class",
          "items": {
            "type": "string"
          },
          "order": 21
        },
        "preserved": {
          "type": "boolean",
          "title": "Preserved",
          "description": "Preserved",
          "order": 13
        },
        "sn": {
          "type": "array",
          "title": "SN",
          "description": "SN",
          "items": {
            "type": "string"
          },
          "order": 25
        },
        "sshpubkeyfp": {
          "type": "array",
          "title": "SSH Pub Key FP",
          "description": "SSH pub key FP",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "uid": {
          "type": "array",
          "title": "UID",
          "description": "UID",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "uidnumber": {
          "type": "array",
          "title": "UID Number",
          "description": "UID number",
          "items": {
            "type": "string"
          },
          "order": 12
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
