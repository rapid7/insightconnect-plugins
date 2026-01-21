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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|credential_secret_key|None|True|Client ID|None|c163eff0-d1a1-4618-ee2a-453534f43cee21|None|None|
|company|string|None|True|Name of the company|None|example_cs1|None|None|
|private_key|credential_secret_key|None|True|API private key|None|ExAmPl3PriVat3kEy|None|None|
|public_key|string|None|True|API public key|None|ExAmPl3PubLiCkEy3|None|None|
|region|string|na|False|The region of your ConnectWise Manage instance|["na", "eu", "au"]|na|None|None|

Example input:

```
{
  "client_id": "c163eff0-d1a1-4618-ee2a-453534f43cee21",
  "company": "example_cs1",
  "private_key": "ExAmPl3PriVat3kEy",
  "public_key": "ExAmPl3PubLiCkEy3",
  "region": "na"
}
```

## Technical Details

### Actions


#### Create Ticket

This action is used to create a new ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agreement|details_input|None|False|Name or ID of the agreement|None|{"id": 19}|None|None|
|automaticEmailCc|string|None|False|Address to which the email will be sent with information about the added note|None|user@example.com|None|None|
|automaticEmailCcFlag|boolean|None|False|Whether to send an email to the specified email address in CC when a note to the ticket is added|None|True|None|None|
|automaticEmailContactFlag|boolean|None|False|Whether to send an email to the specified contact when a note to the ticket is added|None|True|None|None|
|automaticEmailResourceFlag|boolean|None|False|Whether to send an email to the specified resource when a note to the ticket is added|None|True|None|None|
|board|details_input|None|False|Name or ID of the board|None|{"name": "Network Security"}|None|None|
|budgetHours|float|None|False|Budget hours for the ticket|None|8.5|None|None|
|company_id|integer|None|True|Company Rec ID. This ID can be found in `Share` link on the company page|None|23|None|None|
|contact|details_input|None|False|Name or ID of the contact|None|{"id": 144}|None|None|
|department|details_input|None|False|Name or ID of the department|None|{"name": "Engineering"}|None|None|
|estimatedStartDate|date|None|False|Estimated start date for the ticket|None|2022-09-23T00:00:00+02:00|None|None|
|impact|string|None|False|Impact of the ticket|None|Medium|None|None|
|initialDescription|string|None|False|Initial description|None|example description|None|None|
|location|details_input|None|False|Name or ID of the location|None|{"id": 11}|None|None|
|owner|details_input|None|False|Name or ID of the ticket owner|None|{"id": 11}|None|None|
|predecessorId|integer|None|False|ID of the ticket predecessor|None|1234|None|None|
|predecessortype|string|None|False|Type of the ticket predecessor|None|Ticket|None|None|
|priority|details_input|None|False|Name or ID of the priority|None|{"id": 7}|None|None|
|requiredDate|date|None|False|Due date for the ticket|None|2022-09-26T00:00:00+02:00|None|None|
|serviceLocation|details_input|None|False|Name or ID of the service location|None|{"name": "Remote"}|None|None|
|severity|string|None|False|Severity of the ticket|None|Medium|None|None|
|site|details_input|None|False|Name or ID of the site|None|{"id": 1}|None|None|
|source|details_input|None|False|Name or ID of the source|None|{"name": "Call"}|None|None|
|status|details_input|None|True|Name or ID of the ticket status|None|{"name": "In Progress"}|None|None|
|subtype|details_input|None|False|Name or ID of the subtype|None|{"name": "Active Directory"}|None|None|
|summary|string|None|True|Summary of the ticket|None|example summary|None|None|
|team|details_input|None|False|Name or ID of the team|None|{"id": 10}|None|None|
|type|details_input|None|False|Name or ID of the type|None|{"name": "Testing"}|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|False|Information about the ticket with the given ID|{'ticket': {'id': 945370, 'summary': 'update_ticket_few_parameters', 'recordType': 'ServiceTicket', 'board': {'id': 30, 'name': 'Network Security', 'info': {'board_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30'}}, 'status': {'id': 550, 'name': 'In Progress', 'info': {'status_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550'}}, 'company': {'id': 23, 'identifier': 'Example', 'name': 'Example Company', 'info': {'company_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298', 'mobileGuid': '5ec92caf-0922-4120-9268-21580dbbcef8'}}, 'team': {'id': 10, 'name': 'Network Security', 'info': {'team_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10'}}, 'priority': {'id': 8, 'name': 'Priority 4 - Low', 'sort': 4, 'info': {'priority_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z'}}, 'severity': 'Medium', 'impact': 'Medium', 'allowAllClientsPortalView': False, 'customerUpdatedFlag': False, 'automaticEmailContactFlag': True, 'automaticEmailResourceFlag': True, 'automaticEmailCcFlag': True, 'closedFlag': False, 'approved': True, 'estimatedExpenseCost': 0.0, 'estimatedExpenseRevenue': 0.0, 'estimatedProductCost': 0.0, 'estimatedProductRevenue': 0.0, 'estimatedTimeCost': 0.0, 'estimatedTimeRevenue': 0.0, 'billingMethod': 'ActualRates', 'subBillingMethod': 'ActualRates', 'dateResplan': '2022-09-07T09:46:59Z', 'dateResponded': '2022-09-07T09:46:59Z', 'resolveMinutes': 0, 'resPlanMinutes': 0, 'respondMinutes': 0, 'isInSla': True, 'resources': 'userint', 'hasChildTicket': False, 'hasMergedChildTicketFlag': False, 'billTime': 'NoDefault', 'billExpenses': 'NoDefault', 'billProducts': 'NoDefault', 'location': {'id': 11, 'name': 'Example South', 'info': {'location_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11'}}, 'department': {'id': 5, 'identifier': 'Engineering', 'name': 'Engineering', 'info': {'department_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5'}}, 'mobileGuid': '40ddd5b7-f6f1-4679-9bc9-f80db3fc3daf', 'sla': {'id': 3, 'name': 'Example Standard SLA', 'info': {'sla_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3'}}, 'slaStatus': 'Resolve by Tue 10/04 11:00 PM UTC-05', 'currency': {'id': 7, 'symbol': '$', 'currencyCode': 'USD', 'decimalSeparator': '.', 'numberOfDecimals': 2, 'thousandsSeparator': ',', 'negativeParenthesesFlag': False, 'displaySymbolFlag': True, 'currencyIdentifier': 'USD', 'displayIdFlag': False, 'rightAlign': False, 'name': 'US Dollars', 'info': {'currency_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7'}}, 'info': {'lastUpdated': '2022-09-15T08:30:12Z', 'updatedBy': 'user', 'dateEntered': '2022-09-07T09:46:58Z', 'enteredBy': 'user', 'activities_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945370', 'scheduleentries_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945370', 'documents_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945370', 'configurations_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/configurations', 'tasks_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/tasks', 'notes_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/notes', 'products_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945370", 'timeentries_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370", 'expenseEntries_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370"}, 'escalationStartDateUTC': '2022-09-30T04:00:00Z', 'escalationLevel': 10, 'minutesBeforeWaiting': 0, 'respondedSkippedMinutes': 0, 'resplanSkippedMinutes': 0, 'customFields': [{'id': 7, 'caption': 'Dispatch Billing Required', 'type': 'Text', 'entryMethod': 'List', 'numberOfDecimals': 0}, {'id': 36, 'caption': 'Business App assigned ', 'type': 'Date', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 37, 'caption': 'T&M Billing Required', 'type': 'Checkbox', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}]}}|
  
Example output:

```
{
  "ticket": {
    "ticket": {
      "allowAllClientsPortalView": false,
      "approved": true,
      "automaticEmailCcFlag": true,
      "automaticEmailContactFlag": true,
      "automaticEmailResourceFlag": true,
      "billExpenses": "NoDefault",
      "billProducts": "NoDefault",
      "billTime": "NoDefault",
      "billingMethod": "ActualRates",
      "board": {
        "id": 30,
        "info": {
          "board_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30"
        },
        "name": "Network Security"
      },
      "closedFlag": false,
      "company": {
        "id": 23,
        "identifier": "Example",
        "info": {
          "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298",
          "mobileGuid": "5ec92caf-0922-4120-9268-21580dbbcef8"
        },
        "name": "Example Company"
      },
      "currency": {
        "currencyCode": "USD",
        "currencyIdentifier": "USD",
        "decimalSeparator": ".",
        "displayIdFlag": false,
        "displaySymbolFlag": true,
        "id": 7,
        "info": {
          "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
        },
        "name": "US Dollars",
        "negativeParenthesesFlag": false,
        "numberOfDecimals": 2,
        "rightAlign": false,
        "symbol": "$",
        "thousandsSeparator": ","
      },
      "customFields": [
        {
          "caption": "Dispatch Billing Required",
          "entryMethod": "List",
          "id": 7,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Business App assigned ",
          "entryMethod": "EntryField",
          "id": 36,
          "numberOfDecimals": 0,
          "type": "Date"
        },
        {
          "caption": "T&M Billing Required",
          "entryMethod": "EntryField",
          "id": 37,
          "numberOfDecimals": 0,
          "type": "Checkbox"
        }
      ],
      "customerUpdatedFlag": false,
      "dateResplan": "2022-09-07T09:46:59Z",
      "dateResponded": "2022-09-07T09:46:59Z",
      "department": {
        "id": 5,
        "identifier": "Engineering",
        "info": {
          "department_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5"
        },
        "name": "Engineering"
      },
      "escalationLevel": 10,
      "escalationStartDateUTC": "2022-09-30T04:00:00Z",
      "estimatedExpenseCost": 0.0,
      "estimatedExpenseRevenue": 0.0,
      "estimatedProductCost": 0.0,
      "estimatedProductRevenue": 0.0,
      "estimatedTimeCost": 0.0,
      "estimatedTimeRevenue": 0.0,
      "hasChildTicket": false,
      "hasMergedChildTicketFlag": false,
      "id": 945370,
      "impact": "Medium",
      "info": {
        "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945370",
        "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/configurations",
        "dateEntered": "2022-09-07T09:46:58Z",
        "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945370",
        "enteredBy": "user",
        "expenseEntries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370",
        "lastUpdated": "2022-09-15T08:30:12Z",
        "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/notes",
        "products_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945370",
        "scheduleentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945370",
        "tasks_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/tasks",
        "timeentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370",
        "updatedBy": "user"
      },
      "isInSla": true,
      "location": {
        "id": 11,
        "info": {
          "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11"
        },
        "name": "Example South"
      },
      "minutesBeforeWaiting": 0,
      "mobileGuid": "40ddd5b7-f6f1-4679-9bc9-f80db3fc3daf",
      "priority": {
        "id": 8,
        "info": {
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z",
          "priority_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8"
        },
        "name": "Priority 4 - Low",
        "sort": 4
      },
      "recordType": "ServiceTicket",
      "resPlanMinutes": 0,
      "resolveMinutes": 0,
      "resources": "userint",
      "resplanSkippedMinutes": 0,
      "respondMinutes": 0,
      "respondedSkippedMinutes": 0,
      "severity": "Medium",
      "sla": {
        "id": 3,
        "info": {
          "sla_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3"
        },
        "name": "Example Standard SLA"
      },
      "slaStatus": "Resolve by Tue 10/04 11:00 PM UTC-05",
      "status": {
        "id": 550,
        "info": {
          "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550"
        },
        "name": "In Progress"
      },
      "subBillingMethod": "ActualRates",
      "summary": "update_ticket_few_parameters",
      "team": {
        "id": 10,
        "info": {
          "team_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10"
        },
        "name": "Network Security"
      }
    }
  }
}
```

#### Create Ticket Note

This action is used to create a note for the specified ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|detailDescriptionFlag|boolean|None|False|Discussion flag|None|True|None|None|
|internalAnalysisFlag|boolean|None|False|Internal analysis flag|None|True|None|None|
|resolutionFlag|boolean|None|False|Resolution flag|None|False|None|None|
|text|string|None|True|Ticket's note text|None|note text|None|None|
|ticket_id|integer|None|True|ID of the ticket for which a new note will be created|None|332|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|ticket_note|ticket_note|False|Information about the created note for the specified ticket|{'ticket_note': {'id': 1546048, 'ticketId': 332, 'text': 'note text', 'detailDescriptionFlag': True, 'internalAnalysisFlag': True, 'resolutionFlag': False, 'issueFlag': False, 'member': {'id': 637, 'identifier': 'user', 'name': 'user', 'info': {'member_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z'}}, 'dateCreated': '2022-09-15T09:41:06Z', 'createdBy': 'user', 'internalFlag': True, 'externalFlag': True, 'info': {'lastUpdated': '2022-09-15T09:41:06Z', 'updatedBy': 'user'}}}|
  
Example output:

```
{
  "ticket_note": {
    "ticket_note": {
      "createdBy": "user",
      "dateCreated": "2022-09-15T09:41:06Z",
      "detailDescriptionFlag": true,
      "externalFlag": true,
      "id": 1546048,
      "info": {
        "lastUpdated": "2022-09-15T09:41:06Z",
        "updatedBy": "user"
      },
      "internalAnalysisFlag": true,
      "internalFlag": true,
      "issueFlag": false,
      "member": {
        "id": 637,
        "identifier": "user",
        "info": {
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z",
          "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637"
        },
        "name": "user"
      },
      "resolutionFlag": false,
      "text": "note text",
      "ticketId": 332
    }
  }
}
```

#### Delete Ticket

This action is used to delete the given ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ticket_id|integer|None|True|ID of the ticket which will be deleted|None|112|None|None|
  
Example input:

