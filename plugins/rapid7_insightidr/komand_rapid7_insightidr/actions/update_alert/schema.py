# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Updates information for a single alert"


class Input:
    ALERT_RRN = "alert_rrn"
    ASSIGNEE_ID = "assignee_id"
    COMMENT = "comment"
    DISPOSITION = "disposition"
    INVESTIGATION_RRN = "investigation_rrn"
    PRIORITY = "priority"
    STATUS = "status"
    TAGS = "tags"


class Output:
    ALERT = "alert"


class UpdateAlertInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_rrn": {
      "type": "string",
      "title": "Alert RRN",
      "description": "The unique identifier of the alert",
      "order": 1
    },
    "assignee_id": {
      "type": "string",
      "title": "Assignee ID",
      "description": "The new user to assign to the alert",
      "order": 5
    },
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "The reason for updating the alert, which is captured in the alert audit log for tracking purposes",
      "order": 8
    },
    "disposition": {
      "type": "string",
      "title": "Disposition",
      "description": "The alert disposition",
      "enum": [
        "UNMAPPED",
        "UNDECIDED",
        "MALICIOUS",
        "BENIGN",
        "UNKNOWN",
        "NOT_APPLICABLE"
      ],
      "order": 3
    },
    "investigation_rrn": {
      "type": "string",
      "title": "Investigation RRN",
      "description": "The RRN of the investigation to add the alert to",
      "order": 6
    },
    "priority": {
      "type": "string",
      "title": "Priority",
      "description": "The alert priority",
      "enum": [
        "UNMAPPED",
        "INFO",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
      ],
      "order": 4
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The alert status",
      "enum": [
        "UNMAPPED",
        "OPEN",
        "INVESTIGATING",
        "WAITING",
        "CLOSED"
      ],
      "order": 2
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "The tags to apply to the alerts.",
      "items": {
        "type": "object"
      },
      "order": 7
    }
  },
  "required": [
    "alert_rrn"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateAlertOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert": {
      "$ref": "#/definitions/alert_object",
      "title": "Alert",
      "description": "The updated alert",
      "order": 1
    }
  },
  "definitions": {
    "alert_object": {
      "type": "object",
      "title": "alert_object",
      "properties": {
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The unique identifier for this alert.",
          "order": 1
        },
        "version": {
          "type": "integer",
          "title": "Version",
          "description": "The version of the alert.",
          "order": 2
        },
        "created_at": {
          "type": "string",
          "title": "Created at",
          "description": "The timestamp when InsightIDR finished creating the alert in the Alerts experience.",
          "order": 3
        },
        "updated_at": {
          "type": "string",
          "title": "Updated at",
          "description": "The timestamp when the alert was last updated in InsightIDR.",
          "order": 4
        },
        "alerted_at": {
          "type": "string",
          "title": "Alerted at",
          "description": "The timestamp associated with the underlying event or evidence that InsightIDR detected in the source system.",
          "order": 5
        },
        "ingested_at": {
          "type": "string",
          "title": "Ingested at",
          "description": "The timestamp when the event or evidence from the source system was received by the Alerts experience in InsightIDR.",
          "order": 6
        },
        "external_source": {
          "type": "string",
          "title": "External Source",
          "description": "The source of the alert.",
          "order": 7
        },
        "external_id": {
          "type": "string",
          "title": "External ID",
          "description": "The identifier of the alert in the system, identified by external_source.",
          "order": 8
        },
        "organization": {
          "$ref": "#/definitions/organization_object",
          "title": "organization",
          "description": "The details of the organization that the alert belongs to.",
          "order": 9
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "The description of the alert.",
          "order": 10
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of alert.",
          "order": 11
        },
        "rule": {
          "$ref": "#/definitions/rule_object",
          "title": "Rule",
          "description": "The details about the alert's detection rule.",
          "order": 12
        },
        "rule_matching_keys": {
          "type": "array",
          "title": "Rule Matching Keys",
          "description": "The keys and values used when matching detection rule logic.",
          "items": {
            "type": "object"
          },
          "order": 13
        },
        "rule_keys_of_interest": {
          "type": "array",
          "title": "Rule Keys of Interest",
          "description": "The keys and values used when matching detection rule logic.",
          "items": {
            "type": "object"
          },
          "order": 14
        },
        "responsibility": {
          "type": "string",
          "title": "Responsibility",
          "description": "Indicates the party responsible for the alert.",
          "enum": [
            "UNMAPPED",
            "CUSTOMER",
            "MDR"
          ],
          "order": 15
        },
        "monitored": {
          "type": "boolean",
          "title": "Monitored",
          "description": "Indicates whether monitoring for the organization was active at the time of the alert.",
          "order": 16
        },
        "assignee": {
          "$ref": "#/definitions/assignee_object",
          "title": "Assignee",
          "description": "The user assigned to the alert.",
          "order": 17
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "The priority of the alert.",
          "enum": [
            "UNMAPPED",
            "INFO",
            "LOW",
            "MEDIUM",
            "HIGH",
            "CRITICAL"
          ],
          "order": 18
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the alert.",
          "enum": [
            "UNMAPPED",
            "OPEN",
            "INVESTIGATING",
            "WAITING",
            "CLOSED"
          ],
          "order": 19
        },
        "status_transitions": {
          "$ref": "#/definitions/status_transitions_object",
          "title": "Status Transitions",
          "description": "Information about when the alert status was changed.",
          "order": 20
        },
        "disposition": {
          "type": "string",
          "title": "Disposition",
          "description": "The disposition of the alert.",
          "enum": [
            "UNMAPPED",
            "UNDECIDED",
            "MALICIOUS",
            "BENIGN",
            "UNKNOWN",
            "NOT_APPLICABLE"
          ],
          "order": 21
        },
        "investigation_rrn": {
          "type": "string",
          "title": "Investigation RRN",
          "description": "The RRN of the investigation that the alert is part of.",
          "order": 22
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "The tags applied to the alert.",
          "items": {
            "type": "string"
          },
          "order": 23
        },
        "permissions": {
          "$ref": "#/definitions/permissions_object",
          "title": "Permissions",
          "description": "The permissions the current caller has for the alert.",
          "order": 24
        },
        "fields": {
          "type": "array",
          "title": "Fields",
          "description": "Additional fields specified in the request.",
          "items": {
            "type": "object"
          },
          "order": 25
        }
      }
    },
    "organization_object": {
      "type": "object",
      "title": "organization_object",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The unique identifier of the organization.",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The display name of the organization.",
          "order": 2
        },
        "region": {
          "type": "string",
          "title": "Region",
          "description": "The region that the organization is assigned to.",
          "order": 3
        },
        "product_token": {
          "type": "string",
          "title": "Product Token",
          "description": "The Platform productToken associated with the organization's product.",
          "order": 4
        },
        "customer_id": {
          "type": "string",
          "title": "Customer ID",
          "description": "The unique identifier of the customer.",
          "order": 5
        },
        "customer_name": {
          "type": "string",
          "title": "Customer Name",
          "description": "The display name of the customer.",
          "order": 6
        },
        "customer_code": {
          "type": "string",
          "title": "Customer Code",
          "description": "The customer code for the organization.",
          "order": 7
        },
        "customer_group": {
          "type": "string",
          "title": "Customer Group",
          "description": "The customer group responsible for the organization.",
          "order": 8
        },
        "flags": {
          "type": "array",
          "title": "Flags",
          "description": "The flags associated with the organization.",
          "items": {
            "type": "string"
          },
          "order": 9
        }
      }
    },
    "rule_object": {
      "type": "object",
      "title": "rule_object",
      "properties": {
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The unique identifier of the detection rule.",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The display name for the detection rule.",
          "order": 2
        },
        "mitre_tcodes": {
          "type": "array",
          "title": "Mitre Tcodes",
          "description": "The mitreTCodes associated with the detection rule.",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "version_rrn": {
          "type": "string",
          "title": "Version RRN",
          "description": "The version RRN of the detection rule.",
          "order": 4
        }
      }
    },
    "assignee_object": {
      "type": "object",
      "title": "assignee_object",
      "properties": {
        "at": {
          "type": "string",
          "title": "At",
          "description": "The timestamp when the user was assigned.",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The unique identifier of the user.",
          "order": 2
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email address of the user.",
          "order": 3
        },
        "first_name": {
          "type": "string",
          "title": "First Name",
          "description": "The displayed first name of the user.",
          "order": 4
        },
        "last_name": {
          "type": "string",
          "title": "Last Name",
          "description": "The displayed last name of the user.",
          "order": 5
        }
      }
    },
    "status_transitions_object": {
      "type": "object",
      "title": "status_transitions_object",
      "properties": {
        "seconds_to_first_investigating": {
          "type": "integer",
          "title": "Seconds to first investigating",
          "description": "The number of seconds between when the alert was created and when the alert moved to the INVESTIGATING status, or when it moved directly to the CLOSED status.",
          "order": 1
        },
        "seconds_to_first_closed": {
          "type": "integer",
          "title": "Seconds to first closed",
          "description": "The number of seconds between when the alert was created and when the alert moved to the CLOSED status.",
          "order": 2
        }
      }
    },
    "permissions_object": {
      "type": "object",
      "title": "permissions_object",
      "properties": {
        "canEdit": {
          "type": "boolean",
          "title": "Can edit",
          "description": "Indicates whether the current caller can edit the alert.",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
