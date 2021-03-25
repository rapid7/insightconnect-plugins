# Description

[IBM Resilient](https://www.ibm.com/security/intelligent-orchestration/resilient) is an incident response, orchestration, and automation tool.

# Key Features

* Threat Detection
* Incident Reporting

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|password|password|None|False|Password used for login|None|
|hostname|string|None|False|Hostname for the Resilient application|None|
|email|string|None|False|Email used for login|None|

## Technical Details

### Actions

#### Get Individual Incident

This action is used to get an individual incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|FullIncidentDataDTO|False|Incident|

Example output:

```

{
  "incident": {
      "actions": [
          {
              "enabled": true,
              "id": 39,
              "name": "Send to ServiceNow"
          }
      ],
      "cm": {
          "geo_counts": {},
          "total": 0,
          "unassigneds": []
      },
      "confirmed": true,
      "create_date": 1443803779000,
      "creator": {
          "email": "John@doe.com",
          "fname": "John",
          "id": 1,
          "is_external": false,
          "last_login": 1502831720543,
          "lname": "Doe",
          "locked": false,
          "status": "A"
      },
      "creator_id": 1,
      "crimestatus_id": 5,
      "data_compromised": false,
      "description": "Description here",
      "discovered_date": 1443803580000,
      "draft": false,
      "dtm": {},
      "end_date": 1443805254988,
      "exposure": 0,
      "exposure_type_id": 2,
      "exposure_vendor_id": 214,
      "hard_liability": 0,
      "hipaa": {},
      "id": 2096,
      "inc_start": 1443736800000,
      "inc_training": false,
      "incident_type_ids": [
          1003
      ],
      "is_scenario": false,
      "members": [],
      "name": "BlackOS FTP credentials",
      "nist_attack_vectors": [],
      "org_id": 201,
      "owner_id": 1,
      "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
      },
      "phase_id": 1004,
      "pii": {
          "data_compromised": false,
          "data_format": 0,
          "data_source_ids": [],
          "exposure": 0,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2
      },
      "plan_status": "C",
      "properties": {},
      "regulators": {
          "ids": [
              70,
              64,
              62,
              72,
              149
          ]
      },
      "resolution_id": 56,
      "resolution_summary": "<div>Emailed customer with steps to reset account information.</div>",
      "severity_code": 50,
      "start_date": 1443736800000,
      "task_changes": {
          "added": [],
          "removed": []
      },
      "vers": 7
  }
}

```

#### Create Incident

This action is used to create an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident|object|None|True|The incident to create, in JSON format. Please see the IncidentDTO JSON reference in your Resilient API documentation|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|FullIncidentDataDTO|False|Incident|

Example output:

```

{
  "actions": [
      {
          "enabled": true,
          "id": 39,
          "name": "Send to ServiceNow"
      }
  ],
  "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
  "cm": {
      "geo_counts": {},
      "total": 0,
      "unassigneds": []
  },
  "confirmed": false,
  "create_date": 1502901551000,
  "creator": {
      "cell": "1112223333",
      "email": "email@email.com",
      "fname": "Joe",
      "id": 18,
      "is_external": false,
      "last_login": 1502901550197,
      "lname": "Smith",
      "locked": false,
      "status": "A",
      "title": "Software Engineer"
  },
  "creator_id": 18,
  "crimestatus_id": 1,
  "description": "<div>New Incident</div>",
  "discovered_date": 0,
  "draft": false,
  "dtm": {},
  "exposure": 0,
  "exposure_type_id": 1,
  "hard_liability": 0,
  "hipaa": {},
  "id": 3979,
  "inc_training": false,
  "incident_type_ids": [],
  "is_scenario": false,
  "members": [],
  "name": "New Incident",
  "nist_attack_vectors": [],
  "org_id": 201,
  "owner_id": 18,
  "perms": {
      "assign": true,
      "attach_file": true,
      "change_members": true,
      "close": true,
      "comment": true,
      "create_artifacts": true,
      "create_milestones": true,
      "delete": true,
      "delete_attachments": true,
      "list_artifacts": true,
      "list_milestones": true,
      "read": true,
      "read_attachments": true,
      "write": true
  },
  "phase_id": 1002,
  "pii": {
      "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
      "data_source_ids": [],
      "exposure": 0,
      "gdpr_lawful_data_processing_categories": [],
      "harmstatus_id": 2
  },
  "plan_status": "A",
  "properties": {},
  "regulators": {
      "ids": []
  },
  "task_changes": {
      "added": [],
      "removed": []
  },
  "vers": 1
}

```

#### Create Artifact for Incident

This action is used to create a new artifact on an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|
|artifact|object|None|True|Accepts a IncidentArtifactDTO JSON object. Please see the IncidentArtifactDTO JSON reference in your Resilient API documentation|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|artifact|IncidentArtifactDTO|False|Artifact|

Example output:

```

{
  "actions": [],
  "created": 1502902168214,
  "creator": {
      "cell": "1112223333",
      "email": "john@doe.com",
      "fname": "John",
      "id": 18,
      "is_external": false,
      "last_login": 1502902167865,
      "lname": "Doe",
      "locked": false,
      "status": "A",
      "title": "Software Engineer"
  },
  "hash": "5f83e771e01b3e7bef98a72dddf30fffa22156f545913bacb8d991ce9ff49e549",
  "hits": [],
  "id": 2979,
  "inc_id": 3944,
  "inc_name": "Test Incident",
  "inc_owner": 18,
  "pending_sources": [
      3,
      100,
      8,
      10,
      9,
      4,
      7,
      5
  ],
  "perms": {
      "delete": true,
      "read": true,
      "write": true
  },
  "relating": true,
  "type": 30,
  "value": "Test"
}

```

#### Update Artifact

This action is used to save changes to an artifact.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|
|artifact_id|number|None|True|The artifact ID|None|
|artifact|object|None|True|Accepts a IncidentArtifactDTO JSON object. Please see the IncidentArtifactDTO JSON reference in your Resilient API documentation|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|artifact|IncidentArtifactDTO|False|Artifact|

Example output:

```

{
  "actions": [],
  "created": 1502902168214,
  "creator": {
      "cell": "1112223333",
      "email": "john@doe.com",
      "fname": "John",
      "id": 18,
      "is_external": false,
      "last_login": 1502902167865,
      "lname": "Doe",
      "locked": false,
      "status": "A",
      "title": "Software Engineer"
  },
  "hash": "5f83e771e01b3e7bef98a72dddf30fffa22156f545913bacb8d991ce9ff49e549",
  "hits": [],
  "id": 2979,
  "inc_id": 3944,
  "inc_name": "Test Incident",
  "inc_owner": 18,
  "pending_sources": [
      3,
      100,
      8,
      10,
      9,
      4,
      7,
      5
  ],
  "perms": {
      "delete": true,
      "read": true,
      "write": true
  },
  "relating": true,
  "type": 30,
  "value": "Test"
}

```

#### Get Incident Tasks

This action is used to get the list of tasks for the incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tasks|[]TaskDTO|False|Tasks|

Example output:

```

[
  {
      "actions": [],
      "active": true,
      "attachments_count": 0,
      "auto_deactivate": true,
      "cat_name": "Initial",
      "creator": {
          "cell": "1112223333",
          "email": "john@doe.com",
          "fname": "John",
          "id": 18,
          "is_external": false,
          "last_login": 1502902383087,
          "lname": "Doe",
          "locked": false,
          "status": "A",
          "title": "Software Engineer"
      },
      "custom": true,
      "frozen": false,
      "id": 2260608,
      "inc_id": 3944,
      "inc_name": "Test Incident",
      "inc_owner_id": 18,
      "inc_training": false,
      "init_date": 1502757723522,
      "instr_text": "<div>Just a sample task.</div>",
      "name": "Task 1",
      "notes": [],
      "notes_count": 0,
      "owner_fname": "John",
      "owner_id": 18,
      "owner_lname": "Doe",
      "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "close": true,
          "comment": true,
          "delete_attachments": true,
          "read": true,
          "read_attachments": true,
          "write": true
      },
      "phase_id": 1002,
      "regs": {},
      "required": true,
      "status": "O"
  }
]

```

#### Get Artifacts for Incident

This action is used to get the list of artifacts associated with the specified incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|artifacts|[]IncidentArtifactDTO|False|Artifacts|

Example output:

```

[
  {
      "actions": [],
      "created": 1444744723361,
      "creator": {
          "email": "john@doe.com",
          "fname": "John",
          "id": 1,
          "is_external": false,
          "last_login": 1502831720543,
          "lname": "Doe",
          "locked": false,
          "status": "A"
      },
      "hash": "78d12ced9efaff355b96f29e5175a838b16675339375ec72774f012eadc77816",
      "hits": [],
      "id": 1,
      "inc_id": 2110,
      "inc_name": "OpenDNS Access Request",
      "inc_owner": 1,
      "pending_sources": [],
      "perms": {
          "delete": true,
          "read": true,
          "write": true
      },
      "type": 3,
      "value": "http://browsersafeguard.com"
  }
]

```

#### Patch Incident

This action is used to patch a single incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|
|patch|object|None|True|The incident properties to update, in JSON format. Please see the PatchDTO JSON reference in your Resilient API documentation|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|patch_status|PatchStatusDTO|False|Patch status|

Example output:

```

{
  "hints": [],
  "success": true
}

```

#### Query Incidents

This action is used to query for incidents.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|query|object|None|False|Accepts a QueryDTO JSON object. Please see the QueryDTO JSON reference in your Resilient API documentation|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]PartialIncidentDTO|False|Incidents|

