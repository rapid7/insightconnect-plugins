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

The following information are required for using this plugin:
* Bitwarden Client ID
* Bitwarden Client Secret

Read more:
[Bitwarden API Key](https://bitwarden.com/help/public-api/#authentication).

Access to the Bitwarden Public API is available to customers on the Enterprise or Teams organizations plans.

# Supported Product Versions

* Bitwarden 2023-01-10

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|clientId|string|None|True|Client ID of the organization|None|organization.u8iid299-888p-12sp-1234-es123456s987|
|clientSecret|credential_secret_key|None|True|Client secret|None|KuHDkd3Pfhe4Scms6kEHdPPA5dAJDX|

Example input:

```
{
  "clientId": "organization.u8iid299-888p-12sp-1234-es123456s987",
  "clientSecret": {
        "secretKey": "KuHDkd3Pfhe4Scms6kEHdPPA5dAJDX"
      }
}
```

## Technical Details

### Actions

#### List Events

This action is used to return a filtered list of your organization's event logs. If no filters are provided, it will return the last 30 days of event for the organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|actingUserId|string|None|False|The unique identifier of the user that performed the event|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|
|end|date|None|False|The end date. Must be greater than the start date|None|2023-01-12T00:00:00Z|
|itemId|string|None|False|The unique identifier of the related item that the event describes|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|start|date|None|False|The start date. Must be less than the end date|None|2023-01-10T00:00:00Z|

Example input:

```
{
  "actingUserId": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
  "end": "2023-01-12T00:00:00Z",
  "itemId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "start": "2023-01-10T00:00:00Z"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|events|[]event|False|The filtered list of your organization's event logs|[]|

Example output:

```
{
  "events": [
    {
      "object": "event",
      "type": 1100,
      "itemId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "actingUserId": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
      "date": "2023-01-11T11:59:07.6144531Z",
      "device": 9,
      "ipAddress": "198.51.100.1"
    }
  ]
}
```

#### Retrieve a Member

This action retrieves the details of an existing member of the organization. You need only supply the unique member identifier that was returned upon member creation.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The identifier of the member to be retrieved|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|

Example input:

```
{
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|member|member|False|An organization member|{}|

Example output:

```
{
  "member": {
    "type": "0-Owner",
    "accessAll": true,
    "externalId": "external_id_123456",
    "resetPasswordEnrolled": true,
    "object": "member",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "name": "John Smith",
    "email": "user@example.com",
    "twoFactorEnabled": true,
    "status": "0-Invited",
    "collections": [
      {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "readOnly": true
      }
    ]
  }
}
```

#### Create a Member

This action creates a new member object by inviting a user to the organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|accessAll|boolean|None|True|Determines if this member can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments|None|True|
|collections|[]collection|None|False|The associated collections that this member can access|None|[]|
|email|string|None|True|The member's email address|None|user@example.com|
|externalId|string|None|False|External identifier for reference or linking this member to another system, such as a user directory|None|external_id_123456|
|type|string|None|True|Organization user type|['0-Owner', '1-Admin', '2-User', '3-Manager']|0-Owner|

Example input:

```
{
  "accessAll": true,
  "collections": [],
  "email": "user@example.com",
  "externalId": "external_id_123456",
  "type": "0-Owner"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|member|member|False|An organization member|{}|

Example output:

```
{
  "member": {
    "type": "0-Owner",
    "accessAll": true,
    "externalId": "external_id_123456",
    "resetPasswordEnrolled": true,
    "object": "member",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "name": "John Smith",
    "email": "user@example.com",
    "twoFactorEnabled": true,
    "status": "0-Invited",
    "collections": [
      {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "readOnly": true
      }
    ]
  }
}
```

#### Delete a Member

This action is used to permanently deletes a member from the organization. This cannot be undone. The user account will still remain. The user is only removed from the organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The identifier of the member to be deleted|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|

Example input:

```
{
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|True|

Example output:

```
{
  "success": true
}
```

#### List All Collections

This action returns a list of your organization's collections. Collection objects listed in this call do not include information about their associated groups.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|collections|[]collectionObject|False|List of collections|[]|

Example output:

```
{
  "collections": [
    {
      "externalId": "external_id_123456",
      "object": "collection",
      "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
    }
  ]
}
```

#### List All Groups

This action returns a list of your organization's groups. Group objects listed in this call do not include information about their associated collections.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|groups|[]group|False|List of groups|[]|

Example output:

```
{
  "groups": [
    {
      "name": "Development Team",
      "accessAll": true,
      "externalId": "external_id_123456",
      "object": "group",
      "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
    }
  ]
}
```

#### List All Members

This action returns a list of your organization's members. Member objects listed in this call do not include information about their associated collections.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|members|[]member|False|List of members|[]|

Example output:

```
{
  "members": [
    {
      "type": "0-Owner",
      "accessAll": true,
      "externalId": "external_id_123456",
      "resetPasswordEnrolled": true,
      "object": "member",
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "John Smith",
      "email": "user@example.com",
      "twoFactorEnabled": true,
      "status": "0-Invited"
    }
  ]
}
```

#### Re-invite a Member

This action re-sends the invitation email to an organization member.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The identifier of the member to re-invite|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|

Example input:

```
{
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|True|

Example output:

```
{
  "success": true
}
```

#### Retrieve a Member's Group Ids

This action retrieves the unique identifiers for all groups that are associated with this member. You need only supply the unique member identifier that was returned upon member creation.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The identifier of the member to be retrieved|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|

Example input:

```
{
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
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

This action updates the specified member object. If a property is not provided, the value of the existing property will be reset.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|accessAll|boolean|None|True|Determines if this member can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments|None|True|
|collections|[]collection|None|False|The associated collections that this member can access|None|[]|
|externalId|string|None|False|External identifier for reference or linking this member to another system, such as a user directory|None|external_id_123456|
|id|string|None|True|The identifier of the member to be updated|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|
|type|string|None|True|Organization user type|['0-Owner', '1-Admin', '2-User', '3-Manager']|0-Owner|

Example input:

```
{
  "accessAll": true,
  "collections": [],
  "externalId": "external_id_123456",
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
  "type": "0-Owner"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|member|member|False|An organization member|{}|

Example output:

```
{
  "member": {
    "type": "0-Owner",
    "accessAll": true,
    "externalId": "external_id_123456",
    "resetPasswordEnrolled": true,
    "object": "member",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "userId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "name": "John Smith",
    "email": "user@example.com",
    "twoFactorEnabled": true,
    "status": "0-Invited",
    "collections": [
      {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "readOnly": true
      }
    ]
  }
}
```

#### Update a Member's Groups

This action updates the specified member's group associations.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|groupIds|[]string|None|True|The associated group IDs that this object can access|None|["3fa85f64-5717-4562-b3fc-2c963f66afa6"]|
|id|string|None|True|The identifier of the member to be updated|None|539a36c5-e0d2-4cf9-979e-51ecf5cf6593|

Example input:

```
{
  "accessAll": true,
  "collections": [],
  "externalId": "external_id_123456",
  "id": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593",
  "type": "0-Owner"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|True|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### collection

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|The associated object's unique identifier|
|Read Only|boolean|False|When true, the read only permission will not allow the user or group to make changes to items|

#### collectionObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|External ID|string|False|External identifier for reference or linking this collection to another system|
|ID|string|False|The collection's unique identifier|
|Object|string|False|String representing the object's type. Objects of the same type share the same properties|

#### event

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Acting User ID|string|False|The unique identifier of the user that performed the event|
|Collection ID|string|False|The unique identifier of the related collection that the event describes|
|Date|string|False|The timestamp when the event occurred|
|Device|integer|False|The type of the device|
|Group ID|string|False|The unique identifier of the related group that the event describes|
|IP Address|string|False|The IP address of the acting user|
|Item ID|string|False|The unique identifier of the related item that the event describes|
|Member ID|string|False|The unique identifier of the related member that the event describes|
|Object|string|False|The type of the object|
|Policy ID|string|False|The unique identifier of the related policy that the event describes|
|Type|integer|False|The type of the event|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access All|boolean|False|Determines if this group can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments|
|External ID|string|False|External identifier for reference or linking this group to another system, such as a user director|
|ID|string|False|The group's unique identifier|
|Name|string|False|The name of the group|

#### member

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access All|boolean|False|Determines if this member can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments|
|Collections|[]collection|False|The associated collections that this member can access|
|Email|string|False|The member's email address|
|External ID|string|False|External identifier for reference or linking this member to another system, such as a user directory|
|ID|string|False|The member's unique identifier within the organization|
|Name|string|False|The member's name, set from their user account profile|
|Object|string|False|String representing the object's type. Objects of the same type share the same properties|
|Reset Password Enrolled|boolean|False|Returns 'true' if the member has enrolled in Password Reset assistance within the organization|
|Status|string|False|Organization user status type|
|Two Factor Enabled|boolean|False|Returns 'true' if the member has a two-step login method enabled on their user account|
|Type|string|False|Organization user type|
|User ID|string|False|The member's unique identifier across Bitwarden|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin - Actions: `Retrieve a Member`, `Update a Member`, `Delete a Member`, `Retrieve a Member's Group Ids`, `Update a Member's Groups`, `List All Members`, `Create a Member`, `Re-invite a Member`, `List All Groups`, `List All Collections`, `List Events`.

# Links

* [Bitwarden](https://bitwarden.com/)

## References

* [Bitwarden](https://bitwarden.com/)
