# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Watches for newly-created or updated issues"


class Input:
    GET_ATTACHMENTS = "get_attachments"
    INCLUDE_FIELDS = "include_fields"
    INTERVAL = "interval"
    JQL = "jql"
    PROJECTS = "projects"


class Output:
    ISSUE = "issue"


class MonitorIssuesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "get_attachments": {
      "type": "boolean",
      "title": "Get Attachments",
      "description": "Get attachments from issue",
      "default": false,
      "order": 3
    },
    "include_fields": {
      "type": "boolean",
      "title": "Include Fields",
      "description": "Whether returned Issues should include fields",
      "default": false,
      "order": 5
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "Interval between next poll in seconds, default is 60 seconds",
      "default": 60,
      "order": 4
    },
    "jql": {
      "type": "string",
      "title": "JQL",
      "description": "JQL search string to use",
      "order": 2
    },
    "projects": {
      "type": "array",
      "title": "Projects",
      "description": "List of Project IDs or names",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorIssuesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "issue": {
      "$ref": "#/definitions/issue",
      "title": "Issue",
      "description": "New or updated issue",
      "order": 1
    }
  },
  "definitions": {
    "issue": {
      "type": "object",
      "title": "issue",
      "properties": {
        "id": {
          "type": "string",
          "description": "Issue ID",
          "order": 1
        },
        "project": {
          "type": "string",
          "description": "Project",
          "order": 2
        },
        "key": {
          "type": "string",
          "description": "Issue Key",
          "order": 3
        },
        "status": {
          "type": "string",
          "description": "Status",
          "order": 4
        },
        "url": {
          "type": "string",
          "description": "Issue URL",
          "order": 5
        },
        "summary": {
          "type": "string",
          "description": "Summary",
          "order": 6
        },
        "description": {
          "type": "string",
          "description": "Description",
          "order": 7
        },
        "resolution": {
          "type": "string",
          "description": "Resolution",
          "order": 8
        },
        "labels": {
          "type": "array",
          "description": "Labels",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "reporter": {
          "type": "string",
          "description": "Reporting User",
          "order": 10
        },
        "assignee": {
          "type": "string",
          "description": "Assigned User",
          "order": 11
        },
        "created_at": {
          "type": "string",
          "description": "Created At",
          "order": 12
        },
        "updated_at": {
          "type": "string",
          "description": "Updated At",
          "order": 13
        },
        "resolved_at": {
          "type": "string",
          "description": "Resolved At",
          "order": 14
        },
        "attachments": {
          "type": "array",
          "description": "Attachments",
          "items": {
            "$ref": "#/definitions/file"
          },
          "order": 15
        },
        "fields": {
          "type": "object",
          "description": "Full list of fields",
          "order": 16
        }
      }
    },
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        },
        "content": {
          "type": "string",
          "format": "bytes",
          "title": "Content",
          "description": "File contents"
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
