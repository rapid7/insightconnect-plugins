# Description

Fetch feeds from Luminar Taxii server

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2025-09-10

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_id|string|None|True|Enter the account ID|None|None|None|None|
|client_id|string|None|True|Enter the client ID|None|None|None|None|
|client_secret|credential_secret_key|None|True|Enter the client secret|None|None|None|None|

Example input:

```
{
  "account_id": "",
  "client_id": "",
  "client_secret": {
    "secretKey": ""
  }
}
```

## Technical Details

### Actions
  
*This plugin does not contain any actions.*
### Triggers


#### Get Cyberfeed feeds

This trigger is used to trigger workflows to get cyberfeeds from Luminar

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|300|False|Poll frequency in seconds|None|300|None|None|
|initial_fetch_date|string|None|True|The date from which the initial fetch will start. eg YYYY-MM-DD|None|2025-01-01|None|None|
  
Example input:

```
{
  "frequency": 300,
  "initial_fetch_date": "2025-01-01"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]results|True|cyber feed results|None|
  
Example output:

```
{
  "results": [
    {
      "Comment Count": 0
    }
  ]
}
```

#### Get IOC feeds

This trigger is used to trigger workflows to get IOC feeds from Luminar

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|300|False|Poll frequency in seconds|None|300|None|None|
|initial_fetch_date|string|None|True|The date from which the initial fetch will start. eg YYYY-MM-DD|None|2025-01-01|None|None|
  
Example input:

```
{
  "frequency": 300,
  "initial_fetch_date": "2025-01-01"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]results|True|IOC feed results|None|
  
Example output:

```
{
  "results": [
    {
      "Comment Count": 0
    }
  ]
}
```

#### Get Leaked Records feeds

This trigger is used to trigger workflows to get leaked records feeds from Luminar

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|300|False|Poll frequency in seconds|None|300|None|None|
|initial_fetch_date|string|None|True|The date from which the initial fetch will start. eg YYYY-MM-DD|None|2025-01-01|None|None|
  
Example input:

```
{
  "frequency": 300,
  "initial_fetch_date": "2025-01-01"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]results|True|leaked records feed results|None|
  
Example output:

```
{
  "results": [
    {
      "Comment Count": 0
    }
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**results**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment Count|integer|None|False|Comment count|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History
  
*This plugin does not contain a version history.*

# Links
  
*This plugin does not contain any links.*

## References
  
*This plugin does not contain any references.*