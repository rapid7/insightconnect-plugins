# Microsoft Office365 Email Security

## About

[Microsoft Office365](https://www.office.com/) is a complete, intelligent solution, powered by Office 365 and Windows 10, allowing you to empower your team, safeguard your business, and simplify IT management.

This plugin adds utilities to help administrators manage their Office 365 instances.

## Actions

### Block Sender Transport Rule

This action is used to add a domain or email address to a blocking transport rule in Exchange Admin Center.

In the Office 365 cloud, transport rules are limited to 8k of data or roughly 8100 characters. This is roughly 400 email address. If a new email address is added that would break that limit, the oldest email address(es) in the current rule will be deleted to make room.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain_or_email_to_block|string|None|True|Domain or email address to block|None|
|transport_rule_name|string|InsightConnect Block List|True|Transport rule name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|True|Result|

Example output:

```
{
    "result": "Success"
}
```

### Email Compliance Search

This action is used to create a compliance search for a provided email.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|compliance_search_name|string|None|True|Name of compliance search|None|
|content_match_query|string|None|True|This parameter uses a text search string or a query that's formatted by using the Keyword Query Language (KQL). For more information about KQL, see Keyword Query Language syntax reference (https://go.microsoft.com/fwlink/p/?linkid=269603)|None|
|query_timeout|integer|60|False|Query timeout in minutes|None|
|users|[]string|True|Email address of all affected users|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected_users|integer|True|Number of affected users|
|emails_found|integer|True|Emails found that matched|

Example output:

```
{
  "affected_users": 1,
  "emails_found": 4,
  "users": ["userA@company.com", "userB@company.com"]
}
```

### Email Compliance Purge

This action is used to purge a provided email.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|compliance_search_name|string|None|True|Name of compliance search|None|
|query_timeout|integer|60|False|Query timeout in minutes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
    "result": "Success"
}
```

### Email Compliance Search and Purge

This action is used to execute a search and purge for a provided email.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|compliance_search_name|string|None|True|Name of compliance search|None|
|content_match_query|string|None|True|This parameter uses a text search string or a query that's formatted by using the Keyword Query Language (KQL). For more information about KQL, see Keyword Query Language syntax reference (https://go.microsoft.com/fwlink/p/?linkid=269603)|None|
|delete_items|boolean|False|False|The script only executes the delete action if this parameter is true|None|
|query_timeout|integer|60|False|Query timeout in minutes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
    "result": "Success"
}
```

### Message Trace

This action is used to run a message trace.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Sender_address|string|None|True|Sender address|None|
|end_date|string|None|True|End date in format MM/DD/YYYY e.g. 09/27/2019|None|
|start_date|string|None|True|Start date in format MM/DD/YYYY e.g. 09/27/2019|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message_traces|[]message_trace|True|Success|

Example output:

```
[
  {
    "PSComputerName": "outlook.office365.com",
    "RunspaceId": "eb0ea814-0c3d-45eb-a189-f41118e8582d",
    "PSShowComputerName": false,
    "Organization": "things.com",
    "MessageId": "<***********************.namprd12.prod.outlook.com>",
    "Received": "2019-09-24T14:18:57.4237718",
    "SenderAddress": "a_compny@things.com",
    "RecipientAddress": "a_compny@things.com",
    "Subject": "Android Update 5.2.1",
    "Status": "Delivered",
    "ToIP": null,
    "FromIP": "216.93.244.203",
    "Size": 15846,
    "MessageTraceId": "d7b67cd8-a69c-46e5-8816-08d740fa2349",
    "StartDate": "2019-09-20T00:00:00",
    "EndDate": "2019-09-25T00:00:00",
    "Index": 0
  }
]
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Username and password|None|
|office_365_url|string|https://ps.compliance.protection.outlook.com/powershell-liveid/|False|This parameter sets the location of the Office 365 or on-premise exchange server from which to execute the compliance actions E.G. https://management.exchangelabs.com/Management|None|

## Troubleshooting

Queries are expected to be wrapped in quotes e.g. subject:"a subject"

## Workflows

Examples:

* Block an email or domain for an organization

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Fix issue where plugin would fail when creating transport rule on first run
* 2.0.0 - New actions Mass Search, Purge and combined Search and Purge
* 2.1.0 - Add user email address array to Search action
* 2.2.0 - New action Message Trace

## References

* [Microsoft Office365](https://www.office.com/)
* [Transport Rule Limits](https://docs.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits#journal-transport-and-inbox-rule-limits)
* [New-TransportRule](https://docs.microsoft.com/en-us/powershell/module/exchange/policy-and-compliance/new-transportrule?view=exchange-ps)
* [Set-TransportRule](https://docs.microsoft.com/en-us/powershell/module/exchange/policy-and-compliance/set-transportrule?view=exchange-ps)

## Custom Output Types

_This plugin does not contain any custom output types._
