# Description

[Salesforce](https://www.salesforce.com) is a CRM solution that brings together all customer information in a single, integrated platform that enables building a customer-centered business from marketing right through to sales, customer service and business analysis.
The Salesforce plugin allows you to search, update, and manage salesforce records.

This plugin utilizes the [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Name of the Salesforce user|None|
|client_secret|password|None|True|'Consumer Secret' of the connected app|None|
|password|password|None|True|Password of the Salesforce user|None|
|client_id|string|None|True|'Consumer Key' of the connected app|None|
|security_token|password|None|True|Security token of the Salesforce user|None|

## Technical Details

### Actions

#### Advanced Search

This action is used to execute a SOQL (Salesforce Object Query Language) query.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|SOQL query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_results|[]search_result|False|List of search results|

Example output:

```
{
  "search_results": [
    {
      "type": "Account",
      "url": "/services/data/v44.0/sobjects/Account/0011t00000Es5S5AAJ",
      "name": "Express Logistics and Transport"
    },
    {
      "type": "Account",
      "url": "/services/data/v44.0/sobjects/Account/0011t00000Es5S6AAJ",
      "name": "University of Arizona"
    },
    {
      "type": "Account",
      "url": "/services/data/v44.0/sobjects/Account/0011t00000Es5S4AAJ",
      "name": "United Oil & Gas Corp."
    },
    {
      "type": "Account",
      "url": "/services/data/v44.0/sobjects/Account/0011t00000Es5SAAAZ",
      "name": "sForce"
    },
    {
      "type": "Account",
      "url": "/services/data/v44.0/sobjects/Account/0011t00000Es5S3AAJ",
      "name": "Grand Hotels & Resorts Ltd"
    }
  ]
}
```

#### Update Record

This action is used to update a record.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|record_id|string|None|True|The ID of an existing record|None|
|object_name|string|Account|True|The name of the object (e.g. 'Account')|None|
|object_data|object|None|True|Updated SObject information|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was the operation successful|

Example output:

```
{
  "success": true
}
```

#### Get Fields

This action is used to retrieve field values from a record.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|record_id|string|None|True|The ID of an existing record|None|
|fields|[]string|None|True|The fields which values should be retrieved|None|
|object_name|string|Account|True|The name of the object (e.g. 'Account')|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|fields|object|False|An object with field names as keys, each with the corresponding value|

Example output:

```
{
  "fields": {
    "Name": "updated_test_record",
    "Id": "0011t00000FPQVKAA5"
  }
}
```

#### Get Record

This action is used to retrieve a record.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|record_id|string|None|True|The ID of an existing record|None|
|external_id_field_name|string||False|The name of the external ID field that should be matched with record_id. If empty, the 'Id' field of the record is used|None|
|object_name|string|Account|True|The name of the object (e.g. 'Account')|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|record|object|False|Matched record|

Example output:

```
{
  "record": {
    "attributes": {
      "type": "Account",
      "url": "/services/data/v44.0/sobjects/Account/0011t00000FPQVKAA5"
    },
    "Id": "0011t00000FPQVKAA5",
    "IsDeleted": false,
    "MasterRecordId": null,
    "Name": "updated_test_record",
    "Type": null,
    "ParentId": null,
    "BillingStreet": null,
    "BillingCity": null,
    "BillingState": null,
    "BillingPostalCode": null,
    "BillingCountry": null,
    "BillingLatitude": null,
    "BillingLongitude": null,
    "BillingGeocodeAccuracy": null,
    "BillingAddress": null,
    "ShippingStreet": null,
    "ShippingCity": null,
    "ShippingState": null,
    "ShippingPostalCode": null,
    "ShippingCountry": null,
    "ShippingLatitude": null,
    "ShippingLongitude": null,
    "ShippingGeocodeAccuracy": null,
    "ShippingAddress": null,
    "Phone": null,
    "Fax": null,
    "AccountNumber": null,
    "Website": null,
    "PhotoUrl": "/services/images/photo/0011t00000FPQVKAA5",
    "Sic": null,
    "Industry": null,
    "AnnualRevenue": null,
    "NumberOfEmployees": null,
    "Ownership": null,
    "TickerSymbol": null,
    "Description": null,
    "Rating": null,
    "Site": null,
    "OwnerId": "0051t000002aoBsAAI",
    "CreatedDate": "2019-01-14T16:42:40.000+0000",
    "CreatedById": "0051t000002aoBsAAI",
    "LastModifiedDate": "2019-01-14T19:10:13.000+0000",
    "LastModifiedById": "0051t000002aoBsAAI",
    "SystemModstamp": "2019-01-14T19:10:13.000+0000",
    "LastActivityDate": null,
    "LastViewedDate": "2019-01-15T14:19:44.000+0000",
    "LastReferencedDate": "2019-01-15T14:19:44.000+0000",
    "Jigsaw": null,
    "JigsawCompanyId": null,
    "CleanStatus": "Pending",
    "AccountSource": null,
    "DunsNumber": null,
    "Tradestyle": null,
    "NaicsCode": null,
    "NaicsDesc": null,
    "YearStarted": null,
    "SicDesc": null,
    "DandbCompanyId": null,
    "CustomerPriority__c": null,
    "SLA__c": null,
    "Active__c": null,
    "NumberofLocations__c": null,
    "UpsellOpportunity__c": null,
    "SLASerialNumber__c": null,
    "SLAExpirationDate__c": null
  }
}
```

#### Get Blob Data

This action is used to retrieve blob data for a given record.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|record_id|string|None|True|The ID of an existing record|None|
|object_name|string|Attachment|True|The name of the object (e.g. 'Account')|None|
|field_name|string|body|True|Blob field name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|bytes|False|The value of the selected blob field|

Example output:

```
{
  "data": "hello"
}
```

#### Simple Search

This action is used to execute a simple search for a text.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|text|string|None|True|Text to search for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_results|[]search_result|False|List of search results|

Example output:

```
{
  "search_results": [
    {
      "type": "Lead",
      "url": "/services/data/v44.0/sobjects/Lead/00Q1t000002uvSnEAI",
      "id": "00Q1t000002uvSnEAI"
    }
  ]
}
```

#### Create Record

This action is used to create a new SObject record.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|object_name|string|Account|True|The name of the object (e.g. 'Account')|None|
|object_data|object|None|True|SObject information for the newly created record|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|ID of the newly created record|

Example output:

```
{
  "id": "0011t00000FQ0RGAA1"
}
```

#### Delete Record

This action is used to delete a record.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|record_id|string|None|True|The ID of an existing record|None|
|object_name|string|Account|True|The name of the object (e.g. 'Account')|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was the operation successful|

Example output:

```
{
  "success": true
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [Salesforce](https://salesforce.com)
* [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm)
* [Connecting your app to the API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/quickstart.htm)
* [SOQL](https://developer.salesforce.com/docs/atlas.en-us.216.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)

