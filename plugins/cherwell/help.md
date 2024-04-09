# Description

The Cherwell plugin is used to administrate incidents in Cherwell

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 22-03-2024

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|authentication_mode|string|Internal|True|Authentication mode. Either Internal, Windows, LDAP, SAML, Auto|["Internal", "Windows", "LDAP", "SAML", "Auto"]|Internal|
|client_id|credential_secret_key|None|True|Cherwell Client ID / API Key|None|a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99|
|ssl_verify|boolean|None|True|Whether to access the server over HTTPS|None|True|
|url|string|https://guideit.cherwellondemand.com|True|Protocol and hostname of the Cherwell instance. HTTPS is recommended to ensure security and avoid connection errors|None|https://guideit.cherwellondemand.com|
|username_and_password|credential_username_password|None|True|Cherwell username and password|None|{"username": "user@example.com", "password": "mypassword"}|

Example input:

```
{
  "authentication_mode": "Internal",
  "client_id": "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99",
  "ssl_verify": true,
  "url": "https://guideit.cherwellondemand.com",
  "username_and_password": {
    "password": "mypassword",
    "username": "user@example.com"
  }
}
```

## Technical Details

### Actions


#### Create Incident

This action is used to create a Cherwell incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|business_object_id|string|None|True|BusObjID of the template to create the incident from|None|7cc53665c0c24cab86870a21cf6434cc|
|fields_to_change|object|None|True|A JSON blob of keys and values that are to be replaced in the template e.g. {"Status": "New"} will update the Status field from the template|None|{'Status': 'New'}|
  
Example input:

