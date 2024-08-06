# Description

Bitwarden is an integrated open source password management solution for individuals, teams, and business organizations

# Key Features

* Retrieve a Member
* Update a Member
* Delete a Member
* Retrieve a Member's Group IDs
* Update a Member's Groups
* List All Members
* Create a Member
* Re-invite a Member
* List All Groups
* List All Collections
* List Events

# Requirements

* Bitwarden Client ID
* Bitwarden Client Secret

# Supported Product Versions

* Cloud-hosted Bitwarden instance 2023.1.1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|clientId|string|None|True|Client ID of the organization|None|organization.u8iid299-888p-12sp-1234-es123456s987|None|None|
|clientSecret|credential_secret_key|None|True|Client secret|None|KuHDkd3Pfhe4Scms6kEHdPPA5dAJDX|None|None|

Example input:

```
{
  "clientId": "organization.u8iid299-888p-12sp-1234-es123456s987",
  "clientSecret": "KuHDkd3Pfhe4Scms6kEHdPPA5dAJDX"
}
```

## Technical Details

### Actions


#### Create a Member

This action is used to create a new member object by inviting a user to the organization

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|accessAll|boolean|None|True|Determines if this member can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments|None|True|None|None|
|collections|[]collection|None|False|The associated collections that this member can access|None|[]|None|None|
|email|string|None|True|The member's email address|None|user@example.com|None|None|
|externalId|string|None|False|External identifier for reference or linking this member to another system, such as a user directory|None|external_id_123456|None|None|
|type|string|None|True|Organization user type|["Owner", "Admin", "User", "Custom"]|Owner|None|None|
  
Example input:

