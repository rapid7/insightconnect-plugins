# Description

EasyVista Service Manager platform supports even the most complex requirements, while bringing a new level of simplicity, agility, and mobility required to make cloud based IT Service Management (ITSM) software easy to use and easy to deliver. Using the EasyVista plugin for Rapid7 InsightConnect, users can manage the creation, update, search and closure of incident, service request, problem or event tickets

# Key Features

* Create, close, update and search tickets

# Requirements

* EasyVista Service Manager username and password
* EasyVista Service Manager server URL and account

# Supported Product Versions

* EasyVista API v1 2022-05-25

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account|integer|50004|True|Service Manager account used|None|50004|None|None|
|client_login|credential_username_password|None|True|The EasyVista username and password for basic authentication API interaction|None|{"username":"user1", "password":"mypassword"}|None|None|
|url|string|None|True|The full URL for your EasyVista server, e.g. https://example.easyvista.com|None|https://example.easyvista.com|None|None|

Example input:

```
{
  "account": 50004,
  "client_login": {
    "password": "mypassword",
    "username": "user1"
  },
  "url": "https://example.easyvista.com"
}
```

## Technical Details

### Actions


#### Close Ticket

This action is used to close an EasyVista ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|catalog_guid|string|None|False|Identifier of the topic of the ticket. Required if the ticket needs to be requalified before closing|None|44D88612-FEA8-A8F3-6DE8-2E1278ABB02F|None|None|
|comment|string|None|False|Comment that explains why the ticket was closed|None|Ticket closed via InsightConnect|None|None|
|delete_actions|boolean|False|False|Used to indicate the measures to be taken for ongoing actions in the ticket|None|False|None|None|
|end_date|string|None|False|Closing date of open actions associated with the ticket and the anticipated closure action. By default, the current date|None|04/20/2021 12:00:00|None|None|
|rfc_number|string|None|True|Reference number of the ticket to be closed|None|I210412_000001|None|None|
|status_guid|string|None|False|Identifier (GUID) of the final status of the ticket|None|DC97DD1D-0F35-4153-B0E1-0F2E0155365D|None|None|
  
Example input:

