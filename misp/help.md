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

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|automation_code|credential_secret_key|None|True|API/Automation code of MISP server|None|None|
|ssl|boolean|None|True|If true will use SSL for communication to MISP|None|None|
|url|string|None|True|URL of the MISP server e.g. https://misp-2-4.example.com|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Add Context

This action is used to add context. This action returns `true` or `false` on whether the context was successfully added.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|comment_input|None|True|Comment|None|None|
|link|link_input|None|True|Link|None|None|
|other|other_input|None|True|Other|None|None|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|None|
|text|text_input|None|True|Text|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Context add status|

Example output:

```

{
 "status": true
}

```

#### Export Events

This action is used to export all events in XML format.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|encode_attachments|boolean|True|True|Encode attachments in export|None|None|
|event_id|string|None|False|Specify single event to export|None|None|
|from|string|None|False|From date E.g. 2015-02-15|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|None|
|to|string|None|False|To date E.g. 2015-02-17|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|bytes|False|Event output|

#### Create Event

This action is used to create a MISP event.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analysis|string|None|False|The analysis level of the event|['2', '1', '0']|None|
|distribution|string|This Organization|False|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|None|
|info|string|None|True|Extra event information|None|None|
|org_id|string|None|False|Organization ID|None|None|
|orgc_id|string|None|False|Organization C ID|None|None|
|published|boolean|None|True|Published event?|None|None|
|sharing_group_id|string|None|False|Sharing group ID|None|None|
|threat_level_id|string|None|True|Importance of the threat|['4', '3', '2', '1']|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attribute|[]base_output|False|Attribute|
|RelatedEvent|[]object|False|Related event|
|analysis|string|False|Analysis|
|attribute_count|string|False|Attribute count|
|date|date|False|Date|
|disable_correlation|boolean|False|Disable correlation|
|distribution|string|False|Distribution|
|event_creator_email|string|False|Event creator's email|
|id|string|False|Event ID|
|info|string|False|Info|
|locked|boolean|False|Locked|
|org_id|string|False|Organization ID|
|orgc_id|string|False|Organization C ID|
|proposal_email_lock|boolean|False|Lock proposal email|
|publish_timestamp|string|False|Publish timestamp|
|published|boolean|False|Published|
|sharing_group_id|string|False|Sharing group ID|
|threat_level_id|string|False|Threat level ID|
|timestamp|string|False|Timestamp|
|uuid|string|False|Unique event ID|

#### Export RPZ

This action is used to export RPZ zone files.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event_id|string|None|False|Specify single event to export|None|None|
|from|string|None|False|From date E.g. 2015-02-15|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|None|
|to|string|None|False|To date E.g. 2015-02-17|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rpz|bytes|False|RPZ output|

#### Add Tag

This action is used to add a tag. The event tag must already exist in MISP. This action returns `true` or `false` on whether the tag successfully added.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event|string|None|True|Event ID to append to|None|None|
|tag|string|None|True|Event tag to add|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Tag add status|

Example output:

```

{
 "status": true
}

```

#### Export STIX

This action is used to export events in STIX format.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|encode_attachments|boolean|True|True|Encode attachments in export|None|None|
|event_id|string|None|False|Specify single event to export|None|None|
|from|string|None|False|From date E.g. 2015-02-15|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|None|
|to|string|None|False|To date E.g. 2015-02-17|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stix|bytes|False|STIX output|

#### Add Sightings

This action is used to add sightings to an organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|sightings|[]string|None|True|Event sightings|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Sightings add status|

Example output:

```

{
 "status": true
}

```

#### Add URLs

This action is used to add URLs to an event. This action returns `true` or `false` on whether the URLs were successfully added.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Attribute comment|None|None|
|distribution|string|None|False|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|None|
|event|string|None|False|Event ID to append to|None|None|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|None|
|urls|[]string|None|False|URLs to add|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|URL add status|

Example output:

```

{
 "status": true
}

```

#### Export Hashes

This action is used to export hashes from the HIDS database.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|format|string|None|True|Export format as either MD5 or SHA1|['md5', 'sha1']|None|
|from|string|None|False|From date E.g. 2015-02-15|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|None|
|to|string|None|False|To date E.g. 2015-02-17|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|hashes|bytes|False|Hashes|

#### Rules Export

