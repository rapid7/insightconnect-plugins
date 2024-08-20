# Description

[MISP](http://www.misp-project.org/) is an open source threat sharing platform. Gather, store and then find correlations of indicators of compromise. Quality of data is determined by the open source community. This plugin utilizes the [MISP API](https://circl.lu/doc/misp/automation/index.html) and leverages the [pymisp](https://github.com/CIRCL/PyMISP) library

# Key Features

* Library of known threats
* Global sharing platform of known threats

# Requirements

* MISP server
* Automation key for MISP server (found under Automation -> API key section in MISP server)

# Supported Product Versions

* 2.4.194

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|automation_code|credential_secret_key|None|True|API/Automation code of MISP server|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|ssl|boolean|True|True|If true will use SSL for communication to MISP|None|True|None|None|
|url|string|None|True|URL of the MISP server e.g. https://example.com|None|https://example.com|None|None|

Example input:

```
{
  "automation_code": "9de5069c5afe602b2ea0a04b66beb2c0",
  "ssl": true,
  "url": "https://example.com"
}
```

## Technical Details

### Actions


#### Add Attribute

This action is used to add an attribute to an event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|category|string|None|True|The attribute category e.g. external analysis, network activity|None|Example category|None|None|
|comment|string|None|False|Optional comment to add to attribute|None|Example comment|None|None|
|event|string|None|True|ID of event to append to|None|1099|None|None|
|type_value|string|None|True|The Type of attribute e.g. URL, SHA256|None|URL|None|None|
|value|string|None|True|The Value of the attribute e.g. for a URL|None|https://example.com|None|None|
  
Example input:

```
{
  "category": "Example category",
  "comment": "Example comment",
  "event": 1099,
  "type_value": "URL",
  "value": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attribute|attribute|False|A summary of the added attribute|{'id': '173007', 'event_id': '777', 'category': 'Network activity', 'type': 'url', 'value1': 'https://example.com', 'value2': '', 'to_ids': False, 'uuid': '5b05a903-f35c-42aa-8ed2-64d60a041dcd', 'timestamp': '1527097603', 'distribution': '0', 'sharing_group_id': '0', 'comment': 'this is a test', 'deleted': False, 'disable_correlation': False, 'value': 'https://malware.com'}|
  
Example output:

```
{
  "attribute": {
    "category": "Network activity",
    "comment": "this is a test",
    "deleted": false,
    "disable_correlation": false,
    "distribution": "0",
    "event_id": "777",
    "id": "173007",
    "sharing_group_id": "0",
    "timestamp": "1527097603",
    "to_ids": false,
    "type": "url",
    "uuid": "5b05a903-f35c-42aa-8ed2-64d60a041dcd",
    "value": "https://malware.com",
    "value1": "https://example.com",
    "value2": ""
  }
}
```

#### Add Sightings

This action is used to add sightings to organization

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|sightings|[]string|None|True|Event sighting|None|["sighting"]|None|None|
  
Example input:

```
{
  "sightings": [
    "sighting"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Whether any of the sightings provided were added|True|
  
Example output:

```
{
  "status": true
}
```

#### Add Tag

This action is used to add tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event|string|None|True|Event ID to append to|None|1099|None|None|
|tag|string|None|True|Event tag to add|None|Example tag|None|None|
  
Example input:

```
{
  "event": 1099,
  "tag": "Example tag"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Tag add status|True|
  
Example output:

```
{
  "status": true
}
```

#### Create Event

This action is used to create a MISP event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analysis|string|0|False|The analysis level of the event|["2", "1", "0"]|0|None|None|
|distribution|string|This Organization|False|Distribution type|["This Community", "This Organization", "Connected Communities", "All Communities"]|This Organization|None|None|
|info|string|None|True|Extra event information|None|Example information|None|None|
|org_id|string|None|False|Organization ID|None|12345|None|None|
|orgc_id|string|None|False|Organization C ID|None|12345|None|None|
|published|boolean|True|True|Published event?|None|True|None|None|
|sharing_group_id|string|None|False|Sharing group ID|None|1|None|None|
|threat_level_id|string|1|True|Importance of the threat|["4", "3", "2", "1"]|1|None|None|
  
Example input:

```
{
  "analysis": 0,
  "distribution": "This Organization",
  "info": "Example information",
  "org_id": 12345,
  "orgc_id": 12345,
  "published": true,
  "sharing_group_id": 1,
  "threat_level_id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|Attribute|[]base_output|False|Attribute|[]|
|RelatedEvent|[]object|False|Related event|[]|
|analysis|string|False|Analysis|0|
|attribute_count|string|False|Attribute count|1|
|date|date|False|Date|1991-01-15|
|disable_correlation|boolean|False|Disable correlation|False|
|distribution|string|False|Distribution|0|
|event_creator_email|string|False|Event creator's email|user@example.com|
|id|string|False|Event ID|12345|
|info|string|False|Info|logged source ip|
|locked|boolean|False|Locked|True|
|org_id|string|False|Organization ID|12345|
|orgc_id|string|False|Organization C ID|12345|
|proposal_email_lock|boolean|False|Lock proposal email|True|
|publish_timestamp|string|False|Publish timestamp|1617875568|
|published|boolean|False|Published|False|
|sharing_group_id|string|False|Sharing group ID|1|
|threat_level_id|string|False|Threat level ID|1|
|timestamp|string|False|Timestamp|1617875568|
|uuid|string|False|Unique event ID|c99506a6-1255-4b71-afa5-7b8ba48c3b1b|
  
Example output:

```
{
  "Attribute": [],
  "RelatedEvent": [],
  "analysis": 0,
  "attribute_count": 1,
  "date": "1991-01-15",
  "disable_correlation": false,
  "distribution": 0,
  "event_creator_email": "user@example.com",
  "id": 12345,
  "info": "logged source ip",
  "locked": true,
  "org_id": 12345,
  "orgc_id": 12345,
  "proposal_email_lock": true,
  "publish_timestamp": 1617875568,
  "published": false,
  "sharing_group_id": 1,
  "threat_level_id": 1,
  "timestamp": 1617875568,
  "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b"
}
```

#### Export Attributes

This action is used to export all attributes in CSV format

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|category|string|None|False|Attribute category|None|Example attribute category|None|None|
|event_id|[]string|None|False|Array of events to download|None|["1"]|None|None|
|from|string|None|False|From date E.g. 2015-02-15T00:00:00|None|2015-02-15T00:00:00|None|None|
|include|boolean|True|True|Include attributes not marked as to_ids|None|True|None|None|
|include_context|boolean|True|True|Include event data with each attribute|None|True|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|["tag"]|None|None|
|to|string|None|False|To date E.g. 2015-02-17T00:00:00|None|2015-02-17T00:00:00|None|None|
|type|string|None|False|Attribute type e.g. URL, SHA256|None|URL|None|None|
  
Example input:

```
{
  "category": "Example attribute category",
  "event_id": [
    "1"
  ],
  "from": "2015-02-15",
  "include": true,
  "include_context": true,
  "last": "5d",
  "tags": [
    "tag"
  ],
  "to": "2015-02-17",
  "type": "URL"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attributes|bytes|False|Attributes output|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "attributes": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Export Events

This action is used to export all events in XML format

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|encode_attachments|boolean|True|True|Encode attachments in export|None|True|None|None|
|event_id|string|None|False|Specify single event to export|None|1099|None|None|
|from|string|None|False|From date E.g. 2015-02-15T00:00:00|None|2015-02-15T00:00:00|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|["tag"]|None|None|
|to|string|None|False|To date E.g. 2015-02-17T00:00:00|None|2015-02-17T00:00:00|None|None|
  
Example input:

```
{
  "encode_attachments": true,
  "event_id": 1099,
  "from": "2015-02-15",
  "last": "5d",
  "tags": [
    "tag"
  ],
  "to": "2015-02-17"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|bytes|False|Event output|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "events": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Export RPZ

This action is used to export RPZ zone files

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event_id|string|None|False|Specify single event to export|None|1099|None|None|
|from_date|string|None|False|From date E.g. 2015-02-15T00:00:00|None|2015-02-15T00:00:00|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|["example tag"]|None|None|
|to_date|string|None|False|To date E.g. 2015-02-17T00:00:00|None|2015-02-17T00:00:00|None|None|
  
Example input:

```
{
  "event_id": 1099,
  "from_date": "2015-02-15",
  "tags": [
    "example tag"
  ],
  "to_date": "2015-02-17"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rpz|bytes|False|RPZ output|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "rpz": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Rules Export

This action is used to export Snort or Suricata rules

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event_id|string|None|False|Narrow results to a single event|None|1099|None|None|
|format|string|None|True|Export format as either Suricata or Snort|["suricata", "snort"]|suricata|None|None|
|frame|boolean|True|True|Commented out explanation framing the data|None|True|None|None|
|from|string|None|False|From date E.g. 2015-02-15T00:00:00|None|2015-02-15T00:00:00|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|["example tag"]|None|None|
|to|string|None|False|To date E.g. 2015-02-17T00:00:00|None|2015-02-17T00:00:00|None|None|
  
Example input:

```
{
  "event_id": 1099,
  "format": "suricata",
  "frame": true,
  "from": "2015-02-15",
  "last": "5d",
  "tags": [
    "example tag"
  ],
  "to": "2015-02-17"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rules|bytes|False|Rules output|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "rules": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Export STIX

This action is used to export events in STIX format

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|encode_attachments|boolean|True|True|Encode attachments in export|None|True|None|None|
|event_id|string|None|False|Specify single event to export|None|1099|None|None|
|from|string|None|False|From date E.g. 2015-02-15T00:00:00|None|2015-02-15T00:00:00|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|["example tag"]|None|None|
|to|string|None|False|To date E.g. 2015-02-17T00:00:00|None|2015-02-17T00:00:00|None|None|
  
Example input:

```
{
  "encode_attachments": true,
  "event_id": 1099,
  "from": "2015-02-15",
  "last": "5d",
  "tags": [
    "example tag"
  ],
  "to": "2015-02-17"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|stix|bytes|False|STIX output|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "stix": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Find Event

This action is used to receive events based on criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event_id|string|None|True|Event ID e.g. 123|None|1099|None|None|
  
Example input:

```
{
  "event_id": 1099
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|errors|[]string|False|Errors|["No errors."]|
|event|Event|False|Event|{'ShadowAttribute': [], 'locked': False, 'proposal_email_lock': False, 'published': False, 'event_creator_email': 'user@example.com', 'RelatedEvent': [], 'analysis': '1', 'org_id': '1', 'distribution': '2', 'Tag': [{'hide_tag': False, 'name': 'Phishing', 'exportable': True, 'id': '167', 'colour': '#856c13'}], 'Galaxy': [], 'id': '773', 'Attribute': [{'ShadowAttribute': [], 'timestamp': '1516127675', 'id': '172996', 'value': 'http://badguy.net', 'sharing_group_id': '0', 'event_id': '773', 'type': 'url', 'distribution': '5', 'disable_correlation': False, 'to_ids': False, 'deleted': False, 'category': 'Network activity', 'comment': 'URLs found in suspected phishing e-mail', 'uuid': '5a5e45bb-c994-46da-9cb5-711f0a04180d'}, {'ShadowAttribute': [], 'timestamp': '1516127671', 'id': '172999', 'value': 'Hey,Check out this cool link!', 'sharing_group_id': '0', 'event_id': '773', 'type': 'email-subject', 'distribution': '5', 'disable_correlation': False, 'to_ids': True, 'deleted': False, 'category': 'Payload delivery', 'comment': 'Suspected phishing e-mail with this subject', 'uuid': '5a5e45b7-8500-443b-8c38-03780a04180d'}], 'Orgc': {'name': 'MISP', 'id': '1', 'uuid': '56ef3277-1ad4-42f6-b90b-04e5c0a83832'}, 'orgc_id': '1', 'attribute_count': '4', 'sharing_group_id': '0', 'date': '2018-01-16', 'Org': {'name': 'MISP', 'id': '1', 'uuid': '56ef3277-1ad4-42f6-b90b-04e5c0a83832'}, 'timestamp': '1516127664', 'disable_correlation': False, 'publish_timestamp': '1516127661', 'info': 'Test from Komand', 'threat_level_id': '2', 'uuid': '5a5e45ad-55b4-4e8e-8c97-711c0a04180d'}|
|message|string|False|Message|Event found|
  
Example output:

```
{
  "errors": [
    "No errors."
  ],
  "event": {
    "Attribute": [
      {
        "ShadowAttribute": [],
        "category": "Network activity",
        "comment": "URLs found in suspected phishing e-mail",
        "deleted": false,
        "disable_correlation": false,
        "distribution": "5",
        "event_id": "773",
        "id": "172996",
        "sharing_group_id": "0",
        "timestamp": "1516127675",
        "to_ids": false,
        "type": "url",
        "uuid": "5a5e45bb-c994-46da-9cb5-711f0a04180d",
        "value": "http://badguy.net"
      },
      {
        "ShadowAttribute": [],
        "category": "Payload delivery",
        "comment": "Suspected phishing e-mail with this subject",
        "deleted": false,
        "disable_correlation": false,
        "distribution": "5",
        "event_id": "773",
        "id": "172999",
        "sharing_group_id": "0",
        "timestamp": "1516127671",
        "to_ids": true,
        "type": "email-subject",
        "uuid": "5a5e45b7-8500-443b-8c38-03780a04180d",
        "value": "Hey,Check out this cool link!"
      }
    ],
    "Galaxy": [],
    "Org": {
      "id": "1",
      "name": "MISP",
      "uuid": "56ef3277-1ad4-42f6-b90b-04e5c0a83832"
    },
    "Orgc": {
      "id": "1",
      "name": "MISP",
      "uuid": "56ef3277-1ad4-42f6-b90b-04e5c0a83832"
    },
    "RelatedEvent": [],
    "ShadowAttribute": [],
    "Tag": [
      {
        "colour": "#856c13",
        "exportable": true,
        "hide_tag": false,
        "id": "167",
        "name": "Phishing"
      }
    ],
    "analysis": "1",
    "attribute_count": "4",
    "date": "2018-01-16",
    "disable_correlation": false,
    "distribution": "2",
    "event_creator_email": "user@example.com",
    "id": "773",
    "info": "Test from Komand",
    "locked": false,
    "org_id": "1",
    "orgc_id": "1",
    "proposal_email_lock": false,
    "publish_timestamp": "1516127661",
    "published": false,
    "sharing_group_id": "0",
    "threat_level_id": "2",
    "timestamp": "1516127664",
    "uuid": "5a5e45ad-55b4-4e8e-8c97-711c0a04180d"
  },
  "message": "Event found"
}
```

#### Publish

This action is used to publish an event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event|string|None|False|Search by event ID|None|1099|None|None|
  
Example input:

```
{
  "event": 1099
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|published|published|False|Info on published event|{'name': 'Alert', 'message': 'Job queued', 'url': '/events/alert/776', 'id': '776'}|
  
Example output:

```
{
  "published": {
    "id": "776",
    "message": "Job queued",
    "name": "Alert",
    "url": "/events/alert/776"
  }
}
```

#### Remove Tag

This action is used to remove tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event|string|None|True|Event ID to append to|None|1099|None|None|
|tag|string|None|True|Event tag for search|None|Example tag|None|None|
  
Example input:

```
{
  "event": 1099,
  "tag": "Example tag"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Tag add status|True|
  
Example output:

```
{
  "status": true
}
```

#### Search Events

This action is used to search for events

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analysis|string|Do not search on|False|Search by analysis level|["Do not search on", "Initial", "Ongoing", "Completed"]|Do not search on|None|None|
|category|string|None|False|Search by attribute category|None|Person|None|None|
|date_from|string|None|False|Search after this date e.g. 2018-03-22T00:00:00|None|2018-03-22T00:00:00|None|None|
|date_until|string|None|False|Search before this date e.g. 2018-03-22T00:00:00|None|2018-03-22T00:00:00|None|None|
|event|string|None|False|Search by event ID|None|1099|None|None|
|organization|string|None|False|Search by organization|None|Organization name|None|None|
|published|string|Do not search on|False|Search by if published|["Do not search on", "True", "False"]|Do not search on|None|None|
|tag|string|None|False|Search by tag|None|tag|None|None|
|threat_level|string|Do not search on|False|Search by threat level|["Do not search on", "Undefined", "Low", "Medium", "High"]|Do not search on|None|None|
|type_attribute|string|None|False|Search by any valid MISP attribute type|None|text|None|None|
|values|[]string|None|False|Search by given values of attributes value field|None|["example_one", "example_two"]|None|None|
  
Example input:

```
{
  "analysis": "Do not search on",
  "category": "Person",
  "date_from": "2018-03-22",
  "date_until": "2018-03-22",
  "event": 1099,
  "organization": "Organization name",
  "published": "Do not search on",
  "tag": "tag",
  "threat_level": "Do not search on",
  "type_attribute": "text",
  "values": [
    "example_one",
    "example_two"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|event_list|[]string|False|A list of event IDs that match the search|["1", "2"]|
  
Example output:

```
{
  "event_list": [
    "1",
    "2"
  ]
}
```
### Triggers


#### Search for Tag

This trigger is used to this trigger will search MISP for any events with a specified tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|60|True|How frequently (in seconds) to trigger a search|None|60|None|None|
|remove|boolean|False|True|If true the tag will be removed|None|False|None|None|
|tag|string|None|True|The tag to search for|None|Example tag|None|None|
  
Example input:

```
{
  "interval": 60,
  "remove": false,
  "tag": "Example tag"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]string|True|A list of event_ids with the tag|["1098", "1099"]|
  
Example output:

```
{
  "events": [
    "1098",
    "1099"
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**org**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|ID|None|
|Name|string|None|None|Name|None|
|UUID|string|None|None|UUID|None|
  
**base_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|None|Attribute category|None|
|Comment|string|None|None|Attribute comment|None|
|Deleted|boolean|None|None|Deleted?|None|
|Email|string|None|None|Email address|None|
|Event ID|string|None|None|Event ID|None|
|Event Organization ID|string|None|None|Organization ID|None|
|ID|string|None|None|Email ID|None|
|Old ID|string|None|None|Old ID|None|
|Timestamp|string|None|None|Time created|None|
|To IDs|boolean|None|None|To IDs|None|
|Type|string|None|None|Type of email|None|
|UUID|string|None|None|Unique ID|None|
|Value|string|None|None|Value|None|
  
**comment_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|None|Attribute comment|Example attribute comment|
|Comment|string|None|None|Comment for context|Example context comment|
|Distribution|string|None|None|Distribution type|All Communities|
|Event ID|string|None|None|Event ID to append to|1099|
  
**link_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|None|Attribute comment|Example attribute comment|
|Distribution|string|None|None|Distribution type|All Communities|
|Event ID|string|None|None|Event ID to append to|1099|
|Link|string|None|None|Link|Link|
  
**other_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|None|Attribute comment|Add UUID to an event|
|Distribution|string|None|None|Distribution type|All Communities|
|Event ID|string|None|None|Event ID to append to|1099|
|Other|string|None|None|Other|Other|
  
**text_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|None|Attribute comment|Updating title|
|Distribution|string|None|None|Distribution type|All Communities|
|Event ID|string|None|None|Event ID to append to|1099|
|Text|string|None|None|Text|Example text|
  
**base_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|None|Attribute comment|None|
|Distribution|string|None|None|Distribution type|None|
|Event ID|string|None|None|Event ID to append to|None|
|Value|string|None|None|Input value|None|
  
**SharingGroup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**Tag**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Colour|string|None|None|Colour|None|
|Exportable|boolean|None|None|Exportable|None|
|Hide Tag|boolean|None|None|Hide Tag|None|
|ID|string|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**Event**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Org|SharingGroup|None|None|None|None|
|Orgc|SharingGroup|None|None|None|None|
|Sharing Group|SharingGroup|None|None|Sharing group|None|
|Tag|[]Tag|None|None|None|None|
|Analysis|string|None|None|None|None|
|Attribute Count|string|None|None|None|None|
|Date|string|None|None|None|None|
|Disable Correlation|boolean|None|None|None|None|
|Distribution|string|None|None|None|None|
|ID|string|None|None|None|None|
|Info|string|None|None|Info|None|
|Locked|boolean|None|None|None|None|
|Org ID|string|None|None|None|None|
|Org ID|string|None|None|Org ID|None|
|Proposal Email Lock|boolean|None|None|None|None|
|Publish Timestamp|string|None|None|None|None|
|Published|boolean|None|None|None|None|
|Sharing Group ID|string|None|None|None|None|
|Threat Level ID|string|None|None|None|None|
|Timestamp|string|None|None|None|None|
|UUID|string|None|None|None|None|
  
**attribute**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|None|None|None|
|Comment|string|None|None|None|None|
|Deleted|boolean|None|None|None|None|
|Disable Correlation|boolean|None|None|None|None|
|Distribution|string|None|None|None|None|
|Event ID|string|None|None|None|None|
|ID|string|None|None|None|None|
|Sharing Group ID|string|None|None|None|None|
|TimeStamp|string|None|None|None|None|
|To IDs|boolean|None|None|None|None|
|Type|string|None|None|None|None|
|UUID|string|None|None|None|None|
|Value|string|None|None|None|None|
|Value1|string|None|None|None|None|
|Value2|string|None|None|None|None|
  
**published**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|None|None|
|Message|string|None|None|None|None|
|Name|string|None|None|None|None|
|URL|string|None|None|None|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 6.0.0 - Removed deprecated actions and updated API calls for several actions
* 5.0.3 - SSL configuration for all actions
* 5.0.2 - Update to latest SDK | Bumping `pymisp` version
* 5.0.1 - Set default value for fields `analysis`, `published`, `threat_level` in Search Events action | Update insight connect SDK to 4
* 5.0.0 - New fields added to Search Events action for `values`, `category` and `type_attribute`
* 4.0.0 - New spec and help.md format for the Extension Library | Fix spelling of variable titled Commented Explanation
* 3.0.0 - Fixed issue where Add URLs, Add Context, Add Email Sender, Add Email Subject and Add Email Recipient actions sent requests as a proposal | Fixed an issue where the distribution list was set incorrectly within Add URLs, Add Context, Create an Event, Add Email Sender, Add Email Subject, Add Email Recipient actions
* 2.0.0 - Updated to new credential types | Update `hostname` variable in Connection to `url`
* 1.0.0 - Add trigger. Add actions: Add Attachment, Remove Tag, Search Events, Publish. Support web server mode
* 0.4.1 - Bug fix for CI tool incorrectly uploading plugins
* 0.4.0 - Added add attachment feature | Update to v2 architecture
* 0.3.0 - Add Find Event action
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - 8 new actions to add data to MISP: Add Email Recipient, Add Email Sender, Add Email Subject, Add Sightings, Add Tag, Add Context, Add URL, and Create An Event
* 0.1.0 - Initial plugin

# Links

* [MISP](http://www.misp-project.org/)

## References

* [MISP](http://www.misp-project.org/)
* [MISP API](https://circl.lu/doc/misp/automation/index.html)
* [pymisp](https://github.com/MISP/PyMISP)