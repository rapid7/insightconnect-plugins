# Description

[PagerDuty](https://www.pagerduty.com/) provides enterprise-grade incident management that helps you 
orchestrate the ideal response to create better customer, employee, and business value. Use this plugin to manage users
and incidents within workflows.
The PagerDuty plugin makes requests to the V2 API.

# Key Features
  
* Create and manage PagerDuty incidents
* Access PagerDuty user information

# Requirements
  
* PagerDuty API key

# Supported Product Versions
  
* 2023-10-12

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|API Key|None|stRbCzL92kpAfwCkSiA9|
  
Example input:

```
{
  "api_key": "stRbCzL92kpAfwCkSiA9"
}
```

## Technical Details

### Actions


#### Create User
  
Create a User

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|color|string|None|False|The schedule color|None|green|
|email|string|None|True|The email address for the new account to be created|None|user1@example.com|
|from_email|string|None|True|The email address of user that is creating the account|None|user2@example.com|
|job_title|string|None|False|The description of the new user|None|job title|
|license|object|None|False|The license of the new user|None|{'id': 'PTDVERC', 'type': 'license_reference'}|
|name|string|None|True|Name|None|test user|
|role|string|None|False|Role|['admin', 'limited_user', 'owner', 'read_only_user', 'user']|user|
|time_zone|string|None|False|Time Zone, e.g. America/Lima|None|Europe/London|
|user_description|string|None|False|The description of the new user|None|test description of the new use|
  
Example input:

```
{
  "color": "green",
  "email": "user1@example.com",
  "from_email": "user2@example.com",
  "job_title": "job title",
  "license": {
    "id": "PTDVERC",
    "type": "license_reference"
  },
  "name": "test user",
  "role": "user",
  "time_zone": "Europe/London",
  "user_description": "test description of the new use"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User|{'avatar_url': 'https://secure.gravatar.com/avatar/c67b6c8ed606dec999bb064ada88cf5c.png?d=mm&r=PG', 'billed': True, 'color': 'purple', 'contact_methods': [{'html_url': None, 'id': 'P9CU341', 'self': 'https://api.pagerduty.com/users/PYGDZB8/contact_methods/P9CU341', 'summary': 'Default', 'type': 'email_contact_method_reference'}], 'coordinated_incidents': [], 'description': '', 'email': 'user1@example.com', 'html_url': 'https://api.pagerduty.com/users/PYGDZB8', 'id': 'PYGDZB8', 'invitation_sent': False, 'job_title': '', 'name': 'test user', 'notification_rules': [{'html_url': None, 'id': 'POMMNCV', 'self': 'https://api.pagerduty.com/users/PYGDZB8/notification_rules/POMMNCV', 'summary': '0 minutes: channel P9CU341', 'type': 'assignment_notification_rule_reference'}, {'html_url': None, 'id': 'PSZNORI', 'self': 'https://api.pagerduty.com/users/PYGDZB8/notification_rules/PSZNORI', 'summary': '0 minutes: channel P9CU341', 'type': 'assignment_notification_rule_reference'}], 'role': 'owner', 'self': 'https://api.pagerduty.com/users/PYGDZB8', 'summary': 'test summary', 'teams': [{'html_url': 'https://api.pagerduty.com/teams/PLBLK3G', 'id': 'PLBLK3G', 'self': 'https://api.pagerduty.com/teams/PLBLK3G', 'summary': 'Engineering', 'type': 'team_reference'}], 'time_zone': 'Europe/London', 'type': 'user'}|
  
Example output:

```
{
  "user": {
    "avatar_url": "https://secure.gravatar.com/avatar/c67b6c8ed606dec999bb064ada88cf5c.png?d=mm&r=PG",
    "billed": true,
    "color": "purple",
    "contact_methods": [
      {
        "html_url": null,
        "id": "P9CU341",
        "self": "https://api.pagerduty.com/users/PYGDZB8/contact_methods/P9CU341",
        "summary": "Default",
        "type": "email_contact_method_reference"
      }
    ],
    "coordinated_incidents": [],
    "description": "",
    "email": "user1@example.com",
    "html_url": "https://api.pagerduty.com/users/PYGDZB8",
    "id": "PYGDZB8",
    "invitation_sent": false,
    "job_title": "",
    "name": "test user",
    "notification_rules": [
      {
        "html_url": null,
        "id": "POMMNCV",
        "self": "https://api.pagerduty.com/users/PYGDZB8/notification_rules/POMMNCV",
        "summary": "0 minutes: channel P9CU341",
        "type": "assignment_notification_rule_reference"
      },
      {
        "html_url": null,
        "id": "PSZNORI",
        "self": "https://api.pagerduty.com/users/PYGDZB8/notification_rules/PSZNORI",
        "summary": "0 minutes: channel P9CU341",
        "type": "assignment_notification_rule_reference"
      }
    ],
    "role": "owner",
    "self": "https://api.pagerduty.com/users/PYGDZB8",
    "summary": "test summary",
    "teams": [
      {
        "html_url": "https://api.pagerduty.com/teams/PLBLK3G",
        "id": "PLBLK3G",
        "self": "https://api.pagerduty.com/teams/PLBLK3G",
        "summary": "Engineering",
        "type": "team_reference"
      }
    ],
    "time_zone": "Europe/London",
    "type": "user"
  }
}
```

#### Delete User by ID
  
Delete a User by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|True|The email address of a valid user associated with the account making the delete request|None|user1@example.com|
|id|string|None|True|User ID|None|PYGDZB8|
  
Example input:

```
{
  "email": "user1@example.com",
  "id": "PYGDZB8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|string|False|A message to show if the user was deleted as expected|The user PYGDZB8 has been deleted|
  
Example output:

```
{
  "success": "The user PYGDZB8 has been deleted"
}
```

#### Get On-Call Users
  
Get list of on-call users

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|schedule_id|string|None|True|Schedule ID|None|P9E0DZT|
  
Example input:

```
{
  "schedule_id": "P9E0DZT"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|users|[]user|True|List of on-call users|[{"avatar_url": "https://secure.gravatar.com/avatar/c67b6c8ed606dec999bb064ada88cf5c.png?d=mm&r=PG", "billed": True, "color": "purple", "contact_methods": [{"html_url": None, "id": "P9CU341", "self": "https://api.pagerduty.com/users/PYGDZB8/contact_methods/P9CU341", "summary": "Default", "type": "email_contact_method_reference"}], "coordinated_incidents": [], "description": "", "email": "user1@example.com", "html_url": "https://api.pagerduty.com/users/PYGDZB8", "id": "PYGDZB8", "invitation_sent": False, "job_title": "", "name": "Test account", "notification_rules": [{"html_url": None, "id": "POMMNCV", "self": "https://api.pagerduty.com/users/PYGDZB8/notification_rules/POMMNCV", "summary": "0 minutes: channel P9CU341", "type": "assignment_notification_rule_reference"}, {"html_url": None, "id": "PSZNORI", "self": "https://api.pagerduty.com/users/PYGDZB8/notification_rules/PSZNORI", "summary": "0 minutes: channel P9CU341", "type": "assignment_notification_rule_reference"}], "role": "owner", "self": "https://api.pagerduty.com/users/PYGDZB8", "summary": "test summary", "teams": [{"html_url": "https://api.pagerduty.com/teams/PLBLK3G", "id": "PLBLK3G", "self": "https://api.pagerduty.com/teams/PLBLK3G", "summary": "Engineering", "type": "team_reference"}], "time_zone": "Europe/London", "type": "user"}]|
  
Example output:

```
{
  "users": {
    "avatar_url": "https://secure.gravatar.com/avatar/c67b6c8ed606dec999bb064ada88cf5c.png?d=mm&r=PG",
    "billed": true,
    "color": "purple",
    "contact_methods": [
      {
        "html_url": null,
        "id": "P9CU341",
        "self": "https://api.pagerduty.com/users/PYGDZB8/contact_methods/P9CU341",
        "summary": "Default",
        "type": "email_contact_method_reference"
      }
    ],
    "coordinated_incidents": [],
    "description": "",
    "email": "user1@example.com",
    "html_url": "https://api.pagerduty.com/users/PYGDZB8",
    "id": "PYGDZB8",
    "invitation_sent": false,
    "job_title": "",
    "name": "Test account",
    "notification_rules": [
      {
        "html_url": null,
        "id": "POMMNCV",
        "self": "https://api.pagerduty.com/users/PYGDZB8/notification_rules/POMMNCV",
        "summary": "0 minutes: channel P9CU341",
        "type": "assignment_notification_rule_reference"
      },
      {
        "html_url": null,
        "id": "PSZNORI",
        "self": "https://api.pagerduty.com/users/PYGDZB8/notification_rules/PSZNORI",
        "summary": "0 minutes: channel P9CU341",
        "type": "assignment_notification_rule_reference"
      }
    ],
    "role": "owner",
    "self": "https://api.pagerduty.com/users/PYGDZB8",
    "summary": "test summary",
    "teams": [
      {
        "html_url": "https://api.pagerduty.com/teams/PLBLK3G",
        "id": "PLBLK3G",
        "self": "https://api.pagerduty.com/teams/PLBLK3G",
        "summary": "Engineering",
        "type": "team_reference"
      }
    ],
    "time_zone": "Europe/London",
    "type": "user"
  }
}
```

#### Get User by ID
  
Get a User by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|User ID|None|P9CU341|
  
Example input:

```
{
  "id": "P9CU341"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User|{'avatar_url': 'https://secure.gravatar.com/avatar/c67b6c8ed606dec999bb064ada88cf5c.png?d=mm&r=PG', 'billed': True, 'color': 'purple', 'contact_methods': [{'html_url': None, 'id': 'P9CU341', 'self': 'https://api.pagerduty.com/users/PYGDZB8/contact_methods/P9CU341', 'summary': 'Default', 'type': 'email_contact_method_reference'}], 'coordinated_incidents': [], 'description': '', 'email': 'user1@example.com', 'html_url': 'https://api.pagerduty.com/users/PYGDZB8', 'id': 'PYGDZB8', 'invitation_sent': False, 'job_title': '', 'name': 'Test account', 'notification_rules': [{'html_url': None, 'id': 'POMMNCV', 'self': 'https://api.pagerduty.com/users/PYGDZB8/notification_rules/POMMNCV', 'summary': '0 minutes: channel P9CU341', 'type': 'assignment_notification_rule_reference'}, {'html_url': None, 'id': 'PSZNORI', 'self': 'https://api.pagerduty.com/users/PYGDZB8/notification_rules/PSZNORI', 'summary': '0 minutes: channel P9CU341', 'type': 'assignment_notification_rule_reference'}], 'role': 'owner', 'self': 'https://api.pagerduty.com/users/PYGDZB8', 'summary': 'test summary', 'teams': [{'html_url': 'https://api.pagerduty.com/teams/PLBLK3G', 'id': 'PLBLK3G', 'self': 'https://api.pagerduty.com/teams/PLBLK3G', 'summary': 'Engineering', 'type': 'team_reference'}], 'time_zone': 'Europe/London', 'type': 'user'}|
  
Example output:

```
{
  "user": {
    "avatar_url": "https://secure.gravatar.com/avatar/c67b6c8ed606dec999bb064ada88cf5c.png?d=mm&r=PG",
    "billed": true,
    "color": "purple",
    "contact_methods": [
      {
        "html_url": null,
        "id": "P9CU341",
        "self": "https://api.pagerduty.com/users/PYGDZB8/contact_methods/P9CU341",
        "summary": "Default",
        "type": "email_contact_method_reference"
      }
    ],
    "coordinated_incidents": [],
    "description": "",
    "email": "user1@example.com",
    "html_url": "https://api.pagerduty.com/users/PYGDZB8",
    "id": "PYGDZB8",
    "invitation_sent": false,
    "job_title": "",
    "name": "Test account",
    "notification_rules": [
      {
        "html_url": null,
        "id": "POMMNCV",
        "self": "https://api.pagerduty.com/users/PYGDZB8/notification_rules/POMMNCV",
        "summary": "0 minutes: channel P9CU341",
        "type": "assignment_notification_rule_reference"
      },
      {
        "html_url": null,
        "id": "PSZNORI",
        "self": "https://api.pagerduty.com/users/PYGDZB8/notification_rules/PSZNORI",
        "summary": "0 minutes: channel P9CU341",
        "type": "assignment_notification_rule_reference"
      }
    ],
    "role": "owner",
    "self": "https://api.pagerduty.com/users/PYGDZB8",
    "summary": "test summary",
    "teams": [
      {
        "html_url": "https://api.pagerduty.com/teams/PLBLK3G",
        "id": "PLBLK3G",
        "self": "https://api.pagerduty.com/teams/PLBLK3G",
        "summary": "Engineering",
        "type": "team_reference"
      }
    ],
    "time_zone": "Europe/London",
    "type": "user"
  }
}
```

#### Send Acknowledge Event
  
Acknowledge an incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|True|The email address of a valid user associated with the account making the request|None|user1@example.com|
|incident_id|string|None|True|The ID of the incident|None|Q1GXLD8EXPKU32|
  
Example input:

```
{
  "email": "user1@example.com",
  "incident_id": "Q1GXLD8EXPKU32"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident_output|False|The incident object that was acknowledged|{'incident': {'acknowledgements': [{'acknowledger': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'at': '2015-11-10T00:32:52Z'}], 'alert_counts': {'all': 0, 'resolved': 0, 'triggered': 0}, 'assigned_via': 'escalation_policy', 'assignments': [{'assignee': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'at': '2015-11-10T00:31:52Z'}], 'conference_bridge': {'conference_number': '555-123-4567', 'conference_url': 'https://example.com/123-456-789'}, 'created_at': '2015-10-06T21:30:42Z', 'escalation_policy': {'html_url': 'https://subdomain.pagerduty.com/escalation_policies/PT20YPA', 'id': 'PT20YPA', 'self': 'https://api.pagerduty.com/escalation_policies/PT20YPA', 'summary': 'Another Escalation Policy', 'type': 'escalation_policy_reference'}, 'first_trigger_log_entry': {'html_url': 'https://subdomain.pagerduty.com/incidents/PT4KHLK/log_entries/Q02JTSNZWHSEKV', 'id': 'Q02JTSNZWHSEKV', 'self': 'https://api.pagerduty.com/log_entries/Q02JTSNZWHSEKV?incident_id=PT4KHLK', 'summary': 'Triggered through the API', 'type': 'trigger_log_entry_reference'}, 'html_url': 'https://subdomain.pagerduty.com/incidents/PT4KHLK', 'id': 'PT4KHLK', 'incident_key': 'baf7cf21b1da41b4b0221008339ff357', 'incident_number': 1234, 'is_mergeable': True, 'last_status_change_at': '2015-10-06T21:38:23Z', 'last_status_change_by': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'pending_actions': [{'at': '2015-11-10T01:02:52Z', 'type': 'unacknowledge'}, {'at': '2015-11-10T04:31:52Z', 'type': 'resolve'}], 'priority': {'id': 'P53ZZH5', 'self': 'https://api.pagerduty.com/priorities/P53ZZH5', 'summary': 'P2', 'type': 'priority_reference'}, 'self': 'https://api.pagerduty.com/incidents/PT4KHLK', 'service': {'html_url': 'https://subdomain.pagerduty.com/service-directory/PIJ90N7', 'id': 'PIJ90N7', 'self': 'https://api.pagerduty.com/services/PIJ90N7', 'summary': 'My Mail Service', 'type': 'service_reference'}, 'status': 'resolved', 'summary': '[#1234] The server is on fire.', 'teams': [{'html_url': 'https://subdomain.pagerduty.com/teams/PQ9K7I8', 'id': 'PQ9K7I8', 'self': 'https://api.pagerduty.com/teams/PQ9K7I8', 'summary': 'Engineering', 'type': 'team_reference'}], 'title': 'The server is on fire.', 'type': 'incident', 'updated_at': '2015-10-08T21:30:42Z', 'urgency': 'high'}}|
  
Example output:

```
{
  "incident": {
    "incident": {
      "acknowledgements": [
        {
          "acknowledger": {
            "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
            "id": "PXPGF42",
            "self": "https://api.pagerduty.com/users/PXPGF42",
            "summary": "Earline Greenholt",
            "type": "user_reference"
          },
          "at": "2015-11-10T00:32:52Z"
        }
      ],
      "alert_counts": {
        "all": 0,
        "resolved": 0,
        "triggered": 0
      },
      "assigned_via": "escalation_policy",
      "assignments": [
        {
          "assignee": {
            "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
            "id": "PXPGF42",
            "self": "https://api.pagerduty.com/users/PXPGF42",
            "summary": "Earline Greenholt",
            "type": "user_reference"
          },
          "at": "2015-11-10T00:31:52Z"
        }
      ],
      "conference_bridge": {
        "conference_number": "555-123-4567",
        "conference_url": "https://example.com/123-456-789"
      },
      "created_at": "2015-10-06T21:30:42Z",
      "escalation_policy": {
        "html_url": "https://subdomain.pagerduty.com/escalation_policies/PT20YPA",
        "id": "PT20YPA",
        "self": "https://api.pagerduty.com/escalation_policies/PT20YPA",
        "summary": "Another Escalation Policy",
        "type": "escalation_policy_reference"
      },
      "first_trigger_log_entry": {
        "html_url": "https://subdomain.pagerduty.com/incidents/PT4KHLK/log_entries/Q02JTSNZWHSEKV",
        "id": "Q02JTSNZWHSEKV",
        "self": "https://api.pagerduty.com/log_entries/Q02JTSNZWHSEKV?incident_id=PT4KHLK",
        "summary": "Triggered through the API",
        "type": "trigger_log_entry_reference"
      },
      "html_url": "https://subdomain.pagerduty.com/incidents/PT4KHLK",
      "id": "PT4KHLK",
      "incident_key": "baf7cf21b1da41b4b0221008339ff357",
      "incident_number": 1234,
      "is_mergeable": true,
      "last_status_change_at": "2015-10-06T21:38:23Z",
      "last_status_change_by": {
        "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
        "id": "PXPGF42",
        "self": "https://api.pagerduty.com/users/PXPGF42",
        "summary": "Earline Greenholt",
        "type": "user_reference"
      },
      "pending_actions": [
        {
          "at": "2015-11-10T01:02:52Z",
          "type": "unacknowledge"
        },
        {
          "at": "2015-11-10T04:31:52Z",
          "type": "resolve"
        }
      ],
      "priority": {
        "id": "P53ZZH5",
        "self": "https://api.pagerduty.com/priorities/P53ZZH5",
        "summary": "P2",
        "type": "priority_reference"
      },
      "self": "https://api.pagerduty.com/incidents/PT4KHLK",
      "service": {
        "html_url": "https://subdomain.pagerduty.com/service-directory/PIJ90N7",
        "id": "PIJ90N7",
        "self": "https://api.pagerduty.com/services/PIJ90N7",
        "summary": "My Mail Service",
        "type": "service_reference"
      },
      "status": "resolved",
      "summary": "[#1234] The server is on fire.",
      "teams": [
        {
          "html_url": "https://subdomain.pagerduty.com/teams/PQ9K7I8",
          "id": "PQ9K7I8",
          "self": "https://api.pagerduty.com/teams/PQ9K7I8",
          "summary": "Engineering",
          "type": "team_reference"
        }
      ],
      "title": "The server is on fire.",
      "type": "incident",
      "updated_at": "2015-10-08T21:30:42Z",
      "urgency": "high"
    }
  }
}
```

#### Send Resolve Event
  
Resolve an incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|True|The email address of a valid user associated with the account making the request|None|user1@example.com|
|incident_id|string|None|True|The ID of the incident|None|Q1GXLD8EXPKU32|
  
Example input:

```
{
  "email": "user1@example.com",
  "incident_id": "Q1GXLD8EXPKU32"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident_output|False|The incident object that was resolved|{'incident': {'acknowledgements': [{'acknowledger': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'at': '2015-11-10T00:32:52Z'}], 'alert_counts': {'all': 0, 'resolved': 0, 'triggered': 0}, 'assigned_via': 'escalation_policy', 'assignments': [{'assignee': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'at': '2015-11-10T00:31:52Z'}], 'conference_bridge': {'conference_number': '555-123-4567', 'conference_url': 'https://example.com/123-456-789'}, 'created_at': '2015-10-06T21:30:42Z', 'escalation_policy': {'html_url': 'https://subdomain.pagerduty.com/escalation_policies/PT20YPA', 'id': 'PT20YPA', 'self': 'https://api.pagerduty.com/escalation_policies/PT20YPA', 'summary': 'Another Escalation Policy', 'type': 'escalation_policy_reference'}, 'first_trigger_log_entry': {'html_url': 'https://subdomain.pagerduty.com/incidents/PT4KHLK/log_entries/Q02JTSNZWHSEKV', 'id': 'Q02JTSNZWHSEKV', 'self': 'https://api.pagerduty.com/log_entries/Q02JTSNZWHSEKV?incident_id=PT4KHLK', 'summary': 'Triggered through the API', 'type': 'trigger_log_entry_reference'}, 'html_url': 'https://subdomain.pagerduty.com/incidents/PT4KHLK', 'id': 'PT4KHLK', 'incident_key': 'baf7cf21b1da41b4b0221008339ff357', 'incident_number': 1234, 'is_mergeable': True, 'last_status_change_at': '2015-10-06T21:38:23Z', 'last_status_change_by': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'pending_actions': [{'at': '2015-11-10T01:02:52Z', 'type': 'unacknowledge'}, {'at': '2015-11-10T04:31:52Z', 'type': 'resolve'}], 'priority': {'id': 'P53ZZH5', 'self': 'https://api.pagerduty.com/priorities/P53ZZH5', 'summary': 'P2', 'type': 'priority_reference'}, 'self': 'https://api.pagerduty.com/incidents/PT4KHLK', 'service': {'html_url': 'https://subdomain.pagerduty.com/service-directory/PIJ90N7', 'id': 'PIJ90N7', 'self': 'https://api.pagerduty.com/services/PIJ90N7', 'summary': 'My Mail Service', 'type': 'service_reference'}, 'status': 'resolved', 'summary': '[#1234] The server is on fire.', 'teams': [{'html_url': 'https://subdomain.pagerduty.com/teams/PQ9K7I8', 'id': 'PQ9K7I8', 'self': 'https://api.pagerduty.com/teams/PQ9K7I8', 'summary': 'Engineering', 'type': 'team_reference'}], 'title': 'The server is on fire.', 'type': 'incident', 'updated_at': '2015-10-08T21:30:42Z', 'urgency': 'high'}}|
  
Example output:

```
{
  "incident": {
    "incident": {
      "acknowledgements": [
        {
          "acknowledger": {
            "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
            "id": "PXPGF42",
            "self": "https://api.pagerduty.com/users/PXPGF42",
            "summary": "Earline Greenholt",
            "type": "user_reference"
          },
          "at": "2015-11-10T00:32:52Z"
        }
      ],
      "alert_counts": {
        "all": 0,
        "resolved": 0,
        "triggered": 0
      },
      "assigned_via": "escalation_policy",
      "assignments": [
        {
          "assignee": {
            "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
            "id": "PXPGF42",
            "self": "https://api.pagerduty.com/users/PXPGF42",
            "summary": "Earline Greenholt",
            "type": "user_reference"
          },
          "at": "2015-11-10T00:31:52Z"
        }
      ],
      "conference_bridge": {
        "conference_number": "555-123-4567",
        "conference_url": "https://example.com/123-456-789"
      },
      "created_at": "2015-10-06T21:30:42Z",
      "escalation_policy": {
        "html_url": "https://subdomain.pagerduty.com/escalation_policies/PT20YPA",
        "id": "PT20YPA",
        "self": "https://api.pagerduty.com/escalation_policies/PT20YPA",
        "summary": "Another Escalation Policy",
        "type": "escalation_policy_reference"
      },
      "first_trigger_log_entry": {
        "html_url": "https://subdomain.pagerduty.com/incidents/PT4KHLK/log_entries/Q02JTSNZWHSEKV",
        "id": "Q02JTSNZWHSEKV",
        "self": "https://api.pagerduty.com/log_entries/Q02JTSNZWHSEKV?incident_id=PT4KHLK",
        "summary": "Triggered through the API",
        "type": "trigger_log_entry_reference"
      },
      "html_url": "https://subdomain.pagerduty.com/incidents/PT4KHLK",
      "id": "PT4KHLK",
      "incident_key": "baf7cf21b1da41b4b0221008339ff357",
      "incident_number": 1234,
      "is_mergeable": true,
      "last_status_change_at": "2015-10-06T21:38:23Z",
      "last_status_change_by": {
        "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
        "id": "PXPGF42",
        "self": "https://api.pagerduty.com/users/PXPGF42",
        "summary": "Earline Greenholt",
        "type": "user_reference"
      },
      "pending_actions": [
        {
          "at": "2015-11-10T01:02:52Z",
          "type": "unacknowledge"
        },
        {
          "at": "2015-11-10T04:31:52Z",
          "type": "resolve"
        }
      ],
      "priority": {
        "id": "P53ZZH5",
        "self": "https://api.pagerduty.com/priorities/P53ZZH5",
        "summary": "P2",
        "type": "priority_reference"
      },
      "self": "https://api.pagerduty.com/incidents/PT4KHLK",
      "service": {
        "html_url": "https://subdomain.pagerduty.com/service-directory/PIJ90N7",
        "id": "PIJ90N7",
        "self": "https://api.pagerduty.com/services/PIJ90N7",
        "summary": "My Mail Service",
        "type": "service_reference"
      },
      "status": "resolved",
      "summary": "[#1234] The server is on fire.",
      "teams": [
        {
          "html_url": "https://subdomain.pagerduty.com/teams/PQ9K7I8",
          "id": "PQ9K7I8",
          "self": "https://api.pagerduty.com/teams/PQ9K7I8",
          "summary": "Engineering",
          "type": "team_reference"
        }
      ],
      "title": "The server is on fire.",
      "type": "incident",
      "updated_at": "2015-10-08T21:30:42Z",
      "urgency": "high"
    }
  }
}
```

#### Send Trigger Event
  
Trigger an incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assignments|[]assignee|None|False|Assign the incident to these assignees. Cannot be specified if an escalation policy is given|None|[{"assignee": {"id": "PXPGF42", "type": "user_reference"}}]|
|conference_bridge|conference_bridge_input|None|False|The conference bridge information attached to the incident. Only returned if the include[]=conference_bridge query parameter is provided|None|{'conference_number': '555-123-4567', 'conference_url': 'https://example.com/123-456-789'}|
|email|string|None|True|The email address of a valid user associated with the account making the request|None|user1@example.com|
|escalation_policy|escalation_policy_input|None|False|Assign the incident to this escalation policy. Cannot be specified if Assignments given|None|{'html_url': 'https://subdomain.pagerduty.com/escalation_policies/PT20YPA', 'id': 'PT20YPA', 'self': 'https://api.pagerduty.com/escalation_policies/PT20YPA', 'summary': 'Another Escalation Policy', 'type': 'escalation_policy_reference'}|
|incident_key|string|None|False|A string which identifies the incident. Sending subsequent requests referencing the same service and with the same incident_key will result in those requests being rejected if an open incident matches that incident_key|None|baf7cf21b1da41b4b0221008339ff357|
|priority|priority_input|None|False|The priority that the incident is to be set to|None|{'id': 'P53ZZH5', 'type': 'priority_reference'}|
|service|service_input|None|True|The service that the incident is related to|None|{'id': 'PIJ90N7', 'type': 'service_reference'}|
|title|string|None|True|A description of the nature, symptoms, cause, or effect of the incident|None|The server is on fire.|
|urgency|string|None|False|The urgency that the incident is to be set to|None|high|
|body|body_input|None|False|Details to be added to the incident body|None|{'details': 'A disk is getting full on this machine. You should investigate what is causing the disk to fill.', 'type': 'incident_body'}|
  
Example input:

```
{
  "assignments": {
    "assignee": {
      "id": "PXPGF42",
      "type": "user_reference"
    }
  },
  "body": {
    "details": "A disk is getting full on this machine. You should investigate what is causing the disk to fill.",
    "type": "incident_body"
  },
  "conference_bridge": {
    "conference_number": "555-123-4567",
    "conference_url": "https://example.com/123-456-789"
  },
  "email": "user1@example.com",
  "escalation_policy": {
    "html_url": "https://subdomain.pagerduty.com/escalation_policies/PT20YPA",
    "id": "PT20YPA",
    "self": "https://api.pagerduty.com/escalation_policies/PT20YPA",
    "summary": "Another Escalation Policy",
    "type": "escalation_policy_reference"
  },
  "incident_key": "baf7cf21b1da41b4b0221008339ff357",
  "priority": {
    "id": "P53ZZH5",
    "type": "priority_reference"
  },
  "service": {
    "id": "PIJ90N7",
    "type": "service_reference"
  },
  "title": "The server is on fire.",
  "urgency": "high"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident_output|False|The incident object that was created|{'incident': {'acknowledgements': [{'acknowledger': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'at': '2015-11-10T00:32:52Z'}], 'alert_counts': {'all': 0, 'resolved': 0, 'triggered': 0}, 'assigned_via': 'escalation_policy', 'assignments': [{'assignee': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'at': '2015-11-10T00:31:52Z'}], 'conference_bridge': {'conference_number': '555-123-4567', 'conference_url': 'https://example.com/123-456-789'}, 'created_at': '2015-10-06T21:30:42Z', 'escalation_policy': {'html_url': 'https://subdomain.pagerduty.com/escalation_policies/PT20YPA', 'id': 'PT20YPA', 'self': 'https://api.pagerduty.com/escalation_policies/PT20YPA', 'summary': 'Another Escalation Policy', 'type': 'escalation_policy_reference'}, 'first_trigger_log_entry': {'html_url': 'https://subdomain.pagerduty.com/incidents/PT4KHLK/log_entries/Q02JTSNZWHSEKV', 'id': 'Q02JTSNZWHSEKV', 'self': 'https://api.pagerduty.com/log_entries/Q02JTSNZWHSEKV?incident_id=PT4KHLK', 'summary': 'Triggered through the API', 'type': 'trigger_log_entry_reference'}, 'html_url': 'https://subdomain.pagerduty.com/incidents/PT4KHLK', 'id': 'PT4KHLK', 'incident_key': 'baf7cf21b1da41b4b0221008339ff357', 'incident_number': 1234, 'is_mergeable': True, 'last_status_change_at': '2015-10-06T21:38:23Z', 'last_status_change_by': {'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42', 'id': 'PXPGF42', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'summary': 'Earline Greenholt', 'type': 'user_reference'}, 'pending_actions': [{'at': '2015-11-10T01:02:52Z', 'type': 'unacknowledge'}, {'at': '2015-11-10T04:31:52Z', 'type': 'resolve'}], 'priority': {'id': 'P53ZZH5', 'self': 'https://api.pagerduty.com/priorities/P53ZZH5', 'summary': 'P2', 'type': 'priority_reference'}, 'self': 'https://api.pagerduty.com/incidents/PT4KHLK', 'service': {'html_url': 'https://subdomain.pagerduty.com/service-directory/PIJ90N7', 'id': 'PIJ90N7', 'self': 'https://api.pagerduty.com/services/PIJ90N7', 'summary': 'My Mail Service', 'type': 'service_reference'}, 'status': 'resolved', 'summary': '[#1234] The server is on fire.', 'teams': [{'html_url': 'https://subdomain.pagerduty.com/teams/PQ9K7I8', 'id': 'PQ9K7I8', 'self': 'https://api.pagerduty.com/teams/PQ9K7I8', 'summary': 'Engineering', 'type': 'team_reference'}], 'title': 'The server is on fire.', 'type': 'incident', 'updated_at': '2015-10-08T21:30:42Z', 'urgency': 'high'}}|
  
Example output:

```
{
  "incident": {
    "incident": {
      "acknowledgements": [
        {
          "acknowledger": {
            "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
            "id": "PXPGF42",
            "self": "https://api.pagerduty.com/users/PXPGF42",
            "summary": "Earline Greenholt",
            "type": "user_reference"
          },
          "at": "2015-11-10T00:32:52Z"
        }
      ],
      "alert_counts": {
        "all": 0,
        "resolved": 0,
        "triggered": 0
      },
      "assigned_via": "escalation_policy",
      "assignments": [
        {
          "assignee": {
            "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
            "id": "PXPGF42",
            "self": "https://api.pagerduty.com/users/PXPGF42",
            "summary": "Earline Greenholt",
            "type": "user_reference"
          },
          "at": "2015-11-10T00:31:52Z"
        }
      ],
      "conference_bridge": {
        "conference_number": "555-123-4567",
        "conference_url": "https://example.com/123-456-789"
      },
      "created_at": "2015-10-06T21:30:42Z",
      "escalation_policy": {
        "html_url": "https://subdomain.pagerduty.com/escalation_policies/PT20YPA",
        "id": "PT20YPA",
        "self": "https://api.pagerduty.com/escalation_policies/PT20YPA",
        "summary": "Another Escalation Policy",
        "type": "escalation_policy_reference"
      },
      "first_trigger_log_entry": {
        "html_url": "https://subdomain.pagerduty.com/incidents/PT4KHLK/log_entries/Q02JTSNZWHSEKV",
        "id": "Q02JTSNZWHSEKV",
        "self": "https://api.pagerduty.com/log_entries/Q02JTSNZWHSEKV?incident_id=PT4KHLK",
        "summary": "Triggered through the API",
        "type": "trigger_log_entry_reference"
      },
      "html_url": "https://subdomain.pagerduty.com/incidents/PT4KHLK",
      "id": "PT4KHLK",
      "incident_key": "baf7cf21b1da41b4b0221008339ff357",
      "incident_number": 1234,
      "is_mergeable": true,
      "last_status_change_at": "2015-10-06T21:38:23Z",
      "last_status_change_by": {
        "html_url": "https://subdomain.pagerduty.com/users/PXPGF42",
        "id": "PXPGF42",
        "self": "https://api.pagerduty.com/users/PXPGF42",
        "summary": "Earline Greenholt",
        "type": "user_reference"
      },
      "pending_actions": [
        {
          "at": "2015-11-10T01:02:52Z",
          "type": "unacknowledge"
        },
        {
          "at": "2015-11-10T04:31:52Z",
          "type": "resolve"
        }
      ],
      "priority": {
        "id": "P53ZZH5",
        "self": "https://api.pagerduty.com/priorities/P53ZZH5",
        "summary": "P2",
        "type": "priority_reference"
      },
      "self": "https://api.pagerduty.com/incidents/PT4KHLK",
      "service": {
        "html_url": "https://subdomain.pagerduty.com/service-directory/PIJ90N7",
        "id": "PIJ90N7",
        "self": "https://api.pagerduty.com/services/PIJ90N7",
        "summary": "My Mail Service",
        "type": "service_reference"
      },
      "status": "resolved",
      "summary": "[#1234] The server is on fire.",
      "teams": [
        {
          "html_url": "https://subdomain.pagerduty.com/teams/PQ9K7I8",
          "id": "PQ9K7I8",
          "self": "https://api.pagerduty.com/teams/PQ9K7I8",
          "summary": "Engineering",
          "type": "team_reference"
        }
      ],
      "title": "The server is on fire.",
      "type": "incident",
      "updated_at": "2015-10-08T21:30:42Z",
      "urgency": "high"
    }
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|avatar_url|string|None|None|Avatar URL|https://secure.gravatar.com/avatar/c67b6c8ed606dec999bb064ada88cf5c.png?d=mm&r=PG|
|color|string|None|None|Color|purple|
|description|string|None|None|Description|test description|
|email|string|None|True|Email|user1@example.com|
|id|string|None|None|ID|PYGDZB8|
|job_title|string|None|None|Job Title|engineer|
|name|string|None|True|Name|test user|
|role|string|None|None|Role|None|
|self|string|None|None|URL to view object|https://api.pagerduty.com/users/PYGDZB8|
|summary|string|None|None|Summary|test summary|
|time_zone|string|None|None|Time Zone, e.g. America/Lima|Europe/London|
  
**incident_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|acknowledgements|array|None|None|List of all acknowledgements for this incident. This list will be empty if the Incident.status is resolved or triggered. If the include[]=acknowledgers query parameter is provided, the full user or service definitions will be returned for each acknowledgement entry|[{'at': '2015-11-10T00:32:52Z', 'acknowledger': {'id': 'PXPGF42', 'type': 'user_reference', 'summary': 'Earline Greenholt', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42'}}]|
|alert_counts|object|None|None|The counts of alerts grouped into this incident|{'all': 0, 'resolved': 0, 'triggered': 0}|
|assigned_via|string|None|None|How the current incident assignments were decided. Note that direct_assignment incidents will not escalate up the attached escalation_policy|escalation_policy|
|assignments|array|None|None|Which accounts the incident will be assigned to|[{'at': '2015-11-10T00:31:52Z', 'assignee': {'id': 'PXPGF42', 'type': 'user_reference', 'summary': 'Earline Greenholt', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42'}}]|
|conference_bridge|object|None|None|The conference bridge information attached to the incident. Only returned if the include[]=conference_bridge query parameter is provided|{'conference_number': '555-123-4567', 'conference_url': 'https://example.com/123-456-789'}|
|created_at|string|None|None|The time the incident was first triggered|2015-10-06T21:30:42Z|
|escalation_policy|object|None|None|The escalation policy attached to the service that the incident is on. If the include[]=escalation_policies query parameter is provided, the full escalation policy definition will be returned|{'id': 'PT20YPA', 'type': 'escalation_policy_reference', 'summary': 'Another Escalation Policy', 'self': 'https://api.pagerduty.com/escalation_policies/PT20YPA', 'html_url': 'https://subdomain.pagerduty.com/escalation_policies/PT20YPA'}|
|first_trigger_log_entry|object|None|None|The first log entry on the incident. The log entry will be of type TriggerLogEntry and will represent information about how the incident was triggered. If the include[]=first_trigger_log_entries query parameter is provided, the full log entry definition will be returned|{'id': 'Q02JTSNZWHSEKV', 'type': 'trigger_log_entry_reference', 'summary': 'Triggered through the API', 'self': 'https://api.pagerduty.com/log_entries/Q02JTSNZWHSEKV?incident_id=PT4KHLK', 'html_url': 'https://subdomain.pagerduty.com/incidents/PT4KHLK/log_entries/Q02JTSNZWHSEKV'}|
|html_url|string|None|None|a URL at which the entity is uniquely displayed in the Web app|https://subdomain.pagerduty.com/incidents/PT4KHLK|
|id|string|None|None|the id of the incident|PT4KHLK|
|incident_key|string|None|None|The incident's de-duplication key|baf7cf21b1da41b4b0221008339ff357|
|incident_number|integar|None|None|The number of the incident. This is unique across your account.|1234|
|is_mergeable|boolean|None|None|Whether the incident is mergeable. Only incidents that have alerts, or that are manually created can be merged|True|
|last_status_change_at|string|None|None|The time the status of the incident last changed. If the incident is not currently acknowledged or resolved, this will be the incident's updated_at|2015-10-06T21:38:23Z|
|last_status_change_by|object|None|None|The agent (user, service or integration) that created or modified the Incident Log Entry|{'id': 'PXPGF42', 'type': 'user_reference', 'summary': 'Earline Greenholt', 'self': 'https://api.pagerduty.com/users/PXPGF42', 'html_url': 'https://subdomain.pagerduty.com/users/PXPGF42'}|
|pending_actions|array|None|None|The list of pending_actions on the incident. A pending_action object contains a type of action which can be escalate, unacknowledge, resolve or urgency_change. A pending_action object contains at, the time at which the action will take place. An urgency_change pending_action will contain to, the urgency that the incident will change to|[{'type': 'unacknowledge', 'at': '2015-11-10T01:02:52Z'}, {'type': 'resolve', 'at': '2015-11-10T04:31:52Z'}]|
|priority|object|None|None|The priority of the object|{'id': 'P53ZZH5', 'type': 'priority_reference', 'summary': 'P2', 'self': 'https://api.pagerduty.com/priorities/P53ZZH5'}|
|self|string|None|None|the API show URL at which the object is accessible|https://api.pagerduty.com/incidents/PT4KHLK|
|service|object|None|None|The service the incident is on. If the include[]=services query parameter is provided, the full service definition will be returned|{'id': 'PIJ90N7', 'type': 'service_reference', 'summary': 'My Mail Service', 'self': 'https://api.pagerduty.com/services/PIJ90N7', 'html_url': 'https://subdomain.pagerduty.com/service-directory/PIJ90N7'}|
|status|string|None|None|The current status of the incident|resolved|
|summary|string|None|None|A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier|[#1234] The server is on fire.|
|teams|array|None|None|Teams that the alert is assigned to|[{'id': 'PQ9K7I8', 'type': 'team_reference', 'summary': 'Engineering', 'self': 'https://api.pagerduty.com/teams/PQ9K7I8', 'html_url': 'https://subdomain.pagerduty.com/teams/PQ9K7I8'}]|
|title|string|None|None|A succinct description of the nature, symptoms, cause, or effect of the incident|The server is on fire.|
|type|string|None|None|A string that determines the schema of the object|incident|
|updated_at|string|None|None|The time the incident was last modified|2015-10-08T21:30:42Z|
|urgency|string|None|None|The current urgency of the incident|high|
  
**service_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The id of the service that the incident is related to|PWIXJZS|
|type|string|None|True|The type of the service that the incident is related to|service_reference|
  
**priority_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The id of the priority that the incident is to be set to|P53ZZH5|
|type|string|None|True|The type of the priority that the incident is to be set to|priority_reference|
  
**body_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|details|string|None|True|The id of the priority that the incident is to be set to|A disk is getting full on this machine. You should investigate what is causing the disk to fill|
|type|string|None|True|The type of the body is to be added to|incident_body|
  
**assignee**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|None|The id of the user that the new incident will be assigned to|PXPGF42|
|type|string|None|None|A string that determines the schema of the object.|user_reference|
  
**escalation_policy_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|html_url|string|None|None|a URL at which the entity is uniquely displayed in the Web app|https://subdomain.pagerduty.com/escalation_policies/PT20YPA|
|id|string|None|None|The id of the escalation policy that the new incident will be assigned to|PT20YPA|
|self|string|None|None|the API show URL at which the object is accessible|https://api.pagerduty.com/escalation_policies/PT20YPA|
|summary|string|None|None|A short-form, server-generated string that provides succinct, important information about an object|Another Escalation Policy|
|type|string|None|None|A string that determines the schema of the object.|escalation_policy_reference|
  
**conference_bridge_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|conference_number|string|None|None|The phone number of the conference call for the conference bridge. Phone numbers should be formatted like +1 415-555-1212,,,,1234#, where a comma (,) represents a one-second wait and pound (#) completes access code input|555-123-4567|
|conference_url|string|None|None|An URL for the conference bridge. This could be a link to a web conference or Slack channel|https://example.com/123-456-789|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 3.0.0 - `Refactor`: Re-write plugin to use `requests` instead of `pypd` package | Action: `Get User By Email` - Removed | `Unit Tests`: Added for all actions.
* 2.2.0 - Added Schedule ID optional input to Get On Call action
* 2.1.0 - New action Get On Call
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Fix issue to make 'service_key' required in Send Resolve Request action
* 1.0.1 - Update to [PagerDuty REST API v2](https://v2.developer.pagerduty.com/docs/migrating-to-api-v2)
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [PagerDuty API V2](https://v2.developer.pagerduty.com/v2/page/api-reference)

## References
  
* [PagerDuty API V2](https://v2.developer.pagerduty.com/v2/page/api-reference)