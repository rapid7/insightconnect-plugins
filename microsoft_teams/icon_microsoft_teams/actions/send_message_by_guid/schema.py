# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Sends a message using the GUID for the team and channel. This is more performant than send message"


class Input:
    CHANNEL_GUID = "channel_guid"
    IS_HTML = "is_html"
    MESSAGE = "message"
    TEAM_GUID = "team_guid"
    

class Output:
    MESSAGE = "message"
    

class SendMessageByGuidInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "channel_guid": {
      "type": "string",
      "title": "Channel GUID",
      "description": "Channel GUID",
      "order": 2
    },
    "is_html": {
      "type": "boolean",
      "title": "Is HTML",
      "description": "Is the message HTML",
      "order": 3
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message to send",
      "order": 4
    },
    "team_guid": {
      "type": "string",
      "title": "Team GUID",
      "description": "Team GUID",
      "order": 1
    }
  },
  "required": [
    "channel_guid",
    "is_html",
    "message",
    "team_guid"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SendMessageByGuidOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "$ref": "#/definitions/message",
      "title": "Message",
      "description": "The message object that was created",
      "order": 1
    }
  },
  "definitions": {
    "body": {
      "type": "object",
      "title": "body",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "Content",
          "order": 1
        },
        "contentType": {
          "type": "string",
          "title": "Content Type",
          "description": "Content type",
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
      },
      "definitions": {
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
        }
      }
    },
    "message": {
      "type": "object",
      "title": "message",
      "properties": {
        "body": {
          "$ref": "#/definitions/body",
          "title": "Body",
          "description": "Body",
          "order": 1
        },
        "createdDateTime": {
          "type": "string",
          "title": "Created Date Time",
          "description": "Created date time",
          "order": 3
        },
        "first_word": {
          "type": "string",
          "title": "First Word",
          "description": "Extracted first word from message (easy way to obtain a chat command)",
          "order": 9
        },
        "from": {
          "$ref": "#/definitions/from",
          "title": "From",
          "description": "From",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 8
        },
        "importance": {
          "type": "string",
          "title": "Importance",
          "description": "Importance",
          "order": 5
        },
        "locale": {
          "type": "string",
          "title": "Locale",
          "description": "Locale",
          "order": 7
        },
        "messageType": {
          "type": "string",
          "title": "Message Type",
          "description": "Message type",
          "order": 6
        },
        "webUrl": {
          "type": "string",
          "title": "Web URL",
          "description": "Web URL",
          "order": 4
        },
        "words": {
          "type": "array",
          "title": "Words",
          "description": "The message split by spaces into a list of words. This list makes finding and using parameters in chat commands easier",
          "items": {
            "type": "string"
          },
          "order": 10
        }
      },
      "definitions": {
        "body": {
          "type": "object",
          "title": "body",
          "properties": {
            "content": {
              "type": "string",
              "title": "Content",
              "description": "Content",
              "order": 1
            },
            "contentType": {
              "type": "string",
              "title": "Content Type",
              "description": "Content type",
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
          },
          "definitions": {
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
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