Example output:

```

[
  {
      "actions": [
          {
              "enabled": true,
              "id": 39,
              "name": "Send to ServiceNow"
          }
      ],
      "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
      "cm": {
          "geo_counts": {},
          "total": 0,
          "unassigneds": []
      },
      "confirmed": false,
      "create_date": 1502901551000,
      "creator": {
          "cell": "1112223333",
          "email": "email@email.com",
          "fname": "Joe",
          "id": 18,
          "is_external": false,
          "last_login": 1502901550197,
          "lname": "Smith",
          "locked": false,
          "status": "A",
          "title": "Software Engineer"
      },
      "creator_id": 18,
      "crimestatus_id": 1,
      "description": "<div>New Incident</div>",
      "discovered_date": 0,
      "draft": false,
      "dtm": {},
      "exposure": 0,
      "exposure_type_id": 1,
      "hard_liability": 0,
      "hipaa": {},
      "id": 3979,
      "inc_training": false,
      "incident_type_ids": [],
      "is_scenario": false,
      "members": [],
      "name": "New Incident",
      "nist_attack_vectors": [],
      "org_id": 201,
      "owner_id": 18,
      "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
      },
      "phase_id": 1002,
      "pii": {
          "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
          "data_source_ids": [],
          "exposure": 0,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2
      },
      "plan_status": "A",
      "properties": {},
      "regulators": {
          "ids": []
      },
      "task_changes": {
          "added": [],
          "removed": []
      },
      "vers": 1
  }
]

```

