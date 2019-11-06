# Description

[Jamf](https://instancename.jamfcloud.com/) is a popular product for managing iPads, iPhones, Macs, and Apple TVs for schools and businesses.

This plugin utilizes the [Jamf API](https://developer.jamf.com/apis/classic-api/index).

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
|client_login|credential_username_password|None|True|The Jamf username and password for basic authentication API interaction|None|
|timeout|integer|30|False|The interval in seconds before abandoning an attempt to access Jamf|None|
|url|string|None|True|The full URL for your instance of Jamf, e.g. https://instance.jamfcloud.com|None|

## Technical Details

### Actions

#### Add Computer To A Group

This action is used to add a computer to a group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ID|integer|None|True|Group ID|None|
|computer_ids|[]integer|None|True|Computer IDs|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|True|Status|

Example output:

```
{
  "status": 201
}
```

#### Get Device Groups

This action gets a list of all groups a device is a member of.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ID|integer|None|True|Device ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|device_groups|[]device_group_detail|True|List of device groups|

Example output:

```                                   
{
  "device_groups": [
    {
      "id": 2,
      "name": "All Managed iPhones"
    },
    {
      "id": 5,
      "name": "Smart Group temp"
    }
  ]
}
```

#### Get Devices Names and IDs

This action is used to get a list of user's devices names and IDs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|User name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|device_detail|object|True|Device detail|

Example output:

```
{
  "device_detail": {
  "computers": [],
  "mobile_devices": [
    {
      "id": 2,
      "name": "Jon’s iPhone"
    }
  ],
  "peripherals": [],
  "total_vpp_code_count": 0,
  "vpp_assignments": []
  }
}
```

#### Get Group Details

This action is used to get group details.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Group ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|group_detail|group_detail|True|Group detail|

Example output:

```
{
  "group_detail": {
    "mobile_device_group": {
      "criteria": [
        {
          "and_or": "AND",
          "closing_paren": false,
          "name": "Model",
          "opening_paren": false,
          "priority": 0,
          "search_type": "like",
          "value": "iPhone"
        },
        {
          "and_or": "and",
          "closing_paren": false,
          "name": "Username",
          "opening_paren": false,
          "priority": 1,
          "search_type": "is",
          "value": "Jon"
        },
        {
          "and_or": "and",
          "closing_paren": false,
          "name": "Last Inventory Update",
          "opening_paren": false,
          "priority": 2,
          "search_type": "before (yyyy-mm-dd)",
          "value": "2019-10-10"
        }
      ],
        "id": 2,
        "is_smart": true,
        "mobile_devices": [
          {
            "id": 2,
            "mac_address": "54:4E:90:84:AC:E9",
            "name": "Jon’s iPhone",
            "serial_number": "F17Q4JFBG5MC",
            "udid": "1bdf99f35865df30ccde9a9c786abf021e41d8a9",
            "wifi_mac_address": "54:4E:90:84:AC:E9"
          }
        ],
          "name": "All Managed iPhones",
          "site": {
            "id": -1,
            "name": "None"
          }
    }
  }
}
```

#### Lock Mobile Devices

This action is used to lock mobile devices.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|devices_id|[]string|None|True|List of devices IDs|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|True|None|

Example output:

```
{
  "status": 201
}
```

#### Get User Location Details

This action is used to get user location details by device ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ID|string|None|True|Device ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user_location_detail|user_location_detail|False|User location details|

Example output:

```
{
  "user_location_detail": {
    "building": "",
    "department": "",
    "email_address": "Jon_schipp@domain.com",
    "phone": "999-999-9999",
    "position": "Director",
    "real_name": "Jonathan Schipp",
    "room": "9999",
    "username": "Jon"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.0 - Add action to get user location details by device ID
* 1.0.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Jamf](https://developer.jamf.com/apis/classic-api/index)

