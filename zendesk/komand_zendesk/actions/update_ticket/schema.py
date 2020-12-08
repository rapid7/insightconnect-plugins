# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Update ticket"


class Input:
    ASSIGNEE_ID = "assignee_id"
    COLLABORATOR_IDS = "collaborator_ids"
    COMMENT = "comment"
    DUE_AT = "due_at"
    EXTERNAL_ID = "external_id"
    GROUP_ID = "group_id"
    PRIORITY = "priority"
    PROBLEM_ID = "problem_id"
    RECIPIENT = "recipient"
    REQUESTER_ID = "requester_id"
    STATUS = "status"
    SUBJECT = "subject"
    TAGS = "tags"
    TICKET_ID = "ticket_id"
    TYPE = "type"
    

class Output:
    TICKET = "ticket"
    

class UpdateTicketInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assignee_id": {
      "type": "string",
      "title": "Assignee ID",
      "description": "Assignee ID",
      "order": 4
    },
    "collaborator_ids": {
      "type": "array",
      "title": "Collaborator IDs",
      "description": "List of collaborator IDs",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "comment": {
      "$ref": "#/definitions/comment",
      "title": "Comment",
      "description": "Comment",
      "order": 2
    },
    "due_at": {
      "type": "string",
      "title": "Due At",
      "displayType": "date",
      "description": "Time ticket is due",
      "format": "date-time",
      "order": 6
    },
    "external_id": {
      "type": "string",
      "title": "External ID",
      "description": "Support ticket ID",
      "order": 7
    },
    "group_id": {
      "type": "string",
      "title": "Group ID",
      "description": "Group ID",
      "order": 8
    },
    "priority": {
      "type": "string",
      "title": "Priority",
      "description": "Ticket priority",
      "enum": [
        "Urgent",
        "High",
        "Normal",
        "Low",
        ""
      ],
      "order": 14
    },
    "problem_id": {
      "type": "string",
      "title": "Problem ID",
      "description": "For tickets of type 'incident', the numeric ID of the problem the incident is linked to",
      "order": 10
    },
    "recipient": {
      "type": "string",
      "title": "Recipient ID",
      "description": "ID of user recipient",
      "order": 9
    },
    "requester_id": {
      "type": "string",
      "title": "Requester ID",
      "description": "ID of user requesting support",
      "order": 3
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Ticket status",
      "enum": [
        "New",
        "Open",
        "Pending",
        "Hold",
        "Solved",
        "Closed",
        ""
      ],
      "order": 15
    },
    "subject": {
      "type": "string",
      "title": "Subject",
      "description": "Subject of ticket",
      "order": 11
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "Tags describing ticket",
      "items": {
        "type": "string"
      },
      "order": 12
    },
    "ticket_id": {
      "type": "string",
      "title": "Ticket ID",
      "description": "Ticket ID",
      "order": 1
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Ticket type",
      "enum": [
        "Problem",
        "Incident",
        "Task",
        "Question",
        ""
      ],
      "order": 13
    }
  },
  "required": [
    "requester_id",
    "ticket_id"
  ],
  "definitions": {
    "comment": {
      "type": "object",
      "title": "comment",
      "properties": {
        "author_id": {
          "type": "string",
          "title": "Author ID",
          "description": "Author ID",
          "order": 4
        },
        "body": {
          "type": "string",
          "title": "Body",
          "description": "Comment body",
          "order": 1
        },
        "html_body": {
          "type": "string",
          "title": "HTML Body",
          "description": "The comment formatted as HTML. This will be preferred over body",
          "order": 2
        },
        "public": {
          "type": "boolean",
          "title": "Public",
          "description": "Public (true if public comment, false if an internal note)",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateTicketOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ticket": {
      "$ref": "#/definitions/ticket",
      "title": "Ticket",
      "description": "Ticket meta data",
      "order": 1
    }
  },
  "required": [
    "ticket"
  ],
  "definitions": {
    "comment": {
      "type": "object",
      "title": "comment",
      "properties": {
        "author_id": {
          "type": "string",
          "title": "Author ID",
          "description": "Author ID",
          "order": 4
        },
        "body": {
          "type": "string",
          "title": "Body",
          "description": "Comment body",
          "order": 1
        },
        "html_body": {
          "type": "string",
          "title": "HTML Body",
          "description": "The comment formatted as HTML. This will be preferred over body",
          "order": 2
        },
        "public": {
          "type": "boolean",
          "title": "Public",
          "description": "Public (true if public comment, false if an internal note)",
          "order": 3
        }
      }
    },
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    },
    "ticket": {
      "type": "object",
      "title": "ticket",
      "properties": {
        "assignee_id": {
          "type": "string",
          "title": "Assignee ID",
          "order": 2
        },
        "attachment": {
          "$ref": "#/definitions/file",
          "title": "Attachment",
          "order": 1
        },
        "collaborator_ids": {
          "type": "array",
          "title": "Collaborator IDs",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "comment": {
          "$ref": "#/definitions/comment",
          "title": "Comment",
          "order": 4
        },
        "description": {
          "type": "string",
          "title": "Description",
          "order": 5
        },
        "due_at": {
          "type": "string",
          "title": "Due At",
          "displayType": "date",
          "format": "date-time",
          "order": 6
        },
        "external_id": {
          "type": "string",
          "title": "External ID",
          "order": 7
        },
        "group_id": {
          "type": "string",
          "title": "Group ID",
          "order": 8
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "enum": [
            "Urgent",
            "High",
            "Normal",
            "Low",
            ""
          ],
          "order": 15
        },
        "problem_id": {
          "type": "string",
          "title": "Problem ID",
          "order": 11
        },
        "recipient": {
          "type": "string",
          "title": "Recipient ID",
          "order": 10
        },
        "requester_id": {
          "type": "string",
          "title": "Requester ID",
          "order": 9
        },
        "status": {
          "type": "string",
          "title": "Status",
          "enum": [
            "New",
            "Open",
            "Pending",
            "Hold",
            "Solved",
            "Closed",
            ""
          ],
          "order": 16
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "order": 12
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "items": {
            "type": "string"
          },
          "order": 13
        },
        "type": {
          "type": "string",
          "title": "Type",
          "enum": [
            "Problem",
            "Incident",
            "Task",
            "Question",
            ""
          ],
          "order": 14
        }
      },
      "definitions": {
        "comment": {
          "type": "object",
          "title": "comment",
          "properties": {
            "author_id": {
              "type": "string",
              "title": "Author ID",
              "description": "Author ID",
              "order": 4
            },
            "body": {
              "type": "string",
              "title": "Body",
              "description": "Comment body",
              "order": 1
            },
            "html_body": {
              "type": "string",
              "title": "HTML Body",
              "description": "The comment formatted as HTML. This will be preferred over body",
              "order": 2
            },
            "public": {
              "type": "boolean",
              "title": "Public",
              "description": "Public (true if public comment, false if an internal note)",
              "order": 3
            }
          }
        },
        "file": {
          "id": "file",
          "type": "object",
          "title": "File",
          "description": "File Object",
          "properties": {
            "content": {
              "type": "string",
              "title": "Content",
              "description": "File contents",
              "format": "bytes"
            },
            "filename": {
              "type": "string",
              "title": "Filename",
              "description": "Name of file"
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