#### Get Incident History

This action is used to get history about an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident_history|IncidentHistoryDTO|False|Incident history|

Example output:

```

{
  "incident_detail_history": [
      {
          "create": true,
          "date": 1502757519465,
          "delete": false,
          "diffs": [
              {
                  "name": "Date Occurred",
                  "new_val": 1502697600000,
                  "type": "datetimepicker"
              },
              {
                  "name": "regulators",
                  "new_val": [
                      "Security Incident Best Practices"
                  ],
                  "old_val": [],
                  "type": "Collection"
              }
          ],
          "object_id": 3944,
          "object_name": "Test Incident",
          "revision_number": 1354486,
          "user": "John Doe"
      }
  ]
}

```

#### Delete Incident

This action is used to delete an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|StatusDTO|False|Status|

Example output:

```

{
"success": true,
"title": "Title",
"message": "",
"hints": []
}

```

#### Get Incidents

This action is used to get a list of open and closed incidents.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]IncidentDTO|False|Incidents|

Example output:

```

[
  {
      "actions": [
          {
              "enabled": true,
              "id": 39,
              "name": "Send to ServiceNow"
          }
      ],
      "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
      "cm": {
          "geo_counts": {},
          "total": 0,
          "unassigneds": []
      },
      "confirmed": false,
      "create_date": 1502901551000,
      "creator": {
          "cell": "1112223333",
          "email": "email@email.com",
          "fname": "Joe",
          "id": 18,
          "is_external": false,
          "last_login": 1502901550197,
          "lname": "Smith",
          "locked": false,
          "status": "A",
          "title": "Software Engineer"
      },
      "creator_id": 18,
      "crimestatus_id": 1,
      "description": "<div>New Incident</div>",
      "discovered_date": 0,
      "draft": false,
      "dtm": {},
      "exposure": 0,
      "exposure_type_id": 1,
      "hard_liability": 0,
      "hipaa": {},
      "id": 3979,
      "inc_training": false,
      "incident_type_ids": [],
      "is_scenario": false,
      "members": [],
      "name": "New Incident",
      "nist_attack_vectors": [],
      "org_id": 201,
      "owner_id": 18,
      "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
      },
      "phase_id": 1002,
      "pii": {
          "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
          "data_source_ids": [],
          "exposure": 0,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2
      },
      "plan_status": "A",
      "properties": {},
      "regulators": {
          "ids": []
      },
      "task_changes": {
          "added": [],
          "removed": []
      },
      "vers": 1
  }
]

```

