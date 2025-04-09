# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a conversation member to a private channel"


class Input:
    CHANNEL_NAME = "channel_name"
    GROUP_NAME = "group_name"
    MEMBER_LOGIN = "member_login"
    ROLE = "role"


class Output:
    SUCCESS = "success"


class AddMemberToChannelInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "channel_name": {
      "type": "string",
      "title": "Channel Name",
      "description": "Name of the channel to which the member is to be added",
      "order": 3
    },
    "group_name": {
      "type": "string",
      "title": "Group Name",
      "description": "Name of the group in which the channel is located",
      "order": 2
    },
    "member_login": {
      "type": "string",
      "title": "Member Login",
      "description": "The login of the group member to be added to a channel",
      "order": 1
    },
    "role": {
      "type": "string",
      "title": "Member Role",
      "description": "Role of the member to add",
      "default": "Member",
      "enum": [
        "Owner",
        "Member"
      ],
      "order": 4
    }
  },
  "required": [
    "channel_name",
    "group_name",
    "member_login",
    "role"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddMemberToChannelOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Boolean indicating if this action was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
