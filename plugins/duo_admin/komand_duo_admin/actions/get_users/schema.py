# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get list of users"


class Input:
    pass


class Output:
    USERS = "users"


class GetUsersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUsersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "users": {
      "type": "array",
      "title": "Users",
      "description": "List of users",
      "items": {
        "$ref": "#/definitions/user"
      },
      "order": 1
    }
  },
  "definitions": {
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "alias1": {
          "type": "string",
          "title": "Alias 1",
          "description": "The user's username alias 1",
          "order": 1
        },
        "alias2": {
          "type": "string",
          "title": "Alias 2",
          "description": "The user's username alias 2",
          "order": 2
        },
        "alias3": {
          "type": "string",
          "title": "Alias 3",
          "description": "The user's username alias 3",
          "order": 3
        },
        "alias4": {
          "type": "string",
          "title": "Alias 4",
          "description": "The user's username alias 4",
          "order": 4
        },
        "aliases": {
          "type": "object",
          "title": "Aliases",
          "description": "The user's aliases",
          "order": 5
        },
        "created": {
          "type": "integer",
          "title": "Created",
          "description": "The user's creation date as a UNIX timestamp",
          "order": 6
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The user's email address",
          "order": 7
        },
        "groups": {
          "type": "array",
          "title": "Groups",
          "description": "List of groups to which this user belongs",
          "items": {
            "$ref": "#/definitions/group"
          },
          "order": 8
        },
        "isEnrolled": {
          "type": "boolean",
          "title": "Is Enrolled",
          "description": "Whether the user has a phone, hardware token, U2F token, WebAuthn security key, or other WebAuthn method available for authentication",
          "order": 9
        },
        "lastDirectorySync": {
          "type": "integer",
          "title": "Last Directory Sync",
          "description": "An integer indicating the last update to the user via directory sync as a Unix timestamp, or null if the user has never synced with an external directory or if the directory that originally created the user has been deleted from Duo",
          "order": 10
        },
        "lastLogin": {
          "type": "integer",
          "title": "Last Login",
          "description": "An integer indicating the last time this user logged in, as a Unix timestamp, or null if the user has not logged in",
          "order": 11
        },
        "notes": {
          "type": "string",
          "title": "Notes",
          "description": "Notes about this user",
          "order": 12
        },
        "phones": {
          "type": "array",
          "title": "Phones",
          "description": "A list of phones that this user can use",
          "items": {
            "$ref": "#/definitions/phoneUser"
          },
          "order": 13
        },
        "realname": {
          "type": "string",
          "title": "Real Name",
          "description": "The user's real name or full name",
          "order": 14
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The user's status",
          "order": 15
        },
        "tokens": {
          "type": "array",
          "title": "Tokens",
          "description": "A list of tokens that this user can use",
          "items": {
            "$ref": "#/definitions/token"
          },
          "order": 16
        },
        "userId": {
          "type": "string",
          "title": "User ID",
          "description": "The user's ID",
          "order": 17
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The user's username",
          "order": 18
        },
        "webauthncredentials": {
          "type": "array",
          "title": "Web Auth Credentials",
          "description": "A list of WebAuthn authenticators that this user can use",
          "items": {
            "$ref": "#/definitions/webauthnaredentials"
          },
          "order": 19
        }
      }
    },
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "desc": {
          "type": "string",
          "title": "Description",
          "description": "The group's description",
          "order": 1
        },
        "groupId": {
          "type": "string",
          "title": "Group ID",
          "description": "The group's ID",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The group's name",
          "order": 3
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The group's authentication status",
          "order": 4
        }
      }
    },
    "phoneUser": {
      "type": "object",
      "title": "phoneUser",
      "properties": {
        "activated": {
          "type": "boolean",
          "title": "Activated",
          "description": "Whether the phone has already been activated for Duo Mobile",
          "order": 1
        },
        "capabilities": {
          "type": "array",
          "title": "Capabilities",
          "description": "List of factors that can be used with the phone",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "encrypted": {
          "type": "string",
          "title": "Encrypted",
          "description": "The encryption status of an Android or iOS device file system",
          "order": 3
        },
        "extension": {
          "type": "string",
          "title": "Extension",
          "description": "Extension of the phone",
          "order": 4
        },
        "fingerprint": {
          "type": "string",
          "title": "Fingerprint",
          "description": "Whether an Android or iOS phone is configured for biometric verification",
          "order": 5
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "description": "An integer indicating the timestamp of the last contact between Duo's service and the activated Duo Mobile app installed on the phone",
          "order": 6
        },
        "model": {
          "type": "string",
          "title": "Model",
          "description": "The phone's model",
          "order": 7
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Free-form label for the phone",
          "order": 8
        },
        "number": {
          "type": "string",
          "title": "Number",
          "description": "Number",
          "order": 9
        },
        "phoneId": {
          "type": "string",
          "title": "Phone ID",
          "description": "The phone's ID",
          "order": 10
        },
        "platform": {
          "type": "string",
          "title": "Platform",
          "description": "The phone platform",
          "order": 11
        },
        "postdelay": {
          "type": "string",
          "title": "Postdelay",
          "description": "The time (in seconds) to wait after the extension is dialed and before the speaking the prompt",
          "order": 12
        },
        "predelay": {
          "type": "string",
          "title": "Predelay",
          "description": "The time (in seconds) to wait after the number picks up and before dialing the extension",
          "order": 13
        },
        "screenLock": {
          "type": "string",
          "title": "Screen Lock",
          "description": "Whether screen lock is enabled on an Android or iOS phone",
          "order": 14
        },
        "smsPasscodesSent": {
          "type": "boolean",
          "title": "SMS Passcodes Sent",
          "description": "Whether the SMS passcodes has been sent to this phone",
          "order": 15
        },
        "tampered": {
          "type": "string",
          "title": "Type",
          "description": "Whether an iOS or Android device is jailbroken or rooted",
          "order": 16
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of phone",
          "order": 17
        }
      }
    },
    "token": {
      "type": "object",
      "title": "token",
      "properties": {
        "admins": {
          "type": "array",
          "title": "Admins",
          "description": "A list of administrators associated with this hardware token",
          "items": {
            "type": "object"
          },
          "order": 1
        },
        "serial": {
          "type": "string",
          "title": "Serial",
          "description": "The serial number of the hardware token",
          "order": 2
        },
        "tokenId": {
          "type": "string",
          "title": "Token ID",
          "description": "The hardware token's unique ID",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of hardware token",
          "order": 4
        },
        "users": {
          "type": "array",
          "title": "Users",
          "description": "A list of end users associated with this hardware token",
          "items": {
            "type": "object"
          },
          "order": 5
        }
      }
    },
    "webauthnaredentials": {
      "type": "object",
      "title": "webauthnaredentials",
      "properties": {
        "credentialName": {
          "type": "string",
          "title": "Credential Name",
          "description": "Free-form label for the WebAuthn credential",
          "order": 1
        },
        "dateAdded": {
          "type": "integer",
          "title": "Credential Name",
          "description": "The date the WebAuthn credential was registered in Duo",
          "order": 2
        },
        "label": {
          "type": "string",
          "title": "Label",
          "description": "Indicates the type of WebAuthn credential",
          "order": 3
        },
        "user": {
          "type": "object",
          "title": "User",
          "description": "Selected information about the end user attached to the WebAuthn credential",
          "order": 4
        },
        "webauthnkey": {
          "type": "string",
          "title": "WebAuthnKey",
          "description": "The WebAuthn credential's registration identifier",
          "order": 5
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
