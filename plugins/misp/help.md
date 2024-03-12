# Description

[MISP](http://www.misp-project.org/) is an open source threat sharing platform.
Gather, store and then find correlations of indicators of compromise. Quality of data is determined by the open source community.
This plugin utilizes the [MISP API](https://circl.lu/doc/misp/automation/index.html) and leverages the [pymisp](https://github.com/CIRCL/PyMISP) library.

# Key Features

* Library of known threats
* Global sharing platform of know threats

# Requirements

* MISP server
* Username and Password

# Supported Product Versions
  
* 2.4.187

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|automation_code|credential_secret_key|None|True|API/Automation code of MISP server|None|9de5069c5afe602b2ea0a04b66beb2c0|
|ssl|boolean|True|True|If true will use SSL for communication to MISP|None|True|
|url|string|None|True|URL of the MISP server e.g. https://misp-2-4.example.com|None|https://example.com|
  
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


#### Add Attachment
  
This action is used to add attachment to event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachment|bytes|None|True|Attachment for event|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|event|string|None|True|Event ID to append to|None|1099|
|filename|string|None|False|Filename of attachment|None|setup.exe|
  
Example input:

```
{
  "attachment": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "event": 1099,
  "filename": "setup.exe"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Status of add attachment|True|
  
Example output:

```
{
  "status": true
}
```

#### Add Attribute
  
This action is used to add an attribute to an event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|category|string|None|True|The attribute category e.g. external analysis, network activity|None|Example category|
|comment|string|None|False|Optional comment to add to attribute|None|Example comment|
|event|string|None|True|ID of event to append to|None|1099|
|type_value|string|None|True|The Type of attribute e.g. URL, SHA256|None|URL|
|value|string|None|True|The Value of the attribute e.g. for a URL https://malware.com|None|https://example.com|
  
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
|attribute|attribute|False|A summary of the added attribute|{'id': '173007', 'event_id': '777', 'category': 'Network activity', 'type': 'url', 'value1': 'https://malware.com', 'value2': '', 'to_ids': False, 'uuid': '5b05a903-f35c-42aa-8ed2-64d60a041dcd', 'timestamp': '1527097603', 'distribution': '0', 'sharing_group_id': '0', 'comment': 'this is a test', 'deleted': False, 'disable_correlation': False, 'value': 'https://malware.com'}|
  
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
    "value1": "https://malware.com",
    "value2": ""
  }
}
```

#### Add Context
  
This action is used to add context

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|comment_input|None|True|Comment|None|Example comment|
|link|link_input|None|True|Link|None|Example link|
|other|other_input|None|True|Other|None|Example|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|False|
|text|text_input|None|True|Text|None|Example text|
  
Example input:

```
{
  "comment": "Example comment",
  "link": "Example link",
  "other": "Example",
  "proposal": false,
  "text": "Example text"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Context add status|True|
  
Example output:

```
{
  "status": true
}
```

#### Add Email Recipient
  
This action is used to add email recipient to event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Attribute comment|None|Example comment|
|distribution|string|None|True|Distribution type|["This Community", "This Organization", "Connected Communities", "All Communities"]|All Communities|
|event|string|None|True|Event ID to append to|None|1099|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|False|
|recipient|string|None|True|Recipient email address|None|user@example.com|
  
Example input:

```
{
  "comment": "Example comment",
  "distribution": "All Communities",
  "event": 1099,
  "proposal": false,
  "recipient": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|True|Email recipient add status|True|
  
Example output:

```
{
  "status": true
}
```

#### Add Email Sender
  
This action is used to add email sender to event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Attribute comment|None|Example comment|
|distribution|string|None|True|Distribution type|["This Community", "This Organization", "Connected Communities", "All Communities"]|All Communities|
|event|string|None|True|Event ID to append to|None|1099|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|False|
|sender|string|None|True|Sender email address|None|user@example.com|
  
Example input:

```
{
  "comment": "Example comment",
  "distribution": "All Communities",
  "event": 1099,
  "proposal": false,
  "sender": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|True|Email sender add status|True|
  
Example output:

```
{
  "status": true
}
```

#### Add Email Subject
  
This action is used to add email subject to event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Attribute comment|None|Example comment|
|distribution|string|None|True|Distribution type|["This Community", "This Organization", "Connected Communities", "All Communities"]|All Communities|
|event|string|None|True|Event ID to append to|None|1099|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|False|
|subject|string|None|True|Email subject|None|Example subject|
  
Example input:

```
{
  "comment": "Example comment",
  "distribution": "All Communities",
  "event": 1099,
  "proposal": false,
  "subject": "Example subject"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|True|Email subject add status|True|
  
Example output:

```
{
  "status": true
}
```

#### Add Sightings
  
This action is used to add sightings to organization

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|sightings|[]string|None|True|Event sightings E.g. sighting, false-positive, expiration|None|["sighting"]|
  
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
|status|boolean|False|Sightings add status|True|
  
Example output:

```
{
  "status": true
}
```

#### Add Tag
  
This action is used to add tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event|string|None|True|Event ID to append to|None|1099|
|tag|string|None|True|Event tag to add|None|Example tag|
  
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

#### Add URLs
  
This action is used to add URLs to event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|False|Attribute comment|None|Example comment|
|distribution|string|None|False|Distribution type|["This Community", "This Organization", "Connected Communities", "All Communities"]|All Communities|
|event|string|None|False|Event ID to append to|None|1099|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|False|
|urls|[]string|None|False|URLs to add|None|["https://example.com"]|
  
Example input:

```
{
  "comment": "Example comment",
  "distribution": "All Communities",
  "event": 1099,
  "proposal": false,
  "urls": [
    "https://example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|URL add status|True|
  
Example output:

```
{
  "status": true
}
```

#### Create Event
  
This action is used to create a MISP event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analysis|string|0|False|The analysis level of the event|["2", "1", "0"]|0|
|distribution|string|This Organization|False|Distribution type|["This Community", "This Organization", "Connected Communities", "All Communities"]|This Organization|
|info|string|None|True|Extra event information|None|Example information|
|org_id|string|None|False|Organization ID|None|12345|
|orgc_id|string|None|False|Organization C ID|None|12345|
|published|boolean|True|True|Published event?|None|True|
|sharing_group_id|string|None|False|Sharing group ID|None|1|
|threat_level_id|string|1|True|Importance of the threat|["4", "3", "2", "1"]|1|
  
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

#### Download Attachment
  
This action is used to download attachment

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attribute_id|string|None|True|Attribute ID of attachment or malware sample|None|1|
  
Example input:

```
{
  "attribute_id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attachment|bytes|False|Attachment|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "attachment": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Export Attributes
  
This action is used to export all attributes in CSV format

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|category|string|None|False|Attribute category|None|Example attribute category|
|event_id|[]string|None|False|Array of events to download|None|["1"]|
|from|string|None|False|From date E.g. 2015-02-15|None|2015-02-15|
|include|boolean|True|True|Include attributes not marked as to_ids|None|True|
|include_context|boolean|True|True|Include event data with each attribute|None|True|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|
|tags|[]string|None|False|Array of tags to include in results|None|["tag"]|
|to|string|None|False|To date E.g. 2015-02-17|None|2015-02-17|
|type|string|None|False|Attribute type e.g. URL, SHA256|None|URL|
  
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|encode_attachments|boolean|True|True|Encode attachments in export|None|True|
|event_id|string|None|False|Specify single event to export|None|1099|
|from|string|None|False|From date E.g. 2015-02-15|None|2015-02-15|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|
|tags|[]string|None|False|Array of tags to include in results|None|["tag"]|
|to|string|None|False|To date E.g. 2015-02-17|None|2015-02-17|
  
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

#### Export Hashes
  
This action is used to export hashes from HIDS database

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|format|string|None|True|Export format as either MD5 or SHA1|["md5", "sha1"]|md5|
|from|string|None|False|From date E.g. 2015-02-15|None|2015-02-15|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|
|tags|[]string|None|False|Array of tags to include in results|None|["example tag"]|
|to|string|None|False|To date E.g. 2015-02-17|None|2015-02-17|
  
Example input:

```
{
  "format": "md5",
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
|hashes|bytes|False|Hashes|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "hashes": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Export RPZ
  
This action is used to export RPZ zone files

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event_id|string|None|False|Specify single event to export|None|1099|
|from|string|None|False|From date E.g. 2015-02-15|None|2015-02-15|
|tags|[]string|None|False|Array of tags to include in results|None|["example tag"]|
|to|string|None|False|To date E.g. 2015-02-17|None|2015-02-17|
  
Example input:

```
{
  "event_id": 1099,
  "from": "2015-02-15",
  "tags": [
    "example tag"
  ],
  "to": "2015-02-17"
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event_id|string|None|False|Narrow results to a single event|None|1099|
|format|string|None|True|Export format as either Suricata or Snort|["suricata", "snort"]|suricata|
|frame|boolean|True|True|Commented out explanation framing the data|None|True|
|from|string|None|False|From date E.g. 2015-02-15|None|2015-02-15|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|
|tags|[]string|None|False|Array of tags to include in results|None|["example tag"]|
|to|string|None|False|To date E.g. 2015-02-17|None|2015-02-17|
  
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|encode_attachments|boolean|True|True|Encode attachments in export|None|True|
|event_id|string|None|False|Specify single event to export|None|1099|
|from|string|None|False|From date E.g. 2015-02-15|None|2015-02-15|
|last|string|None|False|Events within x amount of time E.g. 5d|None|5d|
|tags|[]string|None|False|Array of tags to include in results|None|["example tag"]|
|to|string|None|False|To date E.g. 2015-02-17|None|2015-02-17|
  
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event_id|string|None|True|Event ID e.g. 123|None|1099|
  
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event|string|None|False|Search by event ID|None|1099|
  
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event|string|None|True|Event ID to append to|None|1099|
|tag|string|None|True|Event tag for search|None|Example tag|
  
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analysis|string|Do not search on|False|Search by analysis level|["Do not search on", "Initial", "Ongoing", "Completed"]|Do not search on|
|category|string|None|False|Search by attribute category|None|Person|
|date_from|string|None|False|Search after this date e.g. 2018-03-22|None|2018-03-22|
|date_until|string|None|False|Search before this date e.g. 2018-03-22|None|2018-03-22|
|event|string|None|False|Search by event ID|None|1099|
|organization|string|None|False|Search by organization|None|Organization name|
|published|string|Do not search on|False|Search by if published|["Do not search on", "True", "False"]|Do not search on|
|tag|string|None|False|Search by tag|None|tag|
|threat_level|string|Do not search on|False|Search by threat level|["Do not search on", "Undefined", "Low", "Medium", "High"]|Do not search on|
|type_attribute|string|None|False|Search by any valid MISP attribute type|None|text|
|values|[]string|None|False|Search by given values of attributes value field|None|["example_one", "example_two"]|
  
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|60|True|How frequently (in seconds) to trigger a search|None|60|
|remove|boolean|False|True|If true the tag will be removed|None|False|
|tag|string|None|True|The tag to search for|None|Example tag|
  
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
  
*There is no troubleshooting for this plugin.*

# Version History

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
