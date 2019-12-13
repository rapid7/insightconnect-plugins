# Description

[CRITs](https://crits.github.io/) is an open source malware and threat repository for conducting malware analyses.
With the CRITs plugin for Rapid7 InsightConnect, users can manage actors, events, collections, domains, and more.

Using the CRITs plugin, users can quickly automate usecases around threat intelligence, malware analysis, email
file attachment analysis, and other scenarios.

Note: The CRITs server API endpoint, by default, is `/api/$API_VERSION`.

# Key Features

* Malware analysis
* Manage events

# Requirements

* API key
* Username

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Host URL, E.g. https://localhost:8443|None|
|username|string|None|True|Enter the API username|None|
|api_key|credential_secret_key|None|True|Enter the API key|None|
|ssl_verify|boolean|False|True|Verify server's certificate|None|

## Technical Details

### Actions

#### Add Actor Identifier

This action is used to create a new actor identifier.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|params|object|None|False|Object containing related data or metadata|None|
|id_type|string|None|True|Identity Type|None|
|id|string|None|True|The name your organization refers to this Actor by|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "return_code": 1,
    "type": "ActorIdentifier",
    "message": "Unknown Identifier Type",
    "id": ""
  }
}

```

#### Add Target

This action is used to create a new target.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|params|object|None|False|Object containing related data or metadata|None|
|email|string|None|True|The email address of the Target|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "id": "595070faf47016014922a4f3",
    "return_code": 0,
    "message": "Target saved successfully",
    "type": "Target",
    "url": "/api/v1/targets/595070faf47016014922a4f3/"
  }
}

```

#### Add Actor

This action is used to create a new actor.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|params|object|None|False|Object containing related data or metadata|None|
|name|string|None|True|The name your organization refers to this Actor by|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "message": "Success! Click here to view the new Actor: <a href=\"/actors/details/595071f7f47016014922a4f5/\"></a>",
    "id": "595071f7f47016014922a4f5",
    "url": "/api/v1/actors/595071f7f47016014922a4f5/",
    "type": "Actor",
    "return_code": 0
  }
}

```

#### Add Raw Data

This action is used to create new raw data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|params|object|None|False|Object containing related data or metadata|None|
|file|file|None|True|The actual file data|None|
|data_type|string|None|True|The type of raw data. Must match choices in the database|['Text', 'JSON']|
|title|string|None|True|Title for the raw data|None|
|data|string|None|False|The raw data if the upload type is 'metadata'|None|
|type|string|None|True|Upload type|['metadata', 'file']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "return_code": 0,
    "url": "/api/v1/raw_data/595070f7f47016014922a4ee/",
    "type": "RawData",
    "id": "595070f7f47016014922a4ee",
    "message": "Uploaded raw_data"
  }
}

```

#### Add PCAP

This action is used to create a new PCAP.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|False|Name of the source which provided this information|None|
|params|object|None|False|Additional data or metadata|None|
|file|file|None|True|The actual file data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "type": "PCAP",
    "id": "595070f6f47016014922a4ec",
    "url": "/api/v1/pcaps/595070f6f47016014922a4ec/",
    "return_code": 0,
    "message": "Uploaded pcap"
  }
}

```

#### Add Event

This action is used to create a new event.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|title|string|None|True|The title you wish to give this event|None|
|type|string|None|True|The STIX Event Type you wish to assign to this Event|['Application Compromise', 'Denial of Service', 'Distributed Denial of Service', 'Exploitation', 'Intel Sharing', 'Malicious Code', 'Phishing', 'Privileged Account Compromise', 'Scanning', 'Sensor Alert', 'Sniffing', 'Social Engineering', 'Spam', 'Strategic Web Compromise', 'Unauthorized Information Access', 'Unknown', 'Website Defacement']|
|description|string|None|True|description of what happened during this Event.|None|
|params|object|None|False|Object containing related data or metadata|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "id": "59507672f4701601480c8e05",
    "return_code": 0,
    "url": "/api/v1/events/59507672f4701601480c8e05/",
    "type": "Event",
    "message": "<div>Success! Click here to view the new event: <a href=\"/events/details/59507672f4701601480c8e05/\">voluptates</a></div>"
  }
}

```

#### Add Sample

