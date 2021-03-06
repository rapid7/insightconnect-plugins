# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new case observable"


class Input:
    ID = "id"
    OBSERVABLE = "observable"
    

class Output:
    CASE = "case"
    

class CreateCaseObservableInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "Case ID",
      "description": "Case ID e.g. AV_ajI_oYMfcbXhqb9tS",
      "order": 1
    },
    "observable": {
      "$ref": "#/definitions/iobservable",
      "title": "Observable",
      "description": "Observable",
      "order": 2
    }
  },
  "required": [
    "id",
    "observable"
  ],
  "definitions": {
    "iobservable": {
      "type": "object",
      "title": "iobservable",
      "properties": {
        "data": {
          "type": "string",
          "title": "ID",
          "description": "The observable's value e.g. badguy.com",
          "order": 6
        },
        "dataType": {
          "type": "string",
          "title": "Data Type",
          "description": "Observable data type e.g. domain, ip, url, fqdn, uri_path, user-agent, hash, email, mail, mail_subject, registry, regexp, other",
          "order": 1
        },
        "ioc": {
          "type": "boolean",
          "title": "IOC",
          "description": "Indicator of Compromise, default is 2",
          "default": false,
          "order": 5
        },
        "message": {
          "type": "string",
          "title": "Message",
          "description": "Observable message",
          "order": 2
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "List of observable tags",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level, default is 2",
          "default": 2,
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateCaseObservableOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "case": {
      "$ref": "#/definitions/observable",
      "title": "Case",
      "description": "Create case observable output",
      "order": 1
    }
  },
  "definitions": {
    "observable": {
      "type": "object",
      "title": "observable",
      "properties": {
        "_id": {
          "type": "string",
          "title": "ID",
          "description": "Observable _ID",
          "order": 12
        },
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "Observable type",
          "order": 3
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "Time the observable was created at in milliseconds or epoch, e.g. 1496561862924",
          "order": 15
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "Observable created by",
          "order": 10
        },
        "data": {
          "type": "string",
          "title": "Data",
          "description": "Observable data",
          "order": 13
        },
        "dataType": {
          "type": "string",
          "title": "Data Type",
          "description": "Observable data type",
          "order": 6
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Observable ID",
          "order": 14
        },
        "ioc": {
          "type": "boolean",
          "title": "IOC",
          "description": "Indicators of Compromise",
          "order": 7
        },
        "message": {
          "type": "string",
          "title": "Message",
          "description": "Observable message",
          "order": 11
        },
        "reports": {
          "type": "object",
          "title": "Reports",
          "description": "Observable reports",
          "order": 8
        },
        "startDate": {
          "type": "integer",
          "title": "Start Date",
          "description": "Observable start date",
          "order": 2
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Observable status",
          "order": 1
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Observable tags",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level",
          "order": 4
        },
        "user": {
          "type": "string",
          "title": "User",
          "description": "Observable user",
          "order": 9
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
