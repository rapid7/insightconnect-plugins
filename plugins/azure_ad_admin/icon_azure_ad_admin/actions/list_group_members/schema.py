# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of the group's direct members. A group can have users, organizational contacts, devices, service principals and other groups as members"


class Input:
    GROUP_ID = "group_id"


class Output:
    COUNT = "count"
    MEMBERS = "members"


class ListGroupMembersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group_id": {
      "type": "string",
      "title": "Group ID",
      "description": "ID of group to search for",
      "order": 1
    }
  },
  "required": [
    "group_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListGroupMembersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Count of members in group",
      "order": 2
    },
    "members": {
      "type": "array",
      "title": "Members",
      "description": "Members",
      "items": {
        "$ref": "#/definitions/user_information"
      },
      "order": 1
    }
  },
  "definitions": {
    "user_information": {
      "type": "object",
      "title": "user_information",
      "properties": {
        "accountEnabled": {
          "type": "boolean",
          "title": "Account Enabled",
          "description": "Account enabled",
          "order": 1
        },
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "Display name",
          "order": 2
        },
        "mobilePhone": {
          "type": "string",
          "title": "Mobile Phone",
          "description": "Mobile phone",
          "order": 3
        },
        "preferredLanguage": {
          "type": "string",
          "title": "Preferred Language",
          "description": "Preferred language",
          "order": 4
        },
        "jobTitle": {
          "type": "string",
          "title": "Job Title",
          "description": "Job title",
          "order": 5
        },
        "userPrincipalName": {
          "type": "string",
          "title": "User Principal Name",
          "description": "User principal name",
          "order": 6
        },
        "@odata.context": {
          "type": "string",
          "title": "@odata.Context",
          "description": "@odata.context",
          "order": 7
        },
        "officeLocation": {
          "type": "string",
          "title": "Office Location",
          "description": "Office location",
          "order": 8
        },
        "businessPhones": {
          "type": "array",
          "title": "Business Phones",
          "description": "Business phones",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "mail": {
          "type": "string",
          "title": "Mail",
          "description": "Mail",
          "order": 10
        },
        "surname": {
          "type": "string",
          "title": "Surname",
          "description": "Surname",
          "order": 11
        },
        "givenName": {
          "type": "string",
          "title": "Given Name",
          "description": "Given Name",
          "order": 12
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 13
        },
        "manager": {
          "$ref": "#/definitions/manager",
          "title": "Manager",
          "description": "Manager",
          "order": 14
        }
      }
    },
    "manager": {
      "type": "object",
      "title": "manager",
      "properties": {
        "@odata.context": {
          "type": "string",
          "title": "@odata.type",
          "description": "@odata.type",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Manager ID",
          "order": 2
        },
        "deletedDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Deleted Date Time",
          "description": "Deleted Date Time",
          "order": 3
        },
        "accountEnabled": {
          "type": "boolean",
          "title": "Account Enabled",
          "description": "Account Enabled",
          "order": 4
        },
        "ageGroup": {
          "type": "string",
          "title": "Age Group",
          "description": "Age Group",
          "order": 5
        },
        "businessPhones": {
          "type": "array",
          "title": "Business Phones",
          "description": "Business phones",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "companyName": {
          "type": "string",
          "title": "Company Name",
          "description": "Company Name",
          "order": 7
        },
        "consentProvidedForMinor": {
          "type": "string",
          "title": "Consent Provided For Minor",
          "description": "Consent Provided For Minor",
          "order": 8
        },
        "country": {
          "type": "string",
          "title": "Country",
          "description": "Country",
          "order": 9
        },
        "createdDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Created Date Time",
          "description": "Created Date Time",
          "order": 10
        },
        "creationType": {
          "type": "string",
          "title": "Creation Type",
          "description": "Creation Type",
          "order": 11
        },
        "department": {
          "type": "string",
          "title": "Department",
          "description": "Department",
          "order": 12
        },
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "Display Name",
          "order": 13
        },
        "employeeId": {
          "type": "string",
          "title": "Employee ID",
          "description": "Employee ID",
          "order": 14
        },
        "employeeHireDate": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Employee Hire Date",
          "description": "Employee Hire Date",
          "order": 15
        },
        "employeeType": {
          "type": "string",
          "title": "Employee Type",
          "description": "Employee Type",
          "order": 16
        },
        "externalUserState": {
          "type": "string",
          "title": "External User State",
          "description": "External User State",
          "order": 17
        },
        "externalUserStateChangeDateTime": {
          "type": "string",
          "title": "External User State Change Date Time",
          "description": "External User State Change Date Time",
          "order": 18
        },
        "faxNumber": {
          "type": "string",
          "title": "Fax Number",
          "description": "Fax Number",
          "order": 19
        },
        "givenName": {
          "type": "string",
          "title": "Given Name",
          "description": "Given Name",
          "order": 20
        },
        "jobTitle": {
          "type": "string",
          "title": "Job Title",
          "description": "Job Title",
          "order": 21
        },
        "legalAgeGroupClassification": {
          "type": "string",
          "title": "Legal Age Group Classification",
          "description": "Legal Age Group Classification",
          "order": 22
        },
        "mail": {
          "type": "string",
          "title": "Mail",
          "description": "Mail",
          "order": 23
        },
        "mailNickname": {
          "type": "string",
          "title": "Mail Nickname",
          "description": "Mail Nickname",
          "order": 24
        },
        "mobilePhone": {
          "type": "string",
          "title": "Mobile Phone",
          "description": "Mobile Phone",
          "order": 25
        },
        "onPremisesDistinguishedName": {
          "type": "string",
          "title": "On Premises Distinguished Name",
          "description": "On Premises Distinguished Name",
          "order": 26
        },
        "onPremisesDomainName": {
          "type": "string",
          "title": "On Premises Domain Name",
          "description": "On Premises Domain Name",
          "order": 27
        },
        "onPremisesImmutableId": {
          "type": "string",
          "title": "On Premises Immutable ID",
          "description": "On Premises Immutable ID",
          "order": 28
        },
        "onPremisesLastSyncDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "On Premises Last Sync Date Time",
          "description": "On Premises Last Sync Date Time",
          "order": 29
        },
        "onPremisesSecurityIdentifier": {
          "type": "string",
          "title": "On Premises Security Identifier",
          "description": "On Premises Security Identifier",
          "order": 30
        },
        "onPremisesSamAccountName": {
          "type": "string",
          "title": "On Premises Sam Account Name",
          "description": "On Premises Sam Account Name",
          "order": 31
        },
        "onPremisesSyncEnabled": {
          "type": "boolean",
          "title": "On Premises Sync Enabled",
          "description": "On Premises Sync Enabled",
          "order": 32
        },
        "onPremisesUserPrincipalName": {
          "type": "string",
          "title": "On Premises User Principal Name",
          "description": "On Premises User Principal Name",
          "order": 33
        },
        "otherMails": {
          "type": "array",
          "title": "Other Mails",
          "description": "Other Mails",
          "items": {
            "type": "string"
          },
          "order": 34
        },
        "passwordPolicies": {
          "type": "string",
          "title": "Password Policies",
          "description": "Password Policies",
          "order": 35
        },
        "officeLocation": {
          "type": "string",
          "title": "Office Location",
          "description": "Office Location",
          "order": 36
        },
        "postalCode": {
          "type": "string",
          "title": "Postal Code",
          "description": "Postal Code",
          "order": 37
        },
        "preferredDataLocation": {
          "type": "string",
          "title": "Preferred Data Location",
          "description": "Preferred Data Location",
          "order": 38
        },
        "proxyAddresses": {
          "type": "array",
          "title": "Proxy Addresses",
          "description": "Proxy Addresses",
          "items": {
            "type": "string"
          },
          "order": 39
        },
        "refreshTokensValidFromDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Refresh Tokens Valid From Date Time",
          "description": "Refresh Tokens Valid From Date Time",
          "order": 40
        },
        "imAddresses": {
          "type": "array",
          "title": "Im Addresses",
          "description": "Im Addresses",
          "items": {
            "type": "string"
          },
          "order": 41
        },
        "isResourceAccount": {
          "type": "boolean",
          "title": "Is Resource Account",
          "description": "Is Resource Account",
          "order": 42
        },
        "showInAddressList": {
          "type": "boolean",
          "title": "Show In Address List",
          "description": "Show In Address List",
          "order": 43
        },
        "signInSessionsValidFromDateTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Sign In Sessions Valid From Date Time",
          "description": "Sign In Sessions Valid From Date Time",
          "order": 44
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 45
        },
        "streetAddress": {
          "type": "string",
          "title": "Street Address",
          "description": "Street Address",
          "order": 46
        },
        "surname": {
          "type": "string",
          "title": "Surname",
          "description": "Surname",
          "order": 47
        },
        "usageLocation": {
          "type": "string",
          "title": "Usage Location",
          "description": "Usage Location",
          "order": 48
        },
        "userPrincipalName": {
          "type": "string",
          "title": "User Principal Name",
          "description": "User Principal Name",
          "order": 49
        },
        "userType": {
          "type": "string",
          "title": "User Type",
          "description": "User Type",
          "order": 50
        },
        "authorizationInfo": {
          "type": "object",
          "title": "Authorization Info",
          "description": "Authorization Info",
          "order": 51
        },
        "employeeOrgData": {
          "type": "string",
          "title": "Employee Org Data",
          "description": "Employee Org Data",
          "order": 52
        },
        "assignedLicenses": {
          "type": "array",
          "title": "Assigned Licenses",
          "description": "Assigned Licenses",
          "items": {
            "type": "object"
          },
          "order": 53
        },
        "assignedPlans": {
          "type": "array",
          "title": "Assigned Plans",
          "description": "Assigned Plans",
          "items": {
            "type": "object"
          },
          "order": 54
        },
        "identities": {
          "type": "array",
          "title": "Identities",
          "description": "Identities",
          "items": {
            "type": "object"
          },
          "order": 55
        },
        "onPremisesProvisioningErrors": {
          "type": "array",
          "title": "On Premises Provisioning Errors",
          "description": "On Premises Provisioning Errors",
          "items": {
            "type": "string"
          },
          "order": 56
        },
        "passwordProfile": {
          "type": "object",
          "title": "Password Profile",
          "description": "Password Profile",
          "order": 57
        },
        "onPremisesExtensionAttributes": {
          "type": "object",
          "title": "On Premises Extension Attributes",
          "description": "On Premises Extension Attributes",
          "order": 58
        },
        "provisionedPlans": {
          "type": "array",
          "title": "Provisioned Plans",
          "description": "Provisioned Plans",
          "items": {
            "type": "object"
          },
          "order": 59
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
