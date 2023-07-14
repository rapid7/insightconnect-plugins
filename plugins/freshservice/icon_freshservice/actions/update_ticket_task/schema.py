# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update an existing task on a ticket request"


class Input:
    DESCRIPTION = "description"
    DUEDATE = "dueDate"
    GROUPID = "groupId"
    NOTIFYBEFORE = "notifyBefore"
    STATUS = "status"
    TASKID = "taskId"
    TICKETID = "ticketId"
    TITLE = "title"


class Output:
    TASK = "task"


class UpdateTicketTaskInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description of the task",
      "order": 4
    },
    "dueDate": {
      "type": "string",
      "format": "date-time",
      "display_type": "date",
      "title": "Due Date",
      "description": "Due date of the task",
      "order": 6
    },
    "groupId": {
      "type": "integer",
      "title": "Group ID",
      "description": "Unique ID of the group to which the task will be  assigned",
      "order": 8
    },
    "notifyBefore": {
      "type": "integer",
      "title": "Notify Before",
      "description": "Time in seconds before which notification is sent prior to due date",
      "order": 7
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status of the task",
      "enum": [
        "Open",
        "In Progress",
        "Completed"
      ],
      "order": 5
    },
    "taskId": {
      "type": "integer",
      "title": "Task ID",
      "description": "ID of the task which will be updated",
      "order": 2
    },
    "ticketId": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "ID of the ticket for which the task will be updated",
      "order": 1
    },
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Title of the task",
      "order": 3
    }
  },
  "required": [
    "taskId",
    "ticketId"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateTicketTaskOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "task": {
      "$ref": "#/definitions/task",
      "title": "Task",
      "description": "Information about the created task for the provided ticket",
      "order": 1
    }
  },
  "definitions": {
    "task": {
      "type": "object",
      "title": "task",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique ID of the task",
          "order": 1
        },
        "agentId": {
          "type": "integer",
          "title": "Agent ID",
          "description": "ID of the agent to whom the task is assigned",
          "order": 2
        },
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Status of the task",
          "order": 3
        },
        "dueDate": {
          "type": "string",
          "title": "Due Date",
          "description": "Due date of the task",
          "order": 4
        },
        "notifyBefore": {
          "type": "integer",
          "title": "Notify Before",
          "description": "Time in seconds before which notification is sent prior to due date",
          "order": 5
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title of the task",
          "order": 6
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description of the task",
          "order": 7
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Timestamp at which the task was created",
          "order": 8
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "Timestamp at which the task was updated",
          "order": 9
        },
        "closedAt": {
          "type": "string",
          "title": "Closed AT",
          "description": "Timestamp at which the task was closed",
          "order": 10
        },
        "groupId": {
          "type": "integer",
          "title": "Group ID",
          "description": "Unique ID of the group to which the task is assigned",
          "order": 11
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)