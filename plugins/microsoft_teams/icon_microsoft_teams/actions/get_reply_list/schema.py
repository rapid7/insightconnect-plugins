# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List all the replies to a message in a channel of a team"


class Input:
    CHANNEL_NAME = "channel_name"
    MESSAGE_ID = "message_id"
    TEAM_NAME = "team_name"


class Output:
    MESSAGES = "messages"


class GetReplyListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "channel_name": {
      "type": "string",
      "title": "Channel Name",
      "description": "Channel",
      "order": 2
    },
    "message_id": {
      "type": "string",
      "title": "Message ID",
      "description": "The ID of message",
      "order": 3
    },
    "team_name": {
      "type": "string",
      "title": "Team Name",
      "description": "Team name",
      "order": 1
    }
  },
  "required": [
    "channel_name",
    "message_id",
    "team_name"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetReplyListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "messages": {
      "type": "array",
      "title": "Message",
      "description": "The message object that was created",
      "items": {
        "$ref": "#/definitions/chatMessage"
      },
      "order": 1
    }
  },
  "definitions": {
    "chatMessage": {
      "type": "object",
      "title": "chatMessage",
      "properties": {
        "attachments": {
          "type": "array",
          "title": "Attachments",
          "description": "References to attached objects",
          "items": {
            "type": "object"
          },
          "order": 1
        },
        "body": {
          "$ref": "#/definitions/itemBody",
          "title": "Body",
          "description": "Representation of the content of the chat message",
          "order": 2
        },
        "chatId": {
          "type": "string",
          "title": "Chat ID",
          "description": "Represents the identity of the chat",
          "order": 3
        },
        "channelIdentity": {
          "$ref": "#/definitions/channelIdentity",
          "title": "Channel Identity",
          "description": "Represents identity of the channel",
          "order": 4
        },
        "createdDateTime": {
          "type": "string",
          "title": "Created Date Time",
          "description": "Created date time",
          "order": 5
        },
        "deletedDateTime": {
          "type": "string",
          "title": "Deleted Date Time",
          "description": "Deleted date time",
          "order": 6
        },
        "etag": {
          "type": "string",
          "title": "Etag",
          "description": "Version number of the chat message",
          "order": 7
        },
        "eventDetail": {
          "type": "object",
          "title": "Event Detail",
          "description": "Represents details of an event that happened in a chat",
          "order": 8
        },
        "from": {
          "$ref": "#/definitions/from",
          "title": "From",
          "description": "Details of the sender of the chat message",
          "order": 9
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique ID of the message",
          "order": 10
        },
        "importance": {
          "type": "string",
          "title": "Importance",
          "description": "The importance of the chat message",
          "order": 11
        },
        "lastModifiedDateTime": {
          "type": "string",
          "title": "Last Modified Date Time",
          "description": "Timestamp when the chat message is created (initial setting) or modified",
          "order": 12
        },
        "lastEditedDateTime": {
          "type": "string",
          "title": "Last Edited Date Time",
          "description": "Timestamp when edits to the chat message were made",
          "order": 13
        },
        "locale": {
          "type": "string",
          "title": "Locale",
          "description": "Locale of the chat message set by the client",
          "order": 14
        },
        "mentions": {
          "type": "array",
          "title": "Mentions",
          "description": "List of entities mentioned in the chat message",
          "items": {
            "type": "object"
          },
          "order": 15
        },
        "messageHistory": {
          "type": "array",
          "title": "Message History",
          "description": "List of activity history of a message item",
          "items": {
            "type": "object"
          },
          "order": 16
        },
        "messageType": {
          "type": "string",
          "title": "Message Type",
          "description": "The type of chat message",
          "order": 17
        },
        "policyViolation": {
          "type": "object",
          "title": "Policy Violation",
          "description": "Defines the properties of a policy violation",
          "order": 18
        },
        "reactions": {
          "type": "array",
          "title": "Reactions",
          "description": "Reactions for this chat message",
          "items": {
            "$ref": "#/definitions/chatMessageReaction"
          },
          "order": 19
        },
        "replyToId": {
          "type": "string",
          "title": "Reply To ID",
          "description": "ID of the parent chat message or root chat message of the thread",
          "order": 20
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "The subject of the chat message, in plaintext",
          "order": 21
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Summary text of the chat message that could be used for push notifications and summary views or fall back views",
          "order": 22
        },
        "webUrl": {
          "type": "string",
          "title": "Web URL",
          "description": "Link to the message in Microsoft Teams",
          "order": 23
        }
      }
    },
    "itemBody": {
      "type": "object",
      "title": "itemBody",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "The content of the item",
          "order": 1
        },
        "contentType": {
          "type": "string",
          "title": "Content Type",
          "description": "The type of the content, possible values are text and HTML",
          "order": 2
        }
      }
    },
    "channelIdentity": {
      "type": "object",
      "title": "channelIdentity",
      "properties": {
        "channelId": {
          "type": "string",
          "title": "Channel ID",
          "description": "The identity of the channel in which the message was posted",
          "order": 1
        },
        "teamId": {
          "type": "string",
          "title": "Team ID",
          "description": "The identity of the team in which the message was posted",
          "order": 2
        }
      }
    },
    "from": {
      "type": "object",
      "title": "from",
      "properties": {
        "user": {
          "$ref": "#/definitions/user",
          "title": "User",
          "description": "User",
          "order": 1
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "displayName": {
          "type": "string",
          "title": "Display name",
          "description": "Display name",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        }
      }
    },
    "chatMessageReaction": {
      "type": "object",
      "title": "chatMessageReaction",
      "properties": {
        "createdDateTime": {
          "type": "string",
          "title": "Created Date Time",
          "description": "Created date time",
          "order": 1
        },
        "reactionType": {
          "type": "string",
          "title": "Reaction Type",
          "description": "Reaction Type",
          "order": 2
        },
        "user": {
          "$ref": "#/definitions/user",
          "title": "User",
          "description": "The user who reacted to the message",
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
