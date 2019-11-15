# Description

[Cherwell](https://www.cherwell.com/) is a comprehensive service desk verified for eleven ITIL processes.
The Cherwell plugin is used to administrate incidents in Cherwell and leverages the [Cherwell API](https://cherwellsupport.com/CherwellAPI/Documentation/en-US/csm_rest_api.html).

# Key Features

* Manage incidents

# Requirements

* Requires a Client ID, username and password from the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|guideit.cherwellondemand.com|True|Hostname of the Cherwell instance|None|
|authentication_mode|string|Internal|True|Authentication mode. Either Internal, Windows, LDAP, SAML, Auto|['Internal', 'Windows', 'LDAP', 'SAML', 'Auto']|
|username_and_password|credential_username_password|None|True|Cherwell username and password|None|
|client_id|credential_secret_key|None|True|Cherwell Client ID / API Key|None|
|ssl_verify|boolean|None|True|Whether to access the server over HTTPS|None|

## Technical Details

### Actions

#### Lookup Incident

This action is used to lookup an incident, including a list of fields and their record IDs, names, and set values.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|public_id|string|None|True|PublicID of the incident|None|
|business_object_id|string|None|True|BusObjID of the incident|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|raw_response|object|True|The raw JSON returned by the endpoint|
|success|boolean|True|Boolean indicating whether the business object was successfully created|

Example output:

```
{
  "busObId": "string",
  "busObPublicId": "string",
  "busObRecId": "string",
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
  "links": [
    {
      "name": "string",
      "url": "string"
    }
  ],
  "errorCode": "string",
  "errorMessage": "string",
  "hasError": true
}
```

#### Perform Ad Hoc Search

This action is used to run an ad-hoc business object search.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|data_request|object|None|True|Request object to specify search parameters|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_results|object|True|The raw JSON search results returned by the endpoint|

Example output:

```
{
  "businessObjects": [
    {
      "busObId": "string",
      "busObPublicId": "string",
      "busObRecId": "string",
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
      "links": [
        {
          "name": "string",
          "url": "string"
        }
      ],
      "errorCode": "string",
      "errorMessage": "string",
      "hasError": true
    }
  ],
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
      "fieldName": "string",
      "fullFieldId": "string",
      "hasDefaultSortField": true,
      "fieldId": "string",
      "isBinary": true,
      "isCurrency": true,
      "isDateTime": true,
      "isFilterAllowed": true,
      "isLogical": true,
      "isNumber": true,
      "isShortDate": true,
      "isShortTime": true,
      "isVisible": true,
      "sortable": true,
      "sortOrder": "string",
      "storageName": "string",
      "wholeDigits": 0
    }
  ],
  "simpleResults": {
    "groups": [
      {
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
        "title": "string",
        "errorCode": "string",
        "errorMessage": "string",
        "hasError": true
      }
    ],
    "title": "string",
    "errorCode": "string",
    "errorMessage": "string",
    "hasError": true
  },
  "totalRows": 0,
  "errorCode": "string",
  "errorMessage": "string",
  "hasError": true
}
```

#### Create Incident

This action is used to create a Cherwell incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|fields_to_change|object|None|True|A JSON blob of keys and values that are to be replaced in the template e.g. {"Status", "New"} will update the Status field from the templateNone|
|business_object_id|string|None|True|BusObjID of the template to create the incident off of|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|raw_response|object|True|The raw JSON returned by the endpoint|
|success|boolean|True|Boolean indicating whether the business object was successfully created|

Example output:

```
{
  "busObPublicId": "string",
  "busObRecId": "string",
  "cacheKey": "string",
  "fieldValidationErrors": [
    {
      "error": "string",
      "errorCode": "string",
      "fieldId": "string"
    }
  ],
  "notificationTriggers": [
    {
      "sourceType": "string",
      "sourceId": "string",
      "sourceChange": "string",
      "key": "string"
    }
  ],
  "errorCode": "string",
  "errorMessage": "string",
  "hasError": true
}
```

#### Update Incident

This action is used to update an incident within Cherwell.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|business_object_id|string|None|True|Business Object ID of the incident|None|
|public_id|string|None|True|Public ID of the incident|None|
|fields_to_update|object|None|True|A JSON blob of keys and values that are to be updated in the incident e.g. {"Status", "New"} will update the Status field of the incident|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating whether the business object was successfully created|
|raw_response|object|True|The raw JSON returned by the endpoint|

Example output:

```
{
  "success":true,
  "raw_response":{
    "fieldValidationErrors":[],
    "errorMessage":null,
    "errorCode":null,
    "hasError":false,
    "busObPublicId":"762421",
    "busObRecId":"9446e3f047458fd7824f3b400f94be3566ac523802"
  }
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.1.0 - New action Update Incident
* 2.0.1 - Fixes issue where Create Incident was not properly formatting data to be passed to Cherwell
* 2.0.0 - Fixes issue where `client_id` was using the wrong credential type | Update pinned requests version to resolve security vulnerability [CVE-2018-18074](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-18074)
* 1.0.1 - Update vendor and descriptions
* 1.0.0 - Initial plugin

# Links

## References

* [Cherwell API Documentation](https://cherwellsupport.com/CherwellAPI/Documentation/en-US/csm_rest_api.html)