This action is used to export snort or suricata rules.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event_id|string|None|False|Narrow results to a single event|None|None|
|format|string|None|True|Export format as either Suricata or Snort|['suricata', 'snort']|None|
|frame|boolean|True|True|Commented out explanation framing the data|None|None|
|from|string|None|False|From date E.g. 2015-02-15|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|None|
|to|string|None|False|To date E.g. 2015-02-17|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rules|bytes|False|Rules output|

#### Export Attributes

This action is used to export all attributes in CSV format.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|category|string|None|False|Attribute category|None|None|
|event_id|[]string|None|False|Array of events to download|None|None|
|from|string|None|False|From date E.g. 2015-02-15|None|None|
|include|boolean|True|True|Include attributes not marked as to_ids|None|None|
|include_context|boolean|True|True|Include event data with each attribute|None|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|None|
|tags|[]string|None|False|Array of tags to include in results|None|None|
|to|string|None|False|To date E.g. 2015-02-17|None|None|
|type|string|None|False|Attribute type|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attributes|bytes|False|Attributes output|

#### Download Attachment

This action is used to download an attachment.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attribute_id|string|None|True|Attribute ID of attachment or malware sample|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attachment|bytes|False|Attachment|

#### Add Email Recipient

This action is used to add email recipient to event. This action returns `true` or `false` on whether the email was successfully added.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Attribute comment|None|None|
|distribution|string|None|True|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|None|
|event|string|None|True|Event ID to append to|None|None|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|None|
|recipient|string|None|True|Recipient email address|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Email recipient add status|

Example output:

```

{
 "status": true
}

```

#### Add Email Sender

This action is used to add email sender to event. This action returns `true` or `false` on whether the email was successfully added.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Attribute comment|None|None|
|distribution|string|None|True|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|None|
|event|string|None|True|Event ID to append to|None|None|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|None|
|sender|string|None|True|Sender email address|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Email sender add status|

Example output:

```

{
 "status": true
}

```

#### Add Email Subject

This action is used to add email subject to event. This action returns `true` or `false` on whether the email was successfully added.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Attribute comment|None|None|
|distribution|string|None|True|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|None|
|event|string|None|True|Event ID to append to|None|None|
|proposal|boolean|False|True|Mark request as a proposal (Default: false)|None|None|
|subject|string|None|True|Email subject|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Email subject add status|

Example output:

```

{
 "status": true
}

```

#### Find Event

This action is used to receive events based on criteria.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event_id|string|None|True|Event ID e.g. 123|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|errors|[]string|False|Errors|
|event|Event|False|Event|
|message|string|False|Message|

Example output:

```

{
  "event": {
    "ShadowAttribute": [],
    "locked": false,
    "proposal_email_lock": false,
    "published": false,
    "event_creator_email": "user@example.com",
    "RelatedEvent": [],
    "analysis": "1",
    "org_id": "1",
    "distribution": "2",
    "Tag": [
      {
        "hide_tag": false,
        "name": "Phishing",
        "exportable": true,
        "id": "167",
        "colour": "#856c13"
      }
    ],
    "Galaxy": [],
    "id": "773",
    "Attribute": [
      {
        "ShadowAttribute": [],
        "timestamp": "1516127675",
        "id": "172996",
        "value": "http://badguy.net",
        "sharing_group_id": "0",
        "event_id": "773",
        "type": "url",
        "distribution": "5",
        "disable_correlation": false,
        "to_ids": false,
        "deleted": false,
        "category": "Network activity",
        "comment": "URLs found in suspected phishing e-mail",
        "uuid": "5a5e45bb-c994-46da-9cb5-711f0a04180d"
      },
      {
        "ShadowAttribute": [],
        "timestamp": "1516127671",
        "id": "172999",
        "value": "Hey,Check out this cool link!",
        "sharing_group_id": "0",
        "event_id": "773",
        "type": "email-subject",
        "distribution": "5",
        "disable_correlation": false,
        "to_ids": true,
        "deleted": false,
        "category": "Payload delivery",
        "comment": "Suspected phishing e-mail with this subject",
        "uuid": "5a5e45b7-8500-443b-8c38-03780a04180d"
      }
    ],
    "Orgc": {
      "name": "MISP",
      "id": "1",
      "uuid": "56ef3277-1ad4-42f6-b90b-04e5c0a83832"
    },
    "orgc_id": "1",
    "attribute_count": "4",
    "sharing_group_id": "0",
    "date": "2018-01-16",
    "Org": {
      "name": "MISP",
      "id": "1",
      "uuid": "56ef3277-1ad4-42f6-b90b-04e5c0a83832"
    },
    "timestamp": "1516127664",
    "disable_correlation": false,
    "publish_timestamp": "1516127661",
    "info": "Test from Komand",
    "threat_level_id": "2",
    "uuid": "5a5e45ad-55b4-4e8e-8c97-711c0a04180d"
  },
  "errors": [
    "No errors."
  ],
  "message": "Event found."
}

```

