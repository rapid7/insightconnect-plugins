# Description

[Red Canary](https://www.redcanary.com) is a managed endpoint detection and response platform. With the InsightConnect Red Canary plugin you can identify, detect, and mitigate threats to your organization.

# Key Features

* Manage activity monitors
* Trigger new workflows with alert detection
* Mitigate threats with event management

# Requirements

* Red Canary customer ID and API token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|customer_id|string|None|True|Customer ID or name e.g. example from https://example.my.redcanary.co|None|
|api_token|password|None|True|Red Canary API Authentication Token|None|

The `customer_id` is the name or ID in the Red Canary web portal domain e.g. `example` in `https://example.my.redcanary.co`.

## Technical Details

### Actions

#### Retrieve Indicators

This action is used to fetch a list of all indicators of compromise associated with all confirmed detections.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|max_results|integer|100|False|Maximum number of indicators to return|None|
|detection_id|integer|None|True|ID of detection e.g. 12|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|indicators|[]indicator|False|Red Canary indicators|

Example output:

```
{
  "indicators": [
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "40d777b7a95e00593eb1568c68514493",
        "path": "c:\\windows\\explorer.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "ad7b9c14083b52bc532fba5948342b98",
        "path": "c:\\windows\\system32\\cmd.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "ad7b9c14083b52bc532fba5948342b98",
        "path": "c:\\windows\\system32\\cmd.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "eb32c070e658937aa9fa9f3ae629b2b8",
        "path": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "eb32c070e658937aa9fa9f3ae629b2b8",
        "path": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "b9a4dac2192fd78cda097bfa79f6e7b2",
        "path": "c:\\windows\\system32\\net.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "a03cf3838775e0801a0894c8bacd2e56",
        "path": "c:\\windows\\system32\\wbem\\wmic.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "eb32c070e658937aa9fa9f3ae629b2b8",
        "path": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "a03cf3838775e0801a0894c8bacd2e56",
        "path": "c:\\windows\\system32\\wbem\\wmic.exe"
      }
    },
    {
      "type": "primitives.File",
      "attributes": {
        "md5": "a03cf3838775e0801a0894c8bacd2e56",
        "path": "c:\\windows\\system32\\wbem\\wmic.exe"
      }
    },
    {
      "type": "primitives.Domain",
      "attributes": {
        "name": "raw.githubusercontent.com",
        "name_defanged": "raw.githubusercontent[.]com"
      }
    },
    {
      "type": "primitives.IpAddress",
      "attributes": {
        "ip_address": "129.95.36.200",
        "ip_address_defanged": "129.95.36[.]200",
        "ip_address_matches_rfc_1918": false,
        "ip_address_matches_rfc_4193": false,
        "ip_address_is_link_local": false
      }
    }
  ]
}
```

#### Deactivate Activity Monitor

This action is used to deactivate an activity monitor.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|activity_monitor_id|integer|None|True|Activity Monitor identifier|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activity_monitor|activity_monitor|False|Deactivated activity monitor|

Example output:

```
{
  "activity_monitor": {
    "type": "ActivityMonitor",
    "id": 276,
    "attributes": {
      "name": "SSH directory changes",
      "active": false,
      "type": "file_modification",
      "file_modification_types_monitored": [
        "file_modification"
      ],
      "file_paths_monitored": [
        "/var/log/syslog"
      ],
      "usernames_monitored": [
        "everybody"
      ],
      "usernames_ignored": [
        "james_bond"
      ]
    },
    "links": {
      "self": {
        "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/276"
      },
      "matches": {
        "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/276/matches"
      }
    }
  }
}
```

#### Get Activity Monitor

This action is used to fetch a specific activity monitor by unique identifier.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|activity_monitor_id|integer|None|True|Activity Monitor identifier|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activity_monitor|activity_monitor|False|An activity monitor with the given identifier|

Example output:

```
{
  "activity_monitor": {
    "type": "ActivityMonitor",
    "id": 276,
    "attributes": {
      "name": "SSH directory changes",
      "active": false,
      "type": "file_modification",
      "file_modification_types_monitored": [
        "file_modification"
      ],
      "file_paths_monitored": [
        "/var/log/syslog"
      ],
      "usernames_monitored": [
        "everybody"
      ],
      "usernames_ignored": [
        "james_bond"
      ]
    },
    "links": {
      "self": {
        "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/276"
      },
      "matches": {
        "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/276/matches"
      }
    }
  }
}
```

#### Get Event

This action is used to retrieve an event by unique identifier.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|event_id|integer|None|True|Event ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|event|event|True|An event with the given identifier|

Example output:

```
{
  "event": {
    "type": "Event",
    "id": 17,
    "attributes": {
      "process": {
        "type": "primitives.OperatingSystemProcess",
        "attributes": {
          "started_at": "2018-02-01T19:56:32.307Z",
          "operating_system_pid": 3648,
          "image": {
            "type": "primitives.File",
            "attributes": {}
          },
          "command_line": {
            "type": "primitives.ProcessCommandLine",
            "attributes": {
              "identified_encodings": []
            }
          }
        }
      },
      "detectors": [
        {
          "type": "Detector",
          "id": 1031,
          "attributes": {
            "name": "WIN-PUBPRN-SCRIPT-EXECUTION",
            "description": "## Description\nThis detector identifies execution of `PubPrn.vbs` via Windows Script Host (`wscript.exe`) or Console Script Host (`cscript.exe`) with command line options to execute an arbitrary script.\nThis tactic is commonly used to download and execute arbitrary code using a trusted script and binary for bypassing application whitelisting.",
            "contributing_intelligence": "none",
            "attack_technique_identifiers": [
              "ATT&CK Technique T1064 - Scripting"
            ]
          },
          "relationships": {
            "attack_techniques": [
              {
                "links": {
                  "related": "https://kom.my.redcanary.co/openapi/v3/detectors/attack_techniques/T1064"
                },
                "data": {
                  "type": "attack_technique",
                  "id": "T1064"
                }
              }
            ]
          }
        }
      ]
    },
    "relationships": {
      "endpoint": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoints/28"
        },
        "data": {
          "type": "endpoint",
          "id": 28
        }
      },
      "endpoint_user": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoint_users/1"
        },
        "data": {
          "type": "endpoint_user",
          "id": 1
        }
      }
    },
    "links": {
      "self": {
        "href": "https://kom.my.redcanary.co/openapi/v3/events/17"
      }
    }
  }
}
```

#### Create Activity Monitor

This action is used to create a new activity monitor.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|usernames_excluded|[]string|None|False|List of case insensitive globstrings that select which usernames this monitor will filter out|None|
|name|string|None|True|Descriptive name of the activity monitor|None|
|file_modification_types_monitored|[]string|None|True|Types of file modifications this monitor will trigger upon|['file_creation', 'file_deletion', 'file_modification']|
|file_paths_monitored|[]string|None|True|List of case insensitive file path globstrings this monitor will trigger upon|None|
|active|boolean|True|True|If the activity monitor is active and identifying matches|None|
|type|string|file_modification|True|Type of the activity monitor, such as file_modification|None|
|usernames_matched|[]string|None|False|List of case insensitive globstrings that select which usernames this monitor will match against|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activity_monitor|activity_monitor|True|Newly created activity monitor|

Example output:

```
{
  "activity_monitor": {
    "type": "ActivityMonitor",
    "id": 281,
    "attributes": {
      "name": "SSH directory changes",
      "active": true,
      "type": "file_modification",
      "file_modification_types_monitored": [
        "file_modification"
      ],
      "file_paths_monitored": [
        "/var/log/syslog"
      ],
      "usernames_monitored": [
        "everybody"
      ],
      "usernames_ignored": [
        "james_bond"
      ]
    },
    "links": {
      "self": {
        "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/281"
      },
      "matches": {
        "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/281/matches"
      }
    }
  }
}
```

#### Update Remediation State

This action is used to update detection remediation state.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Comment describing the reason why the detection was remediated in this manner|None|
|remediation_state|string|remediated|True|Way in which the detection was remediated|['remediated', 'not_remediated_false_positive', 'not_remediated_sanctioned_activity', 'not_remediated_unwarranted']|
|detection_id|integer|None|True|ID of detection e.g. 12|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|detection|detection|False|Red Canary detection|

Example output:

```
{
  "detection": {
    "type": "Detection",
    "id": 1,
    "attributes": {
      "headline": "[KOM-1] Suspicious Activity (Process)",
      "confirmed_at": "2018-01-16T16:11:53.893Z",
      "summary": "An instance of Regsvr32 was leveraged to download malicious code and execute it on this system. This technique is commonly observed to bypass security controls and application white listing.\n",
      "severity": "high",
      "last_activity_seen_at": "2018-01-16T14:48:02.114Z",
      "classification": {
        "superclassification": "Suspicious Activity",
        "subclassification": [
          "Process"
        ]
      },
      "time_of_occurrence": "2018-01-16T14:48:00.418Z",
      "last_acknowledged_at": "2018-11-15T19:16:41.742Z",
      "last_acknowledged_by": {
        "type": "PortalUser",
        "attributes": {
          "email": "tyler_terenzoni@example.com",
          "name": "Tyler Terenzoni",
          "name_and_email": "Tyler Terenzoni (tyler_terenzoni@example.com)"
        }
      },
      "last_remediated_status": {
        "remediation_state": "remediated",
        "marked_by": {
          "type": "PortalUser",
          "attributes": {
            "email": "tyler_terenzoni@example.com",
            "name": "Tyler Terenzoni",
            "name_and_email": "Tyler Terenzoni (tyler_terenzoni@example.com)"
          }
        },
        "marked_at": "2018-11-15T19:18:19.785Z"
      }
    },
    "relationships": {
      "affected_endpoint": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoints/28"
        },
        "data": {
          "type": "endpoint",
          "id": 28
        }
      },
      "related_endpoint_user": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoint_users/1"
        },
        "data": {
          "type": "endpoint_user",
          "id": 1
        }
      }
    },
    "links": {
      "self": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1"
      },
      "activity_timeline": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/timeline"
      },
      "detectors": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/detectors"
      },
      "response_plans": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/response_plans"
      }
    }
  }
}
```

#### Acknowledge Detection

This action is used to mark a detection as acknowledged.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|detection_id|integer|None|True|ID of detection e.g. 12|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|detection|detection|False|Red Canary detection|

Example output:

```
{
  "detection": {
    "type": "Detection",
    "id": 1,
    "attributes": {
      "headline": "[KOM-1] Suspicious Activity (Process)",
      "confirmed_at": "2018-01-16T16:11:53.893Z",
      "summary": "An instance of Regsvr32 was leveraged to download malicious code and execute it on this system. This technique is commonly observed to bypass security controls and application white listing.\n",
      "severity": "high",
      "last_activity_seen_at": "2018-01-16T14:48:02.114Z",
      "classification": {
        "superclassification": "Suspicious Activity",
        "subclassification": [
          "Process"
        ]
      },
      "time_of_occurrence": "2018-01-16T14:48:00.418Z",
      "last_acknowledged_at": "2018-11-15T19:16:41.742Z",
      "last_acknowledged_by": {
        "type": "PortalUser",
        "attributes": {
          "email": "tyler_terenzoni@example.com",
          "name": "Tyler Terenzoni",
          "name_and_email": "Tyler Terenzoni (tyler_terenzoni@example.com)"
        }
      }
    },
    "relationships": {
      "affected_endpoint": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoints/28"
        },
        "data": {
          "type": "endpoint",
          "id": 28
        }
      },
      "related_endpoint_user": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoint_users/1"
        },
        "data": {
          "type": "endpoint_user",
          "id": 1
        }
      }
    },
    "links": {
      "self": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1"
      },
      "activity_timeline": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/timeline"
      },
      "detectors": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/detectors"
      },
      "response_plans": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/response_plans"
      }
    }
  }
}
```

#### Search for MAC Address Usages

This action is used to find usages of a MAC address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|max_results|integer|100|False|Maximum number of results to return|None|
|mac_address|string|None|True|MAC Address to find usages for (e.g. 00-14-22-01-23-45)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]search_result|True|Search results|

