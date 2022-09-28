# Description

Use the ConnectWise Manage help desk software to effectively oversee your service tickets and resolve client issues with ease

# Key Features

* Create, update and delete a service ticket
* Get ticket by ID or get a list of tickets
* Create, update, delete a service ticket note
* Get ticket note by ID or get a list of ticket notes
* Get company

# Requirements

* [Client ID](https://developer.connectwise.com/ClientID)
* [API Keys](https://docs.connectwise.com/ConnectWise_Support_Wiki/System/How_to_Create_API_Keys) - private key and public key
* Company name

# Supported Product Versions

* ConnectWise Manage API v4.6

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|credential_secret_key|None|True|Client ID|None|c163eff0-d1a1-4618-ee2a-453534f43cee21|
|company|string|None|True|Name of the company|None|example_cs1|
|private_key|credential_secret_key|None|True|API private key|None|ExAmPl3PriVat3kEy|
|public_key|string|None|True|API public key|None|ExAmPl3PubLiCkEy3|

Example input:

```
{
  "client_id": "c163eff0-d1a1-4618-ee2a-453534f43cee21",
  "company": "example_cs1",
  "private_key": "ExAmPl3PriVat3kEy",
  "public_key": "ExAmPl3PubLiCkEy3"
}
```

## Technical Details

### Actions

#### Update Ticket Note

This action is used to update the given note for the specified ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|detailDescriptionFlag|boolean|None|False|Discussion flag|None|True|
|internalAnalysisFlag|boolean|None|False|Internal analysis flag|None|False|
|note_id|integer|None|True|ID of the note which will be updated|None|33213|
|resolutionFlag|boolean|None|False|Resolution flag|None|True|
|text|string|None|False|Ticket's note text|None|note text|
|ticket_id|integer|None|True|ID of the ticket for which a new note will be updated|None|112|

Example input:

```
{
  "detailDescriptionFlag": false,
  "internalAnalysisFlag": true,
  "note_id": 33213,
  "resolutionFlag": false,
  "text": "note text",
  "ticket_id": 112
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|ticket_note|ticket_note|False|Information about the updated note for the specified ticket|{}|

Example output:

```
{
  "ticket_note": {
    "id": 33213,
    "ticketId": 112,
    "text": "note text",
    "detailDescriptionFlag": false,
    "internalAnalysisFlag": true,
    "resolutionFlag": false,
    "issueFlag": false,
    "member": {
      "id": 637,
      "identifier": "user",
      "name": "user",
      "_info": {
        "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637",
        "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z"
      }
    },
    "dateCreated": "2022-09-01T08:59:27Z",
    "createdBy": "user",
    "internalFlag": true,
    "externalFlag": true,
    "_info": {
      "lastUpdated": "2022-09-20T07:20:16Z",
      "updatedBy": "user"
    }
  }
}
```

#### Update Ticket

This action is used to update an existing ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-----|
|agreement|details_input|None|False|Name or ID of the agreement|None|{"id": 19}|
|automaticEmailCc|string|None|False|Address to which the email will be sent with information about the added note|None|user@example.com|
|automaticEmailCcFlag|boolean|None|False|Whether to send an email to the specified email address in CC when a note to the ticket is added|None|True|
|automaticEmailContactFlag|boolean|None|False|Whether to send an email to the specified contact when a note to the ticket is added|None|True|
|automaticEmailResourceFlag|boolean|None|False|Whether to send an email to the specified resource when a note to the ticket is added|None|True|
|board|details_input|None|True|Name or ID of the board|None|{"name": "Network Security"}|
|budgetHours|float|None|False|Budget hours for the ticket|None|8.5|
|company_id|integer|None|True|Company Rec ID. This ID can be found in `Share` link on the company page|None|23|
|contact|details_input|None|False|Name or ID of the contact|None|{"id": 144}|
|department|details_input|None|False|Name or ID of the department|None|{"name": "Engineering"}|
|estimatedStartDate|date|None|False|Estimated start date for the ticket|None|2022-09-23T00:00:00+02:00|
|impact|string|None|True|Impact of the ticket|None|Medium|
|location|details_input|None|False|Name or ID of the location|None|{"id": 11}|
|owner|details_input|None|False|Name or ID of the ticket owner|None|{"id": 11}|
|predecessorId|integer|None|False|ID of the ticket predecessor|None|1234|
|predecessortype|string|None|False|Type of the ticket predecessor|None|Ticket|
|priority_id|integer|None|True|ID of the priority|None|7|
|type|details_input|None|False|Name or ID of the type|None|{"name": "Testing"}|
|requiredDate|date|None|False|Due date for the ticket|None|2022-09-26T00:00:00+02:00|
|serviceLocation|details_input|None|False|Name or ID of the service location|None|{"name": "Remote"}|
|severity|string|None|True|Severity of the ticket|None|Medium|
|site|details_input|None|False|Name or ID of the site|None|{"id": 1}|
|source|details_input|None|False|Name or ID of the source|None|{"name": "Call"}|
|status|details_input|None|True|Name or ID of the ticket status|None|{"name": "In Progress"}|
|subtype|details_input|None|False|Name or ID of the subtype|None|{"name": "Active Directory"}|
|summary|string|None|True|Summary of the ticket|None|example summary|
|team|details_input|None|True|Name or ID of the team|None|{"id": 10}|
|ticket_id|integer|None|True|ID of the ticket which will be updated|None|1122|
|type|details_input|None|False|Name or ID of the type|None|{"name": "Testing"}|

Example input:

```
{
  "agreement": {
    "id": 19
  },
  "automaticEmailCc": "user@example.com",
  "automaticEmailCcFlag": true,
  "automaticEmailContactFlag": true,
  "automaticEmailResourceFlag": true,
  "board": {
    "name": "Network Security"
  },
  "budgetHours": 8.5,
  "company_id": 23,
  "contact": {
    "id": 144
  },
  "department": {
    "name": "Engineering"
  },
  "estimatedStartDate": "2022-09-23T00:00:00+02:00",
  "impact": "Medium",
  "location": {
    "id": 11
  },
  "owner": {
    "id": 11
  },
  "predecessorId": 1234,
  "predecessortype": "Ticket",
  "priority_id": 7,
  "requiredDate": "2022-09-26T00:00:00+02:00",
  "serviceLocation": {
    "name": "Remote"
  },
  "severity": "Medium",
  "site": {
    "id": 1
  },
  "source": {
    "name": "Call"
  },
  "status": {
    "name": "In Progress"
  },
  "subtype": {
    "name": "Active Directory"
  },
  "summary": "example summary",
  "team": {
    "id": 10
  },
  "ticket_id": 1122
  "type": {
    "name": "Testing"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|ticket|ticket|False|Information about the ticket with the given ID|{}|

Example output:

```
{
  "ticket": {
    "id": 945370,
    "summary": "update_ticket_few_parameters",
    "recordType": "ServiceTicket",
    "board": {
      "id": 30,
      "name": "Network Security",
      "_info": {
        "board_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30"
      }
    },
    "status": {
      "id": 550,
      "name": "In Progress",
      "_info": {
        "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550"
      }
    },
    "company": {
      "id": 23,
      "identifier": "Example",
      "name": "Example Company",
      "_info": {
        "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298",
        "mobileGuid": "5ec92caf-0922-4120-9268-21580dbbcef8"
      }
    },
    "team": {
      "id": 10,
      "name": "Network Security",
      "_info": {
        "team_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10"
      }
    },
    "priority": {
      "id": 8,
      "name": "Priority 4 - Low",
      "sort": 4,
      "_info": {
        "priority_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8",
        "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z"
      }
    },
    "severity": "Medium",
    "impact": "Medium",
    "allowAllClientsPortalView": false,
    "customerUpdatedFlag": false,
    "automaticEmailContactFlag": true,
    "automaticEmailResourceFlag": true,
    "automaticEmailCcFlag": true,
    "closedFlag": false,
    "approved": true,
    "estimatedExpenseCost": 0.0,
    "estimatedExpenseRevenue": 0.0,
    "estimatedProductCost": 0.0,
    "estimatedProductRevenue": 0.0,
    "estimatedTimeCost": 0.0,
    "estimatedTimeRevenue": 0.0,
    "billingMethod": "ActualRates",
    "subBillingMethod": "ActualRates",
    "dateResplan": "2022-09-07T09:46:59Z",
    "dateResponded": "2022-09-07T09:46:59Z",
    "resolveMinutes": 0,
    "resPlanMinutes": 0,
    "respondMinutes": 0,
    "isInSla": true,
    "resources": "userint",
    "hasChildTicket": false,
    "hasMergedChildTicketFlag": false,
    "billTime": "NoDefault",
    "billExpenses": "NoDefault",
    "billProducts": "NoDefault",
    "location": {
      "id": 11,
      "name": "Example South",
      "_info": {
        "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11"
      }
    },
    "department": {
      "id": 5,
      "identifier": "Engineering",
      "name": "Engineering",
      "_info": {
        "department_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5"
      }
    },
    "mobileGuid": "40ddd5b7-f6f1-4679-9bc9-f80db3fc3daf",
    "sla": {
      "id": 3,
      "name": "Example Standard SLA",
      "_info": {
        "sla_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3"
      }
    },
    "slaStatus": "Resolve by Tue 10/04 11:00 PM UTC-05",
    "currency": {
      "id": 7,
      "symbol": "$",
      "currencyCode": "USD",
      "decimalSeparator": ".",
      "numberOfDecimals": 2,
      "thousandsSeparator": ",",
      "negativeParenthesesFlag": false,
      "displaySymbolFlag": true,
      "currencyIdentifier": "USD",
      "displayIdFlag": false,
      "rightAlign": false,
      "name": "US Dollars",
      "_info": {
        "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
      }
    },
    "_info": {
      "lastUpdated": "2022-09-15T08:30:12Z",
      "updatedBy": "user",
      "dateEntered": "2022-09-07T09:46:58Z",
      "enteredBy": "user",
      "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945370",
      "scheduleentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945370",
      "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945370",
      "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/configurations",
      "tasks_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/tasks",
      "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/notes",
      "products_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945370",
      "timeentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370",
      "expenseEntries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370"
    },
    "escalationStartDateUTC": "2022-09-30T04:00:00Z",
    "escalationLevel": 10,
    "minutesBeforeWaiting": 0,
    "respondedSkippedMinutes": 0,
    "resplanSkippedMinutes": 0,
    "customFields": [
      {
        "id": 7,
        "caption": "Dispatch Billing Required",
        "type": "Text",
        "entryMethod": "List",
        "numberOfDecimals": 0
      },
      {
        "id": 36,
        "caption": "Business App assigned ",
        "type": "Date",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 37,
        "caption": "T&M Billing Required",
        "type": "Checkbox",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      }
    ]
  }
}
```

#### Get Tickets

This action is used to get a list of tickets.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|conditions|string|None|False|Search results based on the provided fields. Supported operators are =, !=, <, <=, >, >=, contains, like, in, not|None|impact='Medium' or summary contains 'https://example.com'|
|page|integer|None|False|Number of the page|None|1|
|pageSize|integer|None|False|Number of results returned per page (Defaults to 25)|None|10|

Example input:

```
{
  "conditions": "impact='Medium' or summary contains 'https://example.com'",
  "page": 1,
  "pageSize": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|tickets|[]ticket|False|Results containing information about tickets|[]|

Example output:

```
{
  "tickets": [
    {
      "id": 3186,
      "summary": "Hello https://example.com",
      "recordType": "ServiceTicket",
      "board": {
        "id": 30,
        "name": "Network Security - South",
        "_info": {
          "board_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30"
        }
      },
      "status": {
        "id": 562,
        "name": ">Closed",
        "_info": {
          "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/562"
        }
      },
      "company": {
        "id": 19298,
        "identifier": "Example",
        "name": "Example Company",
        "_info": {
          "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298",
          "mobileGuid": "5ec92caf-0922-4120-9268-21580dbbcef8"
        }
      },
      "site": {
        "id": 1000,
        "name": "Main",
        "_info": {
          "site_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298/sites/1000",
          "mobileGuid": "9e51ad16-7cc3-41f0-ab02-ef332ff30024"
        }
      },
      "siteName": "Main",
      "addressLine1": "6505 Windcrest Dr",
      "addressLine2": "Suite 200",
      "city": "Plano",
      "stateIdentifier": "TX",
      "zip": "75024",
      "country": {
        "id": 1,
        "name": "United States",
        "_info": {
          "country_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/countries/1"
        }
      },
      "contactPhoneNumber": "9729056500",
      "type": {
        "id": 250,
        "name": "Reports",
        "_info": {
          "type_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/types/250"
        }
      },
      "team": {
        "id": 10,
        "name": "Network Security",
        "_info": {
          "team_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10"
        }
      },
      "owner": {
        "id": 244,
        "identifier": "User",
        "name": "Example User",
        "_info": {
          "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/244",
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/244/image?lm=2019-07-12T19:54:26Z"
        }
      },
      "priority": {
        "id": 12,
        "name": "Priority 5 - Service Request",
        "sort": 5,
        "_info": {
          "priority_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/12",
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/12/image?lm=2020-05-29T13:25:15Z"
        }
      },
      "serviceLocation": {
        "id": 4,
        "name": "Remote",
        "_info": {
          "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/locations/4"
        }
      },
      "source": {
        "id": 3,
        "name": "Internal",
        "_info": {
          "source_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/sources/3"
        }
      },
      "severity": "Low",
      "impact": "Low",
      "allowAllClientsPortalView": false,
      "customerUpdatedFlag": false,
      "automaticEmailContactFlag": false,
      "automaticEmailResourceFlag": false,
      "automaticEmailCcFlag": false,
      "closedDate": "2018-08-10T17:39:20Z",
      "closedBy": "User",
      "closedFlag": true,
      "actualHours": 1.07,
      "approved": true,
      "estimatedExpenseCost": 0.0,
      "estimatedExpenseRevenue": 0.0,
      "estimatedProductCost": 0.0,
      "estimatedProductRevenue": 0.0,
      "estimatedTimeCost": 0.0,
      "estimatedTimeRevenue": 0.0,
      "billingMethod": "ActualRates",
      "subBillingMethod": "ActualRates",
      "dateResolved": "2018-08-10T17:39:12Z",
      "dateResplan": "2018-08-09T15:22:30Z",
      "dateResponded": "2018-08-09T15:22:30Z",
      "resolveMinutes": 306,
      "resPlanMinutes": 0,
      "respondMinutes": 0,
      "isInSla": true,
      "resources": "User",
      "hasChildTicket": false,
      "hasMergedChildTicketFlag": false,
      "billTime": "NoDefault",
      "billExpenses": "NoDefault",
      "billProducts": "NoDefault",
      "location": {
        "id": 11,
        "name": "Example South",
        "_info": {
          "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11"
        }
      },
      "department": {
        "id": 5,
        "identifier": "Engineering",
        "name": "Engineering",
        "_info": {
          "department_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5"
        }
      },
      "mobileGuid": "b7fd8e26-fcad-4ade-ba53-c0772dcd7913",
      "sla": {
        "id": 6,
        "name": "No SLA",
        "_info": {
          "sla_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/6"
        }
      },
      "slaStatus": "Resolved",
      "requestForChangeFlag": false,
      "currency": {
        "id": 7,
        "symbol": "$",
        "currencyCode": "USD",
        "decimalSeparator": ".",
        "numberOfDecimals": 2,
        "thousandsSeparator": ",",
        "negativeParenthesesFlag": false,
        "displaySymbolFlag": true,
        "currencyIdentifier": "USD",
        "displayIdFlag": false,
        "rightAlign": false,
        "name": "US Dollars",
        "_info": {
          "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
        }
      },
      "_info": {
        "lastUpdated": "2018-11-09T21:19:07Z",
        "updatedBy": "User",
        "dateEntered": "2018-08-09T15:22:36Z",
        "enteredBy": "User",
        "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=3186",
        "scheduleentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=3186",
        "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=3186",
        "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/configurations",
        "tasks_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/tasks",
        "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/notes",
        "products_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=3186",
        "timeentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=3186",
        "expenseEntries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=3186"
      },
      "escalationStartDateUTC": "2018-08-10T17:39:19Z",
      "escalationLevel": 15,
      "minutesBeforeWaiting": 0,
      "respondedSkippedMinutes": 0,
      "resplanSkippedMinutes": 0,
      "customFields": [
        {
          "id": 7,
          "caption": "Dispatch Billing Required",
          "type": "Text",
          "entryMethod": "List",
          "numberOfDecimals": 0
        },
        {
          "id": 36,
          "caption": "Business App assigned ",
          "type": "Date",
          "entryMethod": "EntryField",
          "numberOfDecimals": 0
        },
        {
          "id": 37,
          "caption": "T&M Billing Required",
          "type": "Checkbox",
          "entryMethod": "EntryField",
          "numberOfDecimals": 0
        }
      ]
    }
  ]
}
```

#### Get Ticket Notes

This action is used to get a list of notes for the given ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|conditions|string|None|False|Search results based on the provided fields. Supported operators are =, !=, <, <=, >, >=, contains, like, in, not|None|text contains 'test'|
|page|integer|None|False|Number of the page|None|11|
|pageSize|integer|None|False|Number of results returned per page (Defaults to 25)|None|32|
|ticket_id|integer|None|True|ID of the ticket for which notes will be obtained|None|532|

Example input:

```
{
  "conditions": "text contains 'test'",
  "page": 11,
  "pageSize": 32,
  "ticket_id": 532
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|ticket_notes|[]ticket_note|False|List of notes for the given ticket|[]|

Example output:

```
{
  "ticket_notes": [
    {
      "id": 532,
      "ticketId": 945315,
      "text": "test ticket",
      "detailDescriptionFlag": true,
      "internalAnalysisFlag": true,
      "resolutionFlag": true,
      "issueFlag": false,
      "member": {
        "id": 637,
        "identifier": "user",
        "name": "user",
        "_info": {
          "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637",
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z"
        }
      },
      "dateCreated": "2022-09-01T08:46:36Z",
      "createdBy": "user",
      "internalFlag": true,
      "externalFlag": true,
      "_info": {
        "lastUpdated": "2022-09-01T08:46:36Z",
        "updatedBy": "user"
      }
    },
    {
      "id": 532,
      "ticketId": 945315,
      "text": "test text",
      "detailDescriptionFlag": true,
      "internalAnalysisFlag": true,
      "resolutionFlag": true,
      "issueFlag": false,
      "member": {
        "id": 637,
        "identifier": "user",
        "name": "user",
        "_info": {
          "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637",
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z"
        }
      },
      "dateCreated": "2022-09-01T08:46:38Z",
      "createdBy": "user",
      "internalFlag": true,
      "externalFlag": true,
      "_info": {
        "lastUpdated": "2022-09-01T08:46:38Z",
        "updatedBy": "user"
      }
    }
  ]
}
```

#### Get Ticket by ID

This action is used to get ticket information for given ticket ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ticket_id|integer|None|True|ID of the ticket for which information will be obtained|None|254|

Example input:

```
{
  "ticket_id": 254
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|ticket|ticket|False|Information about the ticket with the given ID|{}|

Example output:

```
{
  "ticket": {
    "id": 254,
    "summary": "test",
    "recordType": "ServiceTicket",
    "board": {
      "id": 30,
      "name": "Network Security - South",
      "_info": {
        "board_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30"
      }
    },
    "status": {
      "id": 550,
      "name": "In Progress",
      "_info": {
        "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550"
      }
    },
    "company": {
      "id": 19298,
      "identifier": "Example",
      "name": "Example Company",
      "_info": {
        "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298",
        "mobileGuid": "5ec92caf-0922-4120-9268-21580dbbcef8"
      }
    },
    "siteName": "Main - Catchall",
    "addressLine1": "address line 1",
    "addressLine2": "address line 2",
    "city": "London",
    "zip": "111111",
    "contact": {
      "id": 17754,
      "name": "Test Contact",
      "_info": {
        "mobileGuid": "1cf867f4-6198-40fe-8f28-91a644f08f3f",
        "contact_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/contacts/17754"
      }
    },
    "contactName": "Test Contact",
    "type": {
      "id": 248,
      "name": "Testing",
      "_info": {
        "type_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/types/248"
      }
    },
    "subType": {
      "id": 701,
      "name": "Active Directory",
      "_info": {
        "subType_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/subtypes/701"
      }
    },
    "team": {
      "id": 10,
      "name": "Network Security",
      "_info": {
        "team_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10"
      }
    },
    "owner": {
      "id": 638,
      "identifier": "userint",
      "name": "user integration",
      "_info": {
        "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/638",
        "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/638/image?lm=2022-08-03T19:50:33Z"
      }
    },
    "priority": {
      "id": 8,
      "name": "Priority 4 - Low",
      "sort": 4,
      "_info": {
        "priority_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8",
        "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z"
      }
    },
    "serviceLocation": {
      "id": 4,
      "name": "Remote",
      "_info": {
        "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/locations/4"
      }
    },
    "source": {
      "id": 11,
      "name": "Automate",
      "_info": {
        "source_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/sources/11"
      }
    },
    "requiredDate": "2022-09-30T00:00:00Z",
    "budgetHours": 10.5,
    "agreement": {
      "id": 249,
      "name": "Example Internal",
      "_info": {
        "agreement_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/agreements/249"
      }
    },
    "severity": "Medium",
    "impact": "Low",
    "allowAllClientsPortalView": false,
    "customerUpdatedFlag": false,
    "automaticEmailContactFlag": true,
    "automaticEmailResourceFlag": true,
    "automaticEmailCcFlag": true,
    "automaticEmailCc": "user@example.com;",
    "closedFlag": false,
    "approved": true,
    "estimatedExpenseCost": 0.0,
    "estimatedExpenseRevenue": 0.0,
    "estimatedProductCost": 0.0,
    "estimatedProductRevenue": 0.0,
    "estimatedTimeCost": 0.0,
    "estimatedTimeRevenue": 0.0,
    "billingMethod": "ActualRates",
    "subBillingMethod": "ActualRates",
    "dateResplan": "2022-09-02T08:29:34Z",
    "dateResponded": "2022-09-02T08:29:34Z",
    "resolveMinutes": 0,
    "resPlanMinutes": 0,
    "respondMinutes": 0,
    "isInSla": true,
    "resources": "userint",
    "hasChildTicket": false,
    "hasMergedChildTicketFlag": false,
    "billTime": "NoDefault",
    "billExpenses": "NoDefault",
    "billProducts": "NoDefault",
    "estimatedStartDate": "2022-09-01T00:00:00Z",
    "duration": 22,
    "location": {
      "id": 11,
      "name": "Example South",
      "_info": {
        "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11"
      }
    },
    "department": {
      "id": 5,
      "identifier": "Engineering",
      "name": "Engineering",
      "_info": {
        "department_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5"
      }
    },
    "mobileGuid": "468dca91-3a2f-4988-9a48-26adcbdd0e69",
    "sla": {
      "id": 3,
      "name": "Example Standard SLA",
      "_info": {
        "sla_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3"
      }
    },
    "slaStatus": "Resolve by Tue 10/04 11:00 PM UTC-05",
    "requestForChangeFlag": false,
    "currency": {
      "id": 7,
      "symbol": "$",
      "currencyCode": "USD",
      "decimalSeparator": ".",
      "numberOfDecimals": 2,
      "thousandsSeparator": ",",
      "negativeParenthesesFlag": false,
      "displaySymbolFlag": true,
      "currencyIdentifier": "USD",
      "displayIdFlag": false,
      "rightAlign": false,
      "name": "US Dollars",
      "_info": {
        "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
      }
    },
    "_info": {
      "lastUpdated": "2022-09-02T08:29:34Z",
      "updatedBy": "user",
      "dateEntered": "2022-09-02T08:29:33Z",
      "enteredBy": "user",
      "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945366",
      "scheduleentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945366",
      "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945366",
      "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/configurations",
      "tasks_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/tasks",
      "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/notes",
      "products_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945366",
      "timeentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945366",
      "expenseEntries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945366"
    },
    "escalationStartDateUTC": "2022-09-30T04:00:00Z",
    "escalationLevel": 10,
    "minutesBeforeWaiting": 0,
    "respondedSkippedMinutes": 0,
    "resplanSkippedMinutes": 0,
    "customFields": [
      {
        "id": 7,
        "caption": "Dispatch Billing Required",
        "type": "Text",
        "entryMethod": "List",
        "numberOfDecimals": 0
      },
      {
        "id": 36,
        "caption": "Business App assigned ",
        "type": "Date",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 37,
        "caption": "T&M Billing Required",
        "type": "Checkbox",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      }
    ]
  }
}
```

#### Get Company

This action is used to get information for the given company ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|company_id|integer|None|True|Company Rec ID. This ID can be found in `Share` link on the company page|None|4321|

Example input:

```
{
  "company_id": 4321
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|company|company|True|Information about the company|{}|

Example output:

```
{
  "company": {
    "id": 4321,
    "identifier": "ExampleCommunications",
    "name": "Example Company",
    "status": {
      "id": 1,
      "name": "Active",
      "_info": {
        "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/statuses/1"
      }
    },
    "addressLine1": "6505 Windcrest Dr",
    "addressLine2": "Suite 200",
    "city": "Plano",
    "state": "TX",
    "zip": "75024",
    "country": {
      "id": 1,
      "name": "United States",
      "_info": {
        "country_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/countries/1"
      }
    },
    "website": "www.example.com",
    "territory": {
      "id": 2,
      "name": "Example Company",
      "_info": {
        "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/2"
      }
    },
    "dateAcquired": "2006-06-21T04:00:00Z",
    "sicCode": {
      "id": 1209,
      "name": "5734 - Computer and software stores"
    },
    "annualRevenue": 0.0,
    "timeZoneSetup": {
      "id": 1,
      "name": "GMT-5/Eastern Time: US & Canada",
      "_info": {
        "timeZoneSetup_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/timeZoneSetups/1"
      }
    },
    "leadFlag": false,
    "unsubscribeFlag": false,
    "userDefinedField5": "1",
    "taxCode": {
      "id": 8,
      "name": "Tax-State",
      "_info": {
        "taxCode_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/taxCodes/8"
      }
    },
    "billingTerms": {
      "id": 1,
      "name": "Net 30 days"
    },
    "billToCompany": {
      "id": 250,
      "identifier": "ExampleCommunications",
      "name": "Example Company",
      "_info": {
        "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250"
      }
    },
    "invoiceDeliveryMethod": {
      "id": 1,
      "name": "Mail"
    },
    "deletedFlag": true,
    "dateDeleted": "2018-11-09T21:19:15Z",
    "deletedBy": "User",
    "mobileGuid": "1df91371-6d7a-4778-ab81-f3e7761f5211",
    "currency": {
      "id": 7,
      "symbol": "$",
      "currencyCode": "USD",
      "decimalSeparator": ".",
      "numberOfDecimals": 2,
      "thousandsSeparator": ",",
      "negativeParenthesesFlag": false,
      "displaySymbolFlag": true,
      "currencyIdentifier": "USD",
      "displayIdFlag": false,
      "rightAlign": false,
      "name": "US Dollars",
      "_info": {
        "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
      }
    },
    "isVendorFlag": false,
    "types": [
      {
        "id": 1,
        "name": "Client",
        "_info": {
          "type_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/types/1"
        }
      }
    ],
    "site": {
      "id": 5353,
      "name": "Plano Office",
      "_info": {
        "site_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/sites/5353"
      }
    },
    "_info": {
      "lastUpdated": "2019-06-13T15:27:10Z",
      "updatedBy": "user",
      "dateEntered": "2006-06-21T16:04:59Z",
      "enteredBy": "CONVERSION",
      "contacts_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/contacts?conditions=company/id=250",
      "agreements_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/agreements?conditions=company/id=250",
      "tickets_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets?conditions=company/id=250",
      "opportunities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/opportunities?conditions=company/id=250",
      "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=company/id=250",
      "projects_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//project/projects?conditions=company/id=250",
      "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/configurations?conditions=company/id=250",
      "orders_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/orders?conditions=company/id=250",
      "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Company&recordId=250",
      "sites_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/sites",
      "teams_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/teams",
      "reports_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/managementSummaryReports",
      "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/notes"
    },
    "customFields": [
      {
        "id": 2,
        "caption": "Parent Company",
        "type": "Text",
        "entryMethod": "List",
        "numberOfDecimals": 0
      },
      {
        "id": 13,
        "caption": "Disconnect Date",
        "type": "Date",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 14,
        "caption": "Transition Date",
        "type": "Date",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 15,
        "caption": "Partner ID",
        "type": "Text",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 17,
        "caption": "Customer Activation Date",
        "type": "Date",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 19,
        "caption": "TTMS Monitoring",
        "type": "Checkbox",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 20,
        "caption": "Channel Partner Type",
        "type": "Text",
        "entryMethod": "List",
        "numberOfDecimals": 0
      },
      {
        "id": 24,
        "caption": "Partner Name",
        "type": "Text",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 25,
        "caption": "Key Count",
        "type": "Number",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 26,
        "caption": "Region",
        "type": "Text",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 27,
        "caption": "Brand",
        "type": "Text",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 28,
        "caption": "Owner",
        "type": "Text",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 29,
        "caption": "Company Property Code",
        "type": "Text",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 30,
        "caption": "Brand Property Code",
        "type": "Text",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 31,
        "caption": "Customer Acquired Date",
        "type": "Date",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      }
    ]
  }
}
```

#### Delete Ticket Note

This action is used to delete the given note for the specified ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|note_id|integer|None|True|ID of the note which will be updated|None|44321|
|ticket_id|integer|None|True|ID of the ticket for which a note will be updated|None|65|

Example input:

```
{
  "note_id": 44321,
  "ticket_id": 65
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|True|

Example output:

```
{
  "success": true
}
```

#### Delete Ticket

This action is used to delete the given ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ticket_id|integer|None|True|ID of the ticket which will be deleted|None|112|

Example input:

```
{
  "ticket_id": 112
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|True|

Example output:

```
{
  "success": true
}
```

#### Create Ticket Note

This action is used to create a note for the specified ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|detailDescriptionFlag|boolean|None|False|Discussion flag|None|True|
|internalAnalysisFlag|boolean|None|False|Internal analysis flag|None|True|
|resolutionFlag|boolean|None|False|Resolution flag|None|False|
|text|string|None|True|Ticket's note text|None|note text|
|ticket_id|integer|None|True|ID of the ticket for which a new note will be created|None|332|

Example input:

```
{
  "detailDescriptionFlag": true,
  "internalAnalysisFlag": true,
  "resolutionFlag": false,
  "text": "note text",
  "ticket_id": 332
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|ticket_note|ticket_note|False|Information about the created note for the specified ticket|{}|

Example output:

```
{
  "ticket_note": {
    "id": 1546048,
    "ticketId": 332,
    "text": "note text",
    "detailDescriptionFlag": true,
    "internalAnalysisFlag": true,
    "resolutionFlag": false,
    "issueFlag": false,
    "member": {
      "id": 637,
      "identifier": "user",
      "name": "user",
      "_info": {
        "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637",
        "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z"
      }
    },
    "dateCreated": "2022-09-15T09:41:06Z",
    "createdBy": "user",
    "internalFlag": true,
    "externalFlag": true,
    "_info": {
      "lastUpdated": "2022-09-15T09:41:06Z",
      "updatedBy": "user"
    }
  }
}
```

#### Create Ticket

This action is used to create a new ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agreement|details_input|None|False|Name or ID of the agreement|None|{"id": 19}|
|automaticEmailCc|string|None|False|Address to which the email will be sent with information about the added note|None|user@example.com|
|automaticEmailCcFlag|boolean|None|False|Whether to send an email to the specified email address in CC when a note to the ticket is added|None|True|
|automaticEmailContactFlag|boolean|None|False|Whether to send an email to the specified contact when a note to the ticket is added|None|True|
|automaticEmailResourceFlag|boolean|None|False|Whether to send an email to the specified resource when a note to the ticket is added|None|True|
|board|details_input|None|False|Name or ID of the board|None|{"name": "Network Security"}|
|budgetHours|float|None|False|Budget hours for the ticket|None|8.5|
|company_id|integer|None|True|Company Rec ID. This ID can be found in `Share` link on the company page|None|23|
|contact|details_input|None|False|Name or ID of the contact|None|{"id": 144}|
|department|details_input|None|False|Name or ID of the department|None|{"name": "Engineering"}|
|estimatedStartDate|date|None|False|Estimated start date for the ticket|None|2022-09-23T00:00:00+02:00|
|impact|string|None|False|Impact of the ticket|None|Medium|
|initialDescription|string|None|False|Initial description|None|example description|
|location|details_input|None|False|Name or ID of the location|None|{"id": 11}|
|owner|details_input|None|False|Name or ID of the ticket owner|None|{"id": 11}|
|predecessorId|integer|None|False|ID of the ticket predecessor|None|1234|
|predecessortype|string|None|False|Type of the ticket predecessor|None|Ticket|
|priority|details_input|None|False|Name or ID of the priority|None|{"id": 7}|
|requiredDate|date|None|False|Due date for the ticket|None|2022-09-26T00:00:00+02:00|
|serviceLocation|details_input|None|False|Name or ID of the service location|None|{"name": "Remote"}|
|severity|string|None|False|Severity of the ticket|None|Medium|
|site|details_input|None|False|Name or ID of the site|None|{"id": 1}|
|source|details_input|None|False|Name or ID of the source|None|{"name": "Call"}|
|status|details_input|None|True|Name or ID of the ticket status|None|{"name": "In Progress"}|
|subtype|details_input|None|False|Name or ID of the subtype|None|{"name": "Active Directory"}|
|summary|string|None|True|Summary of the ticket|None|example summary|
|team|details_input|None|False|Name or ID of the team|None|{"id": 10}|
|type|details_input|None|False|Name or ID of the type|None|{"name": "Testing"}|

Example input:

```
{
  "agreement": {
    "id": 19
  },
  "automaticEmailCc": "user@example.com",
  "automaticEmailCcFlag": true,
  "automaticEmailContactFlag": true,
  "automaticEmailResourceFlag": true,
  "board": {
    "name": "Network Security"
  },
  "budgetHours": 8.5,
  "company_id": 23,
  "contact": {
    "id": 144
  },
  "department": {
    "name": "Engineering"
  },
  "estimatedStartDate": "2022-09-23T00:00:00+02:00",
  "impact": "Medium",
  "initialDescription": "example description",
  "location": {
    "id": 11
  },
  "owner": {
    "id": 11
  },
  "predecessorId": 1234,
  "predecessortype": "Ticket",
  "priority": {
    "id": 7
  },
  "requiredDate": "2022-09-26T00:00:00+02:00",
  "serviceLocation": {
    "name": "Remote"
  },
  "severity": "Medium",
  "site": {
    "id": 1
  },
  "source": {
    "name": "Call"
  },
  "status": {
    "name": "In Progress"
  },
  "subtype": {
    "name": "Active Directory"
  },
  "summary": "example summary",
  "team": {
    "id": 10
  },
  "type": {
    "name": "Testing"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|ticket|ticket|False|Information about the ticket with the given ID|{}|

Example output:

```
{
  "ticket": {
    "id": 945370,
    "summary": "update_ticket_few_parameters",
    "recordType": "ServiceTicket",
    "board": {
      "id": 30,
      "name": "Network Security",
      "_info": {
        "board_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30"
      }
    },
    "status": {
      "id": 550,
      "name": "In Progress",
      "_info": {
        "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550"
      }
    },
    "company": {
      "id": 23,
      "identifier": "Example",
      "name": "Example Company",
      "_info": {
        "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298",
        "mobileGuid": "5ec92caf-0922-4120-9268-21580dbbcef8"
      }
    },
    "team": {
      "id": 10,
      "name": "Network Security",
      "_info": {
        "team_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10"
      }
    },
    "priority": {
      "id": 8,
      "name": "Priority 4 - Low",
      "sort": 4,
      "_info": {
        "priority_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8",
        "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z"
      }
    },
    "severity": "Medium",
    "impact": "Medium",
    "allowAllClientsPortalView": false,
    "customerUpdatedFlag": false,
    "automaticEmailContactFlag": true,
    "automaticEmailResourceFlag": true,
    "automaticEmailCcFlag": true,
    "closedFlag": false,
    "approved": true,
    "estimatedExpenseCost": 0.0,
    "estimatedExpenseRevenue": 0.0,
    "estimatedProductCost": 0.0,
    "estimatedProductRevenue": 0.0,
    "estimatedTimeCost": 0.0,
    "estimatedTimeRevenue": 0.0,
    "billingMethod": "ActualRates",
    "subBillingMethod": "ActualRates",
    "dateResplan": "2022-09-07T09:46:59Z",
    "dateResponded": "2022-09-07T09:46:59Z",
    "resolveMinutes": 0,
    "resPlanMinutes": 0,
    "respondMinutes": 0,
    "isInSla": true,
    "resources": "userint",
    "hasChildTicket": false,
    "hasMergedChildTicketFlag": false,
    "billTime": "NoDefault",
    "billExpenses": "NoDefault",
    "billProducts": "NoDefault",
    "location": {
      "id": 11,
      "name": "Example South",
      "_info": {
        "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11"
      }
    },
    "department": {
      "id": 5,
      "identifier": "Engineering",
      "name": "Engineering",
      "_info": {
        "department_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5"
      }
    },
    "mobileGuid": "40ddd5b7-f6f1-4679-9bc9-f80db3fc3daf",
    "sla": {
      "id": 3,
      "name": "Example Standard SLA",
      "_info": {
        "sla_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3"
      }
    },
    "slaStatus": "Resolve by Tue 10/04 11:00 PM UTC-05",
    "currency": {
      "id": 7,
      "symbol": "$",
      "currencyCode": "USD",
      "decimalSeparator": ".",
      "numberOfDecimals": 2,
      "thousandsSeparator": ",",
      "negativeParenthesesFlag": false,
      "displaySymbolFlag": true,
      "currencyIdentifier": "USD",
      "displayIdFlag": false,
      "rightAlign": false,
      "name": "US Dollars",
      "_info": {
        "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
      }
    },
    "_info": {
      "lastUpdated": "2022-09-15T08:30:12Z",
      "updatedBy": "user",
      "dateEntered": "2022-09-07T09:46:58Z",
      "enteredBy": "user",
      "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945370",
      "scheduleentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945370",
      "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945370",
      "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/configurations",
      "tasks_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/tasks",
      "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/notes",
      "products_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945370",
      "timeentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370",
      "expenseEntries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370"
    },
    "escalationStartDateUTC": "2022-09-30T04:00:00Z",
    "escalationLevel": 10,
    "minutesBeforeWaiting": 0,
    "respondedSkippedMinutes": 0,
    "resplanSkippedMinutes": 0,
    "customFields": [
      {
        "id": 7,
        "caption": "Dispatch Billing Required",
        "type": "Text",
        "entryMethod": "List",
        "numberOfDecimals": 0
      },
      {
        "id": 36,
        "caption": "Business App assigned ",
        "type": "Date",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      },
      {
        "id": 37,
        "caption": "T&M Billing Required",
        "type": "Checkbox",
        "entryMethod": "EntryField",
        "numberOfDecimals": 0
      }
    ]
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### agreement_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Info|object|False|Additional information|
|ID|integer|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### company

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Info|object|False|Info|
|Account Number|string|False|Account number|
|Address Line|string|False|First line of the address|
|Second Address Line|string|False|Second line of the address|
|Annual Revenue|float|False|Annual revenue|
|Bill to Company|more_details|False|Bill to company|
|Billing Contact|details|False|Billing contact|
|Billing Site|details|False|Billing site|
|Billing Terms|details|False|Billing terms|
|Calendar|details|False|Calendar|
|City|string|False|City|
|Company Entity Type|details|False|Company entity type|
|Country|more_details|False|Country|
|Currency|currency_details|False|Currency|
|Custom Fields|[]object|False|Custom fields|
|Date Acquired|string|False|Date acquired|
|Date Deleted|string|False|Date deleted|
|Default Contact|details|False|Default contact|
|Deleted By|string|False|Deleted by|
|Deleted Flag|boolean|False|Deleted flag|
|Facebook URL|string|False|Facebook URL|
|Fax Number|string|False|Fax number|
|ID|integer|False|ID|
|Identifier|string|False|Identifier|
|Integrator Tags|[]string|False|Integrator tags|
|Invoice CC Email Address|string|False|Invoice CC email address|
|Invoice Delivery Method|details|False|Invoice delivery method|
|Invoice Template|details|False|Invoice template|
|Invoice to Email Address|string|False|Invoice to email address|
|Is Vendor Flag|boolean|False|Is vendor flag|
|Lead Flag|boolean|False|Lead flag|
|Lead Source|string|False|Lead source|
|LinkedIn URL|string|False|LinkedIn URL|
|Market|details|False|Market|
|Mobile GUID|string|False|Mobile GUID|
|Name|string|False|Name|
|Number of Employees|integer|False|Number of employees|
|Ownership Type|details|False|Ownership type|
|Parent Company|more_details|False|Parent company|
|Phone Number|string|False|Phone number|
|Pricing Schedule|details|False|Pricing schedule|
|Reseller Identifier|string|False|Reseller identifier|
|Revenue Year|integer|False|Revenue year|
|Sic Code|details|False|Sic code|
|Site|details|False|Site|
|State|string|False|State|
|Status|details|False|Status|
|Tax Code|details|False|Tax code|
|Tax Identifier|string|False|Tax identifier|
|Territory|details|False|Territory|
|Territory Manager|more_details|False|Territory manager|
|Timezone Setup|details|False|Timezone setup|
|Twitter URL|string|False|Twitter URL|
|Types|[]details|False|Types|
|Unsubscribe Flag|boolean|False|Unsubscribe flag|
|Vendor Identifier|string|False|Vendor identifier|
|Website|string|False|Website|
|Year Established|integer|False|Year established|
|Zip|string|False|Zip code|

#### currency_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Info|object|False|Additional information|
|Currency Code|string|False|Currency code|
|Currency Identifier|string|False|Currency identifier|
|Display ID Flag|boolean|False|Display ID flag|
|Display Symbol Flag|boolean|False|Display symbol flag|
|ID|integer|False|ID|
|Name|string|False|Name|
|Negative Parentheses Flag|boolean|False|Negative parentheses flag|
|Number Of Decimals|integer|False|Number of decimals|
|Right Align|boolean|False|Right align|
|Symbol|string|False|Symbol|
|Thousands Separator|string|False|Thousands Separator|

#### details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Info|object|False|Additional information|
|ID|integer|False|ID|
|Name|string|False|Name|

#### details_input

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|ID|
|Name|string|False|Name|

#### merged_parent_ticket_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Info|object|False|Additional information|
|ID|integer|False|ID|
|Summary|string|False|Summary|

#### more_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Info|object|False|Additional information|
|ID|integer|False|ID|
|Identifier|string|False|Identifier|
|Name|string|False|Name|

#### ticket

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Info|object|False|Info|
|Actual Hours|float|False|Actual hours|
|Address Line|string|False|First line of the address|
|Second Address Line|string|False|Second line of the address|
|Agreement|agreement_details|False|Agreement|
|Allow All Client Portal View|boolean|False|Allow all client portal view|
|Approved|boolean|False|Approved|
|Automatic Email CC|string|False|Automatic email CC|
|Automatic Email CC Flag|boolean|False|Automatic email CC flag|
|Automatic Email Contact Flag|boolean|False|Automatic email contact flag|
|Automatic Email Resource Flag|boolean|False|Automatic email resource flag|
|Bill Expenses|string|False|Bill expenses|
|Bill Products|string|False|Bill products|
|Bill Time|string|False|Bill time|
|Billing Amount|float|False|Billing amount|
|Billing Method|string|False|Billing method|
|Board|details|False|Board|
|Budget Hours|float|False|Budget hours|
|City|string|False|City|
|Closed By|string|False|Closed by|
|Closed Date|string|False|Closed date|
|Closed Flag|boolean|False|Closed flag|
|Company|more_details|False|Company|
|Contact|details|False|Contact|
|Contact Email Address|string|False|Contact email address|
|Contact Email Lookup|string|False|Contact Email Lookup|
|Contact Name|string|False|Contact name|
|Contact Phone Extension|string|False|Contact phone extension|
|Contact Phone Number|string|False|Contact phone number|
|Country|more_details|False|Country|
|Currency|currency_details|False|Currency|
|Custom Fields|[]object|False|Custom fields|
|Customer Update Flag|boolean|False|Customer update flag|
|Date Resolved|string|False|Date resolved|
|Date Resplan|string|False|Date resplan|
|Date Responded|string|False|Date responded|
|Department|more_details|False|Department|
|Duration|integer|False|Duration|
|Estimated Expense Cost|float|False|Estimated expense cost|
|Estimated Expense Revenue|float|False|Estimated expense revenue|
|Estimated Product Cost|float|False|Estimated product cost|
|Estimated Product Revenue|float|False|Estimated product revenue|
|Estimated Start Date|string|False|Estimated start date|
|Estimated Time Cost|float|False|Estimated time cost|
|Estimated Time Revenue|float|False|Estimated time revenue|
|External Reference|string|False|External reference|
|Has Child Ticket|boolean|False|Has child ticket|
|Has Merged Child Ticket Flag|boolean|False|Has merged child ticket flag|
|Hourly Rate|float|False|Hourly rate|
|ID|integer|False|Ticket ID|
|Impact|string|False|Impact|
|Initial Description|string|False|Initial description|
|Initial Description From|string|False|Initial description from|
|Initial Internal Analysis|string|False|Initial internal analysis|
|Initial Resolution|string|False|Initial resolution|
|Integrator Tags|[]string|False|Integrator tags|
|Is In SLA|boolean|False|Is in SLA|
|Item|details|False|Item|
|Knowledge Base Category ID|integer|False|Knowledge base category ID|
|Knowledge Base Link ID|integer|False|Knowledge base link ID|
|Knowledge Base Link Type|string|False|Knowledge base link type|
|Knowledge Base Subcategory ID|integer|False|Knowledge base subcategory ID|
|Lag Days|integer|False|Lag days|
|Lag Non Working Days Flag|boolean|False|Lag non working days flag|
|Location|details|False|Location|
|Merged Parent Ticket|merged_parent_ticket_details|False|Merget parent ticket|
|Mobile GUID|string|False|Mobile GUID|
|Opportunity|details|False|Opportunity|
|Owner|more_details|False|Owner|
|Parent Ticket ID|integer|False|Parent ticket ID|
|Predecessor Closed Flag|boolean|False|Predecessor closed flag|
|Predecessor ID|integer|False|Predecessor ID|
|Predecessor Type|string|False|Predecessor type|
|Priority|details|False|Priority|
|Process Notifications|boolean|False|Process notifications|
|Record Type|string|False|Type of the record|
|Required Date|string|False|Required date|
|Resolve Plan Minutes|integer|False|Resolve plan minutes|
|Resolve Minutes|integer|False|Resolve minutes|
|Resources|string|False|Resources|
|Respond Minutes|integer|False|Respond minutes|
|Service Location|details|False|Service location|
|Severity|string|False|Severity|
|Site|details|False|Site|
|Site Name|string|False|Site name|
|Skip Callback|boolean|False|Skip callback|
|SLA|details|False|SLA|
|SLA Status|string|False|SLA status|
|Source|details|False|Source|
|State Identifier|string|False|State identifier|
|Status|agreement_details|False|Status|
|Sub Billing Amount|float|False|Sub billing amount|
|Sub Billing Method|string|False|Sub billing method|
|Sub Date Accepted|string|False|Sub date accepted|
|Subtype|details|False|Subtype|
|Summary|string|False|Ticket summary|
|Team|details|False|Team|
|Type|details|False|Type|
|Work Role|details|False|Work role|
|Work Type|details|False|Work type|
|Zip|string|False|Zip code|

#### ticket_note

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Info|object|False|Info|
|Contact|details|False|Contact|
|Created By|string|False|Created by|
|Customer Updated Flag|boolean|False|Customer updated flag|
|Date Created|string|False|Date created|
|Detail Description Flag|boolean|False|Detail description flag|
|External Flag|boolean|False|External flag|
|ID|integer|False|ID|
|Internal Analysis Flag|boolean|False|Internal analysis flag|
|Internal Flag|boolean|False|Internal flag|
|Issue Flag|boolean|False|Issue flag|
|Member|more_details|False|Member|
|Process Notifications|boolean|False|Process notifications|
|Resolution Flag|boolean|False|Resolution flag|
|Text|string|False|Text|
|Ticket ID|integer|False|Ticket ID|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin - Create actions: `Create Ticket`, `Create Ticket Note`, `Delete Ticket`, `Delete Ticket Note`, `Get Company`, `Get Ticket by ID`, `Get Ticket Notes`, `Get Tickets`, `Update Ticket`, `Update Ticket Note`

# Links

* [ConnectWise](https://www.connectwise.com/)

## References

* [ConnectWise](https://www.connectwise.com/)

