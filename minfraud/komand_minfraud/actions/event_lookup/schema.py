# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Query event info"


class Input:
    ADDRESS = "address"
    EVENT_TYPE = "event_type"
    SHOP_ID = "shop_id"
    TIME = "time"
    TRANSACTION_ID = "transaction_id"
    

class Output:
    RISK_SCORE = "risk_score"
    

class EventLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address to query",
      "order": 1
    },
    "event_type": {
      "type": "string",
      "title": "Event Type",
      "description": "Type of event",
      "enum": [
        "none",
        "account_creation",
        "account_login",
        "email_change",
        "password_reset",
        "purchase",
        "recurring_purchase",
        "referral",
        "survey"
      ],
      "order": 5
    },
    "shop_id": {
      "type": "string",
      "title": "Shop ID",
      "description": "Internal ID for the shop",
      "order": 3
    },
    "time": {
      "type": "string",
      "title": "Time",
      "description": "Time of event",
      "order": 4
    },
    "transaction_id": {
      "type": "string",
      "title": "Transaction ID",
      "description": "Transaction ID",
      "order": 2
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EventLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "risk_score": {
      "type": "string",
      "title": "Risk Score",
      "description": "Overall risk score",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