This action is used to create a new sample.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|type|string|None|True|Upload type|['metadata', 'file']|
|file|file|None|True|The actual file data|None|
|params|object|None|False|Object containing related data or metadata|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "return_code": 0,
    "url": "/api/v1/samples/595070f8f47016014922a4f1/",
    "type": "Sample",
    "message": "Success: Updated sample <a href=\"/samples/details/2905ce7862c53530e91f8a0d8fc00e54/\">2905ce7862c53530e91f8a0d8fc00e54.</a>",
    "id": "595070f8f47016014922a4f1"
  }
}

```

#### Add IP

This action is used to create a new IP.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip|string|None|True|IP Address|None|
|source|string|None|False|Name of the source which provided this information|None|
|type|string|None|True|Type of IP Address|None|
|params|object|None|False|Additional data or metadata|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "url": "/api/v1/ips/595070f5f4701601480c8ddc/",
    "type": "IP",
    "return_code": 0,
    "message": "Updated existing IP: <a href=\"/ips/details/250.14.50.172/\">250.14.50.172</a>",
    "id": "595070f5f4701601480c8ddc"
  }
}

```

#### Add Indicator

This action is used to create a new indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|type|string|None|True|The CybOX Type associated with that Indicator|['API Key', 'AS Name', 'AS Number', 'Adjust Token', 'Bank account', 'Bitcoin account', 'CRX', 'Certificate Fingerprint', 'Certificate Name', 'Checksum CRC16', 'Command Line', 'Company name', 'Cookie Name', 'Country', 'Debug Path', 'Debug String', 'Destination Port', 'Device IO', 'Document from URL', 'Domain', 'Email Address', 'Email Address From', 'Email Address Sender', 'Email Boundary', 'Email HELO', 'Email Header Field', 'Email Message ID', 'Email Originating IP', 'Email Reply-To', 'Email Subject', 'Email X-Mailer', 'Email X-Originating IP', 'File Created', 'File Deleted', 'File Moved', 'File Name', 'File Opened', 'File Path', 'File Read', 'File Written', 'GET Parameter', 'HEX String', 'HTML ID', 'HTTP Request', 'HTTP Response Code', 'IMPHASH', 'IPv4 Address', 'IPv4 Subnet', 'IPv6 Address', 'IPv6 Subnet', 'Latitude', 'Launch Agent', 'Location', 'Longitude', 'MAC Address', 'MD5', 'Malware Name', 'Memory Alloc', 'Memory Protect', 'Memory Read', 'Memory Written', 'Mutant Created', 'Mutex', 'Name Server', 'Other File Operation', 'POST Data', 'Password', 'Password Salt', 'Payload Data', 'Payload Type', 'Pipe', 'Process Name', 'Protocol', 'Referer', 'Referer of Referer', 'Registrar', 'Registry Key', 'Registry Key Created', 'Registry Key Deleted', 'Registry Key Enumerated', 'Registry Key Monitored', 'Registry Key Opened', 'Registry Key Value Created', 'Registry Key Value Deleted', 'Registry Key Value Modified', 'Registry Key Value Queried', 'SHA1', 'SHA256', 'SMS Origin', 'SSDEEP', 'Service Name', 'Source Port', 'TS End', 'TS Start', 'Telephone', 'Time Created', 'Time Updated', 'Tracking ID', 'URI', 'User Agent', 'User ID', 'Victim IP', 'Volume Queried', 'WHOIS Address 1', 'WHOIS Address 2', 'WHOIS Name', 'WHOIS Registrant Email Address', 'WHOIS Telephone', 'Web Payload', 'Webstorage Key', 'XPI']|
|value|string|None|True|The value of the Indicator|None|
|params|object|None|False|Additional data or metadata|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|add_indicator_response|False|None|

Example output:

```

{
  "response": {
    "url": "/api/v1/indicators/595070f4f47016014922a4e7/",
    "return_code": 0,
    "type": "Indicator",
    "id": "595070f4f47016014922a4e7"
  }
}

```

#### Get Collection

This action is used to fetches a collection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|total|integer|10|False|Total number of items to return|None|
|params|object|None|False|Additional parameters|None|
|collection|string|None|True|Type of collection|['Actors', 'Actor Identifiers', 'Campaigns', 'Certificates', 'Domains', 'Emails', 'Events', 'Indicators', 'IPs', 'PCAPs', 'Raw Datas', 'Samples', 'Screenshots', 'Targets']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|collection_response|False|None|

Example output:

