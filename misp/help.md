
# MISP

## About

[MISP](http://www.misp-project.org/) is an open source threat sharing platform.
This plugin utilizes the [MISP API](https://circl.lu/doc/misp/automation/index.html) and leverages the [pymisp](https://github.com/CIRCL/PyMISP) library.

## Actions

### Add Context

This action is used to add context. This action returns `true` or `false` on whether the context was successfully added.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|comment_input|None|True|None|None|
|text|text_input|None|True|None|None|
|other|other_input|None|True|None|None|
|link|link_input|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Context add status|

Example output:

```

{
 "status": true
}

```

### Export Events

This action is used to export all events in XML format.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|to|string|None|False|To date E.g. 2015-02-17|None|
|from|string|None|False|From date E.g. 2015-02-15|None|
|tags|[]string|None|False|Array of tags to include in results|None|
|event_id|string|None|False|Specify single event to export|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|
|encode_attachments|boolean|True|True|Encode attachments in export|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|bytes|False|Event output|

### Create Event

This action is used to create a MISP event.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|info|string|None|True|Extra event information|None|
|orgc_id|string|None|False|Organization C ID|None|
|sharing_group_id|string|None|False|Sharing group ID|None|
|org_id|string|None|False|Organization ID|None|
|analysis|string|None|False|The analysis level of the event|['2', '1', '0']|
|published|boolean|None|True|Published event?|None|
|distribution|string|This Organization|False|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|
|threat_level_id|string|None|True|Importance of the threat|['4', '3', '2', '1']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|orgc_id|string|False|Organization C ID|
|sharing_group_id|string|False|Sharing group ID|
|timestamp|string|False|Timestamp|
|Attribute|[]base_output|False|Attribute|
|date|date|False|Date|
|org|orgc_output|False|Organization|
|disable_correlation|boolean|False|Disable correlation|
|id|string|False|Event ID|
|threat_level_id|string|False|Threat level ID|
|publish_timestamp|string|False|Publish timestamp|
|info|string|False|Info|
|event_creator_email|string|False|Event creator's email|
|locked|boolean|False|Locked|
|uuid|string|False|Unique event ID|
|orgc|orgc_output|False|Orgc|
|attribute_count|string|False|Attribute count|
|org_id|string|False|Organization ID|
|analysis|string|False|Analysis|
|published|boolean|False|Published|
|distribution|string|False|Distribution|
|proposal_email_lock|boolean|False|Lock proposal email|
|RelatedEvent|[]object|False|Related event|

### Export RPZ

This action is used to export RPZ zone files.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|event_id|string|None|False|Specify single event to export|None|
|to|string|None|False|To date E.g. 2015-02-17|None|
|from|string|None|False|From date E.g. 2015-02-15|None|
|tags|[]string|None|False|Array of tags to include in results|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rpz|bytes|False|RPZ output|

### Add Tag

This action is used to add a tag. The event tag must already exist in MISP. This action returns `true` or `false` on whether the tag successfully added.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag|string|None|True|Event tag for search|None|
|event|string|None|True|Event ID to append to|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Tag status|

Example output:

```

{
 "status": true
}

```

### Export STIX

This action is used to export events in STIX format.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|to|string|None|False|To date E.g. 2015-02-17|None|
|from|string|None|False|From date E.g. 2015-02-15|None|
|tags|[]string|None|False|Array of tags to include in results|None|
|event_id|string|None|False|Specify single event to export|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|
|encode_attachments|boolean|True|True|Encode attachments in export|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stix|bytes|False|STIX output|

### Add Sightings

This action is used to add sightings to an organization.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sightings|[]string|None|True|Event sightings|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Sightings add status|

Example output:

```

{
 "status": true
}

```

### Add URLs

This action is used to add URLs to an event. This action returns `true` or `false` on whether the URLs were successfully added.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Attribute comment|None|
|distribution|string|None|False|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|
|event|string|None|False|Event ID to append to|None|
|urls|[]string|None|False|URLs to add|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|URLs add status|

Example output:

```

{
 "status": true
}

```

### Export Hashes

This action is used to export hashes from the HIDS database.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|to|string|None|False|To date E.g. 2015-02-17|None|
|format|string|None|True|Export format as either md5 or sha1|['md5', 'sha1']|
|from|string|None|False|From date E.g. 2015-02-15|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|
|tags|[]string|None|False|Array of tags to include in results|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|hashes|bytes|False|Hashes|

### Rules Export

This action is used to export snort or suricata rules.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|to|string|None|False|To date E.g. 2015-02-17|None|
|from|string|None|False|From date E.g. 2015-02-15|None|
|tags|[]string|None|False|Array of tags to include in results|None|
|event_id|string|None|False|Narrow results to a single event|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|
|frame|boolean|True|True|Commented out expliantion framing the data|None|
|format|string|None|True|Export format as either Suricata or Snort|['suricata', 'snort']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rules|bytes|False|Rules output|

### Export Attributes

This action is used to export all attributes in CSV format.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|category|string|None|False|Attribute category|None|
|from|string|None|False|From date E.g. 2015-02-15|None|
|include_context|boolean|True|True|Include event data with each attribute|None|
|event_id|[]string|None|False|Array of events to download|None|
|tags|[]string|None|False|Array of tags to include in results|None|
|to|string|None|False|To date E.g. 2015-02-17|None|
|last|string|None|False|Events within x amount of time E.g. 5d|None|
|include|boolean|True|True|Include attributes not marked as to_ids|None|
|type|string|None|False|Attribute type|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attributes|bytes|False|Attributes output|

### Download Attachment

This action is used to download an attachment.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|attribute_id|string|None|True|Attribute ID of attachment or malware sample|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attachment|bytes|False|Attachment|

### Add Email Recipient

This action is used to add email recipient to event. This action returns `true` or `false` on whether the email was successfully added.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|True|Attribute comment|None|
|distribution|string|None|True|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|
|recipient|string|None|True|Recipient email address|None|
|event|string|None|True|Event ID to append to|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Email recipient add status|

Example output:

```

{
 "status": true
}

```

### Add Email Sender

This action is used to add email sender to event. This action returns `true` or `false` on whether the email was successfully added.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|True|Attribute comment|None|
|distribution|string|None|True|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|
|sender|string|None|True|Sender email address|None|
|event|string|None|True|Event ID to append to|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Email sender add status|

Example output:

```

{
 "status": true
}

```

### Add Email Subject

This action is used to add email subject to event. This action returns `true` or `false` on whether the email was successfully added.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|True|Attribute comment|None|
|distribution|string|None|True|Distribution type|['This Community', 'This Organization', 'Connected Communities', 'All Communities']|
|event|string|None|True|Event ID to append to|None|
|subject|string|None|True|Email subject|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Email subject add status|

Example output:

```

{
 "status": true
}

```

### Find Event

This action is used to receive events based on criteria.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|event_id|string|None|True|Event ID e.g. 123|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|errors|[]string|False|None|
|result|Event"|False|None|

Example output:

```

{
  "event": {
    "ShadowAttribute": [],
    "locked": false,
    "proposal_email_lock": false,
    "published": false,
    "event_creator_email": "admin@misp.training",
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

### Search Events

This action is used to search for events.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Organization|string|None|False|Search by organisation|None|
|date_until|string|None|False|Search before this data e.g. 2018-03-22|None|
|analysis|string|None|False|Search by analysis level|['Initial', 'Ongoing', 'Completed']|
|event|string|None|False|Search by event ID|None|
|tag|string|None|False|Search by Tag|None|
|published|string|None|False|Search by if Published|None|
|threat_level|string|None|False|Search by threat Level|['Undefined', 'Low', 'Medium', 'High']|
|date_from|string|None|False|Search after this data e.g. 2018-03-22|None|

#### Output

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

### Remove Tag

This action is used to remove a tag.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag|string|None|True|Event tag for search|None|
|event|string|None|True|Event ID to append to|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Tag add status|

Example output:

```

{
  "status": true
}

```

### Add Attribute

This action is used to add an attribute to an event.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|category|string|None|True|The attribute category e.g. external analysis, Network activity|None|
|comment|string|None|False|Optional comment to add to attribute|None|
|type_value|string|None|True|The Type of attribute e.g. url, sha256|None|
|event|string|None|True|Event ID to append to|None|
|value|string|None|True|The Value of the attribute e.g. for a url https\://malware.com|None|

#### Output

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

### Publish

This action is used to publish an event.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|event|string|None|False|Search by event ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|published|publish|False|Info on published event|

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

### Add Attachment

This action is used to add an attachment to event.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|attachment|bytes|None|True|Attachment for event|None|
|event|string|None|True|Event ID to append to|None|
|filename|string|None|False|Filename of attachment|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Status of add attachment|

Example output:

```
```

## Triggers

### Search For Tag

This trigger is used to search MISP for any events with a specified tag.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|60|True|How frequently (in seconds) to trigger a search|None|
|tag|string|None|True|The tag to search for|None|
|remove|boolean|None|True|If true the tag will be removed|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]string|True|A list of event_ids with the tag|

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL of the MISP server e.g. https://misp-2-4.example.com|None|
|automation_code|credential_secret_key|None|True|API/Automation code of MISP server|None|
|ssl|boolean|None|True|If true will use SSL for communication to MISP|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Threat intelligence
* Export events
* Export RPZ zone files
* Download attachment

## Versions

* 0.1.0 - Initial plugin
* 0.2.0 - 8 new actions to add data to MISP: Add Email Recipient, Add Email Sender, Add Email Subject, Add Sightings, Add Tag, Add Context, Add URL, and Create An Event
* 0.2.1 - SSL bug fix in SDK
* 0.3.0 - Add Find Event action
* 0.4.0 - Added add attachment feature | Update to v2 architecture
* 0.4.1 - Bug fix for CI tool incorrectly uploading plugins
* 1.0.0 - Add trigger. Add actions: Add Attachment, Remove Tag, Search Events, Publish. Support web server mode
* 2.0.0 - Updated to new credential types | Update `hostname` variable in Connection to `url`
* 3.0.0 - Fixed issue where Add URLs, Add Context, Add Email Sender, Add Email Subject and Add Email Recipient actions sent requests as a proposal | Fixed an issue where the distribution list was set incorrectly within Add URLs, Add Context, Create an Event, Add Email Sender, Add Email Subject, Add Email Recipient actions
* 3.0.1 - Fix typo in plugin spec

## References

* [MISP](http://www.misp-project.org/)
* [MISP API](https://circl.lu/doc/misp/automation/index.html)
* [pymisp](https://github.com/CIRCL/PyMISP)
