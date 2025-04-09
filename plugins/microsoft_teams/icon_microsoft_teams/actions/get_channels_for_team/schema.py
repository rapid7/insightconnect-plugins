# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Returns all the channels associated with a team"


class Input:
    CHANNEL_NAME = "channel_name"
    TEAM_NAME = "team_name"


class Output:
    CHANNELS = "channels"


class GetChannelsForTeamInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "channel_name": {
      "type": "string",
      "title": "Channel Name",
      "description": "Optional regex-capable channel to look for",
      "order": 2
    },
    "team_name": {
      "type": "string",
      "title": "Team Name",
      "description": "Team name to look for",
      "order": 1
    }
  },
  "required": [
    "team_name"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetChannelsForTeamOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "channels": {
      "type": "array",
      "title": "Channels",
      "description": "Array of channels",
      "items": {
        "$ref": "#/definitions/channel"
      },
      "order": 1
    }
  },
  "definitions": {
    "channel": {
      "type": "object",
      "title": "channel",
      "properties": {
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "Display name",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 3
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
