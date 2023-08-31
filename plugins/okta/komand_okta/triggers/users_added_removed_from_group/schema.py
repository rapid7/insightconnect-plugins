# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Monitors a list of groups for user membership changes"


class Input:
    GROUPIDS = "groupIds"
    INTERVAL = "interval"


class Output:
    USERSADDEDTOGROUPS = "usersAddedToGroups"
    USERSREMOVEDFROMGROUPS = "usersRemovedFromGroups"


class UsersAddedRemovedFromGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "groupIds": {
      "type": "array",
      "title": "Group ID's",
      "description": "A list of group ID's",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "The time in seconds between checks for changes to the groups users",
      "default": 300,
      "order": 2
    }
  },
  "required": [
    "groupIds",
    "interval"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UsersAddedRemovedFromGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "usersAddedToGroups": {
      "type": "array",
      "title": "Additions",
      "description": "Users added to a group since the last check",
      "items": {
        "$ref": "#/definitions/user_group"
      },
      "order": 1
    },
    "usersRemovedFromGroups": {
      "type": "array",
      "title": "Removals",
      "description": "Users removed from a group since the last check",
      "items": {
        "$ref": "#/definitions/user_group"
      },
      "order": 2
    }
  },
  "required": [
    "usersAddedToGroups",
    "usersRemovedFromGroups"
  ],
  "definitions": {
    "user_group": {
      "type": "object",
      "title": "user_group",
      "properties": {
        "groupName": {
          "type": "string",
          "title": "Group Name",
          "description": "Name of the group",
          "order": 1
        },
        "groupId": {
          "type": "string",
          "title": "Group ID",
          "description": "ID of the group",
          "order": 2
        },
        "users": {
          "type": "array",
          "title": "Users",
          "description": "List of users",
          "items": {
            "$ref": "#/definitions/user"
          },
          "order": 3
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Current status of the user",
          "order": 1
        },
        "profile": {
          "$ref": "#/definitions/userProfile",
          "title": "Profile",
          "description": "User profile properties",
          "order": 2
        },
        "passwordChanged": {
          "type": "string",
          "title": "Password Changed",
          "description": "When the password was changed",
          "order": 3
        },
        "created": {
          "type": "string",
          "title": "Created",
          "description": "When the user was created",
          "order": 4
        },
        "activated": {
          "type": "string",
          "title": "Activated",
          "description": "When the user was activated",
          "order": 5
        },
        "lastUpdated": {
          "type": "string",
          "title": "Last Updated",
          "description": "When the user was last updated",
          "order": 6
        },
        "links": {
          "$ref": "#/definitions/userLinks",
          "title": "Links",
          "description": "Link relations for the user's current status",
          "order": 7
        },
        "lastLogin": {
          "type": "string",
          "title": "Last Login",
          "description": "When the last login for the user was",
          "order": 8
        },
        "credentials": {
          "$ref": "#/definitions/credentials",
          "title": "Credentials",
          "description": "User's primary authentication and recovery credentials",
          "order": 9
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "User ID",
          "order": 10
        },
        "statusChanged": {
          "type": "string",
          "title": "Status Changed",
          "description": "When the status of the user changed",
          "order": 11
        },
        "type": {
          "$ref": "#/definitions/userType",
          "title": "User Type",
          "description": "Type of the user",
          "order": 12
        }
      }
    },
    "userProfile": {
      "type": "object",
      "title": "userProfile",
      "properties": {
        "login": {
          "type": "string",
          "title": "Login",
          "description": "Login of the user",
          "order": 1
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Primary email address of the user",
          "order": 2
        },
        "secondEmail": {
          "type": "string",
          "title": "Secondary Email",
          "description": "Secondary email address of user typically used for account recovery",
          "order": 3
        },
        "firstName": {
          "type": "string",
          "title": "First Name",
          "description": "First name of the user",
          "order": 4
        },
        "lastName": {
          "type": "string",
          "title": "Last Name",
          "description": "Last name of the user",
          "order": 5
        },
        "middleName": {
          "type": "string",
          "title": "Middle Name",
          "description": "Middle name(s) of the user",
          "order": 6
        },
        "honorificPrefix": {
          "type": "string",
          "title": "Honorific Prefix",
          "description": "Honorific prefix(es) of the user, or title in most Western languages",
          "order": 7
        },
        "honorificSuffix": {
          "type": "string",
          "title": "Honorific Suffix",
          "description": "Honorific suffix(es) of the user",
          "order": 8
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title of the user",
          "order": 9
        },
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "Name of the user, suitable for display to end users",
          "order": 10
        },
        "nickName": {
          "type": "string",
          "title": "Nick Name",
          "description": "Casual way to address the user in real life",
          "order": 11
        },
        "profileUrl": {
          "type": "string",
          "title": "Profile URL",
          "description": "URL of user's online profile",
          "order": 12
        },
        "primaryPhone": {
          "type": "string",
          "title": "Primary Phone",
          "description": "Primary phone number of user such as home number",
          "order": 13
        },
        "mobilePhone": {
          "type": "string",
          "title": "Mobile Phone",
          "description": "Mobile phone number of user",
          "order": 14
        },
        "streetAddress": {
          "type": "string",
          "title": "Street Address",
          "description": "Full street address component of user's address",
          "order": 15
        },
        "city": {
          "type": "string",
          "title": "City",
          "description": "City or locality component of user's address",
          "order": 16
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State or region component of user's address",
          "order": 17
        },
        "zipCode": {
          "type": "string",
          "title": "ZIP Code",
          "description": "ZIP code or postal code component of user's address",
          "order": 18
        },
        "countryCode": {
          "type": "string",
          "title": "Country Code",
          "description": "Country name component of user's address",
          "order": 19
        },
        "postalAddress": {
          "type": "string",
          "title": "Postal Address",
          "description": "Mailing address component of user's address",
          "order": 20
        },
        "preferredLanguage": {
          "type": "string",
          "title": "Preferred Language",
          "description": "User's preferred written or spoken languages",
          "order": 21
        },
        "locale": {
          "type": "string",
          "title": "Locale",
          "description": "User's default location for purposes of localizing items such as currency, date time format, numerical representations, and so on",
          "order": 22
        },
        "timezone": {
          "type": "string",
          "title": "Time Zone",
          "description": "User's time zone",
          "order": 23
        },
        "userType": {
          "type": "string",
          "title": "User Type",
          "description": "Used to describe the organization to user relationship such as 'Employee' or 'Contractor'",
          "order": 24
        },
        "employeeNumber": {
          "type": "string",
          "title": "Employee Number",
          "description": "Organization or company assigned unique identifier for the user",
          "order": 25
        },
        "costCenter": {
          "type": "string",
          "title": "Cost Center",
          "description": "Name of a cost center assigned to user",
          "order": 26
        },
        "organization": {
          "type": "string",
          "title": "Organization",
          "description": "Name of user's organization",
          "order": 27
        },
        "division": {
          "type": "string",
          "title": "Division",
          "description": "Name of user's division",
          "order": 28
        },
        "department": {
          "type": "string",
          "title": "Department",
          "description": "Name of user's department",
          "order": 29
        },
        "managerId": {
          "type": "string",
          "title": "Manager ID",
          "description": "The identifier of a user's manager",
          "order": 30
        },
        "manager": {
          "type": "string",
          "title": "Manager",
          "description": "Name of the user's manager, suitable for display to end users",
          "order": 31
        }
      }
    },
    "userLinks": {
      "type": "object",
      "title": "userLinks",
      "properties": {
        "self": {
          "$ref": "#/definitions/userLink",
          "title": "Self Link",
          "description": "A self-referential link to this user",
          "order": 1
        },
        "activate": {
          "$ref": "#/definitions/userLink",
          "title": "Activate Link",
          "description": "Lifecycle action to activate the user",
          "order": 2
        },
        "deactivate": {
          "$ref": "#/definitions/userLink",
          "title": "Deactivate Link",
          "description": "Lifecycle action to deactivate the user",
          "order": 3
        },
        "suspend": {
          "$ref": "#/definitions/userLink",
          "title": "Suspend Link",
          "description": "Lifecycle action to suspend the user",
          "order": 4
        },
        "unsuspend": {
          "$ref": "#/definitions/userLink",
          "title": "Unsuspend Link",
          "description": "Lifecycle action to unsuspend the user",
          "order": 5
        },
        "resetPassword": {
          "$ref": "#/definitions/userLink",
          "title": "Reset Password Link",
          "description": "Lifecycle action to trigger a password reset",
          "order": 6
        },
        "expirePassword": {
          "$ref": "#/definitions/userLink",
          "title": "Expire Password Link",
          "description": "Lifecycle action to expire the user's password",
          "order": 7
        },
        "resetFactors": {
          "$ref": "#/definitions/userLink",
          "title": "Reset Factors Link",
          "description": "Lifecycle action to reset all MFA factors",
          "order": 8
        },
        "unlock": {
          "$ref": "#/definitions/userLink",
          "title": "Unlock Link",
          "description": "Lifecycle action to unlock a locked-out user",
          "order": 9
        },
        "forgotPassword": {
          "$ref": "#/definitions/userLink",
          "title": "Forgot Password Link",
          "description": "Resets a user's password by validating the user's recovery credential",
          "order": 10
        },
        "changePassword": {
          "$ref": "#/definitions/userLink",
          "title": "Change Password Link",
          "description": "Changes a user's password validating the user's current password",
          "order": 11
        },
        "changeRecoveryQuestion": {
          "$ref": "#/definitions/userLink",
          "title": "Change Recovery Question Link",
          "description": "Changes a user's recovery credential by validating the user's current password",
          "order": 12
        }
      }
    },
    "userLink": {
      "type": "object",
      "title": "userLink",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "description": "Hyperlink to the operation",
          "order": 1
        },
        "method": {
          "type": "string",
          "title": "Method",
          "description": "Method of the request for the operation",
          "order": 2
        }
      }
    },
    "credentials": {
      "type": "object",
      "title": "credentials",
      "properties": {
        "password": {
          "$ref": "#/definitions/password",
          "title": "Password",
          "description": "Password details",
          "order": 1
        },
        "provider": {
          "$ref": "#/definitions/provider",
          "title": "Provider",
          "description": "Provider details",
          "order": 2
        },
        "recoveryQuestion": {
          "$ref": "#/definitions/recoveryQuestion",
          "title": "Recovery Question",
          "description": "Recovery question details",
          "order": 3
        }
      }
    },
    "password": {
      "type": "string",
      "format": "password",
      "displayType": "password"
    },
    "provider": {
      "type": "object",
      "title": "provider",
      "properties": {
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Provider type",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Provider name",
          "order": 2
        }
      }
    },
    "recoveryQuestion": {
      "type": "object",
      "title": "recoveryQuestion",
      "properties": {
        "question": {
          "type": "string",
          "title": "Recovery Question",
          "description": "Question used for account recovery",
          "order": 1
        },
        "answer": {
          "type": "string",
          "title": "Answer",
          "description": "Answer for the recovery question",
          "order": 2
        }
      }
    },
    "userType": {
      "type": "object",
      "title": "userType",
      "properties": {
        "id": {
          "type": "string",
          "title": "The identifier of the type",
          "description": "ID",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
