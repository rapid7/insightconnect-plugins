# Description

[Salesforce](https://www.salesforce.com) is a CRM solution that brings together all customer information in a single, integrated platform that enables building a customer-centered business from marketing right through to sales, customer service and business analysis. The Salesforce plugin allows you to search, update, and manage salesforce records. This plugin utilizes the [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm)

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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|clientId|string|None|True|Consumer Key of the connected app|None|1234567890aBcdEFRoeRxDE1234567890abCDef6Etz7VLwwLQZn19jyW3U_1234567890AbcdEF4VkuMS4ze|None|None|
|clientSecret|credential_secret_key|None|True|Consumer Secret of the connected app|None|1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF|None|None|
|loginURL|string|https://login.salesforce.com|False|Salesforce login URL|None|https://login.salesforce.com|None|None|
|salesforceAccountUsernameAndPassword|credential_username_password|None|True|Name and password of the Salesforce user|None|{"username": "user@example.com", "password": "password"}|None|None|
|securityToken|credential_secret_key|None|True|Security token of the Salesforce user|None|Ier6YY78KxJwKtHy7HeK0oPc|None|None|

Example input:

```
{
  "clientId": "1234567890aBcdEFRoeRxDE1234567890abCDef6Etz7VLwwLQZn19jyW3U_1234567890AbcdEF4VkuMS4ze",
  "clientSecret": "1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF",
  "loginURL": "https://login.salesforce.com",
  "salesforceAccountUsernameAndPassword": {
    "password": "password",
    "username": "user@example.com"
  },
  "securityToken": "Ier6YY78KxJwKtHy7HeK0oPc"
}
```

## Technical Details

### Actions


#### Advanced Search

This action is used to execute a SOQL (Salesforce Object Query Language) query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|SOQL query|None|SELECT FIELDS(STANDARD) FROM Account WHERE Name='Example Account'|None|None|
  
Example input:

```
{
  "query": "SELECT FIELDS(STANDARD) FROM Account WHERE Name='Example Account'"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|searchResults|[]searchResult|False|List of search results|[{"type":"Account","url":"/services/data/v58.0/sobjects/Account/001Hn00001uLl12aBC","name":"Example Account","id":"001Hn00001uLl12aBC"}]|
  
Example output:

```
{
  "searchResults": [
    {
      "id": "001Hn00001uLl12aBC",
      "name": "Example Account",
      "type": "Account",
      "url": "/services/data/v58.0/sobjects/Account/001Hn00001uLl12aBC"
    }
  ]
}
```

#### Create Record

This action is used to create a new SObject record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|objectData|object|None|True|SObject information for the newly created record|None|{"name": "example-name"}|None|None|
|objectName|string|None|True|The name of the object (e.g. 'Account')|None|Account|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|id|string|False|ID of the newly created record|000AA000000aa0aAAA|
  
Example output:

```
{
  "id": "000AA000000aa0aAAA"
}
```

#### Delete Record

This action is used to delete a record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|objectName|string|Account|True|The name of the object (e.g. 'Account')|None|Account|None|None|
|recordId|string|None|True|The ID of an existing record|None|000AA000000aa0aAAA|None|None|
  
Example input:

```
{
  "objectName": "Account",
  "recordId": "000AA000000aa0aAAA"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Was the operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Blob Data

This action is used to retrieve blob data for a given record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fieldName|string|body|True|Blob field name|None|body|None|None|
|objectName|string|Attachment|True|The name of the object (e.g. 'Attachment')|None|Attachment|None|None|
|recordId|string|None|True|The ID of an existing record|None|001Hn00001uAJRtaB3|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|data|bytes|False|The value of the selected blob field|dGVzdA==|
  
Example output:

```
{
  "data": "dGVzdA=="
}
```

#### Get Fields

This action is used to retrieve field values from the record of the given object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|[]string|None|True|The fields which values should be retrieved|None|["Id", "Name", "Description"]|None|None|
|objectName|string|Account|True|The name of the object (e.g. 'Account')|None|Account|None|None|
|recordId|string|None|True|The ID of an existing record|None|001Hn00001uAJRtaB3|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|fields|object|False|An object with field names as keys, each with the corresponding value|{"id":"001Hn00001uAJRtaB3","name":"Example Account","description":"Example description"}|
  
Example output:

```
{
  "fields": {
    "description": "Example description",
    "id": "001Hn00001uAJRtaB3",
    "name": "Example Account"
  }
}
```

#### Get Record

This action is used to retrieve a record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|externalIdFieldName|string|None|False|The name of the external ID field that should be matched with record_id. If empty, the 'Id' field of the record is used|None|ExampleExtID__c|None|None|
|objectName|string|Account|True|The name of the object|None|Folder|None|None|
|recordId|string|None|True|The ID of an existing record|None|999Hn99999uM8mnBBB|None|None|
  
Example input:

```
{
  "externalIdFieldName": "ExampleExtID__c",
  "objectName": "Account",
  "recordId": "999Hn99999uM8mnBBB"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|record|object|False|Matched record|{"attributes":{"type":"Folder","url":"/services/data/v58.0/sobjects/Folder/00lHn000002nFolder"},"id":"00lHn000002nFolder","name":"Example Folder","developerName":"Bot_v5","accessType":"Hidden","isReadonly":true,"type":"Report","namespacePrefix":null,"createdDate":"2022-06-20T01:51:22.000+0000","createdById":"005Hn00000HExample","lastModifiedDate":"2022-06-20T01:51:22.000+0000","lastModifiedById":"005Hn00000HExample","systemModstamp":"2022-06-20T01:51:22.000+0000"}|
  
Example output:

```
{
  "record": {
    "accessType": "Hidden",
    "attributes": {
      "type": "Folder",
      "url": "/services/data/v58.0/sobjects/Folder/00lHn000002nFolder"
    },
    "createdById": "005Hn00000HExample",
    "createdDate": "2022-06-20T01:51:22.000+0000",
    "developerName": "Bot_v5",
    "id": "00lHn000002nFolder",
    "isReadonly": true,
    "lastModifiedById": "005Hn00000HExample",
    "lastModifiedDate": "2022-06-20T01:51:22.000+0000",
    "name": "Example Folder",
    "namespacePrefix": null,
    "systemModstamp": "2022-06-20T01:51:22.000+0000",
    "type": "Report"
  }
}
```

#### Simple Search

This action is used to execute a simple search for a text

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|text|string|None|True|Text to search for|None|test|None|None|
  
Example input:

```
{
  "text": "test"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|searchResults|[]searchResult|False|List of search results|[{"type":"Account","url":"/services/data/v58.0/sobjects/Account/001Hn00001uAccount","id":"001Hn00001uAccount"},{"type":"ExternalObject__c","url":"/services/data/v58.0/sobjects/ExternalObject__c/a00Hn00000External","id":"a00Hn00000External"},{"type":"Customer","url":"/services/data/v58.0/sobjects/Customer/0o6Hn00000Customer","id":"0o6Hn00000Customer"},{"type":"Topic","url":"/services/data/v58.0/sobjects/Topic/0TOHn000000I1Topic","id":"0TOHn000000I1Topic"},{"type":"CollaborationGroup","url":"/services/data/v58.0/sobjects/CollaborationGroup/0F9Hn000000PCollab","id":"0F9Hn000000PCollab"},{"type":"Note","url":"/services/data/v58.0/sobjects/Note/002Hn00000n5KANote","id":"002Hn00000n5KANote"}]|
  
Example output:

```
{
  "searchResults": [
    {
      "id": "001Hn00001uAccount",
      "type": "Account",
      "url": "/services/data/v58.0/sobjects/Account/001Hn00001uAccount"
    },
    {
      "id": "a00Hn00000External",
      "type": "ExternalObject__c",
      "url": "/services/data/v58.0/sobjects/ExternalObject__c/a00Hn00000External"
    },
    {
      "id": "0o6Hn00000Customer",
      "type": "Customer",
      "url": "/services/data/v58.0/sobjects/Customer/0o6Hn00000Customer"
    },
    {
      "id": "0TOHn000000I1Topic",
      "type": "Topic",
      "url": "/services/data/v58.0/sobjects/Topic/0TOHn000000I1Topic"
    },
    {
      "id": "0F9Hn000000PCollab",
      "type": "CollaborationGroup",
      "url": "/services/data/v58.0/sobjects/CollaborationGroup/0F9Hn000000PCollab"
    },
    {
      "id": "002Hn00000n5KANote",
      "type": "Note",
      "url": "/services/data/v58.0/sobjects/Note/002Hn00000n5KANote"
    }
  ]
}
```

#### Update Record

This action is used to update a record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|objectData|object|None|True|Updated SObject information|None|{"name": "example-name"}|None|None|
|objectName|string|Account|True|The name of the object (e.g. 'Account')|None|Account|None|None|
|recordId|string|None|True|The ID of an existing record|None|000AA000000aa0aAAA|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Was the operation successful|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks


#### Monitor Users

This task is used to get information about users, their login history and which users have been updated

##### Input
  
*This task does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|users|[]object|True|Information about users, their login history and which users have been updated|[{"attributes":{"type":"User","url":"/services/data/v58.0/sobjects/User/005Hn00000HVWwxIAH"},"id":"005Hn00000HVWwxIAH","firstName":"Security","lastName":"User","email":"user@example.com","alias":"sec","isActive":true,"dataType":"User Update"},{"attributes":{"type":"User","url":"/services/data/v58.0/sobjects/User/005Hn00000H35JtIAJ"},"id":"005Hn00000H35JtIAJ","firstName":"Example","lastName":"User","email":"user2@example.com","alias":"exam","isActive":true,"dataType":"User"},{"attributes":{"type":"User","url":"/services/data/v58.0/sobjects/User/005Hn00000HVWwxIAH"},"id":"005Hn00000HVWwxIAH","firstName":"Security","lastName":"User","email":"user@example.com","alias":"sec","isActive":true,"dataType":"User"},{"attributes":{"type":"LoginHistory","url":"/services/data/v58.0/sobjects/LoginHistory/0YaHn0000EUyGdHKQV"},"loginTime":"2023-07-23T16:18:23.000+0000","userId":"005Hn00000H35JtIAJ","loginType":"Remote Access 2.0","loginUrl":"login.salesforce.com","sourceIp":"198.51.100.1","status":"Success","application":"New Connected App","browser":"Unknown","dataType":"User Login"},{"attributes":{"type":"LoginHistory","url":"/services/data/v58.0/sobjects/LoginHistory/0YaHn0000EUyGkcKQF"},"loginTime":"2023-07-23T16:20:13.000+0000","userId":"005Hn00000H35JtIAJ","loginType":"Application","loginUrl":"example.salesforce.com","sourceIp":"198.51.100.1","status":"Success","application":"Browser","browser":"Chrome 115","dataType":"User Login"}]|
  
Example output:

```
{
  "users": [
    {
      "alias": "sec",
      "attributes": {
        "type": "User",
        "url": "/services/data/v58.0/sobjects/User/005Hn00000HVWwxIAH"
      },
      "dataType": "User Update",
      "email": "user@example.com",
      "firstName": "Security",
      "id": "005Hn00000HVWwxIAH",
      "isActive": true,
      "lastName": "User"
    },
    {
      "alias": "exam",
      "attributes": {
        "type": "User",
        "url": "/services/data/v58.0/sobjects/User/005Hn00000H35JtIAJ"
      },
      "dataType": "User",
      "email": "user2@example.com",
      "firstName": "Example",
      "id": "005Hn00000H35JtIAJ",
      "isActive": true,
      "lastName": "User"
    },
    {
      "alias": "sec",
      "attributes": {
        "type": "User",
        "url": "/services/data/v58.0/sobjects/User/005Hn00000HVWwxIAH"
      },
      "dataType": "User",
      "email": "user@example.com",
      "firstName": "Security",
      "id": "005Hn00000HVWwxIAH",
      "isActive": true,
      "lastName": "User"
    },
    {
      "application": "New Connected App",
      "attributes": {
        "type": "LoginHistory",
        "url": "/services/data/v58.0/sobjects/LoginHistory/0YaHn0000EUyGdHKQV"
      },
      "browser": "Unknown",
      "dataType": "User Login",
      "loginTime": "2023-07-23T16:18:23.000+0000",
      "loginType": "Remote Access 2.0",
      "loginUrl": "login.salesforce.com",
      "sourceIp": "198.51.100.1",
      "status": "Success",
      "userId": "005Hn00000H35JtIAJ"
    },
    {
      "application": "Browser",
      "attributes": {
        "type": "LoginHistory",
        "url": "/services/data/v58.0/sobjects/LoginHistory/0YaHn0000EUyGkcKQF"
      },
      "browser": "Chrome 115",
      "dataType": "User Login",
      "loginTime": "2023-07-23T16:20:13.000+0000",
      "loginType": "Application",
      "loginUrl": "example.salesforce.com",
      "sourceIp": "198.51.100.1",
      "status": "Success",
      "userId": "005Hn00000H35JtIAJ"
    }
  ]
}
```

### Custom Types
  
**searchResult**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID of the record|001Hn00001uAJRtaB3|
|Name|string|None|None|Name of the record|Example Account|
|Type|string|None|False|Type of the record|Account|
|URL|string|None|False|URL of the record|/services/data/v58.0/sobjects/Account/001Hn00001uAJRtaB3|
  
**userData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alias|string|None|False|The user's alias|jsmith|
|Application|string|None|False|The application used to access the organization|Browser|
|Browser|string|None|False|The current browser version|Chrome 114|
|Data Type|string|None|False|Type of the data|User Login|
|Email|string|None|False|The user's email address|user@example.com|
|First Name|string|None|False|The user's first name|John|
|ID|string|None|False|The ID of the user|005Hn00000HVWwsIAH|
|Is Active|boolean|None|False|Indicates whether the user has access to log in (true) or not (false)|True|
|Last Name|string|None|False|The user's last name|Smith|
|Login Time|string|None|False|The time of user login. Time zone is based on GMT|2023-06-28T09:15:32.000+0000|
|Login Type|string|None|False|The type of login used to access the session|Application|
|Login URL|string|None|False|URL from which the login request is coming|https://example.com|
|Source IP|string|None|False|IP address of the machine from which the login request is coming. The address can be an IPv4 or IPv6 address|198.51.100.1|
|Status|string|None|False|Displays the status of the attempted login. Status is either success or a reason for failure|Success|
|User ID|string|None|False|ID of the user logging in|005Hn00000HVWwsIAH|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.1.14 - Task Monitor Users: Bump SDK to 6.3.8 | Add task delay monitoring
* 2.1.13 - Task Monitor Users: improve error response to UI | Bump SDK to 6.2.4
* 2.1.12 - Task Monitor Users: ensure datetime includes microseconds | Bump SDK to 6.2.0
* 2.1.11 - Task Monitor Users: Return 500 for retry your request error | Bump SDK to 6.1.4
* 2.1.10 - Set Monitor Users task output length | Fix to remove whitespace from connection inputs
* 2.1.9 - SDK Bump to 6.1.0 | Task Connection test added
* 2.1.8 - Task Monitor Users: Allow lookback to be 7 days and initial run to be 24 hours & raise PluginException for API errors.
* 2.1.7 - Task Monitor Users: Update connection to accept instance URL and force new token request per execution.
* 2.1.6 - Task Monitor Users: Implement SDK 5.4.4 for custom_config parameter.
* 2.1.5 - Task Monitor Users: Improved logging
* 2.1.4 - Connection: Remove unnecessary logging
* 2.1.3 - Task Monitor Users: improve deduplication logic on user login history
* 2.1.2 - Task Monitor Users: normalisation for date in state, handle backwards compatibility
* 2.1.1 - Task Monitor Users: query improvement on updated users | Add extra logs on timestamp | Add cutoff time limit for 24 hours
* 2.1.0 - Implemented token auto-refresh on expiration for continuous sessions | Task Monitor Users: add flag `remove_duplicates` for duplicated events | Task Monitor Users: removed formatting of task output and cleaning null
* 2.0.2 - Task Monitor Users: query improvement | Handle exception related with grant type
* 2.0.1 - Add extra logs register
* 2.0.0 - Code refactor | Update plugin to be cloud enabled | Add new task Monitor Users
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [Salesforce](https://salesforce.com)

## References

* [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm)
* [Connecting your app to the API](https://developer.salesforce.com/docs/atlas.en-us.216.0.api_rest.meta/api_rest/quickstart.htm)
* [SOQL](https://developer.salesforce.com/docs/atlas.en-us.216.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)