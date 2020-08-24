# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a list of activities"


class Input:
    ACCOUNT_IDS = "account_ids"
    ACTIVITY_TYPES = "activity_types"
    AGENT_IDS = "agent_ids"
    COUNT_ONLY = "count_only"
    CREATED_AT_BETWEEN = "created_at_between"
    CREATED_AT_GT = "created_at_gt"
    CREATED_AT_GTE = "created_at_gte"
    CREATED_AT_LT = "created_at_lt"
    CREATED_AT_LTE = "created_at_lte"
    CURSOR = "cursor"
    GROUP_IDS = "group_ids"
    IDS = "ids"
    INCLUDE_HIDDEN = "include_hidden"
    LIMIT = "limit"
    SITE_IDS = "site_ids"
    SKIP = "skip"
    SKIP_COUNT = "skip_count"
    SORT_BY = "sort_by"
    SORT_ORDER = "sort_order"
    THREAT_IDS = "threat_ids"
    USER_EMAILS = "user_emails"
    USER_IDS = "user_ids"
    

class Output:
    DATA = "data"
    PAGINATION = "pagination"
    

class ActivitiesListInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account_ids": {
      "type": "array",
      "title": "Account IDS",
      "description": "List of Account IDs to filter by",
      "items": {
        "type": "string"
      },
      "order": 15
    },
    "activity_types": {
      "type": "array",
      "title": "Activity Types",
      "description": "Return only these activity codes",
      "items": {
        "type": "string"
      },
      "order": 18
    },
    "agent_ids": {
      "type": "array",
      "title": "Agent IDS",
      "description": "Return activities related to specified agent ids",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "count_only": {
      "type": "boolean",
      "title": "Count Only",
      "description": "If true, only total number of items will be returned, without any of the actual objects",
      "order": 14
    },
    "created_at_between": {
      "type": "string",
      "title": "Between Dates",
      "description": "Return activities created within this range (inclusive), example 1514978764288-1514978999999",
      "order": 12
    },
    "created_at_gt": {
      "type": "string",
      "title": "Greater Then Date",
      "description": "Return activities created after or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z",
      "order": 10
    },
    "created_at_gte": {
      "type": "string",
      "title": "Greater or Equal Date",
      "description": "Return activities created after or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z",
      "order": 11
    },
    "created_at_lt": {
      "type": "string",
      "title": "Less Then Date",
      "description": "Return activities created before this date in ISO-8601, example 2018-02-27T04:49:26.257525Z",
      "order": 8
    },
    "created_at_lte": {
      "type": "string",
      "title": "Less or Equal Date",
      "description": "Return activities created before or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z",
      "order": 9
    },
    "cursor": {
      "type": "string",
      "title": "Cursor Position",
      "description": "Cursor position returned by the last request. Should be used for iterating over more than 1000 items, example YWdlbnRfaWQ6NTgwMjkzODE=",
      "order": 13
    },
    "group_ids": {
      "type": "array",
      "title": "Group IDS",
      "description": "Get a list of activities",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "ids": {
      "type": "array",
      "title": "Activity IDS",
      "description": "If true, total number of items will not be calculated, which speeds up execution time",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "include_hidden": {
      "type": "boolean",
      "title": "Include Hidden",
      "description": "Include internal activities hidden from display",
      "order": 2
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Limit number of returned items (1-100)",
      "order": 16
    },
    "site_ids": {
      "type": "array",
      "title": "Site IDS",
      "description": "List of Site IDs to filter by",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "skip": {
      "type": "integer",
      "title": "Skip First N Items",
      "description": "Skip first number of items (0-1000). For iterating over more than a 1000 items please use cursor instead",
      "order": 3
    },
    "skip_count": {
      "type": "boolean",
      "title": "Skip Count",
      "description": "If true, total number of items will not be calculated, which speeds up execution time",
      "order": 6
    },
    "sort_by": {
      "type": "string",
      "title": "Sort By",
      "description": "The column to sort the results by",
      "enum": [
        "id",
        "activityType",
        "createdAt"
      ],
      "order": 17
    },
    "sort_order": {
      "type": "string",
      "title": "Sort Order",
      "description": "Sort direction",
      "enum": [
        "asc",
        "desc"
      ],
      "order": 20
    },
    "threat_ids": {
      "type": "array",
      "title": "Threat IDS",
      "description": "Return only these activity codes",
      "items": {
        "type": "string"
      },
      "order": 19
    },
    "user_emails": {
      "type": "array",
      "title": "User Emails",
      "description": "Email of the user who invoked the activity (If applicable)",
      "items": {
        "type": "string"
      },
      "order": 21
    },
    "user_ids": {
      "type": "array",
      "title": "User IDS",
      "description": "The user who invoked the activity (If applicable)",
      "items": {
        "type": "string"
      },
      "order": 22
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ActivitiesListOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Data",
      "description": "Result of activities list",
      "items": {
        "$ref": "#/definitions/activities_list"
      },
      "order": 1
    },
    "pagination": {
      "$ref": "#/definitions/pagination",
      "title": "Pagination",
      "description": "Pagination object",
      "order": 2
    }
  },
  "required": [
    "data",
    "pagination"
  ],
  "definitions": {
    "activities_list": {
      "type": "object",
      "title": "activities_list",
      "properties": {
        "accountId": {
          "type": "string",
          "title": "Account ID",
          "description": "Related account (If applicable)",
          "order": 3
        },
        "activityType": {
          "type": "integer",
          "title": "Activity Type",
          "description": "Activity type",
          "order": 14
        },
        "agentId": {
          "type": "string",
          "title": "Agent ID",
          "description": "Related agent (If applicable)",
          "order": 12
        },
        "agentUpdatedVersion": {
          "type": "string",
          "title": "Agent Updated Version",
          "description": "Agent's new version (If applicable)",
          "order": 6
        },
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Comments",
          "order": 1
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Activity creation time (UTC)",
          "order": 4
        },
        "data": {
          "type": "object",
          "title": "Data",
          "description": "Extra activity specific data",
          "order": 5
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Extra activity information",
          "order": 10
        },
        "groupId": {
          "type": "string",
          "title": "Group ID",
          "description": "Related group (If applicable)",
          "order": 17
        },
        "hash": {
          "type": "string",
          "title": "Hash",
          "description": "Threat file hash (If applicable)",
          "order": 13
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Activity ID",
          "order": 8
        },
        "osFamily": {
          "type": "string",
          "title": "OS Family",
          "description": "Agent's OS type (if applicable)",
          "order": 15
        },
        "primaryDescription": {
          "type": "string",
          "title": "Primary Description",
          "description": "Primary description",
          "order": 11
        },
        "secondaryDescription": {
          "type": "string",
          "title": "Secondary Description",
          "description": "Secondary description",
          "order": 18
        },
        "siteId": {
          "type": "string",
          "title": "Site ID",
          "description": "Related site (If applicable)",
          "order": 7
        },
        "threatId": {
          "type": "string",
          "title": "Threat ID",
          "description": "Related threat (If applicable)",
          "order": 16
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "Activity last updated time (UTC)",
          "order": 9
        },
        "userId": {
          "type": "string",
          "title": "UserId",
          "description": "The user who invoked the activity (If applicable)",
          "order": 2
        }
      }
    },
    "pagination": {
      "type": "object",
      "title": "pagination",
      "properties": {
        "nextCursor": {
          "type": "string",
          "title": "Next Cursor",
          "description": "Next cursor",
          "order": 2
        },
        "totalItems": {
          "type": "integer",
          "title": "Total Items",
          "description": "Total items",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