#### Search Events

This action is used to search for events.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analysis|string|None|False|Search by analysis level|['Do not search on', 'Initial', 'Ongoing', 'Completed']|None|
|category|string|None|False|Search by attribute category|None|Person|
|date_from|string|None|False|Search after this date e.g. 2018-03-22|None|None|
|date_until|string|None|False|Search before this date e.g. 2018-03-22|None|None|
|event|string|None|False|Search by event ID|None|None|
|organization|string|None|False|Search by organization|None|None|
|published|string|None|False|Search by if published|['Do not search on', 'True', 'False']|None|
|tag|string|None|False|Search by tag|None|None|
|threat_level|string|None|False|Search by threat level|['Do not search on', 'Undefined', 'Low', 'Medium', 'High']|None|
|type_attribute|string|None|False|Search by any valid MISP attribute type|None|text|
|values|[]string|None|False|Search by given values of attributes value field|None|["example_one", "example_two"]|

Example input:

```
{
  "category": "Person",
  "type_attribute": "text",
  "values": [
    "example_one",
    "example_two"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|event_list|[]string|False|A list of event IDs that match the search|

Example output:

```

{
  "event_list": [
    "777",
    "776",
    "775",
    "291",
    "253",
    "233",
    "219",
    "183"
  ]
}

```

#### Remove Tag

This action is used to remove a tag.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event|string|None|True|Event ID to append to|None|None|
|tag|string|None|True|Event tag for search|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Tag add status|

Example output:

```

{
  "status": true
}

```

#### Add Attribute

This action is used to add an attribute to an event.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|category|string|None|True|The attribute category e.g. external analysis, network activity|None|None|
|comment|string|None|False|Optional comment to add to attribute|None|None|
|event|string|None|True|ID of event to append to|None|None|
|type_value|string|None|True|The Type of attribute e.g. URL, SHA256|None|None|
|value|string|None|True|The Value of the attribute e.g. for a URL https://malware.com|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attribute|attribute|False|A summary of the added attribute|

Example output:

```

{
  "attribute": {
    "id": "173007",
    "event_id": "777",
    "category": "Network activity",
    "type": "url",
    "value1": "https://malware.com",
    "value2": "",
    "to_ids": false,
    "uuid": "5b05a903-f35c-42aa-8ed2-64d60a041dcd",
    "timestamp": "1527097603",
    "distribution": "0",
    "sharing_group_id": "0",
    "comment": "this is a test",
    "deleted": false,
    "disable_correlation": false,
    "value": "https://malware.com"
  }
}

```

#### Publish

This action is used to publish an event.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event|string|None|False|Search by event ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|published|published|False|Info on published event|

Example output:

```

{
  "published": {
    "name": "Alert",
    "message": "Job queued.",
    "url": "/events/alert/776",
    "id": "776"
  }
}

```

#### Add Attachment

This action is used to add an attachment to event.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachment|bytes|None|True|Attachment for event|None|None|
|event|string|None|True|Event ID to append to|None|None|
|filename|string|None|False|Filename of attachment|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Status of add attachment|

Example output:

```
```

### Triggers

#### Search for Tag

This trigger this trigger will search MISP for any events with a specified tag.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|interval|integer|60|True|How frequently (in seconds) to trigger a search|None|None|
|remove|boolean|None|True|If true the tag will be removed|None|None|
|tag|string|None|True|The tag to search for|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]string|True|A list of event_ids with the tag|

Example output:

```
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 5.0.0 - New fields added to Search Events action: values, category and type_attribute
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

## References

* [MISP](http://www.misp-project.org/)
* [MISP API](https://circl.lu/doc/misp/automation/index.html)
* [pymisp](https://github.com/MISP/PyMISP)