Example output:

```
{
  "results": []
}
```

#### Search for Endpoint Hostname Usages

This action is used to find usages of an endpoint hostname.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|max_results|integer|100|False|Maximum number of results to return|None|
|endpoint_hostname|string|None|True|Endpoint Hostname to find usages for (e.g. foo-endpoint.bardomain.com)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]search_result|True|Search results|

Example output:

```
{
  "results": []
}
```

#### List All Activity Monitor Matches

This action is used to fetch a list of all activity monitor matches, sorted by the creation time of the match.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|max_results|integer|100|False|Maximum number of matches to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activity_monitor_matches|[]activity_monitor_match|False|All activity monitor matches|

Example output:

```
{
  "activity_monitor_matches": []
}
```

#### List Activity Monitors

This action is used to fetch a list of activity monitors.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|max_results|integer|100|False|Maximum number of activity monitors to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activity_monitors|[]activity_monitor|True|List of activity monitors|

Example output:

```
{
  "activity_monitors": [
    {
      "type": "ActivityMonitor",
      "id": 274,
      "attributes": {
        "name": "SSH directory changes",
        "active": true,
        "type": "file_modification",
        "file_modification_types_monitored": [
          "file_modification"
        ],
        "file_paths_monitored": [
          "/var/log/syslog"
        ],
        "usernames_monitored": [
          "everybody"
        ],
        "usernames_ignored": [
          "james_bond"
        ]
      },
      "links": {
        "self": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/274"
        },
        "matches": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/274/matches"
        }
      }
    },
    {
      "type": "ActivityMonitor",
      "id": 275,
      "attributes": {
        "name": "SSH directory changes",
        "active": true,
        "type": "file_modification",
        "file_modification_types_monitored": [
          "file_modification"
        ],
        "file_paths_monitored": [
          "/var/log/syslog"
        ],
        "usernames_monitored": [
          "everybody"
        ],
        "usernames_ignored": [
          "james_bond"
        ]
      },
      "links": {
        "self": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/275"
        },
        "matches": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/275/matches"
        }
      }
    },
    {
      "type": "ActivityMonitor",
      "id": 276,
      "attributes": {
        "name": "SSH directory changes",
        "active": false,
        "type": "file_modification",
        "file_modification_types_monitored": [
          "file_modification"
        ],
        "file_paths_monitored": [
          "/var/log/syslog"
        ],
        "usernames_monitored": [
          "everybody"
        ],
        "usernames_ignored": [
          "james_bond"
        ]
      },
      "links": {
        "self": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/276"
        },
        "matches": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/276/matches"
        }
      }
    },
    {
      "type": "ActivityMonitor",
      "id": 277,
      "attributes": {
        "name": "SSH directory changes",
        "active": true,
        "type": "file_modification",
        "file_modification_types_monitored": [
          "file_modification"
        ],
        "file_paths_monitored": [
          "/var/log/syslog"
        ],
        "usernames_monitored": [
          "everybody"
        ],
        "usernames_ignored": [
          "james_bond"
        ]
      },
      "links": {
        "self": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/277"
        },
        "matches": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/277/matches"
        }
      }
    },
    {
      "type": "ActivityMonitor",
      "id": 278,
      "attributes": {
        "name": "Test",
        "active": true,
        "type": "file_modification",
        "file_modification_types_monitored": [
          "file_creation"
        ],
        "file_paths_monitored": [],
        "usernames_monitored": [],
        "usernames_ignored": []
      },
      "links": {
        "self": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/278"
        },
        "matches": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/278/matches"
        }
      }
    },
    {
      "type": "ActivityMonitor",
      "id": 279,
      "attributes": {
        "name": "SSH directory changes",
        "active": true,
        "type": "file_modification",
        "file_modification_types_monitored": [
          "file_modification"
        ],
        "file_paths_monitored": [
          "/var/log/syslog"
        ],
        "usernames_monitored": [
          "everybody"
        ],
        "usernames_ignored": [
          "james_bond"
        ]
      },
      "links": {
        "self": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/279"
        },
        "matches": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/279/matches"
        }
      }
    },
    {
      "type": "ActivityMonitor",
      "id": 281,
      "attributes": {
        "name": "SSH directory changes",
        "active": true,
        "type": "file_modification",
        "file_modification_types_monitored": [
          "file_modification"
        ],
        "file_paths_monitored": [
          "/var/log/syslog"
        ],
        "usernames_monitored": [
          "everybody"
        ],
        "usernames_ignored": [
          "james_bond"
        ]
      },
      "links": {
        "self": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/281"
        },
        "matches": {
          "href": "https://kom.my.redcanary.co/openapi/v3/activity_monitors/281/matches"
        }
      }
    }
  ]
}
```

