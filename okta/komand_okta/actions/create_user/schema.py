# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new user"


class Input:
    ACTIVATE = "activate"
    CREDENTIALS = "credentials"
    GROUPIDS = "groupIds"
    NEXTLOGIN = "nextLogin"
    PROFILE = "profile"
    PROVIDER = "provider"
    

class Output:
    _LINKS = "_links"
    ACTIVATED = "activated"
    CREATED = "created"
    CREDENTIALS = "credentials"
    ID = "id"
    LASTLOGIN = "lastLogin"
    LASTUPDATED = "lastUpdated"
    PASSWORDCHANGED = "passwordChanged"
    PROFILE = "profile"
    STATUS = "status"
    STATUSCHANGED = "statusChanged"
    

class CreateUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "activate": {
      "type": "boolean",
      "title": "Activate",
      "description": "Executes activation lifecycle operation when creating the user",
      "default": true,
      "order": 1
    },
    "credentials": {
      "$ref": "#/definitions/credentials_input",
      "title": "Credentials",
      "description": "Credentials for user",
      "order": 4
    },
    "groupIds": {
      "type": "array",
      "title": "Group IDs",
      "description": "IDs of groups that user will be immediately added to at time of creation",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "nextLogin": {
      "type": "boolean",
      "title": "Change Password Next Login",
      "description": "Change password next time the user logs in",
      "order": 6
    },
    "profile": {
      "type": "object",
      "title": "Profile",
      "description": "Profile properties for user",
      "order": 3
    },
    "provider": {
      "type": "boolean",
      "title": "Provider",
      "description": "Indicates whether to create a user with a specified authentication provider",
      "default": false,
      "order": 2
    }
  },
  "required": [
    "activate",
    "nextLogin",
    "profile",
    "provider"
  ],
  "definitions": {
    "credentials_input": {
      "type": "object",
      "title": "credentials_input",
      "properties": {
        "password": {
          "$ref": "#/definitions/password",
          "title": "Password",
          "order": 1
        },
        "provider": {
          "$ref": "#/definitions/provider",
          "title": "Provider",
          "order": 2
        },
        "recovery_question": {
          "$ref": "#/definitions/recovery_question",
          "title": "Recovery Question",
          "order": 3
        }
      },
      "definitions": {
        "password": {
          "type": "object",
          "title": "password",
          "properties": {
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Password value e.g. tlpWENT2m",
              "order": 1
            }
          }
        },
        "provider": {
          "type": "object",
          "title": "provider",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Provider name e.g. OKTA",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Provider type e.g. OKTA",
              "order": 1
            }
          }
        },
        "recovery_question": {
          "type": "object",
          "title": "recovery_question",
          "properties": {
            "answer": {
              "type": "string",
              "title": "Answer",
              "description": "Recovery answer e.g. Annie Oakley",
              "order": 2
            },
            "question": {
              "type": "string",
              "title": "Question",
              "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
              "order": 1
            }
          }
        }
      }
    },
    "password": {
      "type": "object",
      "title": "password",
      "properties": {
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Password value e.g. tlpWENT2m",
          "order": 1
        }
      }
    },
    "provider": {
      "type": "object",
      "title": "provider",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Provider name e.g. OKTA",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Provider type e.g. OKTA",
          "order": 1
        }
      }
    },
    "recovery_question": {
      "type": "object",
      "title": "recovery_question",
      "properties": {
        "answer": {
          "type": "string",
          "title": "Answer",
          "description": "Recovery answer e.g. Annie Oakley",
          "order": 2
        },
        "question": {
          "type": "string",
          "title": "Question",
          "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "_links": {
      "$ref": "#/definitions/_links",
      "title": "Links",
      "description": "Links",
      "order": 7
    },
    "activated": {
      "type": "string",
      "title": "Activated",
      "description": "When the user was activated, e.g. 2013-07-02T21:36:25.344Z",
      "order": 5
    },
    "created": {
      "type": "string",
      "title": "Created",
      "description": "When the user was created, e.g. 2013-07-02T21:36:25.344Z",
      "order": 4
    },
    "credentials": {
      "$ref": "#/definitions/credentials",
      "title": "Credentials",
      "description": "Credentials",
      "order": 9
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "User ID",
      "order": 10
    },
    "lastLogin": {
      "type": "string",
      "title": "Last Login",
      "description": "When the last login for the user was, e.g. 2013-07-02T21:36:25.344Z",
      "order": 8
    },
    "lastUpdated": {
      "type": "string",
      "title": "Last Updated",
      "description": "When the user was last updated, e.g. 2013-07-02T21:36:25.344Z",
      "order": 6
    },
    "passwordChanged": {
      "type": "string",
      "title": "Password Changed",
      "description": "When the password was changed, e.g. 2013-07-02T21:36:25.344Z",
      "order": 3
    },
    "profile": {
      "$ref": "#/definitions/profile",
      "title": "Profile",
      "description": "Profile",
      "order": 2
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 1
    },
    "statusChanged": {
      "type": "string",
      "title": "Status Changed",
      "description": "When the status of the user changed, e.g. 2013-07-02T21:36:25.344Z",
      "order": 11
    }
  },
  "definitions": {
    "_links": {
      "type": "object",
      "title": "_links",
      "properties": {
        "changePassword": {
          "$ref": "#/definitions/changePassword",
          "title": "ChangePassword",
          "order": 1
        },
        "changeRecoveryQuestion": {
          "$ref": "#/definitions/changePassword",
          "title": "ChangeRecoveryQuestion",
          "order": 2
        },
        "deactivate": {
          "$ref": "#/definitions/changePassword",
          "title": "Deactivate",
          "order": 3
        },
        "expirePassword": {
          "$ref": "#/definitions/changePassword",
          "title": "ExpirePassword",
          "order": 4
        },
        "forgotPassword": {
          "$ref": "#/definitions/changePassword",
          "title": "ForgotPassword",
          "order": 5
        },
        "resetFactors": {
          "$ref": "#/definitions/changePassword",
          "title": "ResetFactors",
          "order": 6
        },
        "resetPassword": {
          "$ref": "#/definitions/changePassword",
          "title": "ResetPassword",
          "order": 7
        }
      },
      "definitions": {
        "changePassword": {
          "type": "object",
          "title": "changePassword",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "order": 1
            }
          }
        }
      }
    },
    "changePassword": {
      "type": "object",
      "title": "changePassword",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "order": 1
        }
      }
    },
    "credentials": {
      "type": "object",
      "title": "credentials",
      "properties": {
        "password": {
          "type": "object",
          "title": "Password",
          "order": 1
        },
        "provider": {
          "$ref": "#/definitions/provider",
          "title": "Provider",
          "order": 2
        },
        "recovery_question": {
          "$ref": "#/definitions/recovery_question",
          "title": "Recovery Question",
          "order": 3
        }
      },
      "definitions": {
        "provider": {
          "type": "object",
          "title": "provider",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Provider name e.g. OKTA",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Provider type e.g. OKTA",
              "order": 1
            }
          }
        },
        "recovery_question": {
          "type": "object",
          "title": "recovery_question",
          "properties": {
            "answer": {
              "type": "string",
              "title": "Answer",
              "description": "Recovery answer e.g. Annie Oakley",
              "order": 2
            },
            "question": {
              "type": "string",
              "title": "Question",
              "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
              "order": 1
            }
          }
        }
      }
    },
    "profile": {
      "type": "object",
      "title": "profile",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "order": 1
        },
        "firstName": {
          "type": "string",
          "title": "FirstName",
          "order": 2
        },
        "lastName": {
          "type": "string",
          "title": "LastName",
          "order": 3
        },
        "login": {
          "type": "string",
          "title": "Login",
          "order": 4
        },
        "mobilePhone": {
          "type": "string",
          "title": "MobilePhone",
          "order": 5
        }
      }
    },
    "provider": {
      "type": "object",
      "title": "provider",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Provider name e.g. OKTA",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Provider type e.g. OKTA",
          "order": 1
        }
      }
    },
    "recovery_question": {
      "type": "object",
      "title": "recovery_question",
      "properties": {
        "answer": {
          "type": "string",
          "title": "Answer",
          "description": "Recovery answer e.g. Annie Oakley",
          "order": 2
        },
        "question": {
          "type": "string",
          "title": "Question",
          "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
