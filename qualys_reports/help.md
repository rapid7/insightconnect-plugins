
# Qualys Reports

## About

Qualys Reports allows managing reports via the Qualys V2 API.

## Actions

### Launch Patch Report

This action is used to launche a patch report.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_group_ids|string|None|False|Comma separated list of asset group IDs|None|
|ips|string|None|False|IPs/ranges on which to include in the report|None|
|output_format|string|None|True|Format in which to generate the report|['pdf', 'online', 'csv']|
|template_id|integer|None|True|Template ID of the report to launch|None|
|title|string|None|True|User defined report title|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the launched report|

Example output:

```
```

### Launch Manual Scan Report

This action is used to launche a manual scan report.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|report_refs|string|None|False|Comma separated list of scan report references to include|None|
|ip_restriction|string|None|False|Certain IPs/ranges to include in the report|None|
|title|string|None|True|User defined report title|None|
|output_format|string|None|True|Format in which to generate the report|['pdf', 'html', 'mht', 'xml', 'csv', 'docx']|
|template_id|integer|None|True|Template ID of the report to launch|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the launched report|

Example output:

```
```

### List

This action is used to list reports.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|expires_before|date|None|False|Filter reports by if they will expire before this time|None|
|user_login|string|None|False|Filter by reports launched by a specific user|None|
|state|string|None|False|Filter by reports with a certain state|['Running', 'Finished', 'Submitted', 'Canceled', 'Errors']|
|id|integer|None|False|Filter by ID of a report that is saved in the Report Share storage space|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reports|[]report|True|List of reports based on criteria in input|

Example output:

```
```

### Launch Compliance Policy Report

This action is used to launche a compliance policy report.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|title|string|None|True|User defined report title|None|
|report_refs|string|None|False|Comma separated list of compliance report references to include|None|
|output_format|string|None|True|Format in which to generate the report|['pdf', 'html', 'mht', 'xml', 'csv']|
|ips|string|None|False|IPs/ranges on which to include in the report|None|
|instance|string|None|False|Specifies a single instance on the selected host|None|
|asset_group_ids|string|None|False|Comma separated list of asset group IDs|None|
|host_id|integer|None|False|Show only results for a single host instance|None|
|template_id|integer|None|True|Template ID of the report to launch|None|
|policy_id|integer|None|True|Policy on which to run the report|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the launched report|

Example output:

```
```

### Launch Remediation Report

This action is used to launche a remediation report.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|assignee_type|string|None|True|Whether the report will include tickets assigned to the current user, or all tickets in the user account|['User', 'All']|
|title|string|None|True|User defined report title|None|
|asset_group_ids|string|None|True|Comma separated list of asset group IDs|None|
|output_format|string|None|True|Format in which to generate the report|['pdf', 'html', 'mht', 'csv']|
|ips|string|None|False|IPs/ranges on which to include in the report|None|
|template_id|integer|None|True|Template ID of the report to launch|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the launched report|

Example output:

```
```

### Launch Compliance Report

This action is used to launche a compliance report.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ips|string|None|False|IPs/ranges on which to include in the report|None|
|title|string|None|True|User defined report title|None|
|report_refs|string|None|False|Comma separated list of compliance report references to include|None|
|output_format|string|None|True|Format in which to generate the report|['pdf', 'html', 'mht']|
|asset_group_ids|string|None|True|Comma separated list of asset group IDs|None|
|template_id|integer|None|True|Template ID of the report to launch|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the launched report|

Example output:

```
```

### Cancel

This action is used to cancel a report.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|ID of the report to cancel|None|

#### Output

This action does not contain any outputs.

### Launch Map Report

This action is used to launch a map report.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Target domain for the map report (do not include www)|None|
|title|string|None|True|User defined report title|None|
|report_refs|string|None|False|Map references (1-2) to include (if 2 separate with comma)|None|
|ip_restriction|string|None|False|Certain IPs/ranges to include in the report|None|
|output_format|string|None|True|Format in which to generate the report|['pdf', 'html', 'mht', 'xml', 'csv']|
|template_id|integer|None|True|Template ID of the report to launch|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the launched report|

Example output:

```
```

### Fetch

This action is used to fetch a report in the format in which it was generated.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_name|string|None|True|What to name the report file when downloading|None|
|id|integer|None|True|ID of the report to fetch|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|file|True|Report in the format in which it was generated|

Example output:

```
```

### Delete

This action is used to delete a report.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|ID of the report to delete|None|

#### Output

This action does not contain any outputs.

## Triggers

There are no triggers associated with this plugin.

## Connection

|Name|Type|Default|Required|Description|
|----|----|-------|--------|-----------|
|Hostname|string|https://qualysapi.qualys.com/|True|Base URL of Qualys API Server for your region|
|credentials|credential_username_password|None|True|Qualys username and password|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Obtain a compliance report

## Versions

* 0.0.1 - Initial plugin
* 1.0.0 - Support web server mode | Update credentials | Semver compliance
* 1.0.1 - Updating to Go SDK 2.6.4
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers

## References

* [Qualys API V2 User Guide](https://www.qualys.com/docs/qualys-api-v2-user-guide.pdf)