#### Delete Artifact

This action is used to delete an artifact.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|
|artifact_id|number|None|True|The artifact ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|StatusDTO|False|Status|

Example output:

```

{
"success": true,
"title": "",
"message": "",
"hints": []
}

```

#### Retrieve Specific Incident Artifact

This action is used to retrieve a specific incident artifact.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|
|artifact_id|number|None|True|The artifact ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|artifact|IncidentArtifactDTO|False|Artifact|

Example output:

```

{
  "actions": [],
  "created": 1444744723361,
  "creator": {
      "email": "john@doe.com",
      "fname": "John",
      "id": 1,
      "is_external": false,
      "last_login": 1502831720543,
      "lname": "Doe",
      "locked": false,
      "status": "A"
  },
  "hash": "78d12ced9efaff355b96f29e5175a838b16675339375ec72774f012eadc77816",
  "hits": [],
  "id": 1,
  "inc_id": 2110,
  "inc_name": "OpenDNS Access Request",
  "inc_owner": 1,
  "pending_sources": [],
  "perms": {
      "delete": true,
      "read": true,
      "write": true
  },
  "type": 3,
  "value": "http://browsersafeguard.com"
}

```

#### Add Custom Task to Incident

This action is used to add a custom task to the incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|number|None|True|The organization ID|None|
|incident_id|number|None|True|The incident ID|None|
|body|object|None|True|Accepts a TaskDTO JSON object. Please see the TaskDTO JSON reference in your Resilient API documentation|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|identifier|number|False|Identifier|

Example output:

```

{
  "identifier": 2260738
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For actions that take a JSON object as input, Resilient will sometimes throw an HTTP 404 error code for malformed JSON or JSON that does not match what is required. The Interactive API Test in your Resilient installation is useful for debugging JSON creation.

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [IBM Resilient](https://www.ibm.com/security/intelligent-orchestration/resilient)
