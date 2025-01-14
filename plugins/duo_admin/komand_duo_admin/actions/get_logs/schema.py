# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to get auth logs, limited to past 180 days.
[Currentmillis.com](https://currentmillis.com/) is useful for finding a usable UNIX timestamp.

Available inputs for parameters can be found in [Duo Admin API docs](https://duo.com/docs/adminapi#logs:~:text=The%20factor%20or%20method%20used%20for%20an%20authentication%20attempt.%20One%20of%3A)"


class Input:
    APPLICATIONS = "applications"
    EVENTTYPES = "eventTypes"
    FACTORS = "factors"
    GROUPS = "groups"
    MAXTIME = "maxtime"
    MINTIME = "mintime"
    PHONENUMBERS = "phoneNumbers"
    REASONS = "reasons"
    RESULTS = "results"
    TOKENS = "tokens"
    USERS = "users"


class Output:
    AUTHLOGS = "authLogs"


class GetLogsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "applications": {
      "type": "array",
      "title": "Applications",
      "description": "List of application IDs to filter on",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "eventTypes": {
      "type": "array",
      "title": "Event Types",
      "description": "List of event types(authentication, enrollment) to filter on, to include all leave this parameter empty",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "factors": {
      "type": "array",
      "title": "Factors",
      "description": "List of factors or methods used for an authentication attempt to filter on, to include all leave this parameter empty. Check the help documentation to see all available inputs",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "groups": {
      "type": "array",
      "title": "Groups",
      "description": "List of group IDs to filter on",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "maxtime": {
      "type": "integer",
      "title": "Maxtime",
      "description": "Maximum time in UNIX timestamp milliseconds. Must be 13 or more digits in length and greater than mintime. To use current time leave this parameter empty",
      "order": 2
    },
    "mintime": {
      "type": "integer",
      "title": "Mintime",
      "description": "Minimum time in UNIX timestamp milliseconds. Must be 13 or more digits in length",
      "order": 1
    },
    "phoneNumbers": {
      "type": "array",
      "title": "Phone Numbers",
      "description": "List of phone numbers to filter on",
      "items": {
        "type": "string"
      },
      "order": 8
    },
    "reasons": {
      "type": "array",
      "title": "Reasons",
      "description": "List of reasons associated with an authentication attempt to filter on, to include all leave this parameter empty. Check the help documentation to see all available inputs",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "results": {
      "type": "array",
      "title": "Results",
      "description": "List of results of an authentication attempt(success, denied, fraud) to filter on, to include all leave this parameter empty",
      "items": {
        "type": "string"
      },
      "order": 10
    },
    "tokens": {
      "type": "array",
      "title": "Tokens",
      "description": "List of FIDO U2F token registration IDs or WebAuthn security keys to filter on",
      "items": {
        "type": "string"
      },
      "order": 11
    },
    "users": {
      "type": "array",
      "title": "Users",
      "description": "List of user IDs to filter on",
      "items": {
        "type": "string"
      },
      "order": 4
    }
  },
  "required": [
    "mintime"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetLogsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "authLogs": {
      "type": "array",
      "title": "Logs",
      "description": "Logs",
      "items": {
        "$ref": "#/definitions/authLog"
      },
      "order": 1
    }
  },
  "required": [
    "authLogs"
  ],
  "definitions": {
    "authLog": {
      "type": "object",
      "title": "authLog",
      "properties": {
        "accessDevice": {
          "$ref": "#/definitions/accessDevice",
          "title": "Access Device",
          "description": "Browser, plugin, and operating system information for the endpoint used to access the Duo-protected resource. Values present only when the application accessed features Duo's inline browser prompt",
          "order": 1
        },
        "adaptiveTrustAssessments": {
          "$ref": "#/definitions/adaptiveTrustAssessments",
          "title": "Adaptive Trust Assessments",
          "description": "Risk-based authentication information. Values present only when the application accessed features Duo's inline browser prompt and has a Duo Risk-Based Authentication policy applied",
          "order": 2
        },
        "alias": {
          "type": "string",
          "title": "Alias",
          "description": "The username alias used to log in. No value if the user logged in with their username instead of a username alias",
          "order": 3
        },
        "application": {
          "$ref": "#/definitions/keyNamePair",
          "title": "Application",
          "description": "Information about the application accessed",
          "order": 4
        },
        "authDevice": {
          "$ref": "#/definitions/authDevice",
          "title": "Auth Device",
          "description": "Information about the device used to approve or deny authentication",
          "order": 5
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email address of the user",
          "order": 6
        },
        "eventType": {
          "type": "string",
          "title": "Event Type",
          "description": "The type of activity logged",
          "order": 7
        },
        "factor": {
          "type": "string",
          "title": "Factor",
          "description": "The authentication factor",
          "order": 8
        },
        "isotimestamp": {
          "type": "string",
          "title": "ISO8601 Timestamp",
          "description": "ISO8601 timestamp of the event",
          "order": 9
        },
        "oodSoftware": {
          "type": "string",
          "title": "OOD Software",
          "description": "If authentication was denied due to out-of-date software, shows the name of the software",
          "order": 10
        },
        "reason": {
          "type": "string",
          "title": "Reason",
          "description": "The reason for the authentication attempt result",
          "order": 11
        },
        "result": {
          "type": "string",
          "title": "Result",
          "description": "The result of the authentication attempt. One of: 'success', 'denied', 'failure', 'error', or 'fraud'",
          "order": 12
        },
        "timestamp": {
          "type": "number",
          "title": "Timestamp",
          "description": "An integer indicating the Unix timestamp of the event",
          "order": 13
        },
        "txid": {
          "type": "string",
          "title": "Transaction ID",
          "description": "The transaction ID of the event",
          "order": 14
        },
        "user": {
          "$ref": "#/definitions/authlogUser",
          "title": "User",
          "description": "Information about the authenticating user",
          "order": 15
        }
      }
    },
    "accessDevice": {
      "type": "object",
      "title": "accessDevice",
      "properties": {
        "browser": {
          "type": "string",
          "title": "Access Device",
          "description": "The web browser used for access",
          "order": 1
        },
        "browserVersion": {
          "type": "string",
          "title": "Browser Version",
          "description": "The browser version",
          "order": 2
        },
        "flashVersion": {
          "type": "string",
          "title": "Flash Version",
          "description": "The Flash plugin version used",
          "order": 3
        },
        "hostname": {
          "type": "string",
          "title": "Hostname",
          "description": "The hostname",
          "order": 4
        },
        "ip": {
          "type": "string",
          "title": "IP Address",
          "description": "The access device's IP address",
          "order": 5
        },
        "isEncryptionEnabled": {
          "type": "string",
          "title": "Is Encryption Enabled",
          "description": "Reports the disk encryption state as detected by the Duo Device Health app. One of true, false, or unknown",
          "order": 6
        },
        "isFirewallEnabled": {
          "type": "string",
          "title": "Is Firewall Enabled",
          "description": "Reports the firewall state as detected by the Duo Device Health app. One of true, false, or unknown",
          "order": 7
        },
        "isPasswordSet": {
          "type": "string",
          "title": "Is Password Set",
          "description": "Reports the system password state as detected by the Duo Device Health app. One of true, false, or unknown",
          "order": 8
        },
        "javaVersion": {
          "type": "string",
          "title": "Java Version",
          "description": "The Java plugin version used",
          "order": 9
        },
        "location": {
          "$ref": "#/definitions/location",
          "title": "Location",
          "description": "The GeoIP location of the access device",
          "order": 10
        },
        "os": {
          "type": "string",
          "title": "Operating System",
          "description": "The device operating system name",
          "order": 11
        },
        "osVersion": {
          "type": "string",
          "title": "Operating System Version",
          "description": "The device operating system version",
          "order": 12
        }
      }
    },
    "location": {
      "type": "object",
      "title": "location",
      "properties": {
        "city": {
          "type": "string",
          "title": "City",
          "description": "The city name",
          "order": 1
        },
        "country": {
          "type": "string",
          "title": "Country",
          "description": "The country name",
          "order": 2
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "The state, county, province, or prefecture",
          "order": 3
        }
      }
    },
    "adaptiveTrustAssessments": {
      "type": "object",
      "title": "adaptiveTrustAssessments",
      "properties": {
        "moreSecureAuth": {
          "$ref": "#/definitions/trustAssessmentObject",
          "title": "More Secure Auth",
          "description": "Trust assessment information for Risk-Based Factor Selection",
          "order": 1
        },
        "rememberMe": {
          "$ref": "#/definitions/trustAssessmentObject",
          "title": "Remember Me",
          "description": "Trust assessment information for Risk-Based Remembered Devices",
          "order": 2
        }
      }
    },
    "trustAssessmentObject": {
      "type": "object",
      "title": "trustAssessmentObject",
      "properties": {
        "featuresVersion": {
          "type": "string",
          "title": "Features Version",
          "description": "The feature version for the risk-based authentication trust assessment",
          "order": 1
        },
        "modelVersion": {
          "type": "string",
          "title": "Model Version",
          "description": "The model version for the risk-based authentication trust assessment",
          "order": 2
        },
        "policyEnabled": {
          "type": "boolean",
          "title": "Policy Enabled",
          "description": "Denotes if risk-based authentication was enabled by the policy under which the trust assessment was evaluated",
          "order": 3
        },
        "reason": {
          "type": "string",
          "title": "Reason",
          "description": "The reason behind the trust assessment level",
          "order": 4
        },
        "trustLevel": {
          "type": "string",
          "title": "Trust Level",
          "description": "The trust assessment level. Can be one of: ERROR, LOW, NORMAL, UNKNOWN, or UNSET",
          "order": 5
        }
      }
    },
    "keyNamePair": {
      "type": "object",
      "title": "keyNamePair",
      "properties": {
        "key": {
          "type": "string",
          "title": "Key",
          "description": "The integration key",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name",
          "order": 2
        }
      }
    },
    "authDevice": {
      "type": "object",
      "title": "authDevice",
      "properties": {
        "ip": {
          "type": "string",
          "title": "IP Address",
          "description": "The IP address of the authentication device",
          "order": 1
        },
        "key": {
          "type": "string",
          "title": "Key",
          "description": "The Duo identifier of the authentication device",
          "order": 2
        },
        "location": {
          "$ref": "#/definitions/location",
          "title": "Location",
          "description": "The GeoIP location of the authentication device",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the authentication device",
          "order": 4
        }
      }
    },
    "authlogUser": {
      "type": "object",
      "title": "authlogUser",
      "properties": {
        "groups": {
          "type": "array",
          "title": "Groups",
          "description": "Duo group membership information for the user",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "key": {
          "type": "string",
          "title": "Key",
          "description": "The ID of the user",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the user",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
