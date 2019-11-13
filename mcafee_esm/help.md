# Description

[McAfee ESM](https://www.mcafee.com/enterprise/en-us/products/enterprise-security-manager.html) is a security information and event management (SIEM) solution that delivers actionable intelligence and integrations to prioritize, investigate, and respond to threats.
This plugin utilizes the McAfee ESM API. Documentation about the API can be found on your instance at the following URL `https://hostname/rs/esm/help`.

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
|credentials|credential_username_password|None|True|Username and password for McAfee ESM|None|
|hostname|string|None|True|Hostname to McAfee ESM Server|None|
|port|string|443|True|McAfee ESM host port|None|

## Technical Details

### Actions

This plugin does not contain any actions.

### Triggers

#### Get New Events

This trigger is used to retrieve new events from McAfee ESM.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|event_information|object|False|Event correlation list|

Example output:

```

{
  "event_information":{
    "Alert.AvgSeverity":"19",
    "Rule.msg":"User Logon",
    "Alert.Action":"8",
    "Alert.SrcIP":"192.168.0.36",
    "Alert.AlertID":"4266"
  }
}

```

##### Help

###### ESM Event Field and Filtering

When designing a config for the `Get New Events` trigger. You have a lot of options at hand. Below, we will outline each option with some examples.

`fields` - These are the name/types that will be entered into as an array. Fields help describe the output that you would like returned.
To get a list of fields for events or additional information see `https://<ESM Server>/rs/esm/help/qryGetSelectFields`.

Example Input:

```

[
  {
    "name": "AvgSeverity",
    "types": [
      "FLOAT"
    ]
  },
  {
    "name": "Rule.msg",
    "types": [
      "STRING"
    ]
  },
  {
    "name": "Action",
    "types": [
      "SSTRING"
    ]
  },
  {
    "name": "SrcIP",
    "types": [
      "IP"
    ]
  }
]

```

With will return the output of the above `{"Alert.AvgSeverity":"19", "Rule.msg":"User Logon", "Alert.Action":"8", "Alert.SrcIP":"192.168.0.36"}`

`filters` - ESM Fields Filters define how the event will be sorted. Additional information can be found at the following URL `https://<ESM Server>/rs/esm/help/types/EsmFieldType`.

Example Input:

```

[
  {
    "type": "EsmFieldFilter",
    "field": {
      "types": [
        "STRING"
      ],
      "name": "AvgSeverity"
    }
  }
]

```

###### Tracking Alerts

In `fields`, an AlertID can be returned. If this key is not added to `fields` it will automatically be appended to the end. This ensures that if the same event has been processed and the service fails the event will not show.

This field looks like:

```

{
  "name":"AlertID",
  "types":[
    "STRING"
  ]
}

```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [McAfee ESM](https://www.mcafee.com/enterprise/en-us/products/enterprise-security-manager.html)

