# Description

[Salesforce](https://www.salesforce.com) is a CRM solution that brings together all customer information in a single, integrated platform that enables building a customer-centered business from marketing right through to sales, customer service and business analysis.
The Salesforce plugin allows you to search, update, and manage salesforce records.

This plugin utilizes the [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm).

# Key Features

* Search records
* Get records
* Create records
* Update records
* Delete records
* Get record fields
* Get blob data for a given record

# Requirements

* Salesforce username, password and security token
* Consumer Key and Secret of the connected app

# Supported Product Versions

* Salesforce API v58 2023-06-30

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|clientId|string|None|True|Consumer Key of the connected app|None|1234567890aBcdEFRoeRxDE1234567890abCDef6Etz7VLwwLQZn19jyW3U_1234567890AbcdEF4VkuMS4ze|
|clientSecret|credential_secret_key|None|True|Consumer Secret of the connected app|None|30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050|
|salesforceAccountUsernameAndPassword|credential_username_password|None|True|Name and password of the Salesforce user|None|{"username": "user@example.com", "password": "password"}|
|securityToken|credential_secret_key|None|True|Security token of the Salesforce user|None|Ier6YY78KxJwKtHy7HeK0oPc|

Example input:

```
{
  "clientId": "1234567890aBcdEFRoeRxDE1234567890abCDef6Etz7VLwwLQZn19jyW3U_1234567890AbcdEF4VkuMS4ze",
  "clientSecret": "1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
  "salesforceAccountUsernameAndPassword": {
    "username": "user@example.com",
    "password": "password"
  },
  "securityToken": "Ier6YY78KxJwKtHy7HeK0oPc"
}
```

## Technical Details

### Actions

#### Advanced Search

This action is used to execute a SOQL (Salesforce Object Query Language) query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|SOQL query|None|SELECT FIELDS(STANDARD) FROM Account WHERE Name='Example Account'|

Example input:

```
{
  "query": "SELECT FIELDS(STANDARD) FROM Account WHERE Name='Example Account'"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|searchResults|[]searchResult|False|List of search results|[]|

Example output:

```
{
  "search_results": [
    {
      "type": "Account",
      "url": "/services/data/v58.0/sobjects/Account/001Hn00001uLl12aBC",
      "name": "Example Account",
      "id": "001Hn00001uLl12aBC"
    }
  ]
}
```

#### Update Record

This action is used to update a record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|objectData|object|None|True|Updated SObject information|None|{"name": "example-name"}|
|objectName|string|Account|True|The name of the object (e.g. 'Account')|None|Account|
|recordId|string|None|True|The ID of an existing record|None|000AA000000aa0aAAA|

Example input:
```
{
  "objectData": {
    "name": "example-name"
  },
  "objectName": "Account",
  "recordId": "000AA000000aa0aAAA"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|Was the operation successful|True|

Example output:

```
{
  "success": true
}
```

#### Get Fields

This action is used to retrieve field values from a record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|[]string|None|True|The fields which values should be retrieved|None|["Id", "Name", "Description"]|
|objectName|string|Account|True|The name of the object (e.g. 'Account')|None|Account|
|recordId|string|None|True|The ID of an existing record|None|001Hn00001uAJRtaB3|

Example input:

```
{
  "fields": [
    "Id",
    "Name",
    "Description"
  ],
  "objectName": "Account",
  "recordId": "001Hn00001uAJRtaB3"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|fields|object|False|An object with field names as keys, each with the corresponding value|{}|

Example output:

```
{
  "fields": {
    "id": "001Hn00001uAJRtaB3",
    "name": "Example Account",
    "description": "Example description"
  }
}
```

#### Get Record

This action is used to retrieve a record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|externalIdFieldName|string||False|The name of the external ID field that should be matched with record_id. If empty, the 'Id' field of the record is used|None|ExampleExtID__c|
|objectName|string|Account|True|The name of the object|None|Folder|
|recordId|string|None|True|The ID of an existing record|None|999Hn99999uM8mnBBB|

Example input:

```
{
  "externalIdFieldName": "ExampleExtID__c",
  "objectName": "Folder",
  "recordId": "999Hn99999uM8mnBBB"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|record|object|False|Matched record|{}|

Example output:

```
{
  "record": {
    "attributes": {
      "type": "Folder",
      "url": "/services/data/v58.0/sobjects/Folder/00lHn000002nFolder"
    },
    "id": "00lHn000002nFolder",
    "name": "Example Folder",
    "developerName": "Bot_v5",
    "accessType": "Hidden",
    "isReadonly": true,
    "type": "Report",
    "namespacePrefix": null,
    "createdDate": "2022-06-20T01:51:22.000+0000",
    "createdById": "005Hn00000HExample",
    "lastModifiedDate": "2022-06-20T01:51:22.000+0000",
    "lastModifiedById": "005Hn00000HExample",
    "systemModstamp": "2022-06-20T01:51:22.000+0000"
  }
}
```

#### Get Blob Data

This action is used to retrieve blob data for a given record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fieldName|string|body|True|Blob field name|None|body|
|objectName|string|Attachment|True|The name of the object (e.g. 'Attachment')|None|Attachment|
|recordId|string|None|True|The ID of an existing record|None|001Hn00001uAJRtaB3|

Example input:

```
{
  "fieldName": "body",
  "objectName": "Attachment",
  "recordId": "001Hn00001uAJRtaB3"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|data|bytes|False|The value of the selected blob field|dGVzdA==|

Example output:

```
{
  "data": "dGVzdA=="
}
```

#### Simple Search

This action is used to execute a simple search for a text.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|text|string|None|True|Text to search for|None|test|

Example input:

```
{
  "text": "test"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|searchResults|[]searchResult|False|List of search results|[]|

Example output:

```
{
  "searchResults": [
    {
      "type": "Account",
      "url": "/services/data/v58.0/sobjects/Account/001Hn00001uAccount",
      "id": "001Hn00001uAccount"
    },
    {
      "type": "ExternalObject__c",
      "url": "/services/data/v58.0/sobjects/ExternalObject__c/a00Hn00000External",
      "id": "a00Hn00000External"
    },
    {
      "type": "Customer",
      "url": "/services/data/v58.0/sobjects/Customer/0o6Hn00000Customer",
      "id": "0o6Hn00000Customer"
    },
    {
      "type": "Topic",
      "url": "/services/data/v58.0/sobjects/Topic/0TOHn000000I1Topic",
      "id": "0TOHn000000I1Topic"
    },
    {
      "type": "CollaborationGroup",
      "url": "/services/data/v58.0/sobjects/CollaborationGroup/0F9Hn000000PCollab",
      "id": "0F9Hn000000PCollab"
    },
    {
      "type": "Note",
      "url": "/services/data/v58.0/sobjects/Note/002Hn00000n5KANote",
      "id": "002Hn00000n5KANote"
    }
  ]
}
```

#### Create Record

This action is used to create a new SObject record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|objectData|object|None|True|SObject information for the newly created record|None|{"name": "example-name"}|
|objectName|string|None|True|The name of the object (e.g. 'Account')|None|Account|

Example input:
```
{
  "objectData": {
    "name": "example-name"
  },
  "objectName": "Account"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|id|string|False|ID of the newly created record|000AA000000aa0aAAA|

Example output:

```
{
  "id": "000AA000000aa0aAAA"
}
```

#### Delete Record

This action is used to delete a record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|objectName|string|Account|True|The name of the object (e.g. 'Account')|None|Account|
|recordId|string|None|True|The ID of an existing record|None|000AA000000aa0aAAA|

Example input:

```
{
  "objectName": "Account",
  "recordId": "000AA000000aa0aAAA"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|Was the operation successful|True|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Tasks

#### Monitor Users

This task is used to get information about users, their login history and which users have been updated.

##### Input

_This task does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|users|[]userData|True|Information about users, their login history and which users have been updated|[]|

Example output:

```
{
  "users": [
    {
      "attributes": {
        "type": "User",
        "url": "/services/data/v58.0/sobjects/User/005Hn00000HVWwxIAH"
      },
      "id": "005Hn00000HVWwxIAH",
      "firstName": "Security",
      "lastName": "User",
      "email": "user@example.com",
      "alias": "sec",
      "isActive": true,
      "dataType": "User Update"
    },
    {
      "attributes": {
        "type": "User",
        "url": "/services/data/v58.0/sobjects/User/005Hn00000H35JtIAJ"
      },
      "id": "005Hn00000H35JtIAJ",
      "firstName": "Example",
      "lastName": "User",
      "email": "user2@example.com",
      "alias": "exam",
      "isActive": true,
      "dataType": "User"
    },
    {
      "attributes": {
        "type": "User",
        "url": "/services/data/v58.0/sobjects/User/005Hn00000HVWwxIAH"
      },
      "id": "005Hn00000HVWwxIAH",
      "firstName": "Security",
      "lastName": "User",
      "email": "user@example.com",
      "alias": "sec",
      "isActive": true,
      "dataType": "User"
    },
    {
      "attributes": {
        "type": "LoginHistory",
        "url": "/services/data/v58.0/sobjects/LoginHistory/0YaHn0000EUyGdHKQV"
      },
      "loginTime": "2023-07-23T16:18:23.000+0000",
      "userId": "005Hn00000H35JtIAJ",
      "loginType": "Remote Access 2.0",
      "loginUrl": "login.salesforce.com",
      "sourceIp": "198.51.100.1",
      "status": "Success",
      "application": "New Connected App",
      "browser": "Unknown",
      "dataType": "User Login"
    },
    {
      "attributes": {
        "type": "LoginHistory",
        "url": "/services/data/v58.0/sobjects/LoginHistory/0YaHn0000EUyGkcKQF"
      },
      "loginTime": "2023-07-23T16:20:13.000+0000",
      "userId": "005Hn00000H35JtIAJ",
      "loginType": "Application",
      "loginUrl": "example.salesforce.com",
      "sourceIp": "198.51.100.1",
      "status": "Success",
      "application": "Browser",
      "browser": "Chrome 115",
      "dataType": "User Login"
    }
  ]
}
```

### Custom Output Types

#### searchResult

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID of the record|
|Name|string|False|Name of the record|
|Type|string|False|Type of the record|
|URL|string|False|URL of the record|

#### userData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alias|string|False|The user's alias|
|Application|string|False|The application used to access the organization|
|Browser|string|False|The current browser version|
|Data Type|string|False|Type of the data|
|Email|string|False|The user's email address|
|First Name|string|False|The user's first name|
|ID|string|False|The ID of the user|
|Is Active|boolean|False|Indicates whether the user has access to log in (true) or not (false)|
|Last Name|string|False|The user's last name|
|Login Time|string|False|The time of user login. Time zone is based on GMT|
|Login Type|string|False|The type of login used to access the session|
|Login URL|string|False|URL from which the login request is coming|
|Source IP|string|False|IP address of the machine from which the login request is coming. The address can be an IPv4 or IPv6 address|
|Status|string|False|Displays the status of the attempted login. Status is either success or a reason for failure|
|User ID|string|False|ID of the user logging in|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Code refactor | Update plugin to be cloud enabled | Add new task Monitor Users
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [Salesforce](https://salesforce.com)

## References

* [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm)
* [Connecting your app to the API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/quickstart.htm)
* [SOQL](https://developer.salesforce.com/docs/atlas.en-us.216.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)