```
{
  "business_object_id": "7cc53665c0c24cab86870a21cf6434cc",
  "fields_to_change": {
    "Status": "New"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|raw_response|object|False|The raw JSON returned by the endpoint|{'busObPublicId': 'string', 'busObRecId': 'string', 'cacheKey': 'string', 'fieldValidationErrors': [{'error': 'string', 'errorCode': 'string', 'fieldId': 'string'}], 'notificationTriggers': [{'sourceType': 'string', 'sourceId': 'string', 'sourceChange': 'string', 'key': 'string'}], 'errorCode': 'string', 'errorMessage': 'string', 'hasError': True}|
|success|boolean|False|Boolean indicating whether the business object was successfully created|True|
  
Example output:

```
{
  "raw_response": {
    "busObPublicId": "string",
    "busObRecId": "string",
    "cacheKey": "string",
    "errorCode": "string",
    "errorMessage": "string",
    "fieldValidationErrors": [
      {
        "error": "string",
        "errorCode": "string",
        "fieldId": "string"
      }
    ],
    "hasError": true,
    "notificationTriggers": [
      {
        "key": "string",
        "sourceChange": "string",
        "sourceId": "string",
        "sourceType": "string"
      }
    ]
  },
  "success": true
}
```

#### Lookup Incident

This action is used to lookup that returns an incident that includes a list of fields and their record IDs, names, and 
set values

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|business_object_id|string|None|True|BusObjID of the incident|None|7cc53665c0c24cab86870a21cf6434cc|
|public_id|string|None|True|Public ID of the incident|None|7cc53665c0c24cab86870a21cf6434cc|
  
Example input:

```
{
  "business_object_id": "7cc53665c0c24cab86870a21cf6434cc",
  "public_id": "7cc53665c0c24cab86870a21cf6434cc"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|raw_response|object|False|The raw JSON returned by the endpoint|{'busObId': 'string', 'busObPublicId': 'string', 'busObRecId': 'string', 'fields': [{'dirty': True, 'displayName': 'string', 'fieldId': 'string', 'html': 'string', 'name': 'string', 'value': 'string'}], 'links': [{'name': 'string', 'url': 'string'}], 'errorCode': 'string', 'errorMessage': 'string', 'hasError': True}|
|success|boolean|False|Boolean indicating whether the business object was successfully created|True|
  
Example output:

```
{
  "raw_response": {
    "busObId": "string",
    "busObPublicId": "string",
    "busObRecId": "string",
    "errorCode": "string",
    "errorMessage": "string",
    "fields": [
      {
        "dirty": true,
        "displayName": "string",
        "fieldId": "string",
        "html": "string",
        "name": "string",
        "value": "string"
      }
    ],
    "hasError": true,
    "links": [
      {
        "name": "string",
        "url": "string"
      }
    ]
  },
  "success": true
}
```

#### Perform Ad Hoc Search

This action is used to runs an ad-hoc Business Object search. To execute a search with Prompts, the PromptId and Value 
are required in the data request object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|data_request|object|None|True|Request object to specify search parameters|None|{'busObId': '7cc53665c0c24cab86870a21cf6434cc', 'filters': [{'fieldId': '5eb3234ae1344c64a19819eda437f18d', 'operator': 'equals', 'value': 'open'}], 'sorting': [{'fieldId': '5eb3234ae1344c64a19819eda437f18d', 'sortDirection': 0}]}|
  
Example input:

```
{
  "data_request": {
    "busObId": "7cc53665c0c24cab86870a21cf6434cc",
    "filters": [
      {
        "fieldId": "5eb3234ae1344c64a19819eda437f18d",
        "operator": "equals",
        "value": "open"
      }
    ],
    "sorting": [
      {
        "fieldId": "5eb3234ae1344c64a19819eda437f18d",
        "sortDirection": 0
      }
    ]
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|search_results|object|False|The raw JSON search results returned by the endpoint|{'businessObjects': [{'busObId': 'string', 'busObPublicId': 'string', 'busObRecId': 'string', 'fields': [{'dirty': True, 'displayName': 'string', 'fieldId': 'string', 'html': 'string', 'name': 'string', 'value': 'string'}], 'links': [{'name': 'string', 'url': 'string'}], 'errorCode': 'string', 'errorMessage': 'string', 'hasError': True}], 'hasPrompts': True, 'links': [{'name': 'string', 'url': 'string'}], 'prompts': [{'allowValuesOnly': True, 'busObId': 'string', 'collectionStoreEntireRow': 'string', 'collectionValueField': 'string', 'constraintXml': 'string', 'contents': 'string', 'default': 'string', 'fieldId': 'string', 'isDateRange': True, 'listDisplayOption': 'Auto', 'listReturnFieldId': 'string', 'multiLine': True, 'promptId': 'string', 'promptType': 'None', 'promptTypeName': 'string', 'required': True, 'text': 'string', 'value': {}, 'values': ['string']}], 'searchResultsFields': [{'caption': 'string', 'currencyCulture': 'string', 'currencySymbol': 'string', 'decimalDigits': 0, 'defaultSortOrderAscending': True, 'displayName': 'string', 'fieldName': 'string', 'fullFieldId': 'string', 'hasDefaultSortField': True, 'fieldId': 'string', 'isBinary': True, 'isCurrency': True, 'isDateTime': True, 'isFilterAllowed': True, 'isLogical': True, 'isNumber': True, 'isShortDate': True, 'isShortTime': True, 'isVisible': True, 'sortable': True, 'sortOrder': 'string', 'storageName': 'string', 'wholeDigits': 0}], 'simpleResults': {'groups': [{'isBusObTarget': True, 'simpleResultsListItems': [{'busObId': 'string', 'busObRecId': 'string', 'docRepositoryItemId': 'string', 'galleryImage': 'string', 'links': [{'name': 'string', 'url': 'string'}], 'publicId': 'string', 'scope': 'string', 'scopeOwner': 'string', 'subTitle': 'string', 'text': 'string', 'title': 'string'}], 'subTitle': 'string', 'targetId': 'string', 'title': 'string', 'errorCode': 'string', 'errorMessage': 'string', 'hasError': True}], 'title': 'string', 'errorCode': 'string', 'errorMessage': 'string', 'hasError': True}, 'totalRows': 0, 'errorCode': 'string', 'errorMessage': 'string', 'hasError': True}|
  
Example output:

```
{
  "search_results": {
    "businessObjects": [
      {
        "busObId": "string",
        "busObPublicId": "string",
        "busObRecId": "string",
        "errorCode": "string",
        "errorMessage": "string",
        "fields": [
          {
            "dirty": true,
            "displayName": "string",
            "fieldId": "string",
            "html": "string",
            "name": "string",
            "value": "string"
          }
        ],
        "hasError": true,
        "links": [
          {
            "name": "string",
            "url": "string"
          }
        ]
      }
    ],
    "errorCode": "string",
    "errorMessage": "string",
    "hasError": true,
    "hasPrompts": true,
    "links": [
      {
        "name": "string",
        "url": "string"
      }
    ],
    "prompts": [
      {
        "allowValuesOnly": true,
        "busObId": "string",
        "collectionStoreEntireRow": "string",
        "collectionValueField": "string",
        "constraintXml": "string",
        "contents": "string",
        "default": "string",
        "fieldId": "string",
        "isDateRange": true,
        "listDisplayOption": "Auto",
        "listReturnFieldId": "string",
        "multiLine": true,
        "promptId": "string",
        "promptType": "None",
        "promptTypeName": "string",
        "required": true,
        "text": "string",
        "value": {},
        "values": [
          "string"
        ]
      }
    ],
    "searchResultsFields": [
      {
        "caption": "string",
        "currencyCulture": "string",
        "currencySymbol": "string",
        "decimalDigits": 0,
        "defaultSortOrderAscending": true,
        "displayName": "string",
        "fieldId": "string",
        "fieldName": "string",
        "fullFieldId": "string",
        "hasDefaultSortField": true,
        "isBinary": true,
        "isCurrency": true,
        "isDateTime": true,
        "isFilterAllowed": true,
        "isLogical": true,
        "isNumber": true,
        "isShortDate": true,
        "isShortTime": true,
        "isVisible": true,
        "sortOrder": "string",
        "sortable": true,
        "storageName": "string",
        "wholeDigits": 0
      }
    ],
    "simpleResults": {
      "errorCode": "string",
      "errorMessage": "string",
      "groups": [
        {
          "errorCode": "string",
          "errorMessage": "string",
          "hasError": true,
          "isBusObTarget": true,
          "simpleResultsListItems": [
            {
              "busObId": "string",
              "busObRecId": "string",
              "docRepositoryItemId": "string",
              "galleryImage": "string",
              "links": [
                {
                  "name": "string",
                  "url": "string"
                }
              ],
              "publicId": "string",
              "scope": "string",
              "scopeOwner": "string",
              "subTitle": "string",
              "text": "string",
              "title": "string"
            }
          ],
          "subTitle": "string",
          "targetId": "string",
          "title": "string"
        }
      ],
      "hasError": true,
      "title": "string"
    },
    "totalRows": 0
  }
}
```

#### Update Incident

This action is used to updates an incident within Cherwell

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|business_object_id|string|None|True|Business Object ID of the incident|None|7cc53665c0c24cab86870a21cf6434cc|
|fields_to_update|object|None|True|A JSON blob of keys and values that are to be updated in the incident e.g. {"Status", "New"} will update the Status field of the incident|None|{'Status': 'New'}|
|public_id|string|None|True|Public ID of the incident|None|7cc53665c0c24cab86870a21cf6434cc|
  
Example input:

```
{
  "business_object_id": "7cc53665c0c24cab86870a21cf6434cc",
  "fields_to_update": {
    "Status": "New"
  },
  "public_id": "7cc53665c0c24cab86870a21cf6434cc"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|raw_response|object|False|The raw JSON returned by the endpoint|{'fieldValidationErrors': [], 'errorMessage': None, 'errorCode': None, 'hasError': False, 'busObPublicId': '762421', 'busObRecId': '9446e3f047458fd7824f3b400f94be3566ac523802'}|
|success|boolean|False|Boolean indicating whether the business object was successfully created|True|
  
Example output:

```
{
  "raw_response": {
    "busObPublicId": "762421",
    "busObRecId": "9446e3f047458fd7824f3b400f94be3566ac523802",
    "errorCode": null,
    "errorMessage": null,
    "fieldValidationErrors": [],
    "hasError": false
  },
  "success": true
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
  
*This plugin does not contain a version history.*

# Links
  
*This plugin does not contain any links.*

## References
  
*This plugin does not contain any references.*