```
{
  "ticket_id": 112
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Ticket Note

This action is used to delete the given note for the specified ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|note_id|integer|None|True|ID of the note which will be updated|None|44321|None|None|
|ticket_id|integer|None|True|ID of the ticket for which a note will be updated|None|65|None|None|
  
Example input:

```
{
  "note_id": 44321,
  "ticket_id": 65
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Company

This action is used to get information for the given company ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|company_id|integer|None|True|Company Rec ID. This ID can be found in `Share` link on the company page|None|4321|None|None|
  
Example input:

```
{
  "company_id": 4321
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|company|company|True|Information about the company|{'company': {'id': 4321, 'identifier': 'ExampleCommunications', 'name': 'Example Company', 'status': {'id': 1, 'name': 'Active', 'info': {'status_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/statuses/1'}}, 'addressLine1': '6505 Windcrest Dr', 'addressLine2': 'Suite 200', 'city': 'Plano', 'state': 'TX', 'zip': '75024', 'country': {'id': 1, 'name': 'United States', 'info': {'country_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/countries/1'}}, 'website': 'www.example.com', 'territory': {'id': 2, 'name': 'Example Company', 'info': {'location_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/2'}}, 'dateAcquired': '2006-06-21T04:00:00Z', 'sicCode': {'id': 1209, 'name': '5734 - Computer and software stores'}, 'annualRevenue': 0.0, 'timeZoneSetup': {'id': 1, 'name': 'GMT-5/Eastern Time: US & Canada', 'info': {'timeZoneSetup_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/timeZoneSetups/1'}}, 'leadFlag': False, 'unsubscribeFlag': False, 'userDefinedField5': '1', 'taxCode': {'id': 8, 'name': 'Tax-State', 'info': {'taxCode_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/taxCodes/8'}}, 'billingTerms': {'id': 1, 'name': 'Net 30 days'}, 'billToCompany': {'id': 250, 'identifier': 'ExampleCommunications', 'name': 'Example Company', 'info': {'company_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250'}}, 'invoiceDeliveryMethod': {'id': 1, 'name': 'Mail'}, 'deletedFlag': True, 'dateDeleted': '2018-11-09T21:19:15Z', 'deletedBy': 'User', 'mobileGuid': '1df91371-6d7a-4778-ab81-f3e7761f5211', 'currency': {'id': 7, 'symbol': '$', 'currencyCode': 'USD', 'decimalSeparator': '.', 'numberOfDecimals': 2, 'thousandsSeparator': ',', 'negativeParenthesesFlag': False, 'displaySymbolFlag': True, 'currencyIdentifier': 'USD', 'displayIdFlag': False, 'rightAlign': False, 'name': 'US Dollars', 'info': {'currency_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7'}}, 'isVendorFlag': False, 'types': [{'id': 1, 'name': 'Client', 'info': {'type_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/types/1'}}], 'site': {'id': 5353, 'name': 'Plano Office', 'info': {'site_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/sites/5353'}}, 'info': {'lastUpdated': '2019-06-13T15:27:10Z', 'updatedBy': 'user', 'dateEntered': '2006-06-21T16:04:59Z', 'enteredBy': 'CONVERSION', 'contacts_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/contacts?conditions=company/id=250', 'agreements_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/agreements?conditions=company/id=250', 'tickets_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets?conditions=company/id=250', 'opportunities_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/opportunities?conditions=company/id=250', 'activities_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=company/id=250', 'projects_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//project/projects?conditions=company/id=250', 'configurations_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/configurations?conditions=company/id=250', 'orders_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/orders?conditions=company/id=250', 'documents_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Company&recordId=250', 'sites_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/sites', 'teams_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/teams', 'reports_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/managementSummaryReports', 'notes_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/notes'}, 'customFields': [{'id': 2, 'caption': 'Parent Company', 'type': 'Text', 'entryMethod': 'List', 'numberOfDecimals': 0}, {'id': 13, 'caption': 'Disconnect Date', 'type': 'Date', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 14, 'caption': 'Transition Date', 'type': 'Date', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 15, 'caption': 'Partner ID', 'type': 'Text', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 17, 'caption': 'Customer Activation Date', 'type': 'Date', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 19, 'caption': 'TTMS Monitoring', 'type': 'Checkbox', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 20, 'caption': 'Channel Partner Type', 'type': 'Text', 'entryMethod': 'List', 'numberOfDecimals': 0}, {'id': 24, 'caption': 'Partner Name', 'type': 'Text', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 25, 'caption': 'Key Count', 'type': 'Number', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 26, 'caption': 'Region', 'type': 'Text', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 27, 'caption': 'Brand', 'type': 'Text', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 28, 'caption': 'Owner', 'type': 'Text', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 29, 'caption': 'Company Property Code', 'type': 'Text', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 30, 'caption': 'Brand Property Code', 'type': 'Text', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 31, 'caption': 'Customer Acquired Date', 'type': 'Date', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}]}}|
  
Example output:

```
{
  "company": {
    "company": {
      "addressLine1": "6505 Windcrest Dr",
      "addressLine2": "Suite 200",
      "annualRevenue": 0.0,
      "billToCompany": {
        "id": 250,
        "identifier": "ExampleCommunications",
        "info": {
          "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250"
        },
        "name": "Example Company"
      },
      "billingTerms": {
        "id": 1,
        "name": "Net 30 days"
      },
      "city": "Plano",
      "country": {
        "id": 1,
        "info": {
          "country_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/countries/1"
        },
        "name": "United States"
      },
      "currency": {
        "currencyCode": "USD",
        "currencyIdentifier": "USD",
        "decimalSeparator": ".",
        "displayIdFlag": false,
        "displaySymbolFlag": true,
        "id": 7,
        "info": {
          "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
        },
        "name": "US Dollars",
        "negativeParenthesesFlag": false,
        "numberOfDecimals": 2,
        "rightAlign": false,
        "symbol": "$",
        "thousandsSeparator": ","
      },
      "customFields": [
        {
          "caption": "Parent Company",
          "entryMethod": "List",
          "id": 2,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Disconnect Date",
          "entryMethod": "EntryField",
          "id": 13,
          "numberOfDecimals": 0,
          "type": "Date"
        },
        {
          "caption": "Transition Date",
          "entryMethod": "EntryField",
          "id": 14,
          "numberOfDecimals": 0,
          "type": "Date"
        },
        {
          "caption": "Partner ID",
          "entryMethod": "EntryField",
          "id": 15,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Customer Activation Date",
          "entryMethod": "EntryField",
          "id": 17,
          "numberOfDecimals": 0,
          "type": "Date"
        },
        {
          "caption": "TTMS Monitoring",
          "entryMethod": "EntryField",
          "id": 19,
          "numberOfDecimals": 0,
          "type": "Checkbox"
        },
        {
          "caption": "Channel Partner Type",
          "entryMethod": "List",
          "id": 20,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Partner Name",
          "entryMethod": "EntryField",
          "id": 24,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Key Count",
          "entryMethod": "EntryField",
          "id": 25,
          "numberOfDecimals": 0,
          "type": "Number"
        },
        {
          "caption": "Region",
          "entryMethod": "EntryField",
          "id": 26,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Brand",
          "entryMethod": "EntryField",
          "id": 27,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Owner",
          "entryMethod": "EntryField",
          "id": 28,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Company Property Code",
          "entryMethod": "EntryField",
          "id": 29,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Brand Property Code",
          "entryMethod": "EntryField",
          "id": 30,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Customer Acquired Date",
          "entryMethod": "EntryField",
          "id": 31,
          "numberOfDecimals": 0,
          "type": "Date"
        }
      ],
      "dateAcquired": "2006-06-21T04:00:00Z",
      "dateDeleted": "2018-11-09T21:19:15Z",
      "deletedBy": "User",
      "deletedFlag": true,
      "id": 4321,
      "identifier": "ExampleCommunications",
      "info": {
        "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=company/id=250",
        "agreements_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/agreements?conditions=company/id=250",
        "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/configurations?conditions=company/id=250",
        "contacts_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/contacts?conditions=company/id=250",
        "dateEntered": "2006-06-21T16:04:59Z",
        "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Company&recordId=250",
        "enteredBy": "CONVERSION",
        "lastUpdated": "2019-06-13T15:27:10Z",
        "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/notes",
        "opportunities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/opportunities?conditions=company/id=250",
        "orders_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/orders?conditions=company/id=250",
        "projects_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//project/projects?conditions=company/id=250",
        "reports_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/managementSummaryReports",
        "sites_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/sites",
        "teams_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/teams",
        "tickets_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets?conditions=company/id=250",
        "updatedBy": "user"
      },
      "invoiceDeliveryMethod": {
        "id": 1,
        "name": "Mail"
      },
      "isVendorFlag": false,
      "leadFlag": false,
      "mobileGuid": "1df91371-6d7a-4778-ab81-f3e7761f5211",
      "name": "Example Company",
      "sicCode": {
        "id": 1209,
        "name": "5734 - Computer and software stores"
      },
      "site": {
        "id": 5353,
        "info": {
          "site_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/250/sites/5353"
        },
        "name": "Plano Office"
      },
      "state": "TX",
      "status": {
        "id": 1,
        "info": {
          "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/statuses/1"
        },
        "name": "Active"
      },
      "taxCode": {
        "id": 8,
        "info": {
          "taxCode_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/taxCodes/8"
        },
        "name": "Tax-State"
      },
      "territory": {
        "id": 2,
        "info": {
          "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/2"
        },
        "name": "Example Company"
      },
      "timeZoneSetup": {
        "id": 1,
        "info": {
          "timeZoneSetup_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/timeZoneSetups/1"
        },
        "name": "GMT-5/Eastern Time: US & Canada"
      },
      "types": [
        {
          "id": 1,
          "info": {
            "type_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/types/1"
          },
          "name": "Client"
        }
      ],
      "unsubscribeFlag": false,
      "userDefinedField5": "1",
      "website": "www.example.com",
      "zip": "75024"
    }
  }
}
```

#### Get Ticket by ID

This action is used to get ticket information for given ticket ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ticket_id|integer|None|True|ID of the ticket for which information will be obtained|None|254|None|None|
  
Example input:

```
{
  "ticket_id": 254
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|False|Information about the ticket with the given ID|{'ticket': {'id': 254, 'summary': 'test', 'recordType': 'ServiceTicket', 'board': {'id': 30, 'name': 'Network Security - South', 'info': {'board_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30'}}, 'status': {'id': 550, 'name': 'In Progress', 'info': {'status_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550'}}, 'company': {'id': 19298, 'identifier': 'Example', 'name': 'Example Company', 'info': {'company_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298', 'mobileGuid': '5ec92caf-0922-4120-9268-21580dbbcef8'}}, 'siteName': 'Main - Catchall', 'addressLine1': 'address line 1', 'addressLine2': 'address line 2', 'city': 'London', 'zip': '111111', 'contact': {'id': 17754, 'name': 'Test Contact', 'info': {'mobileGuid': '1cf867f4-6198-40fe-8f28-91a644f08f3f', 'contact_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/contacts/17754'}}, 'contactName': 'Test Contact', 'type': {'id': 248, 'name': 'Testing', 'info': {'type_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/types/248'}}, 'subType': {'id': 701, 'name': 'Active Directory', 'info': {'subType_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/subtypes/701'}}, 'team': {'id': 10, 'name': 'Network Security', 'info': {'team_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10'}}, 'owner': {'id': 638, 'identifier': 'userint', 'name': 'user integration', 'info': {'member_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/638', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/638/image?lm=2022-08-03T19:50:33Z'}}, 'priority': {'id': 8, 'name': 'Priority 4 - Low', 'sort': 4, 'info': {'priority_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z'}}, 'serviceLocation': {'id': 4, 'name': 'Remote', 'info': {'location_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/locations/4'}}, 'source': {'id': 11, 'name': 'Automate', 'info': {'source_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/sources/11'}}, 'requiredDate': '2022-09-30T00:00:00Z', 'budgetHours': 10.5, 'agreement': {'id': 249, 'name': 'Example Internal', 'info': {'agreement_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/agreements/249'}}, 'severity': 'Medium', 'impact': 'Low', 'allowAllClientsPortalView': False, 'customerUpdatedFlag': False, 'automaticEmailContactFlag': True, 'automaticEmailResourceFlag': True, 'automaticEmailCcFlag': True, 'automaticEmailCc': 'user@example.com;', 'closedFlag': False, 'approved': True, 'estimatedExpenseCost': 0.0, 'estimatedExpenseRevenue': 0.0, 'estimatedProductCost': 0.0, 'estimatedProductRevenue': 0.0, 'estimatedTimeCost': 0.0, 'estimatedTimeRevenue': 0.0, 'billingMethod': 'ActualRates', 'subBillingMethod': 'ActualRates', 'dateResplan': '2022-09-02T08:29:34Z', 'dateResponded': '2022-09-02T08:29:34Z', 'resolveMinutes': 0, 'resPlanMinutes': 0, 'respondMinutes': 0, 'isInSla': True, 'resources': 'userint', 'hasChildTicket': False, 'hasMergedChildTicketFlag': False, 'billTime': 'NoDefault', 'billExpenses': 'NoDefault', 'billProducts': 'NoDefault', 'estimatedStartDate': '2022-09-01T00:00:00Z', 'duration': 22, 'location': {'id': 11, 'name': 'Example South', 'info': {'location_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11'}}, 'department': {'id': 5, 'identifier': 'Engineering', 'name': 'Engineering', 'info': {'department_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5'}}, 'mobileGuid': '468dca91-3a2f-4988-9a48-26adcbdd0e69', 'sla': {'id': 3, 'name': 'Example Standard SLA', 'info': {'sla_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3'}}, 'slaStatus': 'Resolve by Tue 10/04 11:00 PM UTC-05', 'requestForChangeFlag': False, 'currency': {'id': 7, 'symbol': '$', 'currencyCode': 'USD', 'decimalSeparator': '.', 'numberOfDecimals': 2, 'thousandsSeparator': ',', 'negativeParenthesesFlag': False, 'displaySymbolFlag': True, 'currencyIdentifier': 'USD', 'displayIdFlag': False, 'rightAlign': False, 'name': 'US Dollars', 'info': {'currency_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7'}}, 'info': {'lastUpdated': '2022-09-02T08:29:34Z', 'updatedBy': 'user', 'dateEntered': '2022-09-02T08:29:33Z', 'enteredBy': 'user', 'activities_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945366', 'scheduleentries_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945366', 'documents_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945366', 'configurations_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/configurations', 'tasks_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/tasks', 'notes_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/notes', 'products_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945366", 'timeentries_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945366", 'expenseEntries_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945366"}, 'escalationStartDateUTC': '2022-09-30T04:00:00Z', 'escalationLevel': 10, 'minutesBeforeWaiting': 0, 'respondedSkippedMinutes': 0, 'resplanSkippedMinutes': 0, 'customFields': [{'id': 7, 'caption': 'Dispatch Billing Required', 'type': 'Text', 'entryMethod': 'List', 'numberOfDecimals': 0}, {'id': 36, 'caption': 'Business App assigned ', 'type': 'Date', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 37, 'caption': 'T&M Billing Required', 'type': 'Checkbox', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}]}}|
  
Example output:

```
{
  "ticket": {
    "ticket": {
      "addressLine1": "address line 1",
      "addressLine2": "address line 2",
      "agreement": {
        "id": 249,
        "info": {
          "agreement_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/agreements/249"
        },
        "name": "Example Internal"
      },
      "allowAllClientsPortalView": false,
      "approved": true,
      "automaticEmailCc": "user@example.com;",
      "automaticEmailCcFlag": true,
      "automaticEmailContactFlag": true,
      "automaticEmailResourceFlag": true,
      "billExpenses": "NoDefault",
      "billProducts": "NoDefault",
      "billTime": "NoDefault",
      "billingMethod": "ActualRates",
      "board": {
        "id": 30,
        "info": {
          "board_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30"
        },
        "name": "Network Security - South"
      },
      "budgetHours": 10.5,
      "city": "London",
      "closedFlag": false,
      "company": {
        "id": 19298,
        "identifier": "Example",
        "info": {
          "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298",
          "mobileGuid": "5ec92caf-0922-4120-9268-21580dbbcef8"
        },
        "name": "Example Company"
      },
      "contact": {
        "id": 17754,
        "info": {
          "contact_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/contacts/17754",
          "mobileGuid": "1cf867f4-6198-40fe-8f28-91a644f08f3f"
        },
        "name": "Test Contact"
      },
      "contactName": "Test Contact",
      "currency": {
        "currencyCode": "USD",
        "currencyIdentifier": "USD",
        "decimalSeparator": ".",
        "displayIdFlag": false,
        "displaySymbolFlag": true,
        "id": 7,
        "info": {
          "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
        },
        "name": "US Dollars",
        "negativeParenthesesFlag": false,
        "numberOfDecimals": 2,
        "rightAlign": false,
        "symbol": "$",
        "thousandsSeparator": ","
      },
      "customFields": [
        {
          "caption": "Dispatch Billing Required",
          "entryMethod": "List",
          "id": 7,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Business App assigned ",
          "entryMethod": "EntryField",
          "id": 36,
          "numberOfDecimals": 0,
          "type": "Date"
        },
        {
          "caption": "T&M Billing Required",
          "entryMethod": "EntryField",
          "id": 37,
          "numberOfDecimals": 0,
          "type": "Checkbox"
        }
      ],
      "customerUpdatedFlag": false,
      "dateResplan": "2022-09-02T08:29:34Z",
      "dateResponded": "2022-09-02T08:29:34Z",
      "department": {
        "id": 5,
        "identifier": "Engineering",
        "info": {
          "department_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5"
        },
        "name": "Engineering"
      },
      "duration": 22,
      "escalationLevel": 10,
      "escalationStartDateUTC": "2022-09-30T04:00:00Z",
      "estimatedExpenseCost": 0.0,
      "estimatedExpenseRevenue": 0.0,
      "estimatedProductCost": 0.0,
      "estimatedProductRevenue": 0.0,
      "estimatedStartDate": "2022-09-01T00:00:00Z",
      "estimatedTimeCost": 0.0,
      "estimatedTimeRevenue": 0.0,
      "hasChildTicket": false,
      "hasMergedChildTicketFlag": false,
      "id": 254,
      "impact": "Low",
      "info": {
        "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945366",
        "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/configurations",
        "dateEntered": "2022-09-02T08:29:33Z",
        "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945366",
        "enteredBy": "user",
        "expenseEntries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945366",
        "lastUpdated": "2022-09-02T08:29:34Z",
        "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/notes",
        "products_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945366",
        "scheduleentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945366",
        "tasks_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945366/tasks",
        "timeentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945366",
        "updatedBy": "user"
      },
      "isInSla": true,
      "location": {
        "id": 11,
        "info": {
          "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11"
        },
        "name": "Example South"
      },
      "minutesBeforeWaiting": 0,
      "mobileGuid": "468dca91-3a2f-4988-9a48-26adcbdd0e69",
      "owner": {
        "id": 638,
        "identifier": "userint",
        "info": {
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/638/image?lm=2022-08-03T19:50:33Z",
          "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/638"
        },
        "name": "user integration"
      },
      "priority": {
        "id": 8,
        "info": {
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z",
          "priority_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8"
        },
        "name": "Priority 4 - Low",
        "sort": 4
      },
      "recordType": "ServiceTicket",
      "requestForChangeFlag": false,
      "requiredDate": "2022-09-30T00:00:00Z",
      "resPlanMinutes": 0,
      "resolveMinutes": 0,
      "resources": "userint",
      "resplanSkippedMinutes": 0,
      "respondMinutes": 0,
      "respondedSkippedMinutes": 0,
      "serviceLocation": {
        "id": 4,
        "info": {
          "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/locations/4"
        },
        "name": "Remote"
      },
      "severity": "Medium",
      "siteName": "Main - Catchall",
      "sla": {
        "id": 3,
        "info": {
          "sla_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3"
        },
        "name": "Example Standard SLA"
      },
      "slaStatus": "Resolve by Tue 10/04 11:00 PM UTC-05",
      "source": {
        "id": 11,
        "info": {
          "source_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/sources/11"
        },
        "name": "Automate"
      },
      "status": {
        "id": 550,
        "info": {
          "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550"
        },
        "name": "In Progress"
      },
      "subBillingMethod": "ActualRates",
      "subType": {
        "id": 701,
        "info": {
          "subType_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/subtypes/701"
        },
        "name": "Active Directory"
      },
      "summary": "test",
      "team": {
        "id": 10,
        "info": {
          "team_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10"
        },
        "name": "Network Security"
      },
      "type": {
        "id": 248,
        "info": {
          "type_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/types/248"
        },
        "name": "Testing"
      },
      "zip": "111111"
    }
  }
}
```

#### Get Ticket Notes

This action is used to get a list of notes for the given ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|conditions|string|None|False|Search results based on the provided fields. Supported operators are =, !=, <, <=, >, >=, contains, like, in, not|None|text contains 'test'|None|None|
|page|integer|None|False|Number of the page|None|11|None|None|
|pageSize|integer|None|False|Number of results returned per page (Defaults to 25)|None|32|None|None|
|ticket_id|integer|None|True|ID of the ticket for which notes will be obtained|None|532|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|ticket_notes|[]ticket_note|False|List of notes for the given ticket|{'ticket_notes': [{'id': 532, 'ticketId': 945315, 'text': 'test ticket', 'detailDescriptionFlag': True, 'internalAnalysisFlag': True, 'resolutionFlag': True, 'issueFlag': False, 'member': {'id': 637, 'identifier': 'user', 'name': 'user', 'info': {'member_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z'}}, 'dateCreated': '2022-09-01T08:46:36Z', 'createdBy': 'user', 'internalFlag': True, 'externalFlag': True, 'info': {'lastUpdated': '2022-09-01T08:46:36Z', 'updatedBy': 'user'}}, {'id': 532, 'ticketId': 945315, 'text': 'test text', 'detailDescriptionFlag': True, 'internalAnalysisFlag': True, 'resolutionFlag': True, 'issueFlag': False, 'member': {'id': 637, 'identifier': 'user', 'name': 'user', 'info': {'member_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z'}}, 'dateCreated': '2022-09-01T08:46:38Z', 'createdBy': 'user', 'internalFlag': True, 'externalFlag': True, 'info': {'lastUpdated': '2022-09-01T08:46:38Z', 'updatedBy': 'user'}}]}|
  
Example output:

```
{
  "ticket_notes": {
    "ticket_notes": [
      {
        "createdBy": "user",
        "dateCreated": "2022-09-01T08:46:36Z",
        "detailDescriptionFlag": true,
        "externalFlag": true,
        "id": 532,
        "info": {
          "lastUpdated": "2022-09-01T08:46:36Z",
          "updatedBy": "user"
        },
        "internalAnalysisFlag": true,
        "internalFlag": true,
        "issueFlag": false,
        "member": {
          "id": 637,
          "identifier": "user",
          "info": {
            "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z",
            "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637"
          },
          "name": "user"
        },
        "resolutionFlag": true,
        "text": "test ticket",
        "ticketId": 945315
      },
      {
        "createdBy": "user",
        "dateCreated": "2022-09-01T08:46:38Z",
        "detailDescriptionFlag": true,
        "externalFlag": true,
        "id": 532,
        "info": {
          "lastUpdated": "2022-09-01T08:46:38Z",
          "updatedBy": "user"
        },
        "internalAnalysisFlag": true,
        "internalFlag": true,
        "issueFlag": false,
        "member": {
          "id": 637,
          "identifier": "user",
          "info": {
            "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z",
            "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637"
          },
          "name": "user"
        },
        "resolutionFlag": true,
        "text": "test text",
        "ticketId": 945315
      }
    ]
  }
}
```

#### Get Tickets

This action is used to get a list of tickets

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|conditions|string|None|False|Search results based on the provided fields. Supported operators are =, !=, <, <=, >, >=, contains, like, in, not|None|impact='Medium' or summary contains 'https://example.com'|None|None|
|page|integer|None|False|Number of the page|None|1|None|None|
|pageSize|integer|None|False|Number of results returned per page (Defaults to 25)|None|10|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|tickets|[]ticket|False|Results containing information about tickets|{'tickets': [{'id': 3186, 'summary': 'Hello https://example.com', 'recordType': 'ServiceTicket', 'board': {'id': 30, 'name': 'Network Security - South', 'info': {'board_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30'}}, 'status': {'id': 562, 'name': '>Closed', 'info': {'status_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/562'}}, 'company': {'id': 19298, 'identifier': 'Example', 'name': 'Example Company', 'info': {'company_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298', 'mobileGuid': '5ec92caf-0922-4120-9268-21580dbbcef8'}}, 'site': {'id': 1000, 'name': 'Main', 'info': {'site_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298/sites/1000', 'mobileGuid': '9e51ad16-7cc3-41f0-ab02-ef332ff30024'}}, 'siteName': 'Main', 'addressLine1': '6505 Windcrest Dr', 'addressLine2': 'Suite 200', 'city': 'Plano', 'stateIdentifier': 'TX', 'zip': '75024', 'country': {'id': 1, 'name': 'United States', 'info': {'country_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/countries/1'}}, 'contactPhoneNumber': '9729056500', 'type': {'id': 250, 'name': 'Reports', 'info': {'type_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/types/250'}}, 'team': {'id': 10, 'name': 'Network Security', 'info': {'team_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10'}}, 'owner': {'id': 244, 'identifier': 'User', 'name': 'Example User', 'info': {'member_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/244', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/244/image?lm=2019-07-12T19:54:26Z'}}, 'priority': {'id': 12, 'name': 'Priority 5 - Service Request', 'sort': 5, 'info': {'priority_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/12', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/12/image?lm=2020-05-29T13:25:15Z'}}, 'serviceLocation': {'id': 4, 'name': 'Remote', 'info': {'location_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/locations/4'}}, 'source': {'id': 3, 'name': 'Internal', 'info': {'source_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/sources/3'}}, 'severity': 'Low', 'impact': 'Low', 'allowAllClientsPortalView': False, 'customerUpdatedFlag': False, 'automaticEmailContactFlag': False, 'automaticEmailResourceFlag': False, 'automaticEmailCcFlag': False, 'closedDate': '2018-08-10T17:39:20Z', 'closedBy': 'User', 'closedFlag': True, 'actualHours': 1.07, 'approved': True, 'estimatedExpenseCost': 0.0, 'estimatedExpenseRevenue': 0.0, 'estimatedProductCost': 0.0, 'estimatedProductRevenue': 0.0, 'estimatedTimeCost': 0.0, 'estimatedTimeRevenue': 0.0, 'billingMethod': 'ActualRates', 'subBillingMethod': 'ActualRates', 'dateResolved': '2018-08-10T17:39:12Z', 'dateResplan': '2018-08-09T15:22:30Z', 'dateResponded': '2018-08-09T15:22:30Z', 'resolveMinutes': 306, 'resPlanMinutes': 0, 'respondMinutes': 0, 'isInSla': True, 'resources': 'User', 'hasChildTicket': False, 'hasMergedChildTicketFlag': False, 'billTime': 'NoDefault', 'billExpenses': 'NoDefault', 'billProducts': 'NoDefault', 'location': {'id': 11, 'name': 'Example South', 'info': {'location_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11'}}, 'department': {'id': 5, 'identifier': 'Engineering', 'name': 'Engineering', 'info': {'department_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5'}}, 'mobileGuid': 'b7fd8e26-fcad-4ade-ba53-c0772dcd7913', 'sla': {'id': 6, 'name': 'No SLA', 'info': {'sla_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/6'}}, 'slaStatus': 'Resolved', 'requestForChangeFlag': False, 'currency': {'id': 7, 'symbol': '$', 'currencyCode': 'USD', 'decimalSeparator': '.', 'numberOfDecimals': 2, 'thousandsSeparator': ',', 'negativeParenthesesFlag': False, 'displaySymbolFlag': True, 'currencyIdentifier': 'USD', 'displayIdFlag': False, 'rightAlign': False, 'name': 'US Dollars', 'info': {'currency_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7'}}, 'info': {'lastUpdated': '2018-11-09T21:19:07Z', 'updatedBy': 'User', 'dateEntered': '2018-08-09T15:22:36Z', 'enteredBy': 'User', 'activities_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=3186', 'scheduleentries_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=3186', 'documents_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=3186', 'configurations_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/configurations', 'tasks_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/tasks', 'notes_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/notes', 'products_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=3186", 'timeentries_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=3186", 'expenseEntries_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=3186"}, 'escalationStartDateUTC': '2018-08-10T17:39:19Z', 'escalationLevel': 15, 'minutesBeforeWaiting': 0, 'respondedSkippedMinutes': 0, 'resplanSkippedMinutes': 0, 'customFields': [{'id': 7, 'caption': 'Dispatch Billing Required', 'type': 'Text', 'entryMethod': 'List', 'numberOfDecimals': 0}, {'id': 36, 'caption': 'Business App assigned ', 'type': 'Date', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 37, 'caption': 'T&M Billing Required', 'type': 'Checkbox', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}]}]}|
  
Example output:

```
{
  "tickets": {
    "tickets": [
      {
        "actualHours": 1.07,
        "addressLine1": "6505 Windcrest Dr",
        "addressLine2": "Suite 200",
        "allowAllClientsPortalView": false,
        "approved": true,
        "automaticEmailCcFlag": false,
        "automaticEmailContactFlag": false,
        "automaticEmailResourceFlag": false,
        "billExpenses": "NoDefault",
        "billProducts": "NoDefault",
        "billTime": "NoDefault",
        "billingMethod": "ActualRates",
        "board": {
          "id": 30,
          "info": {
            "board_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30"
          },
          "name": "Network Security - South"
        },
        "city": "Plano",
        "closedBy": "User",
        "closedDate": "2018-08-10T17:39:20Z",
        "closedFlag": true,
        "company": {
          "id": 19298,
          "identifier": "Example",
          "info": {
            "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298",
            "mobileGuid": "5ec92caf-0922-4120-9268-21580dbbcef8"
          },
          "name": "Example Company"
        },
        "contactPhoneNumber": "9729056500",
        "country": {
          "id": 1,
          "info": {
            "country_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/countries/1"
          },
          "name": "United States"
        },
        "currency": {
          "currencyCode": "USD",
          "currencyIdentifier": "USD",
          "decimalSeparator": ".",
          "displayIdFlag": false,
          "displaySymbolFlag": true,
          "id": 7,
          "info": {
            "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
          },
          "name": "US Dollars",
          "negativeParenthesesFlag": false,
          "numberOfDecimals": 2,
          "rightAlign": false,
          "symbol": "$",
          "thousandsSeparator": ","
        },
        "customFields": [
          {
            "caption": "Dispatch Billing Required",
            "entryMethod": "List",
            "id": 7,
            "numberOfDecimals": 0,
            "type": "Text"
          },
          {
            "caption": "Business App assigned ",
            "entryMethod": "EntryField",
            "id": 36,
            "numberOfDecimals": 0,
            "type": "Date"
          },
          {
            "caption": "T&M Billing Required",
            "entryMethod": "EntryField",
            "id": 37,
            "numberOfDecimals": 0,
            "type": "Checkbox"
          }
        ],
        "customerUpdatedFlag": false,
        "dateResolved": "2018-08-10T17:39:12Z",
        "dateResplan": "2018-08-09T15:22:30Z",
        "dateResponded": "2018-08-09T15:22:30Z",
        "department": {
          "id": 5,
          "identifier": "Engineering",
          "info": {
            "department_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5"
          },
          "name": "Engineering"
        },
        "escalationLevel": 15,
        "escalationStartDateUTC": "2018-08-10T17:39:19Z",
        "estimatedExpenseCost": 0.0,
        "estimatedExpenseRevenue": 0.0,
        "estimatedProductCost": 0.0,
        "estimatedProductRevenue": 0.0,
        "estimatedTimeCost": 0.0,
        "estimatedTimeRevenue": 0.0,
        "hasChildTicket": false,
        "hasMergedChildTicketFlag": false,
        "id": 3186,
        "impact": "Low",
        "info": {
          "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=3186",
          "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/configurations",
          "dateEntered": "2018-08-09T15:22:36Z",
          "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=3186",
          "enteredBy": "User",
          "expenseEntries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=3186",
          "lastUpdated": "2018-11-09T21:19:07Z",
          "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/notes",
          "products_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=3186",
          "scheduleentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=3186",
          "tasks_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/3186/tasks",
          "timeentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=3186",
          "updatedBy": "User"
        },
        "isInSla": true,
        "location": {
          "id": 11,
          "info": {
            "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11"
          },
          "name": "Example South"
        },
        "minutesBeforeWaiting": 0,
        "mobileGuid": "b7fd8e26-fcad-4ade-ba53-c0772dcd7913",
        "owner": {
          "id": 244,
          "identifier": "User",
          "info": {
            "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/244/image?lm=2019-07-12T19:54:26Z",
            "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/244"
          },
          "name": "Example User"
        },
        "priority": {
          "id": 12,
          "info": {
            "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/12/image?lm=2020-05-29T13:25:15Z",
            "priority_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/12"
          },
          "name": "Priority 5 - Service Request",
          "sort": 5
        },
        "recordType": "ServiceTicket",
        "requestForChangeFlag": false,
        "resPlanMinutes": 0,
        "resolveMinutes": 306,
        "resources": "User",
        "resplanSkippedMinutes": 0,
        "respondMinutes": 0,
        "respondedSkippedMinutes": 0,
        "serviceLocation": {
          "id": 4,
          "info": {
            "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/locations/4"
          },
          "name": "Remote"
        },
        "severity": "Low",
        "site": {
          "id": 1000,
          "info": {
            "mobileGuid": "9e51ad16-7cc3-41f0-ab02-ef332ff30024",
            "site_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298/sites/1000"
          },
          "name": "Main"
        },
        "siteName": "Main",
        "sla": {
          "id": 6,
          "info": {
            "sla_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/6"
          },
          "name": "No SLA"
        },
        "slaStatus": "Resolved",
        "source": {
          "id": 3,
          "info": {
            "source_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/sources/3"
          },
          "name": "Internal"
        },
        "stateIdentifier": "TX",
        "status": {
          "id": 562,
          "info": {
            "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/562"
          },
          "name": ">Closed"
        },
        "subBillingMethod": "ActualRates",
        "summary": "Hello https://example.com",
        "team": {
          "id": 10,
          "info": {
            "team_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10"
          },
          "name": "Network Security"
        },
        "type": {
          "id": 250,
          "info": {
            "type_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/types/250"
          },
          "name": "Reports"
        },
        "zip": "75024"
      }
    ]
  }
}
```

#### Update Ticket

This action is used to update an existing ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agreement|details_input|None|False|Name or ID of the agreement|None|{"id": 19}|None|None|
|automaticEmailCc|string|None|False|Address to which the email will be sent with information about the added note|None|user@example.com|None|None|
|automaticEmailCcFlag|boolean|None|False|Whether to send an email to the specified email address in CC when a note to the ticket is added|None|True|None|None|
|automaticEmailContactFlag|boolean|None|False|Whether to send an email to the specified contact when a note to the ticket is added|None|True|None|None|
|automaticEmailResourceFlag|boolean|None|False|Whether to send an email to the specified resource when a note to the ticket is added|None|True|None|None|
|board|details_input|None|True|Name or ID of the board|None|{"name": "Network Security"}|None|None|
|budgetHours|float|None|False|Budget hours for the ticket|None|8.5|None|None|
|company_id|integer|None|True|Company Rec ID. This ID can be found in `Share` link on the company page|None|23|None|None|
|contact|details_input|None|False|Name or ID of the contact|None|{"id": 144}|None|None|
|department|details_input|None|False|Name or ID of the department|None|{"name": "Engineering"}|None|None|
|estimatedStartDate|date|None|False|Estimated start date for the ticket|None|2022-09-23 00:00:00+02:00|None|None|
|impact|string|None|True|Impact of the ticket|None|Medium|None|None|
|location|details_input|None|False|Name or ID of the location|None|{"id": 11}|None|None|
|owner|details_input|None|False|Name or ID of the ticket owner|None|{"id": 11}|None|None|
|predecessorId|integer|None|False|ID of the ticket predecessor|None|1234|None|None|
|predecessortype|string|None|False|Type of the ticket predecessor|None|Ticket|None|None|
|priority_id|integer|None|True|ID of the priority|None|7|None|None|
|requiredDate|date|None|False|Due date for the ticket|None|2022-09-26 00:00:00+02:00|None|None|
|serviceLocation|details_input|None|False|Name or ID of the service location|None|{"name": "Remote"}|None|None|
|severity|string|None|True|Severity of the ticket|None|Medium|None|None|
|site|details_input|None|False|Name or ID of the site|None|{"id": 1}|None|None|
|source|details_input|None|False|Name or ID of the source|None|{"name": "Call"}|None|None|
|status|details_input|None|True|Name or ID of the ticket status|None|{"name": "In Progress"}|None|None|
|subtype|details_input|None|False|Name or ID of the subtype|None|{"name": "Active Directory"}|None|None|
|summary|string|None|True|Summary of the ticket|None|example summary|None|None|
|team|details_input|None|True|Name or ID of the team|None|{"id": 10}|None|None|
|ticket_id|integer|None|True|ID of the ticket which will be updated|None|1122|None|None|
|type|details_input|None|False|Name or ID of the type|None|{"name": "Testing"}|None|None|
  
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
  "estimatedStartDate": "2022-09-23 00:00:00+02:00",
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
  "requiredDate": "2022-09-26 00:00:00+02:00",
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
  "ticket_id": 1122,
  "type": {
    "name": "Testing"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|False|Information about the ticket with the given ID|{'ticket': {'id': 945370, 'summary': 'update_ticket_few_parameters', 'recordType': 'ServiceTicket', 'board': {'id': 30, 'name': 'Network Security', 'info': {'board_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30'}}, 'status': {'id': 550, 'name': 'In Progress', 'info': {'status_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550'}}, 'company': {'id': 23, 'identifier': 'Example', 'name': 'Example Company', 'info': {'company_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298', 'mobileGuid': '5ec92caf-0922-4120-9268-21580dbbcef8'}}, 'team': {'id': 10, 'name': 'Network Security', 'info': {'team_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10'}}, 'priority': {'id': 8, 'name': 'Priority 4 - Low', 'sort': 4, 'info': {'priority_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z'}}, 'severity': 'Medium', 'impact': 'Medium', 'allowAllClientsPortalView': False, 'customerUpdatedFlag': False, 'automaticEmailContactFlag': True, 'automaticEmailResourceFlag': True, 'automaticEmailCcFlag': True, 'closedFlag': False, 'approved': True, 'estimatedExpenseCost': 0.0, 'estimatedExpenseRevenue': 0.0, 'estimatedProductCost': 0.0, 'estimatedProductRevenue': 0.0, 'estimatedTimeCost': 0.0, 'estimatedTimeRevenue': 0.0, 'billingMethod': 'ActualRates', 'subBillingMethod': 'ActualRates', 'dateResplan': '2022-09-07T09:46:59Z', 'dateResponded': '2022-09-07T09:46:59Z', 'resolveMinutes': 0, 'resPlanMinutes': 0, 'respondMinutes': 0, 'isInSla': True, 'resources': 'userint', 'hasChildTicket': False, 'hasMergedChildTicketFlag': False, 'billTime': 'NoDefault', 'billExpenses': 'NoDefault', 'billProducts': 'NoDefault', 'location': {'id': 11, 'name': 'Example South', 'info': {'location_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11'}}, 'department': {'id': 5, 'identifier': 'Engineering', 'name': 'Engineering', 'info': {'department_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5'}}, 'mobileGuid': '40ddd5b7-f6f1-4679-9bc9-f80db3fc3daf', 'sla': {'id': 3, 'name': 'Example Standard SLA', 'info': {'sla_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3'}}, 'slaStatus': 'Resolve by Tue 10/04 11:00 PM UTC-05', 'currency': {'id': 7, 'symbol': '$', 'currencyCode': 'USD', 'decimalSeparator': '.', 'numberOfDecimals': 2, 'thousandsSeparator': ',', 'negativeParenthesesFlag': False, 'displaySymbolFlag': True, 'currencyIdentifier': 'USD', 'displayIdFlag': False, 'rightAlign': False, 'name': 'US Dollars', 'info': {'currency_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7'}}, 'info': {'lastUpdated': '2022-09-15T08:30:12Z', 'updatedBy': 'user', 'dateEntered': '2022-09-07T09:46:58Z', 'enteredBy': 'user', 'activities_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945370', 'scheduleentries_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945370', 'documents_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945370', 'configurations_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/configurations', 'tasks_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/tasks', 'notes_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/notes', 'products_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945370", 'timeentries_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370", 'expenseEntries_href': "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370"}, 'escalationStartDateUTC': '2022-09-30T04:00:00Z', 'escalationLevel': 10, 'minutesBeforeWaiting': 0, 'respondedSkippedMinutes': 0, 'resplanSkippedMinutes': 0, 'customFields': [{'id': 7, 'caption': 'Dispatch Billing Required', 'type': 'Text', 'entryMethod': 'List', 'numberOfDecimals': 0}, {'id': 36, 'caption': 'Business App assigned ', 'type': 'Date', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}, {'id': 37, 'caption': 'T&M Billing Required', 'type': 'Checkbox', 'entryMethod': 'EntryField', 'numberOfDecimals': 0}]}}|
  
Example output:

```
{
  "ticket": {
    "ticket": {
      "allowAllClientsPortalView": false,
      "approved": true,
      "automaticEmailCcFlag": true,
      "automaticEmailContactFlag": true,
      "automaticEmailResourceFlag": true,
      "billExpenses": "NoDefault",
      "billProducts": "NoDefault",
      "billTime": "NoDefault",
      "billingMethod": "ActualRates",
      "board": {
        "id": 30,
        "info": {
          "board_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30"
        },
        "name": "Network Security"
      },
      "closedFlag": false,
      "company": {
        "id": 23,
        "identifier": "Example",
        "info": {
          "company_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//company/companies/19298",
          "mobileGuid": "5ec92caf-0922-4120-9268-21580dbbcef8"
        },
        "name": "Example Company"
      },
      "currency": {
        "currencyCode": "USD",
        "currencyIdentifier": "USD",
        "decimalSeparator": ".",
        "displayIdFlag": false,
        "displaySymbolFlag": true,
        "id": 7,
        "info": {
          "currency_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//finance/currencies/7"
        },
        "name": "US Dollars",
        "negativeParenthesesFlag": false,
        "numberOfDecimals": 2,
        "rightAlign": false,
        "symbol": "$",
        "thousandsSeparator": ","
      },
      "customFields": [
        {
          "caption": "Dispatch Billing Required",
          "entryMethod": "List",
          "id": 7,
          "numberOfDecimals": 0,
          "type": "Text"
        },
        {
          "caption": "Business App assigned ",
          "entryMethod": "EntryField",
          "id": 36,
          "numberOfDecimals": 0,
          "type": "Date"
        },
        {
          "caption": "T&M Billing Required",
          "entryMethod": "EntryField",
          "id": 37,
          "numberOfDecimals": 0,
          "type": "Checkbox"
        }
      ],
      "customerUpdatedFlag": false,
      "dateResplan": "2022-09-07T09:46:59Z",
      "dateResponded": "2022-09-07T09:46:59Z",
      "department": {
        "id": 5,
        "identifier": "Engineering",
        "info": {
          "department_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/departments/5"
        },
        "name": "Engineering"
      },
      "escalationLevel": 10,
      "escalationStartDateUTC": "2022-09-30T04:00:00Z",
      "estimatedExpenseCost": 0.0,
      "estimatedExpenseRevenue": 0.0,
      "estimatedProductCost": 0.0,
      "estimatedProductRevenue": 0.0,
      "estimatedTimeCost": 0.0,
      "estimatedTimeRevenue": 0.0,
      "hasChildTicket": false,
      "hasMergedChildTicketFlag": false,
      "id": 945370,
      "impact": "Medium",
      "info": {
        "activities_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//sales/activities?conditions=ticket/id=945370",
        "configurations_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/configurations",
        "dateEntered": "2022-09-07T09:46:58Z",
        "documents_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/documents?recordType=Ticket&recordId=945370",
        "enteredBy": "user",
        "expenseEntries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//expense/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370",
        "lastUpdated": "2022-09-15T08:30:12Z",
        "notes_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/notes",
        "products_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//procurement/products?conditions=chargeToType='Ticket' AND chargeToId=945370",
        "scheduleentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//schedule/entries?conditions=type/id=4 AND objectId=945370",
        "tasks_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/tickets/945370/tasks",
        "timeentries_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//time/entries?conditions=(chargeToType='ServiceTicket' OR chargeToType='ProjectTicket') AND chargeToId=945370",
        "updatedBy": "user"
      },
      "isInSla": true,
      "location": {
        "id": 11,
        "info": {
          "location_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/locations/11"
        },
        "name": "Example South"
      },
      "minutesBeforeWaiting": 0,
      "mobileGuid": "40ddd5b7-f6f1-4679-9bc9-f80db3fc3daf",
      "priority": {
        "id": 8,
        "info": {
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8/image?lm=2020-05-27T21:17:07Z",
          "priority_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/priorities/8"
        },
        "name": "Priority 4 - Low",
        "sort": 4
      },
      "recordType": "ServiceTicket",
      "resPlanMinutes": 0,
      "resolveMinutes": 0,
      "resources": "userint",
      "resplanSkippedMinutes": 0,
      "respondMinutes": 0,
      "respondedSkippedMinutes": 0,
      "severity": "Medium",
      "sla": {
        "id": 3,
        "info": {
          "sla_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/SLAs/3"
        },
        "name": "Example Standard SLA"
      },
      "slaStatus": "Resolve by Tue 10/04 11:00 PM UTC-05",
      "status": {
        "id": 550,
        "info": {
          "status_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/statuses/550"
        },
        "name": "In Progress"
      },
      "subBillingMethod": "ActualRates",
      "summary": "update_ticket_few_parameters",
      "team": {
        "id": 10,
        "info": {
          "team_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//service/boards/30/teams/10"
        },
        "name": "Network Security"
      }
    }
  }
}
```

#### Update Ticket Note

This action is used to update the given note for the specified ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|detailDescriptionFlag|boolean|None|False|Discussion flag|None|True|None|None|
|internalAnalysisFlag|boolean|None|False|Internal analysis flag|None|False|None|None|
|note_id|integer|None|True|ID of the note which will be updated|None|33213|None|None|
|resolutionFlag|boolean|None|False|Resolution flag|None|True|None|None|
|text|string|None|False|Ticket's note text|None|note text|None|None|
|ticket_id|integer|None|True|ID of the ticket for which a new note will be updated|None|112|None|None|
  
Example input:

```
{
  "detailDescriptionFlag": true,
  "internalAnalysisFlag": false,
  "note_id": 33213,
  "resolutionFlag": true,
  "text": "note text",
  "ticket_id": 112
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket_note|ticket_note|False|Information about the updated note for the specified ticket|{'ticket_note': {'id': 33213, 'ticketId': 112, 'text': 'note text', 'detailDescriptionFlag': False, 'internalAnalysisFlag': True, 'resolutionFlag': False, 'issueFlag': False, 'member': {'id': 637, 'identifier': 'user', 'name': 'user', 'info': {'member_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637', 'image_href': 'https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z'}}, 'dateCreated': '2022-09-01T08:59:27Z', 'createdBy': 'user', 'internalFlag': True, 'externalFlag': True, 'info': {'lastUpdated': '2022-09-20T07:20:16Z', 'updatedBy': 'user'}}}|
  
Example output:

```
{
  "ticket_note": {
    "ticket_note": {
      "createdBy": "user",
      "dateCreated": "2022-09-01T08:59:27Z",
      "detailDescriptionFlag": false,
      "externalFlag": true,
      "id": 33213,
      "info": {
        "lastUpdated": "2022-09-20T07:20:16Z",
        "updatedBy": "user"
      },
      "internalAnalysisFlag": true,
      "internalFlag": true,
      "issueFlag": false,
      "member": {
        "id": 637,
        "identifier": "user",
        "info": {
          "image_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637/image?lm=2022-08-03T19:37:23Z",
          "member_href": "https://sandbox-na.myconnectwise.net/v4_6_release/apis/3.0//system/members/637"
        },
        "name": "user"
      },
      "resolutionFlag": false,
      "text": "note text",
      "ticketId": 112
    }
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**more_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Identifier|string|None|False|Identifier|None|
|Info|object|None|False|Additional information|None|
|Name|string|None|False|Name|None|
  
**agreement_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Info|object|None|False|Additional information|None|
|Name|string|None|False|Name|None|
|Type|string|None|False|Type|None|
  
**currency_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Currency Code|string|None|False|Currency code|None|
|Currency Identifier|string|None|False|Currency identifier|None|
|Display ID Flag|boolean|None|False|Display ID flag|None|
|Display Symbol Flag|boolean|None|False|Display symbol flag|None|
|ID|integer|None|False|ID|None|
|Info|object|None|False|Additional information|None|
|Name|string|None|False|Name|None|
|Negative Parentheses Flag|boolean|None|False|Negative parentheses flag|None|
|Number Of Decimals|integer|None|False|Number of decimals|None|
|Right Align|boolean|None|False|Right align|None|
|Symbol|string|None|False|Symbol|None|
|Thousands Separator|string|None|False|Thousands Separator|None|
  
**merged_parent_ticket_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Info|object|None|False|Additional information|None|
|Summary|string|None|False|Summary|None|
  
**details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Info|object|None|False|Additional information|None|
|Name|string|None|False|Name|None|
  
**details_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Name|string|None|False|Name|None|
  
**company**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account Number|string|None|False|Account number|None|
|Address Line|string|None|False|First line of the address|None|
|Second Address Line|string|None|False|Second line of the address|None|
|Annual Revenue|float|None|False|Annual revenue|None|
|Bill to Company|more_details|None|False|Bill to company|None|
|Billing Contact|details|None|False|Billing contact|None|
|Billing Site|details|None|False|Billing site|None|
|Billing Terms|details|None|False|Billing terms|None|
|Calendar|details|None|False|Calendar|None|
|City|string|None|False|City|None|
|Company Entity Type|details|None|False|Company entity type|None|
|Country|more_details|None|False|Country|None|
|Currency|currency_details|None|False|Currency|None|
|Custom Fields|[]object|None|False|Custom fields|None|
|Date Acquired|string|None|False|Date acquired|None|
|Date Deleted|string|None|False|Date deleted|None|
|Default Contact|details|None|False|Default contact|None|
|Deleted By|string|None|False|Deleted by|None|
|Deleted Flag|boolean|None|False|Deleted flag|None|
|Facebook URL|string|None|False|Facebook URL|None|
|Fax Number|string|None|False|Fax number|None|
|ID|integer|None|False|ID|None|
|Identifier|string|None|False|Identifier|None|
|Info|object|None|False|Info|None|
|Integrator Tags|[]string|None|False|Integrator tags|None|
|Invoice CC Email Address|string|None|False|Invoice CC email address|None|
|Invoice Delivery Method|details|None|False|Invoice delivery method|None|
|Invoice Template|details|None|False|Invoice template|None|
|Invoice to Email Address|string|None|False|Invoice to email address|None|
|Is Vendor Flag|boolean|None|False|Is vendor flag|None|
|Lead Flag|boolean|None|False|Lead flag|None|
|Lead Source|string|None|False|Lead source|None|
|LinkedIn URL|string|None|False|LinkedIn URL|None|
|Market|details|None|False|Market|None|
|Mobile GUID|string|None|False|Mobile GUID|None|
|Name|string|None|False|Name|None|
|Number of Employees|integer|None|False|Number of employees|None|
|Ownership Type|details|None|False|Ownership type|None|
|Parent Company|more_details|None|False|Parent company|None|
|Phone Number|string|None|False|Phone number|None|
|Pricing Schedule|details|None|False|Pricing schedule|None|
|Reseller Identifier|string|None|False|Reseller identifier|None|
|Revenue Year|integer|None|False|Revenue year|None|
|Sic Code|details|None|False|Sic code|None|
|Site|details|None|False|Site|None|
|State|string|None|False|State|None|
|Status|details|None|False|Status|None|
|Tax Code|details|None|False|Tax code|None|
|Tax Identifier|string|None|False|Tax identifier|None|
|Territory|details|None|False|Territory|None|
|Territory Manager|more_details|None|False|Territory manager|None|
|Timezone Setup|details|None|False|Timezone setup|None|
|Twitter URL|string|None|False|Twitter URL|None|
|Types|[]details|None|False|Types|None|
|Unsubscribe Flag|boolean|None|False|Unsubscribe flag|None|
|Vendor Identifier|string|None|False|Vendor identifier|None|
|Website|string|None|False|Website|None|
|Year Established|integer|None|False|Year established|None|
|ZIP|string|None|False|ZIP code|None|
  
**ticket**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actual Hours|float|None|False|Actual hours|None|
|Address Line|string|None|False|First line of the address|None|
|Second Address Line|string|None|False|Second line of the address|None|
|Agreement|agreement_details|None|False|Agreement|None|
|Allow All Client Portal View|boolean|None|False|Allow all client portal view|None|
|Approved|boolean|None|False|Approved|None|
|Automatic Email CC|string|None|False|Automatic email CC|None|
|Automatic Email CC Flag|boolean|None|False|Automatic email CC flag|None|
|Automatic Email Contact Flag|boolean|None|False|Automatic email contact flag|None|
|Automatic Email Resource Flag|boolean|None|False|Automatic email resource flag|None|
|Bill Expenses|string|None|False|Bill expenses|None|
|Bill Products|string|None|False|Bill products|None|
|Bill Time|string|None|False|Bill time|None|
|Billing Amount|float|None|False|Billing amount|None|
|Billing Method|string|None|False|Billing method|None|
|Board|details|None|False|Board|None|
|Budget Hours|float|None|False|Budget hours|None|
|City|string|None|False|City|None|
|Closed By|string|None|False|Closed by|None|
|Closed Date|string|None|False|Closed date|None|
|Closed Flag|boolean|None|False|Closed flag|None|
|Company|more_details|None|False|Company|None|
|Contact|details|None|False|Contact|None|
|Contact Email Address|string|None|False|Contact email address|None|
|Contact Email Lookup|string|None|False|Contact Email Lookup|None|
|Contact Name|string|None|False|Contact name|None|
|Contact Phone Extension|string|None|False|Contact phone extension|None|
|Contact Phone Number|string|None|False|Contact phone number|None|
|Country|more_details|None|False|Country|None|
|Currency|currency_details|None|False|Currency|None|
|Custom Fields|[]object|None|False|Custom fields|None|
|Customer Update Flag|boolean|None|False|Customer update flag|None|
|Date Resolved|string|None|False|Date resolved|None|
|Date Resplan|string|None|False|Date resplan|None|
|Date Responded|string|None|False|Date responded|None|
|Department|more_details|None|False|Department|None|
|Duration|integer|None|False|Duration|None|
|Estimated Expense Cost|float|None|False|Estimated expense cost|None|
|Estimated Expense Revenue|float|None|False|Estimated expense revenue|None|
|Estimated Product Cost|float|None|False|Estimated product cost|None|
|Estimated Product Revenue|float|None|False|Estimated product revenue|None|
|Estimated Start Date|string|None|False|Estimated start date|None|
|Estimated Time Cost|float|None|False|Estimated time cost|None|
|Estimated Time Revenue|float|None|False|Estimated time revenue|None|
|External Reference|string|None|False|External reference|None|
|Has Child Ticket|boolean|None|False|Has child ticket|None|
|Has Merged Child Ticket Flag|boolean|None|False|Has merged child ticket flag|None|
|Hourly Rate|float|None|False|Hourly rate|None|
|ID|integer|None|False|Ticket ID|None|
|Impact|string|None|False|Impact|None|
|Info|object|None|False|Info|None|
|Initial Description|string|None|False|Initial description|None|
|Initial Description From|string|None|False|Initial description from|None|
|Initial Internal Analysis|string|None|False|Initial internal analysis|None|
|Initial Resolution|string|None|False|Initial resolution|None|
|Integrator Tags|[]string|None|False|Integrator tags|None|
|Is In SLA|boolean|None|False|Is in SLA|None|
|Item|details|None|False|Item|None|
|Knowledge Base Category ID|integer|None|False|Knowledge base category ID|None|
|Knowledge Base Link ID|integer|None|False|Knowledge base link ID|None|
|Knowledge Base Link Type|string|None|False|Knowledge base link type|None|
|Knowledge Base Subcategory ID|integer|None|False|Knowledge base subcategory ID|None|
|Lag Days|integer|None|False|Lag days|None|
|Lag Non Working Days Flag|boolean|None|False|Lag non working days flag|None|
|Location|details|None|False|Location|None|
|Merged Parent Ticket|merged_parent_ticket_details|None|False|Merget parent ticket|None|
|Mobile GUID|string|None|False|Mobile GUID|None|
|Opportunity|details|None|False|Opportunity|None|
|Owner|more_details|None|False|Owner|None|
|Parent Ticket ID|integer|None|False|Parent ticket ID|None|
|Predecessor Closed Flag|boolean|None|False|Predecessor closed flag|None|
|Predecessor ID|integer|None|False|Predecessor ID|None|
|Predecessor Type|string|None|False|Predecessor type|None|
|Priority|details|None|False|Priority|None|
|Process Notifications|boolean|None|False|Process notifications|None|
|Record Type|string|None|False|Type of the record|None|
|Required Date|string|None|False|Required date|None|
|Resolve Plan Minutes|integer|None|False|Resolve plan minutes|None|
|Resolve Minutes|integer|None|False|Resolve minutes|None|
|Resources|string|None|False|Resources|None|
|Respond Minutes|integer|None|False|Respond minutes|None|
|Service Location|details|None|False|Service location|None|
|Severity|string|None|False|Severity|None|
|Site|details|None|False|Site|None|
|Site Name|string|None|False|Site name|None|
|Skip Callback|boolean|None|False|Skip callback|None|
|SLA|details|None|False|SLA|None|
|SLA Status|string|None|False|SLA status|None|
|Source|details|None|False|Source|None|
|State Identifier|string|None|False|State identifier|None|
|Status|agreement_details|None|False|Status|None|
|Sub Billing Amount|float|None|False|Sub billing amount|None|
|Sub Billing Method|string|None|False|Sub billing method|None|
|Sub Date Accepted|string|None|False|Sub date accepted|None|
|Subtype|details|None|False|Subtype|None|
|Summary|string|None|False|Ticket summary|None|
|Team|details|None|False|Team|None|
|Type|details|None|False|Type|None|
|Work Role|details|None|False|Work role|None|
|Work Type|details|None|False|Work type|None|
|ZIP|string|None|False|ZIP code|None|
  
**ticket_note**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Contact|details|None|False|Contact|None|
|Created By|string|None|False|Created by|None|
|Customer Updated Flag|boolean|None|False|Customer updated flag|None|
|Date Created|string|None|False|Date created|None|
|Detail Description Flag|boolean|None|False|Detail description flag|None|
|External Flag|boolean|None|False|External flag|None|
|ID|integer|None|False|ID|None|
|Info|object|None|False|Info|None|
|Internal Analysis Flag|boolean|None|False|Internal analysis flag|None|
|Internal Flag|boolean|None|False|Internal flag|None|
|Issue Flag|boolean|None|False|Issue flag|None|
|Member|more_details|None|False|Member|None|
|Process Notifications|boolean|None|False|Process notifications|None|
|Resolution Flag|boolean|None|False|Resolution flag|None|
|Text|string|None|False|Text|None|
|Ticket ID|integer|None|False|Ticket ID|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.1 - Adding regions support for connection | Updated SDK to the latest version (6.4.2)
* 1.0.0 - Initial plugin

# Links

* [Connectwise](https://www.connectwise.com/)

## References
  
*This plugin does not contain any references.*