```
{
  "accessAll": true,
  "collections": [],
  "email": "user@example.com",
  "externalId": "external_id_123456",
  "type": "Owner"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|member|member|False|An organization member|{'type': 'Owner', 'accessAll': True, 'externalId': 'external_id_123456', 'resetPasswordEnrolled': True, 'object': 'member', 'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'userId': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'John Smith', 'email': 'user@example.com', 'twoFactorEnabled': True, 'status': 'Invited', 'collections': [{'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'readOnly': True}]}|
  
Example output:

```
{
  "member": {
    "accessAll": true,
    "collections": [
      {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "readOnly": true
      }
    ],
    "email": "user@example.com",
    "externalId": "external_id_123456",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "name": "John Smith",
    "object": "member",
    "resetPasswordEnrolled": true,
    "status": "Invited",
    "twoFactorEnabled": true,
    "type": "Owner",
    "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
  }
}
```

#### Delete a Member

This action is used to permanently delete a member from the organization. This cannot be undone. The user account will 
still remain. The user is only removed from the organization

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The identifier of the member to be deleted|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|None|None|
  
Example input:

```
{
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### List All Collections

This action is used to return a list of your organization's collections. Collection objects listed in this call do not 
include information about their associated groups

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|collections|[]collectionObject|False|List of collections|[{"externalId": "external_id_123456", "object": "collection", "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"}]|
  
Example output:

```
{
  "collections": [
    {
      "externalId": "external_id_123456",
      "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
      "object": "collection"
    }
  ]
}
```

#### List All Groups

This action is used to return a list of your organization's groups. Group objects listed in this call do not include 
information about their associated collections

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|groups|[]group|False|List of groups|[{"name": "Development Team", "accessAll": True, "externalId": "external_id_123456", "object": "group", "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"}]|
  
Example output:

```
{
  "groups": [
    {
      "accessAll": true,
      "externalId": "external_id_123456",
      "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
      "name": "Development Team",
      "object": "group"
    }
  ]
}
```

#### List All Members

This action is used to return a list of your organization's members. Member objects listed in this call do not include 
information about their associated collections

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|members|[]member|False|List of members|[{"type": "Owner", "accessAll": True, "externalId": "external_id_123456", "resetPasswordEnrolled": True, "object": "member", "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "John Smith", "email": "user@example.com", "twoFactorEnabled": True, "status": "Invited"}]|
  
Example output:

```
{
  "members": [
    {
      "accessAll": true,
      "email": "user@example.com",
      "externalId": "external_id_123456",
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "John Smith",
      "object": "member",
      "resetPasswordEnrolled": true,
      "status": "Invited",
      "twoFactorEnabled": true,
      "type": "Owner",
      "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    }
  ]
}
```

#### List Events

This action is used to return a filtered list of your organization's event logs. If no filters are provided, it will 
return the last 30 days of event for the organization

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|actingUserId|string|None|False|The unique identifier of the user that performed the event|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|None|None|
|end|date|None|False|The end date. Must be greater than the start date|None|2023-01-12 00:00:00+00:00|None|None|
|itemId|string|None|False|The unique identifier of the related item that the event describes|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|start|date|None|False|The start date. Must be less than the end date|None|2023-01-10 00:00:00+00:00|None|None|
  
Example input:

```
{
  "actingUserId": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
  "end": "2023-01-12 00:00:00+00:00",
  "itemId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "start": "2023-01-10 00:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]event|False|The filtered list of your organization's event logs|[{"object": "event", "type": 1100, "itemId": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "actingUserId": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593", "date": "2023-01-11T11:59:07.6144531Z", "device": 9, "ipAddress": "198.51.100.1"}]|
  
Example output:

```
{
  "events": [
    {
      "actingUserId": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
      "date": "2023-01-11T11:59:07.6144531Z",
      "device": 9,
      "ipAddress": "198.51.100.1",
      "itemId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "object": "event",
      "type": 1100
    }
  ]
}
```

#### Re-invite a Member

This action is used to re-send the invitation email to an organization member

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The identifier of the member to re-invite|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|None|None|
  
Example input:

```
{
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Retrieve a Member

This action is used to retrieve the details of an existing member of the organization. You need only supply the unique 
member identifier that was returned upon member creation

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The identifier of the member to be retrieved|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|None|None|
  
Example input:

```
{
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|member|member|False|An organization member|{'type': 'Owner', 'accessAll': True, 'externalId': 'external_id_123456', 'resetPasswordEnrolled': True, 'object': 'member', 'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'userId': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'John Smith', 'email': 'user@example.com', 'twoFactorEnabled': True, 'status': 'Invited', 'collections': [{'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'readOnly': True}]}|
  
Example output:

```
{
  "member": {
    "accessAll": true,
    "collections": [
      {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "readOnly": true
      }
    ],
    "email": "user@example.com",
    "externalId": "external_id_123456",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "name": "John Smith",
    "object": "member",
    "resetPasswordEnrolled": true,
    "status": "Invited",
    "twoFactorEnabled": true,
    "type": "Owner",
    "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
  }
}
```

#### Retrieve a Member's Group Ids

This action is used to retrieve the unique identifiers for all groups that are associated with this member. You need 
only supply the unique member identifier that was returned upon member creation

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The identifier of the member to be retrieved|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|None|None|
  
Example input:

```
{
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|membersGroupIds|[]string|False|Member's group IDs|["3fa85f64-5717-4562-b3fc-2c963f66afa6"]|
  
Example output:

```
{
  "membersGroupIds": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  ]
}
```

#### Update a Member

This action is used to updates the specified member object. If a property is not provided, the value of the existing 
property will be reset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|accessAll|boolean|None|True|Determines if this member can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments|None|True|None|None|
|collections|[]collection|None|False|The associated collections that this member can access|None|[]|None|None|
|externalId|string|None|False|External identifier for reference or linking this member to another system, such as a user directory|None|external_id_123456|None|None|
|id|string|None|True|The identifier of the member to be updated|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|None|None|
|type|string|None|True|Organization user type|["Owner", "Admin", "User", "Custom"]|Owner|None|None|
  
Example input:

```
{
  "accessAll": true,
  "collections": [],
  "externalId": "external_id_123456",
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
  "type": "Owner"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|member|member|False|An organization member|{'type': 'Owner', 'accessAll': True, 'externalId': 'external_id_123456', 'resetPasswordEnrolled': True, 'object': 'member', 'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'userId': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'John Smith', 'email': 'user@example.com', 'twoFactorEnabled': True, 'status': 'Invited', 'collections': [{'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'readOnly': True}]}|
  
Example output:

```
{
  "member": {
    "accessAll": true,
    "collections": [
      {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "readOnly": true
      }
    ],
    "email": "user@example.com",
    "externalId": "external_id_123456",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "name": "John Smith",
    "object": "member",
    "resetPasswordEnrolled": true,
    "status": "Invited",
    "twoFactorEnabled": true,
    "type": "Owner",
    "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
  }
}
```

#### Update a Member's Groups

This action is used to update the specified member's group associations

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groupIds|[]string|None|True|The associated group IDs that this object can access|None|["3fa85f64-5717-4562-b3fc-2c963f66afa6"]|None|None|
|id|string|None|True|The identifier of the member to be updated|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|None|None|
  
Example input:

```
{
  "groupIds": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  ],
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access All|boolean|None|False|Determines if this group can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments|True|
|External ID|string|None|False|External identifier for reference or linking this group to another system, such as a user director|external_id_123456|
|ID|string|None|False|The group's unique identifier|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|
|Name|string|None|False|The name of the group|Development Team|
  
**collection**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The associated object's unique identifier|bfbc8338-e329-4dc0-b0c9-317c2ebf1a09|
|Read Only|boolean|None|False|When true, the read only permission will not allow the user or group to make changes to items|True|
  
**collectionObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|External ID|string|None|False|External identifier for reference or linking this collection to another system|external_id_123456|
|ID|string|None|False|The collection's unique identifier|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|
|Object|string|None|False|String representing the object's type. Objects of the same type share the same properties|collection|
  
**member**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access All|boolean|None|False|Determines if this member can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments|True|
|Collections|[]collection|None|False|The associated collections that this member can access|[]|
|Email|string|None|False|The member's email address|user@example.com|
|External ID|string|None|False|External identifier for reference or linking this member to another system, such as a user directory|external_id_123456|
|ID|string|None|False|The member's unique identifier within the organization|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|
|Name|string|None|False|The member's name, set from their user account profile|John Smith|
|Object|string|None|False|String representing the object's type. Objects of the same type share the same properties|member|
|Reset Password Enrolled|boolean|None|False|Returns 'true' if the member has enrolled in Password Reset assistance within the organization|True|
|Status|string|None|False|Organization user status type|Invited|
|Two Factor Enabled|boolean|None|False|Returns 'true' if the member has a two-step login method enabled on their user account|True|
|Type|string|None|False|Organization user type|Owner|
|User ID|string|None|False|The member's unique identifier across Bitwarden|48b47ee1-493e-4c67-aef7-014996c40eca|
  
**event**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Acting User ID|string|None|False|The unique identifier of the user that performed the event|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|
|Collection ID|string|None|False|The unique identifier of the related collection that the event describes|bce212a4-25f3-4888-8a0a-4c5736d851e0|
|Date|string|None|False|The timestamp when the event occurred|2023-01-11 00:00:00+00:00|
|Device|integer|None|False|The type of the device|1|
|Group ID|string|None|False|The unique identifier of the related group that the event describes|f29a2515-91d2-4452-b49b-5e8040e6b0f4|
|IP Address|string|None|False|The IP address of the acting user|198.51.100.1|
|Item ID|string|None|False|The unique identifier of the related item that the event describes|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Member ID|string|None|False|The unique identifier of the related member that the event describes|e68b8629-85eb-4929-92c0-b84464976ba4|
|Object|string|None|False|The type of the object|event|
|Policy ID|string|None|False|The unique identifier of the related policy that the event describes|f29a2515-91d2-4452-b49b-5e8040e6b0f4|
|Type|integer|None|False|The type of the event|1000|


## Troubleshooting

[Bitwarden API Key Documentation](https://bitwarden.com/help/public-api/#authentication). Access to the Bitwarden Public API is available to customers on the Enterprise or Teams organizations plans.

# Version History

* 2.0.0 - Update enum values for `Create a Member`, `Update a Member` and `List all Members` organisation type to support new 'Custom' type. | Update account status type to include no number prefix.
* 1.0.0 - Initial plugin - Actions: `Retrieve a Member`, `Update a Member`, `Delete a Member`, `Retrieve a Member's Group Ids`, `Update a Member's Groups`, `List All Members`, `Create a Member`, `Re-invite a Member`, `List All Groups`, `List All Collections`, `List Events`.

# Links

* [Bitwarden](https://bitwarden.com/)

## References

* [Bitwarden](https://bitwarden.com/)