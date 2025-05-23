# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a group in Azure and enable it for Microsoft Teams"


class Input:
    GROUP_DESCRIPTION = "group_description"
    GROUP_NAME = "group_name"
    MAIL_ENABLED = "mail_enabled"
    MAIL_NICKNAME = "mail_nickname"
    MEMBERS = "members"
    OWNERS = "owners"


class Output:
    GROUP = "group"


class CreateTeamsEnabledGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group_description": {
      "type": "string",
      "title": "Group Description",
      "description": "Group description",
      "order": 2
    },
    "group_name": {
      "type": "string",
      "title": "Team Name",
      "description": "Team name",
      "order": 1
    },
    "mail_enabled": {
      "type": "boolean",
      "title": "Mail Enabled",
      "description": "Should e-mail should be enabled for this group",
      "order": 4
    },
    "mail_nickname": {
      "type": "string",
      "title": "Mail Nickname",
      "description": "The nickname for the email address of this group in Outlook",
      "order": 3
    },
    "members": {
      "type": "array",
      "title": "Members",
      "description": "A list of usernames to set as members",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "owners": {
      "type": "array",
      "title": "Owners",
      "description": "A list of usernames to set as owners",
      "items": {
        "type": "string"
      },
      "order": 5
    }
  },
  "required": [
    "group_description",
    "group_name",
    "mail_enabled",
    "mail_nickname"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateTeamsEnabledGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group": {
      "$ref": "#/definitions/group",
      "title": "Group",
      "description": "Information about the group that was created",
      "order": 1
    }
  },
  "definitions": {
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "mailNickname": {
          "type": "string",
          "title": "Mail Nickname",
          "description": "Mail nickname",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "mail": {
          "type": "string",
          "title": "Mail",
          "description": "Mail",
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 4
        },
        "securityEnabled": {
          "type": "boolean",
          "title": "Security Enabled",
          "description": "Security enabled",
          "order": 5
        },
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "Display name",
          "order": 6
        },
        "createdDateTime": {
          "type": "string",
          "title": "Created Date Time",
          "description": "Created date time",
          "order": 7
        },
        "mailEnabled": {
          "type": "boolean",
          "title": "Mail Enabled",
          "description": "Mail enabled",
          "order": 8
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
