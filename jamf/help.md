# Jamf

## About

[Jamf](https://instancename.jamfcloud.com/) is a popular product for managing iPads, iPhones, Macs, and Apple TVs for schools and businesses.

This plugin utilizes the [Jamf API](https://developer.jamf.com/apis/classic-api/index).

## Actions

### Add Computer To A Group

This action is used to add a computer to a group.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ID|integer|None|True|Group ID|None|
|computer_ids|[]integer|None|True|Computer IDs|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|True|Status|

Example output:

```
{
  "status": 201
}
```

### Get Device Groups

This action gets a list of all groups a device is a member of.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ID|integer|None|True|Device ID|None|

#### Output

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

### Get Devices Names and IDs

This action is used to get a list of user's devices names and IDs.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|User name|None|

#### Output

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

### Get Group Details

This action is used to get group details.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Group ID|None|

#### Output

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

### Lock Mobile Devices

This action is used to lock mobile devices.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|devices_id|[]string|None|True|List of devices IDs|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|True|None|

Example output:

```
{
  "status": 201
}
```

### Get User Location Details

This action is used to get user location details by device ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ID|string|None|True|Device ID|None|

#### Output

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

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|client_login|credential_username_password|None|True|The Jamf username and password for basic authentication API interaction|None|
|timeout|integer|30|False|The interval in seconds before abandoning an attempt to access Jamf|None|
|url|string|None|True|The full URL for your instance of Jamf, e.g. https://instance.jamfcloud.com|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Get list of device groups
* Lock mobile devices
* Get group details
* Get device name and ID

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - Add action to get user location details by device ID

## References

* [Jamf](https://developer.jamf.com/apis/classic-api/index)

## Custom Output Types

### mobile_device

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|Device ID|
|mac_address|integer|True|MAC address|
|name|string|True|Device name|
|serial_number|string|True|Serial number|
|udid|string|True|Unique device ID|
|wifi_mac_address|string|True|WIFI MAC address|

### device_group_detail

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|Group ID|
|name|string|True|Group name|

### search_criteria

|Name|Type|Required|Description|
|----|----|--------|-----------|
|and_or|string|False|AND_OR|
|closing_paren|boolean|False|Closing Parenthesis|
|name|string|False|None|
|opening_par|boolean|False|Opening Parenthesis|
|priority|integer|False|Priority|
|search_type|string|False|Search type|
|value|string|False|Value|

### site_detail

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|ID|
|name|string|False|Name|

### group_detail

|Name|Type|Required|Description|
|----|----|--------|-----------|
|criteria|[]search_criteria|False|Criteria|
|id|integer|False|Group ID|
|is_smart|boolean|False|Is smart group|
|mobile_devices|[]mobile_device|False|Mobile devices|
|name|string|False|Group name|
|site|site_detail|False|Site|

### user_location_detail

|Name|Type|Required|Description|
|----|----|--------|-----------|
|building|string|True|Building|
|department|string|True|Department|
|email_address|string|True|Email address|
|phone|string|True|Phone|
|position|string|True|Position|
|real_name|string|True|Real name|
|room|string|True|Room number|
|username|string|True|Username|

