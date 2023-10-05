# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Submit or update new indicator"


class Input:
    ACTION = "action"
    APPLICATION = "application"
    DESCRIPTION = "description"
    EXPIRATION_TIME = "expiration_time"
    INDICATOR = "indicator"
    INDICATOR_STATE = "indicator_state"
    RBAC_GROUP_NAMES = "rbac_group_names"
    RECOMMENDED_ACTIONS = "recommended_actions"
    SEVERITY = "severity"
    TITLE = "title"


class Output:
    INDICATOR_ACTION_RESPONSE = "indicator_action_response"


class BlacklistInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "The action that will be taken if the indicator will be discovered in the organization",
      "default": "AlertAndBlock",
      "enum": [
        "Alert",
        "AlertAndBlock",
        "Allowed"
      ],
      "order": 2
    },
    "application": {
      "type": "string",
      "title": "Application",
      "description": "The application associated with the indicator",
      "order": 3
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description of the indicator",
      "default": "Indicator Blacklisted from InsightConnect",
      "order": 5
    },
    "expiration_time": {
      "type": "string",
      "title": "Expiration Time",
      "description": "The expiration time of the indicator, default value is one year from now",
      "order": 6
    },
    "indicator": {
      "type": "string",
      "title": "Indicator",
      "description": "A supported indicator to blacklist or unblacklist. Supported indicators are IP addresses, URLs, domains, and SHA1 and SHA256 hashes",
      "order": 1
    },
    "indicator_state": {
      "type": "boolean",
      "title": "Indicator State",
      "description": "True to add indicator, false to remove it from the list",
      "default": false,
      "order": 10
    },
    "rbac_group_names": {
      "type": "array",
      "title": "RBAC Group Names",
      "description": "List of RBAC group names the indicator would be applied to",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "recommended_actions": {
      "type": "string",
      "title": "Recommended Actions",
      "description": "TI indicator alert recommended actions",
      "order": 8
    },
    "severity": {
      "type": "string",
      "title": "Severity",
      "description": "The severity of the indicator",
      "default": "High",
      "enum": [
        "Informational",
        "Low",
        "Medium",
        "High"
      ],
      "order": 7
    },
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Indicator alert title",
      "order": 4
    }
  },
  "required": [
    "indicator"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BlacklistOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicator_action_response": {
      "$ref": "#/definitions/indicator_action",
      "title": "Indicator Action Response",
      "description": "A response that includes the result of the action, and supplemental information about the action taken",
      "order": 1
    }
  },
  "definitions": {
    "indicator_action": {
      "type": "object",
      "title": "indicator_action",
      "properties": {
        "@odata.context": {
          "type": "string",
          "title": "@Odata.Context",
          "description": "@odata.context",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "Indicator ID",
          "description": "Identity of the indicator entity",
          "order": 2
        },
        "indicatorValue": {
          "type": "string",
          "title": "Indicator Value",
          "description": "The potentially malicious indicator of one of the following types: IP addresses, URLs, domains, and SHA1 and SHA256 hashes",
          "order": 3
        },
        "indicatorType": {
          "type": "string",
          "title": "Indicator Type",
          "description": "Type of the indicator",
          "order": 4
        },
        "application": {
          "type": "string",
          "title": "Application",
          "description": "The application associated with the indicator",
          "order": 5
        },
        "action": {
          "type": "string",
          "title": "Action",
          "description": "The action that will be taken if the indicator will be discovered in the organization",
          "order": 6
        },
        "sourceType": {
          "type": "string",
          "title": "Source Type",
          "description": "User in case the Indicator created by a user (e.g. from the portal), AadApp in case it submitted using automated application via the API.",
          "order": 7
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The name of the user/application that submitted the indicator",
          "order": 8
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "Unique identity of the user/application that submitted the indicator",
          "order": 9
        },
        "createdByDisplayName": {
          "type": "string",
          "title": "Created By Display Name",
          "description": "Created by display name",
          "order": 10
        },
        "createdBySource": {
          "type": "string",
          "title": "Created By Source",
          "description": "Created by source",
          "order": 11
        },
        "generateAlert": {
          "type": "boolean",
          "title": "Generate Alert",
          "description": "Generate alert",
          "order": 12
        },
        "historicalDetection": {
          "type": "boolean",
          "title": "Historical Detection",
          "description": "Historical detection",
          "order": 13
        },
        "lastUpdatedBy": {
          "type": "string",
          "title": "Last Updated By",
          "description": "Identity of the user/application that last updated the indicator",
          "order": 14
        },
        "mitreTechniques": {
          "type": "array",
          "title": "MITRE Techniques",
          "description": "MITRE techniques",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "creationTimeDateTimeUtc": {
          "type": "string",
          "title": "Creation Time",
          "description": "The date and time when the indicator was created",
          "order": 16
        },
        "expirationTime": {
          "type": "string",
          "title": "Expiration Time",
          "description": "The expiration time of the indicator",
          "order": 17
        },
        "lastUpdateTime": {
          "type": "string",
          "title": "Last Update Time",
          "description": "The last time the indicator was updated",
          "order": 18
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "The severity of the indicator",
          "order": 19
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Indicator alert title",
          "order": 20
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description of the indicator",
          "order": 21
        },
        "recommendedActions": {
          "type": "string",
          "title": "Recommended Actions",
          "description": "Recommended actions for the indicator",
          "order": 22
        },
        "rbacGroupIds": {
          "type": "array",
          "title": "RBAC Group IDs",
          "description": "RBAC group IDs",
          "items": {
            "type": "string"
          },
          "order": 23
        },
        "rbacGroupNames": {
          "type": "array",
          "title": "RBAC Group Names",
          "description": "RBAC device group names where the indicator is exposed and active. Empty list in case it exposed to all devices",
          "items": {
            "type": "string"
          },
          "order": 24
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
