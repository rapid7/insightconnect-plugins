# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Edit an issue within Jira"


class Input:
    DESCRIPTION = "description"
    FIELDS = "fields"
    ID = "id"
    NOTIFY = "notify"
    SUMMARY = "summary"
    UPDATE = "update"


class Output:
    SUCCESS = "success"


class EditIssueInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description field on the issue",
      "order": 4
    },
    "fields": {
      "type": "object",
      "title": "Fields",
      "description": "An object of fields and values to change",
      "order": 5
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Issue ID",
      "order": 1
    },
    "notify": {
      "type": "boolean",
      "title": "Notify",
      "description": "Will send a notification email about the issue updated. Admin and project admins credentials need to be used to disable the notification",
      "default": true,
      "order": 2
    },
    "summary": {
      "type": "string",
      "title": "Summary",
      "description": "Summary field on the issue",
      "order": 3
    },
    "update": {
      "type": "object",
      "title": "Update",
      "description": "An object that contains update operations to apply, see examples at https://developer.atlassian.com/server/jira/platform/updating-an-issue-via-the-jira-rest-apis-6848604/",
      "order": 6
    }
  },
  "required": [
    "id",
    "notify"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EditIssueOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "If changes were successful",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