```
{
  "catalog_guid": "44D88612-FEA8-A8F3-6DE8-2E1278ABB02F",
  "comment": "Ticket closed via InsightConnect",
  "delete_actions": false,
  "end_date": "04/20/2021 12:00:00",
  "rfc_number": "I210412_000001",
  "status_guid": "DC97DD1D-0F35-4153-B0E1-0F2E0155365D"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|ticket_data|True|Result that includes URL link (HREF) and reference number of the closed ticket|None|
  
Example output:

```
{
  "result": {
    "href_hyperlink": "https://example.easyvista.com/api/v1...",
    "reference_number": "I210409_000006"
  }
}
```

#### Create Ticket

This action is used to create a new EasyVista ticket. The only required input parameter is `catalog`. All other input 
parameters are optional, and you can only provide the ones you need

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|string|None|False|Identifier of the asset|None|123|None|None|
|asset_name|string|None|False|Name of the asset|None|Example asset name|None|None|
|asset_tag|string|None|False|Tag of the asset|None|10564S|None|None|
|catalog|string|None|True|Identifier (GUID) or code for the subject of the ticket|None|44D88612-FEA8-A8F3-6DE8-2E1278ABB02F|None|None|
|ci_asset_tag|string|None|False|Asset tag of the Configuration Item|None|10564S|None|None|
|ci_id|string|None|False|Identifier of the Configuration Item|None|1|None|None|
|ci_name|string|None|False|Name of the Configuration Item|None|SQL-RDB_IT|None|None|
|department_code|string|None|False|Department code of the requestor|None|DEP01|None|None|
|department_id|string|None|False|Department ID of the requestor|None|1|None|None|
|description|string|None|False|Description of the ticket|None|Example ticket description|None|None|
|external_reference|string|None|False|Identifier of the object attributed by an external application|None|external_ref_example|None|None|
|impact_id|string|None|False|Identifier of the impact level|None|2|None|None|
|location_code|string|None|False|Location code of the requestor|None|LOC01|None|None|
|location_id|string|None|False|Location ID of the requestor|None|10|None|None|
|origin|string|None|False|Identifier of the origin|None|Email|None|None|
|parentrequest|string|None|False|Identifier of the related request (parent request) attached to the object|None|5|None|None|
|phone|string|None|False|Phone number of the requestor|None|11111111|None|None|
|recipient_id|string|None|False|Identifier of the recipient|None|1|None|None|
|recipient_identification|string|None|False|Employee number of the recipient|None|12345|None|None|
|recipient_mail|string|None|False|Email address of the recipient|None|user@example.com|None|None|
|recipient_name|string|None|False|Name of the recipient|None|Example Recipient|None|None|
|requestor_identification|string|None|False|Employee number of the requestor|None|12345|None|None|
|requestor_mail|string|None|False|Email address of the requestor|None|user@example.com|None|None|
|requestor_name|string|None|False|Name of the requestor|None|Example Requestor|None|None|
|severity_id|string|None|False|Identifier of the severity level|None|1|None|None|
|submit_date|string|None|False|Creation date of the ticket|None|04/12/2021 2:00:00 pm|None|None|
|title|string|None|False|Title of the ticket|None|Example ticket title|None|None|
|urgency_id|string|None|False|Identifier of the urgency level|None|1|None|None|
  
Example input:

```
{
  "asset_id": 123,
  "asset_name": "Example asset name",
  "asset_tag": "10564S",
  "catalog": "44D88612-FEA8-A8F3-6DE8-2E1278ABB02F",
  "ci_asset_tag": "10564S",
  "ci_id": 1,
  "ci_name": "SQL-RDB_IT",
  "department_code": "DEP01",
  "department_id": 1,
  "description": "Example ticket description",
  "external_reference": "external_ref_example",
  "impact_id": 2,
  "location_code": "LOC01",
  "location_id": 10,
  "origin": "Email",
  "parentrequest": 5,
  "phone": 11111111,
  "recipient_id": 1,
  "recipient_identification": 12345,
  "recipient_mail": "user@example.com",
  "recipient_name": "Example Recipient",
  "requestor_identification": 12345,
  "requestor_mail": "user@example.com",
  "requestor_name": "Example Requestor",
  "severity_id": 1,
  "submit_date": "04/12/2021 2:00:00 pm",
  "title": "Example ticket title",
  "urgency_id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|ticket_data|True|Result that includes URL link (HREF) and reference number of the created ticket|None|
  
Example output:

```
{
  "result": {
    "href_hyperlink": "https://example.easyvista.com/api/v1...",
    "reference_number": "I210412_000001"
  }
}
```

#### Search Tickets
  
This action is used to search for EasyVista tickets. All available search filters can be found 
[here](https://wiki.easyvista.com/xwiki/bin/view/Documentation/REST+API+-+Options+for+Fields#SearchFilterOptions)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|False|Search query. Returns all tickets if left empty|None|rfc_number:I210412_000001|None|None|
  
Example input:

```
{
  "query": "rfc_number:I210412_000001"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|search_ticket_results|True|Search results for the given query|None|
  
Example output:

```
{
  "results": {
    "record_count": "1",
    "records": [
      {
        "COMMENT": {
          "HREF": "https://example.easyvista.com/api/v1..."
        },
        "DEPARTMENT": {
          "DEPARTMENT_LABEL": "",
          "DEPARTMENT_PATH": "",
          "HREF": "https://example.easyvista.com/api/v1...",
          "DEPARTMENT_CODE": "",
          "DEPARTMENT_EN": "-",
          "DEPARTMENT_ID": "5"
        },
        "KNOWNERROR": {
          "KNOWNERROR_PATH": "",
          "KNOWN_PROBLEMS_ID": "",
          "KP_NUMBER": "",
          "QUESTION_EN": ""
        },
        "LOCATION": {
          "LOCATION_CODE": "",
          "LOCATION_EN": "-",
          "LOCATION_ID": "6",
          "LOCATION_PATH": "",
          "CITY": "",
          "HREF": "https://example.easyvista.com/api/v1..."
        },
        "MAX_RESOLUTION_DATE_UT": "",
        "RECIPIENT": {
          "DEPARTMENT_PATH": "",
          "EMPLOYEE_ID": "16",
          "E_MAIL": "user@example.com",
          "LAST_NAME": "employee3",
          "LOCATION_PATH": "",
          "PHONE_NUMBER": " -",
          "BEGIN_OF_CONTRACT": "2021-04-02",
          "CELLULAR_NUMBER": " -"
        },
        "RFC_NUMBER": "I210412_000001",
        "CATALOG_REQUEST": {
          "CATALOG_REQUEST_PATH": "Incidents/Test_Catalog",
          "CODE": "Test1",
          "HREF": "https://example.easyvista.com/api/v1...",
          "SD_CATALOG_ID": "5218",
          "TITLE_EN": "Test_Catalog"
        },
        "HREF": "https://example.easyvista.com/api/v1...",
        "REQUESTOR": {
          "LOCATION_PATH": "",
          "PHONE_NUMBER": " -",
          "BEGIN_OF_CONTRACT": "2021-04-02",
          "CELLULAR_NUMBER": " -",
          "DEPARTMENT_PATH": "",
          "EMPLOYEE_ID": "16",
          "E_MAIL": "user@example.com",
          "LAST_NAME": "employee1"
        },
        "REQUEST_ID": "9",
        "STATUS": {
          "HREF": "https://example.easyvista.com/api/v1...",
          "STATUS_EN": "Closed",
          "STATUS_GUID": "{C3D9DFA7-7A21-46C2-B3A3-8BC50C9FF4F3}",
          "STATUS_ID": "8"
        },
        "SUBMIT_DATE_UT": "2021-04-09T11:29:36.947Z"
      }
    ],
    "total_record_count": "1",
    "HREF": "https://example.easyvista.com/api/v1..."
  }
}
```

#### Update Ticket

This action is used to update an EasyVista ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analytical_charge_id|string|None|False|Analytical charge ID or code|None|132|None|None|
|asset_id|string|None|False|Identifier of the asset|None|123|None|None|
|asset_serial|string|None|False|Serial number of the asset|None|MXRADF|None|None|
|asset_tag|string|None|False|Tag of the asset|None|10564S|None|None|
|ci|string|None|False|Name of the Configuration Item|None|SQL-RDB_IT|None|None|
|ci_id|string|None|False|Identifier of the Configuration Item|None|1|None|None|
|ci_serial|string|None|False|Serial number of the Configuration Item|None|KD78QGJYU|None|None|
|comment|string|None|False|Comment that explains the reason for the update|None|Comment updated via InsightConnect|None|None|
|continuity_plan_id|string|None|False|Continuity plan ID or code|None|CP01|None|None|
|description|string|None|False|Description of the ticket|None|Example description|None|None|
|external_reference|string|None|False|Identifier of the object used by an external application|None|external_ref_example|None|None|
|impact_id|string|None|False|Identifier of the impact level|None|2|None|None|
|known_problems_id|string|None|False|Identifier of the known problems|None|1|None|None|
|net_price_cur_id|string|None|False|Price currency or currency ID|None|EUR|None|None|
|origin_tool_id|string|None|False|Identifier of the origin tool|None|1|None|None|
|owner_id|string|None|False|Identifier of the owner (Employee ID or name)|None|16|None|None|
|owning_group_id|string|None|False|Owning group ID or name|None|Desktop USA|None|None|
|release_id|string|None|False|Release ID or code|None|1|None|None|
|rental_net_price_cur_id|string|None|False|Rental price currency or currency ID|None|EUR|None|None|
|request_origin_id|string|None|False|Request origin name or ID|None|Email|None|None|
|requestor_phone|string|None|False|Phone number of the requestor|None|11111111|None|None|
|rfc_number|string|None|True|Reference number of the ticket to be updated|None|I210412_000001|None|None|
|root_cause_id|string|None|False|Root Cause ID or name|None|Virus|None|None|
|submit_date_ut|string|None|False|Creation date of the ticket|None|4/12/2021 2:00:00 pm|None|None|
|system_id|string|None|False|System ID or name|None|Supervisor|None|None|
|title|string|None|False|Title of the ticket|None|Example ticket title|None|None|
|urgency_id|string|None|False|Identifier of the urgency level|None|1|None|None|
  
Example input:

```
{
  "analytical_charge_id": 132,
  "asset_id": 123,
  "asset_serial": "MXRADF",
  "asset_tag": "10564S",
  "ci": "SQL-RDB_IT",
  "ci_id": 1,
  "ci_serial": "KD78QGJYU",
  "comment": "Comment updated via InsightConnect",
  "continuity_plan_id": "CP01",
  "description": "Example description",
  "external_reference": "external_ref_example",
  "impact_id": 2,
  "known_problems_id": 1,
  "net_price_cur_id": "EUR",
  "origin_tool_id": 1,
  "owner_id": 16,
  "owning_group_id": "Desktop USA",
  "release_id": 1,
  "rental_net_price_cur_id": "EUR",
  "request_origin_id": "Email",
  "requestor_phone": 11111111,
  "rfc_number": "I210412_000001",
  "root_cause_id": "Virus",
  "submit_date_ut": "4/12/2021 2:00:00 pm",
  "system_id": "Supervisor",
  "title": "Example ticket title",
  "urgency_id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|ticket_data|True|Result that includes URL link (HREF) and reference number of the updated ticket|None|
  
Example output:

```
{
  "result": {
    "href_hyperlink": "https://example.easyvista.com/api/v1...",
    "reference_number": "I210412_000001"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**comment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|False|HREF hyperlink|None|
  
**catalog_request**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Catalog Request Path|string|None|False|Catalog request path|None|
|Code|string|None|False|Code|None|
|HREF|string|None|False|HREF hyperlink|None|
|SD Catalog ID|string|None|False|SD catalog ID|None|
|Title EN|string|None|False|Title EN|None|
  
**status**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|False|HREF hyperlink|None|
|Status EN|string|None|False|Status EN|None|
|Status GUID|string|None|False|Status GUID|None|
|Status ID|string|None|False|Status ID|None|
  
**employee**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Begin of Contract|string|None|False|Begin of contract|None|
|Cellular Number|string|None|False|Cellular number|None|
|Department Path|string|None|False|Department path|None|
|Employee ID|string|None|False|Employee ID|None|
|Email|string|None|False|Email|None|
|Last Name|string|None|False|Last name|None|
|Location Path|string|None|False|Location path|None|
|Phone Number|string|None|False|Phone number|None|
  
**location**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|City|string|None|False|City|None|
|HREF|string|None|False|HREF hyperlink|None|
|Location Code|string|None|False|Location code|None|
|Location EN|string|None|False|Location EN|None|
|Location ID|string|None|False|Location ID|None|
|Location Path|string|None|False|Location path|None|
  
**department**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Department Code|string|None|False|Department code|None|
|Department EN|string|None|False|Department EN|None|
|Department ID|string|None|False|Department ID|None|
|Department Label|string|None|False|Department label|None|
|Department Path|string|None|False|Department path|None|
|HREF|string|None|False|HREF hyperlink|None|
  
**known_error**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Known Error Path|string|None|False|Known error path|None|
|Known Problems ID|string|None|False|Known problems ID|None|
|KP Number|string|None|False|KP number|None|
|Question EN|string|None|False|Question EN|None|
  
**record**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Catalog Request|catalog_request|None|False|Catalog request|None|
|Comment|comment|None|False|Comment|None|
|Department|department|None|False|Department|None|
|HREF|string|None|False|HREF hyperlink|None|
|Known Error|known_error|None|False|Known error|None|
|Location|location|None|False|Location|None|
|Max Resolution Date|string|None|False|Max resolution date|None|
|Recipient|employee|None|False|Recipient|None|
|Requestor|employee|None|False|Requestor|None|
|Request ID|string|None|False|Request ID|None|
|RFC Number|string|None|False|RFC number|None|
|Status|status|None|False|Status|None|
|Submit Date|string|None|False|Submit date|None|
  
**search_ticket_results**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|False|HREF hyperlink|None|
|Record Count|string|None|False|Record count|None|
|Records|[]record|None|False|Records|None|
|Total Record Count|string|None|False|Total record count|None|
  
**ticket_data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF Hyperlink|string|None|False|URL link (HREF) to the ticket|None|
|Reference Number|string|None|False|Reference number of the ticket|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.1 - Bumping requirements.txt | SDK bump to 6.2.0
* 2.0.0 - Fix issue where Create Ticket and Update Ticket actions did not work if `impact_id`, `severity_id` and `urgent_id` were given as `0` | Add error handling for invalid inputs
* 1.0.1 - Fix issue where connection test was failing
* 1.0.0 - Initial plugin

# Links

* [EasyVista](https://www.easyvista.com)

## References

* [EasyVista API Docs](https://docs.blinkops.com/docs/integrations/easyvista)