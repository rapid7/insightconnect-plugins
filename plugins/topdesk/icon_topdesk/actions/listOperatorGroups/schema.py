# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of operator groups"


class Input:
    FIELDS = "fields"
    PAGESIZE = "pageSize"
    QUERY = "query"
    START = "start"


class Output:
    OPERATORGROUPS = "operatorGroups"


class ListOperatorGroupsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "string",
      "title": "Fields",
      "description": "Only include these specific fields in the response. The default is that all fields are included",
      "order": 4
    },
    "pageSize": {
      "type": "integer",
      "title": "Page Size",
      "description": "The amount of operator groups to be returned per page. Must be between 1 and 100",
      "order": 2
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "A FIQL search expression to filter the result",
      "order": 3
    },
    "start": {
      "type": "integer",
      "title": "Start",
      "description": "The offset at which to start listing the operator groups at. Must be greater or equal to 0",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListOperatorGroupsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "operatorGroups": {
      "type": "array",
      "title": "Operator Groups",
      "description": "List of the operator groups",
      "items": {
        "$ref": "#/definitions/operatorGroup"
      },
      "order": 1
    }
  },
  "definitions": {
    "operatorGroup": {
      "type": "object",
      "title": "operatorGroup",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Operator group identifier",
          "order": 1
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Operator group status",
          "order": 2
        },
        "groupName": {
          "type": "string",
          "title": "Group Name",
          "description": "Operator group name",
          "order": 3
        },
        "preset": {
          "type": "string",
          "title": "Preset",
          "description": "Preset",
          "order": 4
        },
        "branch": {
          "$ref": "#/definitions/branch",
          "title": "Branch",
          "description": "Branch",
          "order": 5
        },
        "location": {
          "$ref": "#/definitions/location",
          "title": "Location",
          "description": "Location",
          "order": 6
        },
        "budgetHolder": {
          "$ref": "#/definitions/fieldObject",
          "title": "Budget Holder",
          "description": "Budget holder",
          "order": 7
        },
        "hourlyRate": {
          "type": "integer",
          "title": "Hourly Rate",
          "description": "Hourly rate",
          "order": 8
        },
        "contact": {
          "$ref": "#/definitions/operatorOutput",
          "title": "Contact",
          "description": "Contact",
          "order": 9
        },
        "installer": {
          "type": "boolean",
          "title": "Installer",
          "description": "Installer",
          "order": 10
        },
        "firstLaneCallOperator": {
          "type": "boolean",
          "title": "First Lane Call Operator",
          "description": "First lane call operator",
          "order": 11
        },
        "secondLaneCallOperator": {
          "type": "boolean",
          "title": "Second Lane Call Operator",
          "description": "Second lane call operator",
          "order": 12
        },
        "problemManager": {
          "type": "boolean",
          "title": "Problem Manager",
          "description": "Problem manager",
          "order": 13
        },
        "problemOperator": {
          "type": "boolean",
          "title": "Problem Operator",
          "description": "Problem operator",
          "order": 14
        },
        "changeCoordinator": {
          "type": "boolean",
          "title": "Change Coordinator",
          "description": "Change coordinator",
          "order": 15
        },
        "changeActivitiesOperator": {
          "type": "boolean",
          "title": "Change Activities Operator",
          "description": "Change Activities operator",
          "order": 16
        },
        "requestForChangeOperator": {
          "type": "boolean",
          "title": "Request for Change Operator",
          "description": "Request for change operator",
          "order": 17
        },
        "extensiveChangeOperator": {
          "type": "boolean",
          "title": "Extensive Change Operator",
          "description": "Extensive change operator",
          "order": 18
        },
        "scenarioManager": {
          "type": "boolean",
          "title": "Scenario Manager",
          "description": "Scenario manager",
          "order": 19
        },
        "planningActivityManager": {
          "type": "boolean",
          "title": "Planning Activity Manager",
          "description": "Planning activity manager",
          "order": 20
        },
        "projectCoordinator": {
          "type": "boolean",
          "title": "Project Coordinator",
          "description": "Project coordinator",
          "order": 21
        },
        "projectActiviesOperator": {
          "type": "boolean",
          "title": "Project Activities Operator",
          "description": "Project activities operator",
          "order": 22
        },
        "stockManager": {
          "type": "boolean",
          "title": "Stock Manager",
          "description": "Stock manager",
          "order": 23
        },
        "reservationsOperator": {
          "type": "boolean",
          "title": "Reservations Operator",
          "description": "Reservations operator",
          "order": 24
        },
        "serviceOperator": {
          "type": "boolean",
          "title": "Service Operator",
          "description": "Service operator",
          "order": 25
        },
        "externalHelpDeskParty": {
          "type": "boolean",
          "title": "External HelpDesk party",
          "description": "External helpdesk party",
          "order": 26
        },
        "contractManager": {
          "type": "boolean",
          "title": "Contract Manager",
          "description": "Contract manager",
          "order": 27
        },
        "operationsOperator": {
          "type": "boolean",
          "title": "Operations Operator",
          "description": "Operations operator",
          "order": 28
        },
        "operationsManager": {
          "type": "boolean",
          "title": "Operations Manager",
          "description": "Operations manager",
          "order": 29
        },
        "knowledgeBaseManager": {
          "type": "boolean",
          "title": "Knowledge Base Manager",
          "description": "Knowledge base manager",
          "order": 30
        },
        "accountManager": {
          "type": "boolean",
          "title": "Account Manager",
          "description": "Account manager",
          "order": 31
        },
        "creationDate": {
          "type": "string",
          "title": "Creation Date",
          "description": "Creation date",
          "order": 32
        },
        "creator": {
          "$ref": "#/definitions/fieldObject",
          "title": "Creator",
          "description": "Creator",
          "order": 33
        },
        "modificationDate": {
          "type": "string",
          "title": "Modification Date",
          "description": "Modification date",
          "order": 34
        },
        "modifier": {
          "$ref": "#/definitions/fieldObject",
          "title": "Modifier",
          "description": "Modifier",
          "order": 35
        },
        "accessRoles": {
          "type": "array",
          "title": "Access Roles",
          "description": "Access roles",
          "items": {
            "$ref": "#/definitions/accessRole"
          },
          "order": 36
        },
        "principalId": {
          "type": "string",
          "title": "Principal ID",
          "description": "Principal identifier",
          "order": 37
        },
        "optionalField1": {
          "$ref": "#/definitions/optionalField",
          "title": "Optional Field 1",
          "description": "Optional field 1",
          "order": 38
        },
        "optionalField2": {
          "$ref": "#/definitions/optionalField",
          "title": "Optional Field 2",
          "description": "Optional field 2",
          "order": 39
        }
      }
    },
    "branch": {
      "type": "object",
      "title": "branch",
      "properties": {
        "clientReferenceNumber": {
          "type": "string",
          "title": "Client Reference Number",
          "description": "Client reference number",
          "order": 1
        },
        "timeZone": {
          "type": "string",
          "title": "Time Zone",
          "description": "Time zone of the branch",
          "order": 2
        },
        "extraA": {
          "$ref": "#/definitions/fieldObject",
          "title": "Extra Field A",
          "description": "Extra field A",
          "order": 3
        },
        "extraB": {
          "$ref": "#/definitions/fieldObject",
          "title": "Extra Field B",
          "description": "Extra field B",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Caller identifier",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Branch name",
          "order": 6
        }
      }
    },
    "fieldObject": {
      "type": "object",
      "title": "fieldObject",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The identifier of the field",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the field",
          "order": 2
        }
      }
    },
    "location": {
      "type": "object",
      "title": "location",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Location identifier",
          "order": 1
        },
        "branch": {
          "$ref": "#/definitions/branch",
          "title": "Branch",
          "description": "Location branch",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Location name",
          "order": 3
        },
        "room": {
          "type": "string",
          "title": "Room",
          "description": "Location room",
          "order": 4
        }
      }
    },
    "operatorOutput": {
      "type": "object",
      "title": "operatorOutput",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Operator identifier",
          "order": 1
        },
        "principalId": {
          "type": "string",
          "title": "Principal ID",
          "description": "Principal identifier",
          "order": 2
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 3
        },
        "accountType": {
          "type": "string",
          "title": "Account Type",
          "description": "Account type",
          "order": 4
        },
        "surName": {
          "type": "string",
          "title": "Surname",
          "description": "Surname",
          "order": 5
        },
        "firstName": {
          "type": "string",
          "title": "Firstname",
          "description": "Firstname",
          "order": 6
        },
        "dynamicName": {
          "type": "string",
          "title": "Dynamic Name",
          "description": "Dynamic name",
          "order": 7
        },
        "initials": {
          "type": "string",
          "title": "Initials",
          "description": "Initials",
          "order": 8
        },
        "prefixes": {
          "type": "string",
          "title": "Prefixes",
          "description": "Prefixes",
          "order": 9
        },
        "birthName": {
          "type": "string",
          "title": "Birth Name",
          "description": "Birth name",
          "order": 10
        },
        "title": {
          "type": "string",
          "description": "Title",
          "order": 11
        },
        "gender": {
          "type": "string",
          "title": "Gender",
          "description": "Gender",
          "order": 12
        },
        "language": {
          "$ref": "#/definitions/fieldObject",
          "title": "Language",
          "description": "Language",
          "order": 13
        },
        "branch": {
          "$ref": "#/definitions/branch",
          "title": "Branch",
          "description": "Branch",
          "order": 14
        },
        "location": {
          "$ref": "#/definitions/location",
          "title": "Location",
          "description": "Location",
          "order": 15
        },
        "telephone": {
          "type": "string",
          "title": "Telephone",
          "description": "Telephone",
          "order": 16
        },
        "mobileNumber": {
          "type": "string",
          "title": "Mobile Number",
          "description": "Mobile number",
          "order": 17
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 18
        },
        "exchangeAccount": {
          "type": "string",
          "title": "Exchange Account",
          "description": "Exchange account",
          "order": 19
        },
        "loginName": {
          "type": "string",
          "title": "Login Name",
          "description": "Login name",
          "order": 20
        },
        "loginPermission": {
          "type": "boolean",
          "title": "Login Permission",
          "description": "Login permission",
          "order": 21
        },
        "jobTitle": {
          "type": "string",
          "title": "Job Title",
          "description": "Job title",
          "order": 22
        },
        "department": {
          "$ref": "#/definitions/fieldObject",
          "title": "Department",
          "description": "Department",
          "order": 23
        },
        "budgetHolder": {
          "$ref": "#/definitions/fieldObject",
          "title": "Budget Holder",
          "description": "Budget holder",
          "order": 24
        },
        "employeeNumber": {
          "type": "string",
          "title": "Employee Number",
          "description": "Employee number",
          "order": 25
        },
        "hourlyRate": {
          "type": "integer",
          "title": "Hourly Rate",
          "description": "Hourly rate",
          "order": 26
        },
        "networkLoginName": {
          "type": "string",
          "title": "Network Login Name",
          "description": "Network login name",
          "order": 27
        },
        "mainframeLoginName": {
          "type": "string",
          "title": "Mainframe Login Name",
          "description": "Mainframe login name",
          "order": 28
        },
        "hasAttention": {
          "type": "boolean",
          "title": "Has Attention",
          "description": "Has attention",
          "order": 29
        },
        "attention": {
          "$ref": "#/definitions/fieldObject",
          "title": "Attention",
          "description": "Attention",
          "order": 30
        },
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Comments",
          "order": 31
        },
        "installer": {
          "type": "boolean",
          "title": "Installer",
          "description": "Installer",
          "order": 32
        },
        "firstLaneCallOperator": {
          "type": "boolean",
          "title": "First Lane Call Operator",
          "description": "First lane call operator",
          "order": 33
        },
        "secondLaneCallOperator": {
          "type": "boolean",
          "title": "Second Lane Call Operator",
          "description": "Second lane call operator",
          "order": 34
        },
        "problemManager": {
          "type": "boolean",
          "title": "Problem Manager",
          "description": "Problem manager",
          "order": 35
        },
        "problemOperator": {
          "type": "boolean",
          "title": "Problem Operator",
          "description": "Problem operator",
          "order": 36
        },
        "changeCoordinator": {
          "type": "boolean",
          "title": "Change Coordinator",
          "description": "Change coordinator",
          "order": 37
        },
        "changeActivitiesOperator": {
          "type": "boolean",
          "title": "Change Activities Operator",
          "description": "Change Activities operator",
          "order": 38
        },
        "requestForChangeOperator": {
          "type": "boolean",
          "title": "Request for Change Operator",
          "description": "Request for change operator",
          "order": 39
        },
        "extensiveChangeOperator": {
          "type": "boolean",
          "title": "Extensive Change Operator",
          "description": "Extensive change operator",
          "order": 40
        },
        "scenarioManager": {
          "type": "boolean",
          "title": "Scenario Manager",
          "description": "Scenario manager",
          "order": 41
        },
        "planningActivityManager": {
          "type": "boolean",
          "title": "Planning Activity Manager",
          "description": "Planning activity manager",
          "order": 42
        },
        "projectCoordinator": {
          "type": "boolean",
          "title": "Project Coordinator",
          "description": "Project coordinator",
          "order": 43
        },
        "projectActiviesOperator": {
          "type": "boolean",
          "title": "Project Activities Operator",
          "description": "Project activities operator",
          "order": 44
        },
        "stockManager": {
          "type": "boolean",
          "title": "Stock Manager",
          "description": "Stock manager",
          "order": 45
        },
        "reservationsOperator": {
          "type": "boolean",
          "title": "Reservations Operator",
          "description": "Reservations operator",
          "order": 46
        },
        "serviceOperator": {
          "type": "boolean",
          "title": "Service Operator",
          "description": "Service operator",
          "order": 47
        },
        "externalHelpDeskParty": {
          "type": "boolean",
          "title": "External HelpDesk party",
          "description": "External helpdesk party",
          "order": 48
        },
        "contractManager": {
          "type": "boolean",
          "title": "Contract Manager",
          "description": "Contract manager",
          "order": 49
        },
        "operationsOperator": {
          "type": "boolean",
          "title": "Operations Operator",
          "description": "Operations operator",
          "order": 50
        },
        "operationsManager": {
          "type": "boolean",
          "title": "Operations Manager",
          "description": "Operations manager",
          "order": 51
        },
        "knowledgeBaseManager": {
          "type": "boolean",
          "title": "Knowledge Base Manager",
          "description": "Knowledge base manager",
          "order": 52
        },
        "accountManager": {
          "type": "boolean",
          "title": "Account Manager",
          "description": "Account manager",
          "order": 53
        },
        "creationDate": {
          "type": "string",
          "title": "Creation Date",
          "description": "Creation date",
          "order": 54
        },
        "creator": {
          "$ref": "#/definitions/fieldObject",
          "title": "Creator",
          "description": "Creator",
          "order": 55
        },
        "modificationDate": {
          "type": "string",
          "title": "Modification Date",
          "description": "Modification date",
          "order": 56
        },
        "modifier": {
          "$ref": "#/definitions/fieldObject",
          "title": "Modifier",
          "description": "Modifier",
          "order": 57
        },
        "accessRoles": {
          "type": "array",
          "title": "Access Roles",
          "description": "Access roles",
          "items": {
            "$ref": "#/definitions/accessRole"
          },
          "order": 58
        },
        "optionalField1": {
          "$ref": "#/definitions/optionalField",
          "title": "Optional Field 1",
          "description": "Optional field 1",
          "order": 59
        },
        "optionalField2": {
          "$ref": "#/definitions/optionalField",
          "title": "Optional Field 2",
          "description": "Optional field 2",
          "order": 60
        }
      }
    },
    "accessRole": {
      "type": "object",
      "title": "accessRole",
      "properties": {
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "HREF",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 2
        }
      }
    },
    "optionalField": {
      "type": "object",
      "title": "optionalField",
      "properties": {
        "boolean1": {
          "type": "boolean",
          "title": "Boolean 1",
          "description": "Optional boolean field",
          "order": 1
        },
        "boolean2": {
          "type": "boolean",
          "title": "Boolean 2",
          "description": "Optional boolean field",
          "order": 2
        },
        "boolean3": {
          "type": "boolean",
          "title": "Boolean 3",
          "description": "Optional boolean field",
          "order": 3
        },
        "boolean4": {
          "type": "boolean",
          "title": "Boolean 4",
          "description": "Optional boolean field",
          "order": 4
        },
        "boolean5": {
          "type": "boolean",
          "title": "Boolean 5",
          "description": "Optional boolean field",
          "order": 5
        },
        "number1": {
          "type": "integer",
          "title": "Number 1",
          "description": "Optional number field",
          "order": 6
        },
        "number2": {
          "type": "integer",
          "title": "Number 2",
          "description": "Optional number field",
          "order": 7
        },
        "number3": {
          "type": "integer",
          "title": "Number 3",
          "description": "Optional number field",
          "order": 8
        },
        "number4": {
          "type": "integer",
          "title": "Number 4",
          "description": "Optional number field",
          "order": 9
        },
        "number5": {
          "type": "integer",
          "title": "Number 5",
          "description": "Optional number field",
          "order": 10
        },
        "date1": {
          "type": "string",
          "title": "Date 1",
          "description": "Optional date field",
          "order": 11
        },
        "date2": {
          "type": "string",
          "title": "Date 2",
          "description": "Optional date field",
          "order": 12
        },
        "date3": {
          "type": "string",
          "title": "Date 3",
          "description": "Optional date field",
          "order": 13
        },
        "date4": {
          "type": "string",
          "title": "Date 4",
          "description": "Optional date field",
          "order": 14
        },
        "date5": {
          "type": "string",
          "title": "Date 5",
          "description": "Optional date field",
          "order": 15
        },
        "text1": {
          "type": "string",
          "title": "Text 1",
          "description": "Optional text field",
          "order": 16
        },
        "text2": {
          "type": "string",
          "title": "Text 2",
          "description": "Optional text field",
          "order": 17
        },
        "text3": {
          "type": "string",
          "title": "Text 3",
          "description": "Optional text field",
          "order": 18
        },
        "text4": {
          "type": "string",
          "title": "Text 4",
          "description": "Optional text field",
          "order": 19
        },
        "text5": {
          "type": "string",
          "title": "Text 5",
          "description": "Optional text field",
          "order": 20
        },
        "memo1": {
          "type": "string",
          "title": "Memo 1",
          "description": "Optional memo field",
          "order": 21
        },
        "memo2": {
          "type": "string",
          "title": "Memo 2",
          "description": "Optional memo field",
          "order": 22
        },
        "memo3": {
          "type": "string",
          "title": "Memo 3",
          "description": "Optional memo field",
          "order": 23
        },
        "memo4": {
          "type": "string",
          "title": "Memo 4",
          "description": "Optional memo field",
          "order": 24
        },
        "memo5": {
          "type": "string",
          "title": "Memo 5",
          "description": "Optional memo field",
          "order": 25
        },
        "searchlist1": {
          "type": "string",
          "title": "Search List 1",
          "description": "Optional search list field",
          "order": 26
        },
        "searchlist2": {
          "type": "string",
          "title": "Search List 2",
          "description": "Optional search list field",
          "order": 27
        },
        "searchlist3": {
          "type": "string",
          "title": "Search List 3",
          "description": "Optional search list field",
          "order": 28
        },
        "searchlist4": {
          "type": "string",
          "title": "Search List 4",
          "description": "Optional search list field",
          "order": 29
        },
        "searchlist5": {
          "type": "string",
          "title": "Search List 5",
          "description": "Optional search list field",
          "order": 30
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
