# Description
  
Random plugin  

# Key Features
  

# Requirements
  

# Supported Product Versions
  
* 1.0.0  

# Documentation

## Setup
  
*This plugin does not contain a connection.*  

## Technical Details

### Actions
  

#### Random Choice
  
Chooses a random item from a list  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|list|[]string|None|False|blah|None|['1', '2', 'word', 'string']|
  
Example input:

```
{
  "list": 1
}
```  

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|result|string|None|True|blah|None|None|
  
Example output:

```
{
  "result": ""
}
```  

#### Random Float
  
Returns a random float between the given range  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|start_range|integer|0|True|blah|None|20|
|stop_range|integer|1|True|blah|None|60|
  
Example input:

```
{
  "start_range": 0,
  "stop_range": 1
}
```  

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|result|float|None|True|blah|None|33.33|
  
Example output:

```
{
  "result": 33.33
}
```  

#### Random Range
  
Returns a random number between the given range  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|start_range|integer|None|True|blah|None|1|
|stop_range|integer|None|True|blah|None|1000|
  
Example input:

```
{
  "start_range": 1,
  "stop_range": 1000
}
```  

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|result|integer|None|True|blah|None|15|
  
Example output:

```
{
  "result": 15
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*  

### Custom Types
  
*This plugin does not contain any custom output types.*  

## Troubleshooting
  
*There is no troubleshooting for this plugin.*  

# Version History
  

# Links
  

## References
