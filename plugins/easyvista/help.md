# Description

EasyVista Service Manager platform supports even the most complex requirements, while bringing a new level of simplicity, agility, and mobility required to make cloud based IT Service Management (ITSM) software easy to use and easy to deliver. Using the EasyVista plugin for Rapid7 InsightConnect, users can manage the creation, update, search and closure of incident, service request, problem or event tickets

# Key Features

* Create, close, update and search tickets

# Requirements

* EasyVista Service Manager username and password
* EasyVista Service Manager server URL and account

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account|integer|50004|True|Service Manager account used|None|50004|
|client_login|credential_username_password|None|True|The EasyVista username and password for basic authentication API interaction|None|{"username":"user1", "password":"mypassword"}|
|url|string|None|True|The full URL for your EasyVista server, e.g. https://example.easyvista.com|None|https://example.easyvista.com|

Example input:

```
{
  "account": 50004,
  "client_login": {
    "username": "user1",
    "password": "mypassword"
  },
  "url": "https://example.easyvista.com"
}
```

## Technical Details

### Actions

#### Search Tickets

This action is used to search for EasyVista tickets. All available search filters can be found [here](https://wiki.easyvista.com/xwiki/bin/view/Documentation/REST+API+-+Options+for+Fields#SearchFilterOptions).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|False|Search query. Returns all tickets if left empty|None|rfc_number:I210412_000001|

Example input:

```
{
  "query": "rfc_number:I210412_000001"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|search_ticket_results|True|Search results for the given query|

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
      },
    ],
    "total_record_count": "1",
    "HREF": "https://example.easyvista.com/api/v1..."
  }
}
```

#### Close Ticket

This action is used to close an EasyVista ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|catalog_guid|string|None|False|Identifier of the topic of the ticket. Required if the ticket needs to be requalified before closing|None|44D88612-FEA8-A8F3-6DE8-2E1278ABB02F|
|comment|string|None|False|Comment that explains why the ticket was closed|None|Ticket closed via InsightConnect|
|delete_actions|boolean|False|False|Used to indicate the measures to be taken for ongoing actions in the ticket|None|False|
|end_date|string|None|False|Closing date of open actions associated with the ticket and the anticipated closure action. By default, the current date|None|04/20/2021 12:00:00|
|rfc_number|string|None|True|Reference number of the ticket to be closed|None|I210412_000001|
|status_guid|string|None|False|Identifier (GUID) of the final status of the ticket|None|DC97DD1D-0F35-4153-B0E1-0F2E0155365D|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|ticket_data|True|Result that includes URL link (HREF) and reference number of the closed ticket|

Example output:

```
{
  "result": {
    "href_hyperlink": "https://example.easyvista.com/api/v1...",
    "reference_number": "I210409_000006"
  }
}
```

#### Update Ticket

This action is used to update an EasyVista ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analytical_charge_id|string|None|False|Analytical charge ID or code|None|132|
|asset_id|string|None|False|Identifier of the asset|None|123|
|asset_serial|string|None|False|Serial number of the asset|None|MXRADF|
|asset_tag|string|None|False|Tag of the asset|None|10564S|
|ci|string|None|False|Name of the Configuration Item|None|SQL-RDB_IT|
|ci_id|integer|None|False|Identifier of the Configuration Item|None|1|
|ci_serial|string|None|False|Serial number of the Configuration Item|None|KD78QGJYU|
|comment|string|None|False|Comment that explains the reason for the update|None|Comment updated via InsightConnect|
|continuity_plan_id|string|None|False|Continuity plan ID or code|None|CP01|
|description|string|None|False|Description of the ticket|None|Example description|
|external_reference|string|None|False|Identifier of the object used by an external application|None|external_ref_example|
|impact_id|integer|None|False|Identifier of the impact level|None|2|
|known_problems_id|integer|None|False|Identifier of the known problems|None|1|
|net_price_cur_id|string|None|False|Price currency or currency ID|None|EUR|
|origin_tool_id|string|None|False|Identifier of the origin tool|None|1|
|owner_id|string|None|False|Identifier of the owner (Employee ID or name)|None|16|
|owning_group_id|string|None|False|Owning group ID or name|None|Desktop USA|
|release_id|string|None|False|Release ID or code|None|1|
|rental_net_price_cur_id|string|None|False|Rental price currency or currency ID|None|EUR|
|request_origin_id|string|None|False|Request origin name or ID|None|Email|
|requestor_phone|string|None|False|Phone number of the requestor|None|11111111|
|rfc_number|string|None|True|Reference number of the ticket to be updated|None|I210412_000001|
|root_cause_id|string|None|False|Root Cause ID or name|None|Virus|
|submit_date_ut|string|None|False|Creation date of the ticket|None|4/12/2021 2:00:00 pm|
|system_id|string|None|False|System ID or name|None|Supervisor|
|title|string|None|False|Title of the ticket|None|Example ticket title|
|urgency_id|integer|None|False|Identifier of the urgency level|None|1|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|ticket_data|True|Result that includes URL link (HREF) and reference number of the updated ticket|

Example output:

```
{
  "result": {
    "href_hyperlink": "https://example.easyvista.com/api/v1...",
    "reference_number": "I210412_000001"
  }
}
```

#### Create Ticket

This action is used to create a new EasyVista ticket. The only required input parameter is `catalog`. All other input parameters are optional, and you can only provide the ones you need.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|asset_id|string|None|False|Identifier of the asset|None|123|
|asset_name|string|None|False|Name of the asset|None|Example asset name|
|asset_tag|string|None|False|Tag of the asset|None|10564S|
|catalog|string|None|True|Identifier (GUID) or code for the subject of the ticket|None|44D88612-FEA8-A8F3-6DE8-2E1278ABB02F|
|ci_asset_tag|string|None|False|Asset tag of the Configuration Item|None|10564S|
|ci_id|string|None|False|Identifier of the Configuration Item|None|1|
|ci_name|string|None|False|Name of the Configuration Item|None|SQL-RDB_IT|
|department_code|string|None|False|Department code of the requestor|None|DEP01|
|department_id|string|None|False|Department ID of the requestor|None|1|
|description|string|None|False|Description of the ticket|None|Example ticket description|
|external_reference|string|None|False|Identifier of the object attributed by an external application|None|external_ref_example|
|impact_id|integer|None|False|Identifier of the impact level|None|2|
|location_code|string|None|False|Location code of the requestor|None|LOC01|
|location_id|string|None|False|Location ID of the requestor|None|10|
|origin|string|None|False|Identifier of the origin|None|Email|
|parentrequest|string|None|False|Identifier of the related request (parent request) attached to the object|None|5|
|phone|string|None|False|Phone number of the requestor|None|11111111|
|recipient_id|string|None|False|Identifier of the recipient|None|1|
|recipient_identification|string|None|False|Employee number of the recipient|None|12345|
|recipient_mail|string|None|False|Email address of the recipient|None|user@example.com|
|recipient_name|string|None|False|Name of the recipient|None|Example Recipient|
|requestor_identification|string|None|False|Employee number of the requestor|None|12345|
|requestor_mail|string|None|False|Email address of the requestor|None|user@example.com|
|requestor_name|string|None|False|Name of the requestor|None|Example Requestor|
|severity_id|integer|None|False|Identifier of the severity level|None|1|
|submit_date|string|None|False|Creation date of the ticket|None|04/12/2021 2:00:00 pm|
|title|string|None|False|Title of the ticket|None|Example ticket title|
|urgency_id|integer|None|False|Identifier of the urgency level|None|1|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|ticket_data|True|Result that includes URL link (HREF) and reference number of the created ticket|

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

_This plugin does not contain any triggers._

### Custom Output Types

#### catalog_request

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Catalog Request Path|string|False|Catalog request path|
|Code|string|False|Code|
|HREF|string|False|HREF hyperlink|
|SD Catalog ID|string|False|SD catalog ID|
|Title EN|string|False|Title EN|

#### comment

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HREF|string|False|HREF hyperlink|

#### department

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Department Code|string|False|Department code|
|Department EN|string|False|Department EN|
|Department ID|string|False|Department ID|
|Department Label|string|False|Department label|
|Department Path|string|False|Department path|
|HREF|string|False|HREF hyperlink|

#### employee

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Begin of Contract|string|False|Begin of contract|
|Cellular Number|string|False|Cellular number|
|Department Path|string|False|Department path|
|Employee ID|string|False|Employee ID|
|Email|string|False|Email|
|Last Name|string|False|Last name|
|Location Path|string|False|Location path|
|Phone Number|string|False|Phone number|

#### known_error

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Known Error Path|string|False|Known error path|
|Known Problems ID|string|False|Known problems ID|
|KP Number|string|False|KP number|
|Question EN|string|False|Question EN|

#### location

|Name|Type|Required|Description|
|----|----|--------|-----------|
|City|string|False|City|
|HREF|string|False|HREF hyperlink|
|Location Code|string|False|Location code|
|Location EN|string|False|Location EN|
|Location ID|string|False|Location ID|
|Location Path|string|False|Location path|

#### record

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Catalog Request|catalog_request|False|Catalog request|
|Comment|comment|False|Comment|
|Department|department|False|Department|
|HREF|string|False|HREF hyperlink|
|Known Error|known_error|False|Known error|
|Location|location|False|Location|
|Max Resolution Date|string|False|Max resolution date|
|Recipient|employee|False|Recipient|
|Requestor|employee|False|Requestor|
|Request ID|string|False|Request ID|
|RFC Number|string|False|RFC number|
|Status|status|False|Status|
|Submit Date|string|False|Submit date|

#### search_ticket_results

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HREF|string|False|HREF hyperlink|
|Record Count|string|False|Record count|
|Records|[]record|False|Records|
|Total Record Count|string|False|Total record count|

#### status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HREF|string|False|HREF hyperlink|
|Status EN|string|False|Status EN|
|Status GUID|string|False|Status GUID|
|Status ID|string|False|Status ID|

#### ticket_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HREF Hyperlink|string|False|URL link (HREF) to the ticket|
|Reference Number|string|False|Reference number of the ticket|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - Fix issue where connection test was failing
* 1.0.0 - Initial plugin

# Links

## References

* [EasyVista](https://www.easyvista.com)
