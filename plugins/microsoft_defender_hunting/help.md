# Description

Manage security incidents with Microsoft Defender 365

# Key Features

Actions:
* Advanced Hunting (Query)

# Requirements

Requires to be set of Azure credentials such as application (client) ID, tenant ID, and client secret key with necessary permissions (Microsoft Threat Protection -> Incident.Read.All, Incident.ReadWrite.ALl, and AdvancedHunting.Read.All) to monitor and run Advanced Hunting query

# Supported Product Versions

* 2022-05-06

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|tenant_id|string|None|True|This is Active Directory ID|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|

Example input:

```
{
  "client_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "client_secret": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "tenant_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

## Technical Details

### Actions

#### Advanced Hunting Query

This action runs advanced hunting query and retrieves the data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Advanced Hunting query to run|None|DeviceInfo I where Timestamp > ago(1h)|

Example input:

```
{
  "query": "DeviceInfo | where Timestamp > ago(1h)"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|columns|[]column|True|Schema containing response column's name and type|
|rows|[]object|True|Array of objects containing query response values with keys as specific column name|

Example output:

```
{
  "columns": [
    {
      "Name": "Timestamp",
      "Type": "DateTime"
    },
    {
      "Name": "FileName",
      "Type": "String"
    },
    {
      "Name": "InitiatingProcessFileName",
      "Type": "String"
    },
    {
      "Name": "DeviceId",
      "Type": "String"
    }
  ],
  "rows": [
    {
      "Timestamp": "2020-02-05T01:10:26.2648757Z",
      "FileName": "csc.exe",
      "InitiatingProcessFileName": "powershell.exe",
      "DeviceId": "10cbf9182d4e95660362f65cfa67c7731f62fdb3"
    },
    {
      "Timestamp": "2020-02-05T01:10:26.5614772Z",
      "FileName": "csc.exe",
      "InitiatingProcessFileName": "powershell.exe",
      "DeviceId": "10cbf9182d4e95660362f65cfa67c7731f62fdb3"
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### column

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Column's name|
|Type|string|False|Column's data type|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin (Actions: Advanced Hunting (Query))

# Links

## References

* [Microsoft Defender Advanced Hunting](https://docs.microsoft.com/en-us/microsoft-365/security/defender/api-advanced-hunting?view=o365-worldwide)

