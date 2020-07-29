# Description

[Sophos Central](https://www.sophos.com) is a unified console for managing Sophos products. Using the Sophos Central plugin for Rapid7 InsightConnect, users can get alerts, endpoints, and SIEM events

# Key Features

* Get endpoints
* Get alerts

# Requirements

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|credential_secret_key|None|True|Client ID for Sophos Central instance|None|8a9jbad0-12ab-88be-cad4-3b4cad6f78e0|
|client_secret|credential_secret_key|None|True|Client secret key that allows access to Sophos Central|None|a1e263620c12382b36054cf34512ef836854e61d27ab2d079dda27af903a5b6eec396416b2dc40aabce6edfg670b0790d9a90|
|tenant_id|credential_secret_key|None|False|Tenant ID for Sophos Central instance|None|5b0eba20-ab12-34cd-88be-3a4cdc6a70f8|
|url|string|None|True|Host URL|None|https://api-eu02.central.sophos.com|

Example input:

```
{
  "client_id": "8a9jbad0-12ab-88be-cad4-3b4cad6f78e0",
  "client_secret": "a1e263620c12382b36054cf34512ef836854e61d27ab2d079dda27af903a5b6eec396416b2dc40aabce6edfg670b0790d9a90",
  "tenant_id": "5b0eba20-ab12-34cd-88be-3a4cdc6a70f8",
  "url": "https://api-eu02.central.sophos.com"
}
```

## Technical Details

### Actions

#### Get Alerts

This action is used to get alerts for a customer based on the parameters provided.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from_date|string|None|False|The starting date from which alerts will be retrieved defined as Unix timestamp in UTC. Must be within last 24 hours|None|2019-09-23T12:02:01.700Z|

Example input:

```
{
  "from_date": "2019-09-23T12:02:01.700Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert_entity|True|Alerts for specified time period|

Example output:

```
{
  "alerts": [
    {
      "managedAgent": {},
      "severity": "LOW",
      "type": "Event::Mobile::ApnsCertificateRenewed",
      "allowedActions": [
        "acknowledge"
      ],
      "description": "Your APNs certificate was renewed",
      "id": "1ffcae82-97d2-46e8-83e8-469525c28513",
      "raisedAt": "2020-07-19T07:22:07.019Z",
      "tenant": {
        "id": "11f446c2-a094-427f-868e-bd13e2f5b27e",
        "name": "NinjaRMM LLC"
      },
      "category": "mobiles",
      "groupKey": "MyxFdmVudDo6TW9iaWxlOjpBcG5zQ2VydGlmaWNhdGVSZW5ld2...",
      "product": "mobile"
    }
  ]
}
```

#### Get Endpoints

This action is used to get endpoints for a customer based on the parameters provided.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|since|string|None|False|Last seen after date and time (UTC) or duration inclusive, eg. 2019-09-23T12:02:01.700Z, -P1D, PT20M, PT4H500S|None|2019-09-23T12:02:01.700Z|

Example input:

```
{
  "since": "2019-09-23T12:02:01.700Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|items|[]endpoint_entry|True|Endpoint items|

Example output:

```
{
  "items": [
    {
      "id": "1d65be44-e663-437c-949c-2057b73c5630",
      "type": "computer",
      "tenant": {
        "id": "11f446c2-a094-427f-868e-bd13e2f5b27e"
      },
      "hostname": "WIN-JJS9RP995G8",
      "health": {
        "overall": "suspicious",
        "threats": {
          "status": "good"
        },
        "services": {
          "status": "good",
          "serviceDetails": [
            {
              "name": "File Detection",
              "status": "running"
            }
          ]
        }
      },
      "os": {
        "isServer": false,
        "platform": "windows",
        "name": "Windows 8.1",
        "majorVersion": 6,
        "minorVersion": 3,
        "build": 9600
      },
      "ipv4Addresses": [
        "198.51.100.1"
      ],
      "ipv6Addresses": [
        "2001:db8:8:4::2"
      ],
      "macAddresses": [
        "00:0C:29:9B:2F:DF"
      ],
      "associatedPerson": {
        "name": "WIN-JJS9RP995G8\\User",
        "viaLogin": "WIN-JJS9RP995G8\\User",
        "id": "ceddc646-43b2-4b9f-835a-d1ecb9af8253"
      },
      "tamperProtectionEnabled": true,
      "assignedProducts": [
        {
          "code": "endpointProtection",
          "version": "10.8.6",
          "status": "installed"
        }
      ],
      "capabilities": [],
      "lastSeenAt": "2020-04-08T17:27:32.059Z",
      "encryption": {
        "volumes": []
      }
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### alert_aggregate

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Has More|boolean|False|None|
|Items|[]alert_entity|False|None|
|Next Cursor|string|False|Value of the next cursor. This will be used to make next call of API|

#### alert_entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created At|string|False|The date at which the alert was created|
|Customer Id|string|False|The unique identifier of the customer linked with this record|
|Data|object|False|None|
|Description|string|False|The description of the alert that was generated|
|Event Service Event Id|string|False|The Event Services event id|
|Id|string|False|Identifier for the alert|
|Location|string|False|The location captured for this record|
|Severity|string|False|The severity for this alert|
|Source|string|False|Describes the source from alert was generated|
|Threat|string|False|The name of the threat responsible for the generation of alert|
|Threat Cleanable|boolean|False|None|
|Type|string|False|Describes the type of the device on which alert was generated|
|When|string|False|The date at which the alert was created|

#### chronology

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Zone|date_time_zone|False|None|

#### core_remedy_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Descriptor|string|False|None|
|Result|string|False|None|
|Type|string|False|None|

#### core_remedy_items

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Items|[]core_remedy_item|False|None|
|TotalItems|integer|False|None|

#### current_licenses_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Licenses|[]customer_license|False|None|

#### customer_feature

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ExpirationProcessed|boolean|False|None|
|Expired|boolean|False|None|
|ExpiresOn|date_time|False|None|
|FeatureCode|string|False|None|
|GeneratedFromLicenseId|string|False|None|
|LicenseCode|string|False|None|
|Protection|boolean|False|None|
|Valid|boolean|False|None|

#### customer_featuresResponse

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Features|[]customer_feature|False|None|

#### customer_license

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Expired|boolean|False|None|
|Expires On|date_time|False|None|
|Id|object_id|False|None|
|License Code|string|False|None|
|License Id|string|False|None|
|License Type|string|False|None|
|Quota|integer|False|None|
|Starts On|date_time|False|None|
|Suspended|boolean|False|None|

#### date_time

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AfterNow|boolean|False|None|
|BeforeNow|boolean|False|None|
|CenturyOfEra|integer|False|None|
|Chronology|chronology|False|None|
|DayOfMonth|integer|False|None|
|DayOfWeek|integer|False|None|
|DayOfYear|integer|False|None|
|EqualNow|boolean|False|None|
|Era|integer|False|None|
|HourOfDay|integer|False|None|
|Millis|integer|False|None|
|MillisOfDay|integer|False|None|
|MillisOfSecond|integer|False|None|
|MinuteOfDay|integer|False|None|
|MinuteOfHour|integer|False|None|
|MonthOfYear|integer|False|None|
|SecondOfDay|integer|False|None|
|SecondOfMinute|integer|False|None|
|WeekOfWeekyear|integer|False|None|
|Weekyear|integer|False|None|
|Year|integer|False|None|
|YearOfCentury|integer|False|None|
|YearOfEra|integer|False|None|
|Zone|date_time_zone|False|None|

#### date_time_zone

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Fixed|boolean|False|None|
|Id|string|False|None|

#### endpoint_entry

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AdSyncInfo|object|False|None|
|Alert Status|integer|False|None|
|AssignedProducts|[]string|False|None|
|AwsInfo|object|False|None|
|AzureInfo|object|False|None|
|Beta|boolean|False|None|
|Decloned From|string|False|None|
|Deleted At|string|False|None|
|Device Encryption Status Unmanaged|boolean|False|None|
|Early Access Program|string|False|None|
|Endpoint Type|string|False|None|
|Group Full Name|string|False|None|
|Group Id|string|False|None|
|Group Name|string|False|None|
|Health Status|integer|False|None|
|Heartbeat Utm Name|string|False|None|
|Id|string|False|None|
|Info|object|False|None|
|Is Adsync Group|boolean|False|None|
|Java Id|string|False|None|
|Last Activity|string|False|None|
|Last User|string|False|None|
|Last User Id|string|False|None|
|License Codes|[]string|False|None|
|Machine Id|string|False|None|
|Name|string|False|None|
|Registered At|string|False|None|
|Status|object|False|None|
|Tamper Protection|tamper_protection_entity|False|None|
|Transport|string|False|None|

#### endpoint_whitelist_properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Property|string|False|None|
|Type|string|False|None|

#### endpoints_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Filtered|integer|False|None|
|Items|[]endpoint_entry|False|None|
|Next Key|string|False|None|
|Total|integer|False|None|

#### event_aggregate

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Has More|boolean|False|None|
|Items|[]legacy_event_entity|False|None|
|Next Cursor|string|False|Value of the next cursor. This will be used to make next call of API|

#### hashes_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Hashes|object|False|None|

#### installer_info

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Beta|boolean|False|None|
|Command|string|False|None|
|Platform|string|False|None|
|ProductName|string|False|None|
|Url|string|False|None|

#### installer_info_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Installer Info|[]installer_info|False|None|

#### legacy_event_entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Core Remedy Items|core_remedy_items|False|details of the items cleaned or restored|
|Created At|string|False|The date at which the event was created|
|Customer Id|string|False|The identifier of the customer for which record is created|
|Endpoint Id|string|False|The corresponding endpoint id associated with the record|
|Endpoint Type|string|False|The corresponding endpoint type associated with the record|
|Group|string|False|The group associated with the group|
|Id|string|False|The Identifier for the event|
|Location|string|False|The location captured for this record|
|Name|string|False|The name of the record created|
|Origin|string|False|originating component of a detection|
|Severity|string|False|The severity for this alert|
|Source|string|False|The source for this record|
|Threat|string|False|The threat associated with the record|
|Type|string|False|The type of this record|
|User Id|string|False|The identifier of the user for which record is created|
|When|string|False|The date at which the event was created|
|Whitelist Properties|[]endpoint_whitelist_properties|False|The properties by which this event can be whitelisted on an endpoint, if applicable|

#### object_id

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Counter|integer|False|None|
|Date|string|False|None|
|MachineIdentifier|integer|False|None|
|ProcessIdentifier|integer|False|None|
|Time|integer|False|None|
|TimeSecond|integer|False|None|
|Timestamp|integer|False|None|

#### previous_password_entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Invalidated|date|False|None|
|Password|string|False|None|

#### tamper_protection_entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Enabled|boolean|False|None|
|Globally Enabled|boolean|False|None|
|Password|string|False|None|
|Previous Passwords|[]previous_password_entity|False|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 3.0.0 - Rewrite Sophos Central in Python 3
* 2.0.0 - Update type for Invalidated to date
* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers
* 1.0.0 - Support web server mode | Update to new credential types | Rename "Download hashes" action to "Download Hashes" | Rename "Get endpoints" action to "Get Endpoints" | Rename "Get alerts" action to "Get Alerts" | Rename "Get SIEM events" action to "Get SIEM Events"
* 0.1.0 - Initial plugin

# Links

## References

* [Sophos Central](https://www.sophos.com)