#### Search for IP Address Usages

This action is used to find usages of an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|max_results|integer|100|False|Maximum number of results to return|None|
|ip_address|string|None|True|IPv4 or IPv6 address to find usages for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]search_result|True|Search results|

Example output:

```
{
  "results": []
}
```

### Triggers

#### New Events

This trigger is used to check for new events.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|frequency|integer|5|True|How often the trigger should check for new events in seconds|None|
|date_offset|date|None|False|Set past date to pull events from that time forward|None|
|force_offset|boolean|None|False|Forces offset no matter what's in the cache|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|event|event|False|New event|

Example output:

```
{
  "event": {
    "type": "Event",
    "id": 17,
    "attributes": {
      "process": {
        "type": "primitives.OperatingSystemProcess",
        "attributes": {
          "started_at": "2018-02-01T19:56:32.307Z",
          "operating_system_pid": 3648,
          "image": {
            "type": "primitives.File",
            "attributes": {}
          },
          "command_line": {
            "type": "primitives.ProcessCommandLine",
            "attributes": {
              "identified_encodings": []
            }
          }
        }
      },
      "detectors": [
        {
          "type": "Detector",
          "id": 1031,
          "attributes": {
            "name": "WIN-PUBPRN-SCRIPT-EXECUTION",
            "description": "## Description\nThis detector identifies execution of `PubPrn.vbs` via Windows Script Host (`wscript.exe`) or Console Script Host (`cscript.exe`) with command line options to execute an arbitrary script.\nThis tactic is commonly used to download and execute arbitrary code using a trusted script and binary for bypassing application whitelisting.",
            "contributing_intelligence": "none",
            "attack_technique_identifiers": [
              "ATT&CK Technique T1064 - Scripting"
            ]
          },
          "relationships": {
            "attack_techniques": [
              {
                "links": {
                  "related": "https://kom.my.redcanary.co/openapi/v3/detectors/attack_techniques/T1064"
                },
                "data": {
                  "type": "attack_technique",
                  "id": "T1064"
                }
              }
            ]
          }
        }
      ]
    },
    "relationships": {
      "endpoint": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoints/28"
        },
        "data": {
          "type": "endpoint",
          "id": 28
        }
      },
      "endpoint_user": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoint_users/1"
        },
        "data": {
          "type": "endpoint_user",
          "id": 1
        }
      }
    },
    "links": {
      "self": {
        "href": "https://kom.my.redcanary.co/openapi/v3/events/17"
      }
    }
  }
}
```

