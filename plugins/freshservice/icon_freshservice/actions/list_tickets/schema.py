# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List all tickets for the given filters"


class Input:
    EMAIL = "email"
    FILTER = "filter"
    ORDERTYPE = "orderType"
    PAGE = "page"
    PERPAGE = "perPage"
    REQUESTERID = "requesterId"
    TYPE = "type"
    UPDATEDSINCE = "updatedSince"


class Output:
    TICKETS = "tickets"


class ListTicketsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "Requester Email",
      "description": "Filter tickets by requester email",
      "order": 3
    },
    "filter": {
      "type": "string",
      "title": "Predefined Filters",
      "description": "Filter tickets using predefined filters. The filters available are new_and_my_open, watching, spam, deleted",
      "order": 1
    },
    "orderType": {
      "type": "string",
      "title": "Order Type",
      "description": "Type of the order",
      "default": "desc",
      "enum": [
        "asc",
        "desc"
      ],
      "order": 6
    },
    "page": {
      "type": "integer",
      "title": "Page",
      "description": "The number of the results page to be returned",
      "order": 7
    },
    "perPage": {
      "type": "integer",
      "title": "Page Size",
      "description": "The number of results per page",
      "default": 20,
      "order": 8
    },
    "requesterId": {
      "type": "integer",
      "title": "Requester ID",
      "description": "Filter tickets by requester ID",
      "order": 2
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Filter tickets by type",
      "default": "All",
      "enum": [
        "Incident",
        "Service Request",
        "All"
      ],
      "order": 5
    },
    "updatedSince": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Update Since",
      "description": "Filter tickets by update date",
      "order": 4
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListTicketsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tickets": {
      "type": "array",
      "title": "Tickets",
      "description": "Information about all tickets obtained using the given filters",
      "items": {
        "$ref": "#/definitions/ticket"
      },
      "order": 1
    }
  },
  "definitions": {
    "ticket": {
      "type": "object",
      "title": "ticket",
      "properties": {
        "assets": {
          "type": "array",
          "title": "Assets",
          "description": "Assets associated with the ticket",
          "items": {
            "$ref": "#/definitions/asset"
          },
          "order": 1
        },
        "attachments": {
          "type": "array",
          "title": "Attachments",
          "description": "Ticket attachments",
          "items": {
            "$ref": "#/definitions/attachment"
          },
          "order": 2
        },
        "ccEmails": {
          "type": "array",
          "title": "CC Emails",
          "description": "Email addresses added in the 'cc' field of the incoming ticket email",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "departmentId": {
          "type": "integer",
          "title": "Department ID",
          "description": "ID of the department to which this ticket belongs",
          "order": 4
        },
        "customFields": {
          "type": "object",
          "title": "Custom Fields",
          "description": "Key value pairs containing the names and values of custom fields",
          "order": 5
        },
        "deleted": {
          "type": "boolean",
          "title": "Deleted",
          "description": "Whether the ticket has been deleted",
          "order": 6
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "HTML content of the ticket",
          "order": 7
        },
        "descriptionText": {
          "type": "string",
          "title": "Description Text",
          "description": "Content of the ticket in plain text",
          "order": 8
        },
        "dueBy": {
          "type": "string",
          "title": "Due By",
          "description": "Timestamp that denotes when the ticket is due to be resolved",
          "order": 9
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email address of the requester",
          "order": 10
        },
        "emailConfigId": {
          "type": "integer",
          "title": "Email Config ID",
          "description": "ID of email config which is used for this ticket",
          "order": 11
        },
        "frDueBy": {
          "type": "string",
          "title": "First Response Due By",
          "description": "Timestamp that denotes when the first response is due",
          "order": 12
        },
        "frEscalated": {
          "type": "boolean",
          "title": "First Response Escalated",
          "description": "Set to true if the ticket has been escalated as a result of the first response time being breached",
          "order": 13
        },
        "fwdEmails": {
          "type": "array",
          "title": "Fwd Emails",
          "description": "Email addresses added while forwarding a ticket",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "groupId": {
          "type": "integer",
          "title": "Group ID",
          "description": "ID of the group to which the ticket has been assigned",
          "order": 15
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique ID of the ticket",
          "order": 16
        },
        "isEscalated": {
          "type": "boolean",
          "title": "Is Escalated",
          "description": "Set to true if the ticket has been escalated for any reason",
          "order": 17
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the requester",
          "order": 18
        },
        "phone": {
          "type": "string",
          "title": "Phone",
          "description": "Phone number of the requester",
          "order": 19
        },
        "priority": {
          "type": "integer",
          "title": "Priority",
          "description": "Priority of the ticket",
          "order": 20
        },
        "category": {
          "type": "string",
          "title": "Category",
          "description": "Ticket category",
          "order": 21
        },
        "subCategory": {
          "type": "string",
          "title": "Sub Category",
          "description": "Ticket sub category",
          "order": 22
        },
        "itemCategory": {
          "type": "string",
          "title": "Item Category",
          "description": "Ticket item category",
          "order": 23
        },
        "replyCcEmails": {
          "type": "array",
          "title": "Reply CC Emails",
          "description": "Email addresses added while replying to a ticket",
          "items": {
            "type": "string"
          },
          "order": 24
        },
        "requesterId": {
          "type": "integer",
          "title": "Requester ID",
          "description": "User ID of the requester",
          "order": 25
        },
        "responderId": {
          "type": "integer",
          "title": "Responder ID",
          "description": "ID of the agent to whom the ticket has been assigned",
          "order": 26
        },
        "source": {
          "type": "integer",
          "title": "Source",
          "description": "The channel through which the ticket was created",
          "order": 27
        },
        "spam": {
          "type": "boolean",
          "title": "Spam",
          "description": "Set to true if the ticket has been marked as spam",
          "order": 28
        },
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Status of the ticket",
          "order": 29
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "Subject of the ticket",
          "order": 30
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags that have been associated with the ticket",
          "items": {
            "type": "string"
          },
          "order": 31
        },
        "toEmails": {
          "type": "array",
          "title": "To Emails",
          "description": "Email addresses to which the ticket was originally sent",
          "items": {
            "type": "string"
          },
          "order": 32
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the ticket",
          "order": 33
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Ticket creation timestamp",
          "order": 34
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "Ticket updated timestamp",
          "order": 35
        },
        "urgency": {
          "type": "integer",
          "title": "Urgency",
          "description": "Ticket urgency",
          "order": 36
        },
        "impact": {
          "type": "integer",
          "title": "Impact",
          "description": "Impact",
          "order": 37
        }
      }
    },
    "asset": {
      "type": "object",
      "title": "asset",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the asset",
          "order": 1
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description of the asset",
          "order": 2
        },
        "ciTypeId": {
          "type": "integer",
          "title": "CI Type ID",
          "description": "ID of the configuration item type",
          "order": 3
        },
        "impact": {
          "type": "integer",
          "title": "Impact",
          "description": "Impact",
          "order": 4
        },
        "created": {
          "type": "string",
          "title": "Created",
          "description": "Date and time when the asset was created",
          "order": 5
        },
        "updated": {
          "type": "string",
          "title": "Updated",
          "description": "Date and time when the asset was updated",
          "order": 6
        },
        "userId": {
          "type": "integer",
          "title": "User ID",
          "description": "ID of the user",
          "order": 7
        },
        "departmentId": {
          "type": "integer",
          "title": "Department ID",
          "description": "ID of the department",
          "order": 8
        },
        "assignedOn": {
          "type": "string",
          "title": "Assigned On",
          "description": "Assigned on",
          "order": 9
        },
        "agentId": {
          "type": "integer",
          "title": "Agent ID",
          "description": "ID of the agent",
          "order": 10
        },
        "authorId": {
          "type": "integer",
          "title": "Author ID",
          "description": "ID of the author",
          "order": 11
        },
        "authorType": {
          "type": "string",
          "title": "Author Type",
          "description": "Type of the author",
          "order": 12
        },
        "deleted": {
          "type": "boolean",
          "title": "Deleted",
          "description": "Whether the asset has been deleted",
          "order": 13
        },
        "displayId": {
          "type": "integer",
          "title": "Display ID",
          "description": "Display ID of the asset",
          "order": 14
        }
      }
    },
    "attachment": {
      "type": "object",
      "title": "attachment",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the attachment",
          "order": 1
        },
        "contentType": {
          "type": "string",
          "title": "Content Type",
          "description": "Content type of the attachment",
          "order": 2
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "Size of the attachment",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Size of the attachment",
          "order": 4
        },
        "attachmentUrl": {
          "type": "string",
          "title": "Attachment URL",
          "description": "Attachment URL",
          "order": 5
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Date and time when the attachment was created",
          "order": 6
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
