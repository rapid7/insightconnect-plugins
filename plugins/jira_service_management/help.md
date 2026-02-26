# Description

Notify the right people, reduce response time, and avoid alert fatigue with Jira Service Management

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2026-02-25

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hostname|string|None|True|Enter the hostname|None|https://www.google.com/|None|None|
|port|integer|80|True|Enter the port|None|8080|None|None|
|username|string|None|True|Enter the username|None|UserName|None|None|

Example input:

```
{
  "hostname": "https://www.google.com/",
  "port": 80,
  "username": "UserName"
}
```

## Technical Details

### Actions


#### Close Alert

This action is used to close an existing alert from Jira Service Management

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Name to say goodbye to|None|Rapid7Name|None|None|
  
Example input:

```
{
  "name": "Rapid7Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|User generated message|Hello World!|
  
Example output:

```
{
  "message": "Hello World!"
}
```

#### Create Alert

This action is used to creates an alert for Jira Service Management

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Name to say goodbye to|None|Rapid7Name|None|None|
  
Example input:

```
{
  "name": "Rapid7Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|User generated message|Hello World!|
  
Example output:

```
{
  "message": "Hello World!"
}
```

#### Get Alert

This action is used to retrieve alert from Jira Service Management

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Name to say goodbye to|None|Rapid7Name|None|None|
  
Example input:

```
{
  "name": "Rapid7Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|User generated message|Hello World!|
  
Example output:

```
{
  "message": "Hello World!"
}
```

#### Get On-Calls

This action is used to get current on-call participants

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Name to say goodbye to|None|Rapid7Name|None|None|
  
Example input:

```
{
  "name": "Rapid7Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|User generated message|Hello World!|
  
Example output:

```
{
  "message": "Hello World!"
}
```
### Triggers


#### Trigger a New Greeting

This trigger is used to triggers a greeting every interval

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|15|True|How frequently (in seconds) to trigger a greeting|None|20|None|None|
  
Example input:

```
{
  "interval": 15
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|greeting|person|True|The user generated greeting message|Hello World!|
  
Example output:

```
{
  "greeting": "Hello World!"
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**person**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|First Name|string|None|None|None|None|
|Last Name|string|None|None|None|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.0 - Initial plugin

# Links

* [Jira Service Management](https://www.atlassian.com/software/jira/service-management)

## References
  
*This plugin does not contain any references.*