```

{
  "response": {
    "objects": [
      {
        "threat_types": [],
        "_id": "595074a6f4701601480c8dde",
        "relationships": [],
        "objects": [],
        "campaign": [
          {
            "confidence": "low",
            "date": "2017-06-26 02:42:46.189000",
            "name": "NetTraveler",
            "analyst": "nonroot"
          }
        ],
        "identifiers": [],
        "bucket_list": [],
        "created": "2017-06-26 02:42:46.189000",
        "sectors": [],
        "modified": "2017-06-26 02:42:46.190000",
        "tickets": [],
        "schema_version": 2,
        "motivations": [],
        "screenshots": [],
        "actions": [],
        "name": "Implemented tangible parallelism",
        "intended_effects": [],
        "status": "New",
        "source": [
          {
            "name": "Faker Vault",
            "instances": [
              {
                "date": "2017-06-26 02:42:46.189000",
                "analyst": "nonroot"
              }
            ]
          }
        ],
        "locations": [],
        "releasability": [],
        "aliases": [
          "facilis",
          "nulla"
        ],
        "description": "Reiciendis quas doloribus unde debitis consequatur aliquam corrupti.",
        "sophistications": []
      }
    ]
  }
}

```

#### Get Item

This action is used to fetches a single item.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|item_id|string|None|True|Unique ID of item|None|
|type|string|None|True|Item Type|['Actor', 'Actor Identifier', 'Campaign', 'Certificate', 'Domain', 'Email', 'Event', 'Indicator', 'IP', 'PCAP', 'Raw Data', 'Sample', 'Screenshot', 'Target']|
|params|object|None|False|Additional parameters|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|False|None|

Example output:

```

{
  "response": {
    "sophistications": [],
    "name": "Blah",
    "modified": "2017-06-27 02:41:23.804000",
    "tickets": [],
    "_id": "5951c5d33a097c01425d54e9",
    "source": [
      {
        "name": "FakerVault",
        "instances": [
          {
            "date": "2017-06-27 02:41:23.803000",
            "method": "",
            "reference": "",
            "analyst": "nonroot"
          }
        ]
      }
    ],
    "schema_version": 2,
    "intended_effects": [],
    "created": "2017-06-27 02:41:23.802000",
    "motivations": [],
    "bucket_list": [],
    "campaign": [],
    "screenshots": [],
    "aliases": [
      ""
    ],
    "status": "New",
    "objects": [],
    "releasability": [],
    "sectors": [],
    "locations": [],
    "relationships": [],
    "identifiers": [],
    "threat_types": [],
    "actions": []
  }
}

```

#### Add Certificate

This action is used to create a new certificate.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|params|object|None|False|Object containing related data or metadata|None|
|file|file|None|True|The actual file data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "url": "/api/v1/certificates/595070eff47016014922a4e1/",
    "message": "Uploaded certificate",
    "return_code": 0,
    "id": "595070eff47016014922a4e1",
    "type": "Certificate"
  }
}

```

#### Add Domain

This action is used to create a new domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|domain|string|None|True|The domain name|None|
|params|object|None|False|Object containing related data or metadata|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "url": "/api/v1/domains/595070f0f47016014922a4e3/",
    "type": "Domain",
    "message": "Updated existing domain: <a href=\"/domains/details/harmon-dunlap.net/\">harmon-dunlap.net</a>",
    "return_code": 0,
    "id": "595070f0f47016014922a4e3"
  }
}

```

#### Add Email

This action is used to create a new email.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Name of the source which provided this information|None|
|type|string|None|True|Upload type|['msg', 'eml', 'raw', 'yaml', 'fields']|
|file|file|None|True|The actual file |None|
|params|object|None|False|Object containing related data or metadata|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "message": "The upload file is not a valid Outlook file. It must be in OLE2 format (.msg)",
    "return_code": 1,
    "type": "Email"
  }
}

```

#### Add Campaign

This action is used to create a new campaign.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|params|object|None|False|Object containing related data or metadata|None|
|name|string|None|True|Name of the campaign|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|post_response|False|None|

Example output:

```

{
  "response": {
    "type": "Campaign",
    "return_code": 1,
    "message": "Need a Campaign name."
  }
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

CRITs comes with an authenticated API. It is disabled by default and must be enabled in the Control Panel.
Once it is enabled you must restart the web server for the URLs to be exposed.

Ensure that the user associated with the API key is subscribed to the `source`.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [CRITs](https://crits.github.io/)
* [CRITs Wiki](https://github.com/crits/crits/wiki)
* [pycrits fork](https://github.com/rpip/pycrits)
* [pycrits](https://github.com/crits/pycrits)