#### New Activity Monitor Matches

This trigger is used to check for new matches for a specific activity monitor.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|activity_monitor_id|integer|None|True|Activity Monitor identifier|None|
|frequency|integer|5|True|How often the trigger should check for new matches in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activity_monitor_match|activity_monitor_match|False|New match for a specific activity monitor|

Example output:

```
```

#### New Detections

This trigger is used to check for new detections.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|frequency|integer|5|True|How often the trigger should check for new detections in seconds|None|
|date_offset|date|None|False|Set past date to pull events from that time forward|None|
|force_offset|boolean|None|False|Forces offset no matter whats in the cache|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|detection|detection|False|Red Canary detection|

Example output:

```
{
  "detection": {
    "type": "Detection",
    "id": 1,
    "attributes": {
      "headline": "[KOM-1] Suspicious Activity (Process)",
      "confirmed_at": "2018-01-16T16:11:53.893Z",
      "summary": "An instance of Regsvr32 was leveraged to download malicious code and execute it on this system. This technique is commonly observed to bypass security controls and application white listing.\n",
      "severity": "high",
      "last_activity_seen_at": "2018-01-16T14:48:02.114Z",
      "classification": {
        "superclassification": "Suspicious Activity",
        "subclassification": [
          "Process"
        ]
      },
      "time_of_occurrence": "2018-01-16T14:48:00.418Z",
      "last_acknowledged_at": "2018-11-15T19:16:41.742Z",
      "last_acknowledged_by": {
        "type": "PortalUser",
        "attributes": {
          "email": "tyler_terenzoni@example.com",
          "name": "Tyler Terenzoni",
          "name_and_email": "Tyler Terenzoni (tyler_terenzoni@example.com)"
        }
      },
      "last_remediated_status": {
        "remediation_state": "remediated",
        "marked_by": {
          "type": "PortalUser",
          "attributes": {
            "email": "tyler_terenzoni@example.com",
            "name": "Tyler Terenzoni",
            "name_and_email": "Tyler Terenzoni (tyler_terenzoni@example.com)"
          }
        },
        "marked_at": "2018-11-15T19:18:19.785Z"
      }
    },
    "relationships": {
      "affected_endpoint": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoints/28"
        },
        "data": {
          "type": "endpoint",
          "id": 28
        }
      },
      "related_endpoint_user": {
        "links": {
          "related": "https://kom.my.redcanary.co/openapi/v3/endpoint_users/1"
        },
        "data": {
          "type": "endpoint_user",
          "id": 1
        }
      }
    },
    "links": {
      "self": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1"
      },
      "activity_timeline": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/timeline"
      },
      "detectors": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/detectors"
      },
      "response_plans": {
        "href": "https://kom.my.redcanary.co/openapi/v3/detections/1/response_plans"
      }
    }
  }
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

#

# Version History

* 2.1.5 - New spec and help.md format for the Hub
* 2.1.4 - Bug fix for New Events trigger where PluginException was not supported in SDK image | Update to use the `komand/python-3-37-slim-plugin:3` Docker image to reduce plugin size
* 2.1.3 - Bug fix for New Detection trigger cache where additional dates were being added to the cache file. When the cache was loaded from the file it would set the lastest cache to an older date, allowing old detections to be triggered on
* 2.1.2 - Bug fix for New Detection where needed to be loaded every time the trigger was called
* 2.1.1 - Bug fix for connection test
* 2.1.0 - Updated caching for New Events and New Detection triggers. Caching will now use date vs. caching a separate event ID. The trigger also has the option of setting a date offset for testing workflows
* 2.0.0 - Use Red Canary API v3 | New triggers New Activity Monitor Matches and New Events | New actions Create Activity Monitor, List Activity Monitors, Deactivate Activity Monitor, Get Activity Monitor, List All Activity Monitor Matches, Search for Endpoint Hostname Usages, Search For MAC Address Usages, Search for IP Address Usages | Rename action Retrieve Indicator to Retrieve Indicators, Remediate Detection to Update Remediation State
* 1.1.2 - Use new credential types
* 1.1.1 - Bug fix for trigger not caching all detections
* 1.1.0 - Additional logging for trigger | Support web server mode | Bug fix for optimized trigger speed when processing detections
* 1.0.0 - Bug fix for schema and cache file
* 0.1.1 - Bug fix for schema validation
* 0.1.0 - Initial plugin

# Links

## References

* [Red Canary](https://www.redcanary.com)

