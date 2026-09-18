# Description

Rapid7 Cyber GRC is a governance, risk, and compliance solution. This plugin manages risks, incidents, tasks, audits, control sets, assessments, vendors, certifications, IT assets, and users, and uploads evidence through the Flat File API

# Key Features

* Read, create, update, and delete risks, incidents, tasks, audits, control sets, assessments, vendors, certifications, IT assets, and users
* Query any Cyber GRC record type using OData filters, with automatic paging
* Retrieve the change history of a record
* Upload evidence to Cyber GRC with the Flat File API
* Read the compliance score and automated controls score of each framework
* Read, create, update, and delete contracts, and find the ones renewing soon
* Comment on a record so a workflow can mirror a comment made in a chat or ticketing system
* Trigger workflows when records are created or updated, or when a framework's compliance score falls

# Use Cases

### Tell people about their work in the tool they already live in

**Value:** GRC owners will not sign in to a compliance platform to find out what they owe. Task
reminders reach them where they already are, so due dates are met without anyone chasing.

**How:** Get Tasks, narrowed with Owner and either Due Within Days or Overdue Only, then a chat or
email step. Scheduling the workflow at 30, 14, and 7 days gives the escalating cadence auditors
expect.

### Alert the team when a framework starts slipping

**Value:** A compliance score that falls between audits is the earliest warning that evidence has
stopped arriving. Catching the fall the week it happens is the difference between a fix and a
finding.

**How:** The Monitor Compliance Drift trigger, with Drop Threshold set to the fall worth waking
someone for and Minimum Compliance set to the score you have committed to. It reports the framework
name, the previous and current scores, and the size of the fall, so the notification says what moved
rather than just that something did.

### Keep Cyber GRC and your ticketing system in step

**Value:** Work is tracked where each team already works, without anyone re-typing status updates
into a second system. The compliance record stays complete for the auditor either way.

**How:** The Monitor Records trigger on Tasks to push changes out to Jira, ServiceNow, Zendesk, or
Freshservice, and Update Task with Add Comment to bring the reply back. Add Comment also lets a
workflow write a Slack or Teams reply straight onto the record.

### Chase a contract before it renews itself

**Value:** An auto-renewal nobody reviewed is money spent on a vendor nobody reassessed. A standing
workflow means the notice period is never the thing that was missed.

**How:** Get Contracts with Renewing Within Days set to your notice period, then notify the owner
and Create Task for the review. Include Expired catches the renewals that already slipped past.

### Onboard and offboard vendors without the checklist

**Value:** Every new vendor gets the same assessment, and a vendor that leaves stops holding access
it no longer needs, both without depending on someone remembering the steps.

**How:** The Monitor Records trigger on Vendors to start the onboarding workflow, then Create Task
or Create Assessment for the review. On the way out, Update Vendor or Delete Vendor alongside the
deprovisioning steps in your identity and SaaS tools.

### Publish who your third parties are, and say when that changes

**Value:** Customers ask who you rely on, and a stale list is worse than no list. Answering from the
live vendor register turns a recurring request into a standing report.

**How:** Get Vendors on a schedule to publish the list, and the Monitor Records trigger on Vendors to
notify the people who subscribed to it whenever it changes.

### Feed the risk register from what security is actually seeing

**Value:** A risk register fed by hand drifts away from reality. One fed from live telemetry stays at
the altitude leadership can act on, and stays defensible in front of an auditor.

**How:** Create Risk or Update Risk from an emerging threat, a critical exposure, or a Rapid7 risk
score, so the register carries the reasoning and the evidence rather than a note that someone was
worried once.

### Escalate work that is not getting done

**Value:** A task that keeps slipping is a risk the organisation has not admitted to yet. Escalating
it on a rule rather than an argument gets it in front of the people who can fund the fix.

**How:** Get Tasks with Overdue Only, then Create Risk for the ones past your tolerance, linking the
task so the history travels with it.

### Report the compliance posture on a schedule

**Value:** Board and executive reporting stops being a week of assembly. The same numbers reach the
same people every month, from the system of record.

**How:** Get Compliance Score for the per framework and overall scores, then a document, dashboard,
or email step. The automated controls percentage alongside each score shows how much of the
programme is running without people.

### Push evidence in instead of taking screenshots

**Value:** Evidence collected by hand is the single biggest cost in an audit, and screenshots are the
part auditors trust least. Data that arrives from the source system arrives already dated.

**How:** Upload Flat File to land a CSV or Excel export from any of the 300+ systems InsightConnect
already connects to, on the schedule the control requires.

# Requirements

* A Cyber GRC API key
* The base URL of your Cyber GRC API host

# Supported Product Versions

* Rapid7 Cyber GRC Web API v2
* Rapid7 Cyber GRC API v1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|A Cyber GRC API key, generated under Settings then API Keys. The key inherits the permissions of the user it is assigned to|None|cpyl_0000000000000000000000000000000000000000000000|None|None|
|ssl_verify|boolean|True|True|Verify the TLS certificate presented by the Cyber GRC API host|None|True|None|None|
|url|string|None|True|Base URL of the Cyber GRC API host, without a trailing path|None|https://app-example-std-use2-api-01.azurewebsites.net|None|None|

Example input:

```
{
  "api_key": "cpyl_0000000000000000000000000000000000000000000000",
  "ssl_verify": true,
  "url": "https://app-example-std-use2-api-01.azurewebsites.net"
}
```

### Generating an API key

1. Sign in to the [Rapid7 Platform](https://insight.rapid7.com) and select **GRC** in the top right of the navigation bar to open Cyber GRC.
2. In Cyber GRC, select the gear icon in the top right of the navigation bar and choose **Settings**.

![Opening Settings from the gear menu](https://raw.githubusercontent.com/rapid7/insightconnect-plugins/master/plugins/rapid7_cyber_grc/doc/01-gear-menu-settings.png)

3. Select the **Security** tab, expand **API Keys**, and select **Create New Key**.

![The API Keys section of the Security tab](https://raw.githubusercontent.com/rapid7/insightconnect-plugins/master/plugins/rapid7_cyber_grc/doc/02-settings-security-api-keys.png)

4. Complete the dialog and select **Create**:

* **Key Name** is a descriptive label for the key, for example `InsightConnect`.
* **Expiration Date** is optional. A key stops working on its expiration date, and the connection then fails with a 401, so either leave it blank for an unattended workflow or plan to rotate the key before that date.
* **User** is the user the key authenticates as. The key inherits that user's UAM permissions, so choose a user who can see and change every record type the workflow uses. Requests outside those permissions are answered with a 403.

![The Create New API Key dialog](https://raw.githubusercontent.com/rapid7/insightconnect-plugins/master/plugins/rapid7_cyber_grc/doc/03-create-new-api-key.png)

5. Copy the generated key, which begins with `cpyl_`, and store it in the connection's API Key field.

### Finding the API host

The URL for this connection is the Cyber GRC **API** host, which is not the host used to sign in to the web interface. It follows the pattern `https://app-<tenant>-<brand>-<region>-api-01.azurewebsites.net`. The web interface answers every path with its sign-in page, including API paths, so a connection pointed at it receives HTML rather than JSON. Contact Rapid7 support if the API host for your tenant is not known.

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|A Cyber GRC API key, generated under Settings then API Keys. The key inherits the permissions of the user it is assigned to|None|cpyl_0000000000000000000000000000000000000000000000|None|None|
|ssl_verify|boolean|True|True|Verify the TLS certificate presented by the Cyber GRC API host|None|True|None|None|
|url|string|None|True|Base URL of the Cyber GRC API host, without a trailing path|None|https://app-example-std-use2-api-01.azurewebsites.net|None|None|

Example input:

```
{
  "api_key": "cpyl_0000000000000000000000000000000000000000000000",
  "ssl_verify": true,
  "url": "https://app-example-std-use2-api-01.azurewebsites.net"
}
```

### Query options

The Cyber GRC Web API v2 is an OData v4 API, so every read action and the Monitor Records trigger accept the same query options: **Filter**, **Select**, **Order By**, **Top**, and **Skip**. All of them are optional, and leaving them empty returns whole records with no narrowing.

Two of them repay a closer look, because they are the ones that make a workflow read only what it needs.

#### Filter

Filter is an OData `$filter` expression, evaluated by the API before it answers, so it is the cheapest way to narrow a step. Field names are the camelCase names in the [API reference](https://compyl.readme.io/reference/) record schemas, not the labels shown in the web interface.

|Goal|Filter|
| :--- | :--- |
|Records in one status|`statusID eq 3`|
|One named record|`name eq 'Annual Access Review'`|
|Either of two statuses|`statusID eq 3 or statusID eq 4`|
|Records that are not archived|`isArchived eq false`|
|Records with a due date, due before a date|`dueDate ne null and dueDate lt 2026-12-31T00:00:00.000Z`|
|Records with no due date at all|`dueDate eq null`|
|A status and a date together|`statusID eq 3 and startDate ge 2026-01-01T00:00:00.000Z`|

The literal rules are worth knowing, because getting one wrong is the usual cause of a step that fails rather than returning nothing:

* Text values are wrapped in single quotes, and a literal apostrophe inside one is doubled: `name eq 'Vendor''s review'`.
* Numbers and booleans are unquoted, and booleans are lowercase `true` and `false`.
* Dates and times are unquoted ISO 8601 in UTC, for example `2026-12-31T00:00:00.000Z`. Quoting one is rejected.
* An empty field is tested with `eq null` or `ne null`, and a date comparison is worth pairing with `ne null` so records that have never had a date set are excluded deliberately rather than by accident.
* OData also defines functions such as `contains(name, 'Access')` and `startswith(name, 'Q1')`. They are not supported uniformly across every collection, so try one before relying on it.
* A field that holds a nested object, such as a task's `assignedTo`, has no filterable value beside it. Get Tasks has an **Owner** input for that case, which matches the assignee's email address or user ID after the records are read.

An expression the API cannot parse is answered with a **400 and the reason**, not with an empty result, and the plugin surfaces that reason on the failed step. So a step that returns nothing means the filter was valid and matched nothing.

On the **Monitor Records** trigger the Filter is combined with the trigger's own timestamp filter using `and`, and both sides are parenthesised first. An `or` in the Filter is therefore safe: `statusID eq 3 or statusID eq 4` narrows the emitted records rather than widening them back out to records the trigger has already reported.

#### Why there is no Expand option

OData normally offers `$expand` for pulling in related records that are not returned by
default. This plugin does not offer it, because on this API there is nothing for it to do.

Every record type **already embeds its related collections in every response**. A task
requested with no query options at all comes back with `risks`, `departments`, `controls`,
`itAssets`, `vendors`, `assessments`, `audits`, `clients`, `contracts`, `incidents`,
`locations`, and `securityPolicies` populated, so a workflow that needs a task and the
risks attached to it already has both.

Those collections are ordinary array properties of the record rather than OData navigation
properties, so naming one in `$expand` is rejected:

```
GET /api/v2/Tasks?$expand=risks   ->   400
Property 'risks' on type 'Presentation.DTOs.Task.GetTaskDto' is not a navigation
property or complex property. Only navigation properties can be expanded.
```

`$expand=*` is accepted everywhere but adds nothing, and the only genuine navigation
property in the API is `auditorAssignments` on Audits. An Expand input would therefore
have been a field whose every plausible value broke the step, so it was removed.

The practical consequence is that records are large: 48 properties on a task, one of which
held 65 nested controls in testing. **Select** is the way to cut that down, and it works as
expected, for example `id,name,dueDate,statusID`. Narrowing a polling trigger with Select
is worth doing.

### Monitor Records

The trigger reports what happens from the moment it starts. On its first poll it records where it is and emits nothing; from then on it emits each record the chosen **Event Type** matches. It does not open with a batch of history, so a workflow attached to it never acts on records that were already dealt with before it was switched on.

The position is stored in the plugin's cache, which InsightConnect backs with a volume, so a restart resumes where the trigger left off rather than skipping whatever changed while it was down.

**Event Type** decides which events reach the workflow:

|Event Type|Emits|
| :--- | :--- |
|Any|Both of the below, so a record arrives when it appears and again on every change|
|Created|Each record once, when it first appears|
|Updated|A record every time it changes, but not when it is created|

Deletion is not one of the options, because the API offers no way to see it. A deleted record is removed outright rather than flagged, there is no tombstone collection and no event or webhook endpoint, so a poll cannot tell a deleted record from one that was never there. Archiving is visible, though, on the record types that support it: watch for Updated and add a Filter of `isArchived eq true`.

Each Event Type is found by different timestamps, so each one keeps its own position. Changing Event Type on a running trigger therefore starts a fresh position rather than resuming from another one, which measures something different.

Two timestamps carry the events. `createdDate` is stamped once and never moves. `modifiedDate` is **null until something edits the record** and moves on every edit afterwards, so a record that has only ever been created carries no `modifiedDate` at all. Created therefore watches `createdDate`, Updated watches `modifiedDate`, and Any watches both, because a creation is invisible in `modifiedDate`.

A record is treated as a change when it carries a `modifiedDate`, and where it carries both timestamps they must also differ. A record carrying a `modifiedDate` but no `createdDate` is emitted rather than discarded, because losing a real change is worse than emitting a creation the workflow can ignore.

One caveat on timing: the position starts from the clock of the container the plugin runs in, while record timestamps come from the Cyber GRC server. If the server clock runs behind, records created in the first moments after the trigger starts can be stamped below the opening position and skipped. This only affects the very first poll, and only by the size of the difference between the two clocks.

### Using the trigger output in a workflow

Monitor Records emits `records`, an array of whole records, and `count`. A workflow step
reads a field off the first record with `{{[Monitor Records].[records].[0].[id]}}`, and
loops over `records` when a poll returns several. The emitted record is the record as the
API returns it, so every field the record type has is available to later steps without a
lookup, including the related collections such as `risks` and `departments`.

The **ID** the trigger emits drives every single-record action directly: Get Task, Get
Record, Get Record History, Update Task, Delete Task and their equivalents for each
record type. The trigger's own **Record Type** is what the generic actions want for their
Record Type input. The emitted record can also be passed straight back as the `record`
body of an update, which is the simplest way to change one field and leave every other field untouched.

Three limits are worth knowing before wiring a workflow:

|Limit|What it means|
| :--- | :--- |
|A task cannot be reassigned through the API|`assignedTo` is read only. No update body sets it, and the API has no assignment endpoint, so a workflow can report who a task belongs to but cannot change it. Assignment has to happen in the Cyber GRC web interface. Because Cyber GRC answers such an update with 204 as though it had worked, the update actions log a warning when a body names an assignee, rather than let a workflow believe it reassigned the record|
|Add Comment needs a **User ID** and a record that already has a comment thread|Cyber GRC rejects a comment that does not name an author. It also ties a comment to a record by that record's `discussionFieldID`, which it does not create until the record has been opened in the web interface at least once, so a record the trigger has only just reported usually cannot be commented on yet|
|Record names must be unique|Creating a second record with a name already in use is rejected with `There is already a task named ...`, so a workflow that creates records from an event should put something distinguishing in the name|

## Technical Details

### Actions


#### Add Comment

This action is used to add a comment to a Cyber GRC record, mirroring a comment made in a chat or ticketing system

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Text of the comment|None|Closed in the ticketing system by the asset owner|None|None|
|discussion_field_id|integer|None|False|Overrides the Discussion Field ID the action would otherwise read from the record itself. Only needed if the record does not carry one|None|12|None|None|
|form_discussion_id|integer|None|False|Overrides the Form Discussion ID, which the action defaults to the record ID. Cyber GRC does not document how this field resolves, so set it explicitly if comments do not appear against the record|None|1|None|None|
|id|integer|None|True|ID of the record to comment on|None|1|None|None|
|record_type|string|Tasks|True|The type of record to comment on|["Audits", "Clients", "Contracts", "ControlSets", "Departments", "ITAssets", "Incidents", "Locations", "Risks", "Tasks", "Vendors"]|Tasks|None|None|
|user_id|integer|None|True|Cyber GRC user ID to record as the author. Cyber GRC rejects a comment that does not name an author, so this is required. Get Users lists the IDs to choose from|None|5|None|None|
  
Example input:

```
{
  "comment": "Closed in the ticketing system by the asset owner",
  "discussion_field_id": 12,
  "form_discussion_id": 1,
  "id": 1,
  "record_type": "Tasks",
  "user_id": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|comment|discussion|True|The created comment|None|
  
Example output:

```
{
  "comment": {
    "Comment": "",
    "Created By": {},
    "Created Date": "",
    "Discussion Field ID": {},
    "Form Discussion ID": {},
    "ID": 0,
    "Modified By": {},
    "Modified Date": {},
    "User ID": {}
  }
}
```

#### Count Records

This action is used to count the records of any Cyber GRC record type that match an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the count. Leave empty to count every record|None|statusID eq 3|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of matching records|1|
  
Example output:

```
{
  "count": 1
}
```

#### Create Assessment

This action is used to create a new assessment in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The assessment to create, as a JSON object matching the CreateAssessmentDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example assessment'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example assessment"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assessment|assessment|True|The created assessment|None|
  
Example output:

```
{
  "assessment": {
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "Enabled": {},
    "Form Entry Name": {},
    "Frequency": {},
    "ID": {},
    "Is Accepted": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Should Populate Answers": {},
    "Should Repeat": {},
    "Start Date": "",
    "Submitted Date": {},
    "Summary": {},
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Times Duplicated": {},
    "Trend": {},
    "Users": [
      {
        "Email": {},
        "ID": 0,
        "Name": ""
      }
    ],
    "Was Submitted": "true"
  }
}
```

#### Create Audit

This action is used to create a new audit in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The audit to create, as a JSON object matching the CreateAuditDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example audit'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example audit"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|audit|audit|True|The created audit|None|
  
Example output:

```
{
  "audit": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audit Users": [
      {
        "Active": "true",
        "ID": {},
        "Name": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      }
    ],
    "Auditor Findings": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Set": {
      "ID": 0,
      "Name": {}
    },
    "Control Set ID": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Documents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "Frequency Name": "",
    "ID": {},
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Observation Period End": {},
    "Observation Period Start": "",
    "Start Date": {},
    "Status": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Create Certification

This action is used to create a new certification in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The certification to create, as a JSON object matching the CreateCertificationDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example certification'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example certification"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certification|certification|True|The created certification|None|
  
Example output:

```
{
  "certification": {
    "Created By": {},
    "Created Date": "",
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Active": "true",
    "Modified By": {},
    "Modified Date": {},
    "Name": ""
  }
}
```

#### Create Contract

This action is used to create a new contract in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The contract to create, as a JSON object matching the CreateContractDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example contract'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example contract"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|contract|contract|True|The created contract|None|
  
Example output:

```
{
  "contract": {
    "Annual Cost": {},
    "Approval Status": "true",
    "Category": {
      "ID": {},
      "Name": {}
    },
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Contact Email": {},
    "Contact Name": {},
    "Contract Category ID": {},
    "Contract Documents": [
      {
        "Blob Name": {},
        "Contract ID": {},
        "ID": {},
        "Is Current Version": {},
        "Is Working Version": {},
        "Title": {},
        "Version": {}
      }
    ],
    "Contract Subcategory ID": {},
    "Contract Type": {},
    "Cost Type": {},
    "Created By": "",
    "Created Date": "",
    "Currency": {},
    "Days Until Renewal": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "End Date": {},
    "Extended Fields": {},
    "Generated Date": {},
    "Has Enabled Adobe Sync": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Invoice Frequency": {},
    "Is Key Contract": {},
    "Max Extension": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Notice Date": {},
    "Parent Contract": {
      "ID": {},
      "Name": {}
    },
    "Parent Contract ID": {},
    "Sequence Number": {},
    "Start Date": {},
    "Status": {
      "ID": {},
      "Name": {}
    },
    "Status ID": {},
    "Subcategory": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Termination Notice Period": {},
    "Variation Number": {},
    "Vendors": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Create Control Set

This action is used to create a new control set in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The control set to create, as a JSON object matching the CreateControlSetDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example control set'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example control set"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|control_set|control_set|True|The created control set|None|
  
Example output:

```
{
  "control_set": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Controls": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Description": {},
    "Discussion Field ID": {},
    "Enabled": "true",
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Rapid7 Key": {},
    "Security Policy Info ID": {},
    "Type": {}
  }
}
```

#### Create Incident

This action is used to create a new incident in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The incident to create, as a JSON object matching the CreateIncidentDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example incident'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example incident"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|True|The created incident|None|
  
Example output:

```
{
  "incident": {
    "Client Security Assessments Issued": {},
    "Confidential Data Impacted": {},
    "Created By": {},
    "Created Date": {},
    "Customer Data Impacted": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "How Identified": {},
    "How Occurred": {},
    "ID": 0,
    "Identified Date": "",
    "Immediate Action": {},
    "Impact Type": {},
    "Investigations Fines": {},
    "Lessons Learned": {},
    "Location ID": {},
    "Material Impact": {},
    "Modified By": {},
    "Modified Date": {},
    "Monetary Impact": {},
    "Name": "",
    "Non Confidential Data Impacted": {},
    "Occured Date": {},
    "Personal Identifiable Info Impacted": {},
    "Realized Financial Loss": {},
    "Reputational Damage": {},
    "Root Cause": {},
    "Send Reminders": "true",
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Create IT Asset

This action is used to create a new it asset in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The it asset to create, as a JSON object matching the CreateITAssetDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example it asset'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example it asset"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|it_asset|it_asset|True|The created it asset|None|
  
Example output:

```
{
  "it_asset": {
    "A1": {},
    "A2": {},
    "A3": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "C1": {},
    "C2": {},
    "C3": {},
    "Calculated CIA": {},
    "Certifications": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Sets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Has Personal Data": "true",
    "I1": {},
    "I2": {},
    "I3": {},
    "ID": {},
    "Is BCP": {},
    "Is Client Data Host": {},
    "Is Client Facing": {},
    "Is DFA": {},
    "Is DR": {},
    "Is Data Anonymous": {},
    "Is Data At-Rest": {},
    "Is Data In Transit": {},
    "Is Desktop App": {},
    "Is Dev In House": {},
    "Is Hosted In Cloud": {},
    "Is Individual Perms": {},
    "Is Our Data Host": {},
    "Is Pre Prod Env": {},
    "Is Prod Data Used In Non Prod Env": {},
    "Is Production Env": {},
    "Is Public Internet Facing": {},
    "Is Role Based": {},
    "Is Role Based Access": {},
    "Is SIEM Monitored": {},
    "Is SSO": {},
    "Is SSO Authenticated": {},
    "Is SSO Authorised": {},
    "Is Security Testing Required": {},
    "Is Service Accounts": {},
    "Is Test Data Personal": {},
    "Is Test Env": {},
    "Is Tested": {},
    "Is UAT Env": {},
    "Is Web Based App": {},
    "Life Cycle": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Number Of Users": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "System Type": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {}
  }
}
```

#### Create Record

This action is used to create a record of any Cyber GRC record type

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The record to create, as a JSON object matching the corresponding Create DTO in the Rapid7 Cyber GRC API reference|None|{'name': 'Example record'}|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example record"
  },
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|record|object|True|The created record|None|
  
Example output:

```
{
  "record": {}
}
```

#### Create Risk

This action is used to create a new risk in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The risk to create, as a JSON object matching the CreateRiskDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example risk'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example risk"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|risk|risk|True|The created risk|None|
  
Example output:

```
{
  "risk": {
    "Assessment ID": {},
    "Business Impact": {},
    "Completed Date": {},
    "Complexity": {},
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Days Until Due Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": "",
    "Effort": {},
    "Effort In Days": {},
    "Effort Score": {},
    "Estimated Remaining Risk": {},
    "Extended Fields": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Impact ID": {},
    "Inherent Cost": {},
    "Inherent Risk Score": 0.0,
    "Likelihood ID": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Possible Outcome": {},
    "Priority Based On Risk": {},
    "Residual Cost": {},
    "Residual Risk": {},
    "Risk Category ID": {},
    "Risk Decision": {},
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Create Task

This action is used to create a new task in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The task to create, as a JSON object matching the CreateTaskDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example task'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example task"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task|task|True|The created task|None|
  
Example output:

```
{
  "task": {
    "Approval Status": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Incidents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Instructions": {},
    "Integrations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": "true",
    "Is Auditor Request": {},
    "Is Dynamic Ownership": {},
    "Is Enabled": {},
    "Is Generated By AI": {},
    "Is Query Driven": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Primary Driver": {},
    "Queries": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Raise Service Request": {},
    "Rapid7 AI Event GUID": {},
    "Rapid7 Key": {},
    "Require Acknowledgement": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Security Policies": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Send Reminders": {},
    "Should Repeat": {},
    "Should Reset": {},
    "Start Date": "",
    "Status ID": {},
    "Task Type ID": {},
    "Trend": {},
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Create User

This action is used to create a new user in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The user to create, as a JSON object matching the CreateUserDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example user'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example user"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|True|The created user|None|
  
Example output:

```
{
  "user": {
    "Active": "true",
    "Anti Tampering Enabled": {},
    "Created By": "",
    "Created Date": "",
    "Email": {},
    "First Name": {},
    "ID": 0,
    "Last Login Date": {},
    "Last Name": {},
    "Modified By": {},
    "Modified Date": {},
    "Preferred Dictionary": {},
    "Preferred Unit Of Measure": {},
    "Profile Background Color": {},
    "Theme Preference": {}
  }
}
```

#### Create Vendor

This action is used to create a new vendor in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|record|object|None|True|The vendor to create, as a JSON object matching the CreateVendorDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Example vendor'}|None|None|
  
Example input:

```
{
  "record": {
    "name": "Example vendor"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vendor|vendor|True|The created vendor|None|
  
Example output:

```
{
  "vendor": {
    "Access End Date": {},
    "Access Start Date": "",
    "Access To Client Data": {},
    "Access To Our System": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Compliance": {},
    "Contact Email": {},
    "Contact Name": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controller Or Processor": {},
    "Could Vendor Failure Result In Fines": {},
    "Created By": {},
    "Created Date": {},
    "Date Founded": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Gdpr Compliant": {},
    "Head Quartered": {},
    "Holds Client Data": {},
    "Holds Our Data": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Industry": {},
    "Is Enabled": {},
    "Is Holding Client Data": {},
    "Is Holding Personal Data": {},
    "Is Insured": {},
    "Is NDA Signed": "true",
    "Loss Of Vendor Would Cause Significant Disruption": {},
    "Loss Of Vendor Would Have Material Impact": {},
    "Loss Of Vendor Would Impact Customers": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": "",
    "Negative Impact When Service Down More Than24hr": {},
    "Public Description": {},
    "Rapid7 Key": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {},
    "Type": {},
    "Type Of Asset": {},
    "Vendor Could Impact Reputation": {},
    "Vendor Criticality": {},
    "Website": {}
  }
}
```

#### Delete Assessment

This action is used to delete a assessment by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the assessment to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Audit

This action is used to delete a audit by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the audit to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Certification

This action is used to delete a certification by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the certification to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Contract

This action is used to delete a contract by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the contract to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Control Set

This action is used to delete a control set by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the control set to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Incident

This action is used to delete a incident by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the incident to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete IT Asset

This action is used to delete a it asset by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the it asset to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Record

This action is used to delete a record of any Cyber GRC record type that supports deletion

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the record to delete|None|1|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to delete from|["Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Incidents", "LikelihoodViews", "Locations", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "SystemInfos", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
  
Example input:

```
{
  "id": 1,
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Risk

This action is used to delete a risk by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the risk to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Task

This action is used to delete a task by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the task to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete User

This action is used to delete a user by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the user to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Vendor

This action is used to delete a vendor by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the vendor to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Get Assessment

This action is used to retrieve a single assessment by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the assessment to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assessment|assessment|True|The requested assessment|None|
  
Example output:

```
{
  "assessment": {
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "Enabled": {},
    "Form Entry Name": {},
    "Frequency": {},
    "ID": {},
    "Is Accepted": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Should Populate Answers": {},
    "Should Repeat": {},
    "Start Date": "",
    "Submitted Date": {},
    "Summary": {},
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Times Duplicated": {},
    "Trend": {},
    "Users": [
      {
        "Email": {},
        "ID": 0,
        "Name": ""
      }
    ],
    "Was Submitted": "true"
  }
}
```

#### Get Assessments

This action is used to retrieve assessments from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assessments|[]assessment|True|The matching assessments|None|
|count|integer|True|Number of assessments returned|1|
  
Example output:

```
{
  "assessments": [
    {
      "Audits": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Compliance": {},
      "Created By": {},
      "Created Date": {},
      "Description": {},
      "Discussion Field ID": {},
      "Due Date": {},
      "Enabled": {},
      "Form Entry Name": {},
      "Frequency": {},
      "ID": {},
      "Is Accepted": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Risks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Should Populate Answers": {},
      "Should Repeat": {},
      "Start Date": "",
      "Submitted Date": {},
      "Summary": {},
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Times Duplicated": {},
      "Trend": {},
      "Users": [
        {
          "Email": {},
          "ID": 0,
          "Name": ""
        }
      ],
      "Was Submitted": "true"
    }
  ],
  "count": 1
}
```

#### Get Audit

This action is used to retrieve a single audit by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the audit to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|audit|audit|True|The requested audit|None|
  
Example output:

```
{
  "audit": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audit Users": [
      {
        "Active": "true",
        "ID": {},
        "Name": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      }
    ],
    "Auditor Findings": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Set": {
      "ID": 0,
      "Name": {}
    },
    "Control Set ID": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Documents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "Frequency Name": "",
    "ID": {},
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Observation Period End": {},
    "Observation Period Start": "",
    "Start Date": {},
    "Status": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Get Audits

This action is used to retrieve audits from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|audits|[]audit|True|The matching audits|None|
|count|integer|True|Number of audits returned|1|
  
Example output:

```
{
  "audits": [
    {
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Audit Users": [
        {
          "Active": "true",
          "ID": {},
          "Name": {},
          "Title": {},
          "User Email": {},
          "User First Name": {},
          "User Last Name": {},
          "Users ID": {}
        }
      ],
      "Auditor Findings": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Control Set": {
        "ID": 0,
        "Name": {}
      },
      "Control Set ID": {},
      "Created By": {},
      "Created Date": {},
      "Description": {},
      "Discussion Field ID": {},
      "Documents": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "End Date": {},
      "Extended Fields": {},
      "Frequency": {},
      "Frequency Name": "",
      "ID": {},
      "Is Archived": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Observation Period End": {},
      "Observation Period Start": "",
      "Start Date": {},
      "Status": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ]
    }
  ],
  "count": 1
}
```

#### Get Certification

This action is used to retrieve a single certification by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the certification to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certification|certification|True|The requested certification|None|
  
Example output:

```
{
  "certification": {
    "Created By": {},
    "Created Date": "",
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Active": "true",
    "Modified By": {},
    "Modified Date": {},
    "Name": ""
  }
}
```

#### Get Certifications

This action is used to retrieve certifications from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certifications|[]certification|True|The matching certifications|None|
|count|integer|True|Number of certifications returned|1|
  
Example output:

```
{
  "certifications": [
    {
      "Created By": {},
      "Created Date": "",
      "ID": 0,
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Is Active": "true",
      "Modified By": {},
      "Modified Date": {},
      "Name": ""
    }
  ],
  "count": 1
}
```

#### Get Compliance Score

This action is used to retrieve the most recent compliance score and automated controls score of each framework, along 
with an overall score averaged across them. Control sets that are archived or disabled are left out unless one is named 
with Control Set ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|control_set_id|integer|0|False|ID of a single control set to score. Leave empty or set to 0 to score every control set|None|1|None|None|
  
Example input:

```
{
  "control_set_id": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|frameworks|[]framework_compliance|True|Most recent scores for each control set, most recently calculated first|None|
|overall|overall_compliance|True|Scores averaged across the frameworks returned. Cyber GRC does not publish a tenant wide score, so the plugin calculates this one|None|
  
Example output:

```
{
  "frameworks": [
    {
      "Automated Controls Percentage": {},
      "Compliance": 0.0,
      "Control Set ID": 0,
      "Date Calculated": {},
      "Linked Controls Percentage": {},
      "Name": ""
    }
  ],
  "overall": {
    "Automated Controls Percentage": {},
    "Compliance": 0.0,
    "Framework Count": 0
  }
}
```

#### Get Contract

This action is used to retrieve a single contract by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the contract to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|contract|contract|True|The requested contract|None|
  
Example output:

```
{
  "contract": {
    "Annual Cost": {},
    "Approval Status": "true",
    "Category": {
      "ID": {},
      "Name": {}
    },
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Contact Email": {},
    "Contact Name": {},
    "Contract Category ID": {},
    "Contract Documents": [
      {
        "Blob Name": {},
        "Contract ID": {},
        "ID": {},
        "Is Current Version": {},
        "Is Working Version": {},
        "Title": {},
        "Version": {}
      }
    ],
    "Contract Subcategory ID": {},
    "Contract Type": {},
    "Cost Type": {},
    "Created By": "",
    "Created Date": "",
    "Currency": {},
    "Days Until Renewal": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "End Date": {},
    "Extended Fields": {},
    "Generated Date": {},
    "Has Enabled Adobe Sync": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Invoice Frequency": {},
    "Is Key Contract": {},
    "Max Extension": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Notice Date": {},
    "Parent Contract": {
      "ID": {},
      "Name": {}
    },
    "Parent Contract ID": {},
    "Sequence Number": {},
    "Start Date": {},
    "Status": {
      "ID": {},
      "Name": {}
    },
    "Status ID": {},
    "Subcategory": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Termination Notice Period": {},
    "Variation Number": {},
    "Vendors": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Get Contracts

This action is used to retrieve contracts from Cyber GRC, optionally narrowed with an OData filter or a renewal window

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|include_expired|boolean|False|False|Whether Renewing Within Days also returns contracts that have already ended. Ignored when Renewing Within Days is not set|None|False|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|renewing_within_days|integer|0|False|Return only contracts ending this many days from now or sooner, so a renewal workflow does not have to write the date arithmetic itself. Contracts with no End Date are left out. Leave empty or set to 0 for every contract|None|90|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "include_expired": false,
  "order_by": "modifiedDate desc",
  "renewing_within_days": 0,
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|contracts|[]contract|True|The matching contracts|None|
|count|integer|True|Number of contracts returned|1|
  
Example output:

```
{
  "contracts": [
    {
      "Annual Cost": {},
      "Approval Status": "true",
      "Category": {
        "ID": {},
        "Name": {}
      },
      "Clients": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Contact Email": {},
      "Contact Name": {},
      "Contract Category ID": {},
      "Contract Documents": [
        {
          "Blob Name": {},
          "Contract ID": {},
          "ID": {},
          "Is Current Version": {},
          "Is Working Version": {},
          "Title": {},
          "Version": {}
        }
      ],
      "Contract Subcategory ID": {},
      "Contract Type": {},
      "Cost Type": {},
      "Created By": "",
      "Created Date": "",
      "Currency": {},
      "Days Until Renewal": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "End Date": {},
      "Extended Fields": {},
      "Generated Date": {},
      "Has Enabled Adobe Sync": {},
      "ID": 0,
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Invoice Frequency": {},
      "Is Key Contract": {},
      "Max Extension": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Notice Date": {},
      "Parent Contract": {
        "ID": {},
        "Name": {}
      },
      "Parent Contract ID": {},
      "Sequence Number": {},
      "Start Date": {},
      "Status": {
        "ID": {},
        "Name": {}
      },
      "Status ID": {},
      "Subcategory": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Termination Notice Period": {},
      "Variation Number": {},
      "Vendors": [
        {
          "ID": {},
          "Name": {}
        }
      ]
    }
  ],
  "count": 1
}
```

#### Get Control Set

This action is used to retrieve a single control set by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the control set to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|control_set|control_set|True|The requested control set|None|
  
Example output:

```
{
  "control_set": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Controls": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Description": {},
    "Discussion Field ID": {},
    "Enabled": "true",
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Rapid7 Key": {},
    "Security Policy Info ID": {},
    "Type": {}
  }
}
```

#### Get Control Sets

This action is used to retrieve control sets from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|control_sets|[]control_set|True|The matching control sets|None|
|count|integer|True|Number of control sets returned|1|
  
Example output:

```
{
  "control_sets": [
    {
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Audits": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Compliance": {},
      "Controls": [
        {
          "ID": 0,
          "Name": ""
        }
      ],
      "Created By": {},
      "Created Date": "",
      "Description": {},
      "Discussion Field ID": {},
      "Enabled": "true",
      "ID": {},
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Is Archived": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Rapid7 Key": {},
      "Security Policy Info ID": {},
      "Type": {}
    }
  ],
  "count": 1
}
```

#### Get Incident

This action is used to retrieve a single incident by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the incident to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|True|The requested incident|None|
  
Example output:

```
{
  "incident": {
    "Client Security Assessments Issued": {},
    "Confidential Data Impacted": {},
    "Created By": {},
    "Created Date": {},
    "Customer Data Impacted": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "How Identified": {},
    "How Occurred": {},
    "ID": 0,
    "Identified Date": "",
    "Immediate Action": {},
    "Impact Type": {},
    "Investigations Fines": {},
    "Lessons Learned": {},
    "Location ID": {},
    "Material Impact": {},
    "Modified By": {},
    "Modified Date": {},
    "Monetary Impact": {},
    "Name": "",
    "Non Confidential Data Impacted": {},
    "Occured Date": {},
    "Personal Identifiable Info Impacted": {},
    "Realized Financial Loss": {},
    "Reputational Damage": {},
    "Root Cause": {},
    "Send Reminders": "true",
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Get Incidents

This action is used to retrieve incidents from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of incidents returned|1|
|incidents|[]incident|True|The matching incidents|None|
  
Example output:

```
{
  "count": 1,
  "incidents": [
    {
      "Client Security Assessments Issued": {},
      "Confidential Data Impacted": {},
      "Created By": {},
      "Created Date": {},
      "Customer Data Impacted": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Extended Fields": {},
      "How Identified": {},
      "How Occurred": {},
      "ID": 0,
      "Identified Date": "",
      "Immediate Action": {},
      "Impact Type": {},
      "Investigations Fines": {},
      "Lessons Learned": {},
      "Location ID": {},
      "Material Impact": {},
      "Modified By": {},
      "Modified Date": {},
      "Monetary Impact": {},
      "Name": "",
      "Non Confidential Data Impacted": {},
      "Occured Date": {},
      "Personal Identifiable Info Impacted": {},
      "Realized Financial Loss": {},
      "Reputational Damage": {},
      "Root Cause": {},
      "Send Reminders": "true",
      "Status ID": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ]
    }
  ]
}
```

#### Get IT Asset

This action is used to retrieve a single it asset by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the it asset to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|it_asset|it_asset|True|The requested it asset|None|
  
Example output:

```
{
  "it_asset": {
    "A1": {},
    "A2": {},
    "A3": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "C1": {},
    "C2": {},
    "C3": {},
    "Calculated CIA": {},
    "Certifications": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Sets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Has Personal Data": "true",
    "I1": {},
    "I2": {},
    "I3": {},
    "ID": {},
    "Is BCP": {},
    "Is Client Data Host": {},
    "Is Client Facing": {},
    "Is DFA": {},
    "Is DR": {},
    "Is Data Anonymous": {},
    "Is Data At-Rest": {},
    "Is Data In Transit": {},
    "Is Desktop App": {},
    "Is Dev In House": {},
    "Is Hosted In Cloud": {},
    "Is Individual Perms": {},
    "Is Our Data Host": {},
    "Is Pre Prod Env": {},
    "Is Prod Data Used In Non Prod Env": {},
    "Is Production Env": {},
    "Is Public Internet Facing": {},
    "Is Role Based": {},
    "Is Role Based Access": {},
    "Is SIEM Monitored": {},
    "Is SSO": {},
    "Is SSO Authenticated": {},
    "Is SSO Authorised": {},
    "Is Security Testing Required": {},
    "Is Service Accounts": {},
    "Is Test Data Personal": {},
    "Is Test Env": {},
    "Is Tested": {},
    "Is UAT Env": {},
    "Is Web Based App": {},
    "Life Cycle": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Number Of Users": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "System Type": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {}
  }
}
```

#### Get IT Assets

This action is used to retrieve it assets from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of it assets returned|1|
|it_assets|[]it_asset|True|The matching it assets|None|
  
Example output:

```
{
  "count": 1,
  "it_assets": [
    {
      "A1": {},
      "A2": {},
      "A3": {},
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Assigned To": {
        "Active": {},
        "Associated User ID": {},
        "RACI Option": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      },
      "C1": {},
      "C2": {},
      "C3": {},
      "Calculated CIA": {},
      "Certifications": [
        {
          "ID": 0,
          "Name": ""
        }
      ],
      "Compliance": {},
      "Contracts": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Control Sets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Created By": {},
      "Created Date": "",
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Extended Fields": {},
      "Has Personal Data": "true",
      "I1": {},
      "I2": {},
      "I3": {},
      "ID": {},
      "Is BCP": {},
      "Is Client Data Host": {},
      "Is Client Facing": {},
      "Is DFA": {},
      "Is DR": {},
      "Is Data Anonymous": {},
      "Is Data At-Rest": {},
      "Is Data In Transit": {},
      "Is Desktop App": {},
      "Is Dev In House": {},
      "Is Hosted In Cloud": {},
      "Is Individual Perms": {},
      "Is Our Data Host": {},
      "Is Pre Prod Env": {},
      "Is Prod Data Used In Non Prod Env": {},
      "Is Production Env": {},
      "Is Public Internet Facing": {},
      "Is Role Based": {},
      "Is Role Based Access": {},
      "Is SIEM Monitored": {},
      "Is SSO": {},
      "Is SSO Authenticated": {},
      "Is SSO Authorised": {},
      "Is Security Testing Required": {},
      "Is Service Accounts": {},
      "Is Test Data Personal": {},
      "Is Test Env": {},
      "Is Tested": {},
      "Is UAT Env": {},
      "Is Web Based App": {},
      "Life Cycle": {},
      "Locations": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Number Of Users": {},
      "Risks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "System Type": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Trend": {}
    }
  ]
}
```

#### Get Record

This action is used to retrieve a single record of any Cyber GRC record type by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the record to retrieve|None|1|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "record_type": "Risks",
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|record|object|True|The requested record|None|
  
Example output:

```
{
  "record": {}
}
```

#### Get Record History

This action is used to retrieve the change history of a record for the record types that track history

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the record whose history should be retrieved|None|1|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to read history from|["Assessments", "Audits", "Certifications", "Contracts", "ControlSets", "ITAssets", "Incidents", "Risks", "Tasks", "Users"]|Risks|None|None|
  
Example input:

```
{
  "id": 1,
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of history entries returned|1|
|history|[]object|True|Change history entries for the record, most recent first as returned by the API|None|
  
Example output:

```
{
  "count": 1,
  "history": [
    {}
  ]
}
```

#### Get Risk

This action is used to retrieve a single risk by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the risk to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|risk|risk|True|The requested risk|None|
  
Example output:

```
{
  "risk": {
    "Assessment ID": {},
    "Business Impact": {},
    "Completed Date": {},
    "Complexity": {},
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Days Until Due Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": "",
    "Effort": {},
    "Effort In Days": {},
    "Effort Score": {},
    "Estimated Remaining Risk": {},
    "Extended Fields": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Impact ID": {},
    "Inherent Cost": {},
    "Inherent Risk Score": 0.0,
    "Likelihood ID": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Possible Outcome": {},
    "Priority Based On Risk": {},
    "Residual Cost": {},
    "Residual Risk": {},
    "Risk Category ID": {},
    "Risk Decision": {},
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Get Risks

This action is used to retrieve risks from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of risks returned|1|
|risks|[]risk|True|The matching risks|None|
  
Example output:

```
{
  "count": 1,
  "risks": [
    {
      "Assessment ID": {},
      "Business Impact": {},
      "Completed Date": {},
      "Complexity": {},
      "Controls": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Created By": {},
      "Created Date": {},
      "Days Until Due Date": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Due Date": "",
      "Effort": {},
      "Effort In Days": {},
      "Effort Score": {},
      "Estimated Remaining Risk": {},
      "Extended Fields": {},
      "ID": {},
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Impact ID": {},
      "Inherent Cost": {},
      "Inherent Risk Score": 0.0,
      "Likelihood ID": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Possible Outcome": {},
      "Priority Based On Risk": {},
      "Residual Cost": {},
      "Residual Risk": {},
      "Risk Category ID": {},
      "Risk Decision": {},
      "Status ID": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Vendors": [
        {
          "ID": 0,
          "Name": ""
        }
      ]
    }
  ]
}
```

#### Get Task

This action is used to retrieve a single task by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the task to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task|task|True|The requested task|None|
  
Example output:

```
{
  "task": {
    "Approval Status": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Incidents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Instructions": {},
    "Integrations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": "true",
    "Is Auditor Request": {},
    "Is Dynamic Ownership": {},
    "Is Enabled": {},
    "Is Generated By AI": {},
    "Is Query Driven": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Primary Driver": {},
    "Queries": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Raise Service Request": {},
    "Rapid7 AI Event GUID": {},
    "Rapid7 Key": {},
    "Require Acknowledgement": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Security Policies": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Send Reminders": {},
    "Should Repeat": {},
    "Should Reset": {},
    "Start Date": "",
    "Status ID": {},
    "Task Type ID": {},
    "Trend": {},
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Get Tasks

This action is used to retrieve tasks from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|due_within_days|integer|0|False|Return only tasks due this many days from now or sooner, so a reminder workflow does not have to write the date arithmetic itself. Tasks with no Due Date are left out. Leave empty or set to 0 for every task|None|7|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|overdue_only|boolean|False|False|Return only tasks whose Due Date has already passed. Applied in addition to Due Within Days, so setting both returns only the overdue tasks|None|False|None|None|
|owner|string|None|False|Return only tasks assigned to this user, given as an email address or a numeric Cyber GRC user ID. The API exposes the assignee as a nested object with no filterable ID field, so this match is applied by the plugin after the records are read, which means Top and Skip apply to the matching tasks rather than to every task|None|user@example.com|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|status_id|integer|0|False|Return only tasks in this status. Leave empty or set to 0 for every status|None|3|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "due_within_days": 0,
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "overdue_only": false,
  "owner": "user@example.com",
  "select": "id,name,statusID",
  "skip": 0,
  "status_id": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of tasks returned|1|
|tasks|[]task|True|The matching tasks|None|
  
Example output:

```
{
  "count": 1,
  "tasks": [
    {
      "Approval Status": {},
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Assigned To": {
        "Active": {},
        "Associated User ID": {},
        "RACI Option": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      },
      "Audits": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Clients": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Compliance": {},
      "Contracts": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Controls": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Created By": {},
      "Created Date": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Due Date": {},
      "End Date": {},
      "Extended Fields": {},
      "Frequency": {},
      "ID": {},
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Incidents": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Instructions": {},
      "Integrations": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Is Archived": "true",
      "Is Auditor Request": {},
      "Is Dynamic Ownership": {},
      "Is Enabled": {},
      "Is Generated By AI": {},
      "Is Query Driven": {},
      "Locations": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Primary Driver": {},
      "Queries": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Raise Service Request": {},
      "Rapid7 AI Event GUID": {},
      "Rapid7 Key": {},
      "Require Acknowledgement": {},
      "Risks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Security Policies": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Send Reminders": {},
      "Should Repeat": {},
      "Should Reset": {},
      "Start Date": "",
      "Status ID": {},
      "Task Type ID": {},
      "Trend": {},
      "Vendors": [
        {
          "ID": 0,
          "Name": ""
        }
      ]
    }
  ]
}
```

#### Get User

This action is used to retrieve a single user by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the user to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|True|The requested user|None|
  
Example output:

```
{
  "user": {
    "Active": "true",
    "Anti Tampering Enabled": {},
    "Created By": "",
    "Created Date": "",
    "Email": {},
    "First Name": {},
    "ID": 0,
    "Last Login Date": {},
    "Last Name": {},
    "Modified By": {},
    "Modified Date": {},
    "Preferred Dictionary": {},
    "Preferred Unit Of Measure": {},
    "Profile Background Color": {},
    "Theme Preference": {}
  }
}
```

#### Get Users

This action is used to retrieve users from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of users returned|1|
|users|[]user|True|The matching users|None|
  
Example output:

```
{
  "count": 1,
  "users": [
    {
      "Active": "true",
      "Anti Tampering Enabled": {},
      "Created By": "",
      "Created Date": "",
      "Email": {},
      "First Name": {},
      "ID": 0,
      "Last Login Date": {},
      "Last Name": {},
      "Modified By": {},
      "Modified Date": {},
      "Preferred Dictionary": {},
      "Preferred Unit Of Measure": {},
      "Profile Background Color": {},
      "Theme Preference": {}
    }
  ]
}
```

#### Get Vendor

This action is used to retrieve a single vendor by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the vendor to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vendor|vendor|True|The requested vendor|None|
  
Example output:

```
{
  "vendor": {
    "Access End Date": {},
    "Access Start Date": "",
    "Access To Client Data": {},
    "Access To Our System": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Compliance": {},
    "Contact Email": {},
    "Contact Name": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controller Or Processor": {},
    "Could Vendor Failure Result In Fines": {},
    "Created By": {},
    "Created Date": {},
    "Date Founded": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Gdpr Compliant": {},
    "Head Quartered": {},
    "Holds Client Data": {},
    "Holds Our Data": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Industry": {},
    "Is Enabled": {},
    "Is Holding Client Data": {},
    "Is Holding Personal Data": {},
    "Is Insured": {},
    "Is NDA Signed": "true",
    "Loss Of Vendor Would Cause Significant Disruption": {},
    "Loss Of Vendor Would Have Material Impact": {},
    "Loss Of Vendor Would Impact Customers": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": "",
    "Negative Impact When Service Down More Than24hr": {},
    "Public Description": {},
    "Rapid7 Key": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {},
    "Type": {},
    "Type Of Asset": {},
    "Vendor Could Impact Reputation": {},
    "Vendor Criticality": {},
    "Website": {}
  }
}
```

#### Get Vendors

This action is used to retrieve vendors from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of vendors returned|1|
|vendors|[]vendor|True|The matching vendors|None|
  
Example output:

```
{
  "count": 1,
  "vendors": [
    {
      "Access End Date": {},
      "Access Start Date": "",
      "Access To Client Data": {},
      "Access To Our System": {},
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Assigned To": {
        "Active": {},
        "Associated User ID": {},
        "RACI Option": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      },
      "Compliance": {},
      "Contact Email": {},
      "Contact Name": {},
      "Contracts": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Controller Or Processor": {},
      "Could Vendor Failure Result In Fines": {},
      "Created By": {},
      "Created Date": {},
      "Date Founded": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Extended Fields": {},
      "Gdpr Compliant": {},
      "Head Quartered": {},
      "Holds Client Data": {},
      "Holds Our Data": {},
      "ID": 0,
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Industry": {},
      "Is Enabled": {},
      "Is Holding Client Data": {},
      "Is Holding Personal Data": {},
      "Is Insured": {},
      "Is NDA Signed": "true",
      "Loss Of Vendor Would Cause Significant Disruption": {},
      "Loss Of Vendor Would Have Material Impact": {},
      "Loss Of Vendor Would Impact Customers": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": "",
      "Negative Impact When Service Down More Than24hr": {},
      "Public Description": {},
      "Rapid7 Key": {},
      "Risks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Trend": {},
      "Type": {},
      "Type Of Asset": {},
      "Vendor Could Impact Reputation": {},
      "Vendor Criticality": {},
      "Website": {}
    }
  ]
}
```

#### List Records

This action is used to retrieve records of any Cyber GRC record type, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "record_type": "Risks",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of records returned|1|
|records|[]object|True|The matching records|None|
  
Example output:

```
{
  "count": 1,
  "records": [
    {}
  ]
}
```

#### Update Assessment

This action is used to update an existing assessment in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the assessment to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateAssessmentDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed assessment'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed assessment"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assessment|assessment|True|The updated assessment|None|
  
Example output:

```
{
  "assessment": {
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "Enabled": {},
    "Form Entry Name": {},
    "Frequency": {},
    "ID": {},
    "Is Accepted": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Should Populate Answers": {},
    "Should Repeat": {},
    "Start Date": "",
    "Submitted Date": {},
    "Summary": {},
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Times Duplicated": {},
    "Trend": {},
    "Users": [
      {
        "Email": {},
        "ID": 0,
        "Name": ""
      }
    ],
    "Was Submitted": "true"
  }
}
```

#### Update Audit

This action is used to update an existing audit in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the audit to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateAuditDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed audit'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed audit"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|audit|audit|True|The updated audit|None|
  
Example output:

```
{
  "audit": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audit Users": [
      {
        "Active": "true",
        "ID": {},
        "Name": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      }
    ],
    "Auditor Findings": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Set": {
      "ID": 0,
      "Name": {}
    },
    "Control Set ID": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Documents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "Frequency Name": "",
    "ID": {},
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Observation Period End": {},
    "Observation Period Start": "",
    "Start Date": {},
    "Status": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Update Certification

This action is used to update an existing certification in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the certification to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateCertificationDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed certification'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed certification"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certification|certification|True|The updated certification|None|
  
Example output:

```
{
  "certification": {
    "Created By": {},
    "Created Date": "",
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Active": "true",
    "Modified By": {},
    "Modified Date": {},
    "Name": ""
  }
}
```

#### Update Contract

This action is used to update an existing contract in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the contract to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateContractDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed contract'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed contract"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|contract|contract|True|The updated contract|None|
  
Example output:

```
{
  "contract": {
    "Annual Cost": {},
    "Approval Status": "true",
    "Category": {
      "ID": {},
      "Name": {}
    },
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Contact Email": {},
    "Contact Name": {},
    "Contract Category ID": {},
    "Contract Documents": [
      {
        "Blob Name": {},
        "Contract ID": {},
        "ID": {},
        "Is Current Version": {},
        "Is Working Version": {},
        "Title": {},
        "Version": {}
      }
    ],
    "Contract Subcategory ID": {},
    "Contract Type": {},
    "Cost Type": {},
    "Created By": "",
    "Created Date": "",
    "Currency": {},
    "Days Until Renewal": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "End Date": {},
    "Extended Fields": {},
    "Generated Date": {},
    "Has Enabled Adobe Sync": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Invoice Frequency": {},
    "Is Key Contract": {},
    "Max Extension": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Notice Date": {},
    "Parent Contract": {
      "ID": {},
      "Name": {}
    },
    "Parent Contract ID": {},
    "Sequence Number": {},
    "Start Date": {},
    "Status": {
      "ID": {},
      "Name": {}
    },
    "Status ID": {},
    "Subcategory": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Termination Notice Period": {},
    "Variation Number": {},
    "Vendors": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Update Control Set

This action is used to update an existing control set in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the control set to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateControlSetDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed control set'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed control set"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|control_set|control_set|True|The updated control set|None|
  
Example output:

```
{
  "control_set": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Controls": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Description": {},
    "Discussion Field ID": {},
    "Enabled": "true",
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Rapid7 Key": {},
    "Security Policy Info ID": {},
    "Type": {}
  }
}
```

#### Update Incident

This action is used to update an existing incident in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the incident to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateIncidentDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed incident'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed incident"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|True|The updated incident|None|
  
Example output:

```
{
  "incident": {
    "Client Security Assessments Issued": {},
    "Confidential Data Impacted": {},
    "Created By": {},
    "Created Date": {},
    "Customer Data Impacted": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "How Identified": {},
    "How Occurred": {},
    "ID": 0,
    "Identified Date": "",
    "Immediate Action": {},
    "Impact Type": {},
    "Investigations Fines": {},
    "Lessons Learned": {},
    "Location ID": {},
    "Material Impact": {},
    "Modified By": {},
    "Modified Date": {},
    "Monetary Impact": {},
    "Name": "",
    "Non Confidential Data Impacted": {},
    "Occured Date": {},
    "Personal Identifiable Info Impacted": {},
    "Realized Financial Loss": {},
    "Reputational Damage": {},
    "Root Cause": {},
    "Send Reminders": "true",
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Update IT Asset

This action is used to update an existing it asset in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the it asset to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateITAssetDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed it asset'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed it asset"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|it_asset|it_asset|True|The updated it asset|None|
  
Example output:

```
{
  "it_asset": {
    "A1": {},
    "A2": {},
    "A3": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "C1": {},
    "C2": {},
    "C3": {},
    "Calculated CIA": {},
    "Certifications": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Sets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Has Personal Data": "true",
    "I1": {},
    "I2": {},
    "I3": {},
    "ID": {},
    "Is BCP": {},
    "Is Client Data Host": {},
    "Is Client Facing": {},
    "Is DFA": {},
    "Is DR": {},
    "Is Data Anonymous": {},
    "Is Data At-Rest": {},
    "Is Data In Transit": {},
    "Is Desktop App": {},
    "Is Dev In House": {},
    "Is Hosted In Cloud": {},
    "Is Individual Perms": {},
    "Is Our Data Host": {},
    "Is Pre Prod Env": {},
    "Is Prod Data Used In Non Prod Env": {},
    "Is Production Env": {},
    "Is Public Internet Facing": {},
    "Is Role Based": {},
    "Is Role Based Access": {},
    "Is SIEM Monitored": {},
    "Is SSO": {},
    "Is SSO Authenticated": {},
    "Is SSO Authorised": {},
    "Is Security Testing Required": {},
    "Is Service Accounts": {},
    "Is Test Data Personal": {},
    "Is Test Env": {},
    "Is Tested": {},
    "Is UAT Env": {},
    "Is Web Based App": {},
    "Life Cycle": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Number Of Users": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "System Type": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {}
  }
}
```

#### Update Record

This action is used to update a record of any Cyber GRC record type

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the record to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the corresponding Update DTO in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed record'}|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed record"
  },
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|record|object|True|The updated record|None|
  
Example output:

```
{
  "record": {}
}
```

#### Update Risk

This action is used to update an existing risk in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the risk to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateRiskDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed risk'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed risk"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|risk|risk|True|The updated risk|None|
  
Example output:

```
{
  "risk": {
    "Assessment ID": {},
    "Business Impact": {},
    "Completed Date": {},
    "Complexity": {},
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Days Until Due Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": "",
    "Effort": {},
    "Effort In Days": {},
    "Effort Score": {},
    "Estimated Remaining Risk": {},
    "Extended Fields": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Impact ID": {},
    "Inherent Cost": {},
    "Inherent Risk Score": 0.0,
    "Likelihood ID": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Possible Outcome": {},
    "Priority Based On Risk": {},
    "Residual Cost": {},
    "Residual Risk": {},
    "Risk Category ID": {},
    "Risk Decision": {},
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Update Task

This action is used to update an existing task in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the task to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateTaskDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed task'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed task"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task|task|True|The updated task|None|
  
Example output:

```
{
  "task": {
    "Approval Status": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Incidents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Instructions": {},
    "Integrations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": "true",
    "Is Auditor Request": {},
    "Is Dynamic Ownership": {},
    "Is Enabled": {},
    "Is Generated By AI": {},
    "Is Query Driven": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Primary Driver": {},
    "Queries": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Raise Service Request": {},
    "Rapid7 AI Event GUID": {},
    "Rapid7 Key": {},
    "Require Acknowledgement": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Security Policies": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Send Reminders": {},
    "Should Repeat": {},
    "Should Reset": {},
    "Start Date": "",
    "Status ID": {},
    "Task Type ID": {},
    "Trend": {},
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Update User

This action is used to update an existing user in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the user to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateUserDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed user'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed user"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|True|The updated user|None|
  
Example output:

```
{
  "user": {
    "Active": "true",
    "Anti Tampering Enabled": {},
    "Created By": "",
    "Created Date": "",
    "Email": {},
    "First Name": {},
    "ID": 0,
    "Last Login Date": {},
    "Last Name": {},
    "Modified By": {},
    "Modified Date": {},
    "Preferred Dictionary": {},
    "Preferred Unit Of Measure": {},
    "Profile Background Color": {},
    "Theme Preference": {}
  }
}
```

#### Update Vendor

This action is used to update an existing vendor in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the vendor to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateVendorDto schema in the Rapid7 Cyber GRC API reference|None|{'name': 'Renamed vendor'}|None|None|
  
Example input:

```
{
  "id": 1,
  "record": {
    "name": "Renamed vendor"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vendor|vendor|True|The updated vendor|None|
  
Example output:

```
{
  "vendor": {
    "Access End Date": {},
    "Access Start Date": "",
    "Access To Client Data": {},
    "Access To Our System": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Compliance": {},
    "Contact Email": {},
    "Contact Name": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controller Or Processor": {},
    "Could Vendor Failure Result In Fines": {},
    "Created By": {},
    "Created Date": {},
    "Date Founded": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Gdpr Compliant": {},
    "Head Quartered": {},
    "Holds Client Data": {},
    "Holds Our Data": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Industry": {},
    "Is Enabled": {},
    "Is Holding Client Data": {},
    "Is Holding Personal Data": {},
    "Is Insured": {},
    "Is NDA Signed": "true",
    "Loss Of Vendor Would Cause Significant Disruption": {},
    "Loss Of Vendor Would Have Material Impact": {},
    "Loss Of Vendor Would Impact Customers": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": "",
    "Negative Impact When Service Down More Than24hr": {},
    "Public Description": {},
    "Rapid7 Key": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {},
    "Type": {},
    "Type Of Asset": {},
    "Vendor Could Impact Reputation": {},
    "Vendor Criticality": {},
    "Website": {}
  }
}
```

#### Upload Flat File

This action is used to upload an XLSX or CSV file to Cyber GRC through the v1 Flat File API. Uploading a file whose 
name already exists updates the existing flat file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Optional description to store alongside the flat file|None|Weekly vulnerability export|None|None|
|file|bytes|None|True|Base64 encoded contents of the XLSX or CSV file to upload|None|aWQsbmFtZQoxLGV4YW1wbGUK|None|None|
|file_name|string|None|True|Name of the file including its extension. Cyber GRC tracks flat files by name, so reusing a name updates the existing file|None|vulnerabilities.csv|None|None|
|id|integer|0|False|ID of an existing flat file integration. Leave at 0 to let Cyber GRC match on file name|None|0|None|None|
|operation_type|string|Append|True|Whether to add the rows to the existing values or replace them|["Append", "Replace"]|Append|None|None|
  
Example input:

```
{
  "description": "Weekly vulnerability export",
  "file": "aWQsbmFtZQoxLGV4YW1wbGUK",
  "file_name": "vulnerabilities.csv",
  "id": 0,
  "operation_type": "Append"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|object|True|Response returned by the Flat File API|None|
  
Example output:

```
{
  "result": {}
}
```
### Triggers


#### Monitor Compliance Drift

This trigger is used to poll the framework compliance scores and emit the frameworks whose score has fallen

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|control_set_id|integer|0|False|ID of a single control set to watch. Leave empty or set to 0 to watch every control set that is enabled and not archived|None|0|None|None|
|drop_threshold|float|5|True|How far a compliance score has to fall between polls before it is reported, in percentage points. Set to 0 to report every fall|None|5|None|None|
|interval|integer|3600|True|Number of seconds to wait between polls. Cyber GRC recalculates scores periodically rather than continuously, so polling faster than it recalculates adds load without adding detail|None|3600|None|None|
|minimum_compliance|float|0|True|Report any framework scoring below this as it crosses the floor, so a framework that is already failing is reported on the first poll rather than only after a further fall. Set to 0 to disable the floor|None|80|None|None|
  
Example input:

```
{
  "control_set_id": 0,
  "drop_threshold": 5,
  "interval": 3600,
  "minimum_compliance": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of frameworks reported|1|
|drifts|[]compliance_drift|True|Frameworks whose compliance score fell by at least the Drop Threshold or sits below the Minimum Compliance floor, worst fall first|None|
  
Example output:

```
{
  "count": 1,
  "drifts": [
    {
      "Compliance Change": {},
      "Control Set ID": 0,
      "Current Automated Controls Percentage": {},
      "Current Compliance": {},
      "Date Calculated": {},
      "Name": "",
      "Previous Automated Controls Percentage": {},
      "Previous Compliance": 0.0,
      "Reason": {}
    }
  ]
}
```

#### Monitor Records

This trigger is used to poll a Cyber GRC record type and emit records as they are created or updated

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event_type|string|Any|True|Which events to emit. Created emits each record once, when it first appears. Updated emits a record every time it changes, but not when it is created. Any emits both|["Any", "Created", "Updated"]|Created|None|None|
|filter|string|None|False|Additional OData $filter expression narrowing which records are emitted, combined with the timestamp filter using and. Field names are the camelCase names in the API reference, text values are single quoted, and dates are unquoted, for example statusID eq 3, or name eq 'Access Review', or dueDate ne null and dueDate lt 2026-12-31T00:00:00.000Z|None|statusID eq 3|None|None|
|interval|integer|300|True|Number of seconds to wait between polls|None|300|None|None|
|record_type|string|Tasks|True|The Cyber GRC record type to poll|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "SystemInfos", "TaskTypes", "Tasks", "Users", "VendorTypes", "Vendors"]|Tasks|None|None|
  
Example input:

```
{
  "event_type": "Any",
  "filter": "statusID eq 3",
  "interval": 300,
  "record_type": "Tasks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of records emitted|1|
|records|[]object|True|Records created or updated since the previous poll|None|
  
Example output:

```
{
  "count": 1,
  "records": [
    {}
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**risk**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assessment ID|integer|None|None|Assessment ID|None|
|Business Impact|string|None|None|Business Impact|None|
|Completed Date|date|None|None|Completed Date|None|
|Complexity|string|None|None|Complexity|None|
|Controls|[]risk_control_lookup|None|None|Controls|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Days Until Due Date|integer|None|None|Days Until Due Date|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Due Date|date|None|None|Due Date|None|
|Effort|string|None|None|Effort|None|
|Effort In Days|integer|None|None|Effort In Days|None|
|Effort Score|integer|None|None|Effort Score|None|
|Estimated Remaining Risk|integer|None|None|Estimated Remaining Risk|None|
|Extended Fields|object|None|None|Extended Fields|None|
|ID|integer|None|None|ID|None|
|Impact ID|integer|None|None|Impact ID|None|
|Inherent Cost|float|None|None|Inherent Cost|None|
|Inherent Risk Score|float|None|None|Inherent Risk Score|None|
|IT Assets|[]it_asset_lookup|None|None|IT Assets|None|
|Likelihood ID|integer|None|None|Likelihood ID|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Possible Outcome|string|None|None|Possible Outcome|None|
|Priority Based On Risk|float|None|None|Priority Based On Risk|None|
|Residual Cost|float|None|None|Residual Cost|None|
|Residual Risk|float|None|None|Residual Risk|None|
|Risk Category ID|integer|None|None|Risk Category ID|None|
|Risk Decision|string|None|None|Risk Decision|None|
|Status ID|integer|None|None|Status ID|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
|Vendors|[]risk_vendor_risk_lookup|None|None|Vendors|None|
  
**risk_vendor_risk_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**risk_control_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**it_asset_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**department_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**tag_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**incident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Client Security Assessments Issued|boolean|None|None|Client Security Assessments Issued|None|
|Confidential Data Impacted|boolean|None|None|Confidential Data Impacted|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Customer Data Impacted|boolean|None|None|Customer Data Impacted|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Extended Fields|object|None|None|Extended Fields|None|
|How Identified|string|None|None|How Identified|None|
|How Occurred|string|None|None|How Occurred|None|
|ID|integer|None|None|ID|None|
|Identified Date|date|None|None|Identified Date|None|
|Immediate Action|string|None|None|Immediate Action|None|
|Impact Type|string|None|None|Impact Type|None|
|Investigations Fines|boolean|None|None|Investigations Fines|None|
|Lessons Learned|string|None|None|Lessons Learned|None|
|Location ID|integer|None|None|Location ID|None|
|Material Impact|boolean|None|None|Material Impact|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Monetary Impact|integer|None|None|Monetary Impact|None|
|Name|string|None|None|Name|None|
|Non Confidential Data Impacted|boolean|None|None|Non Confidential Data Impacted|None|
|Occured Date|date|None|None|Occured Date|None|
|Personal Identifiable Info Impacted|boolean|None|None|Personal Identifiable Info Impacted|None|
|Realized Financial Loss|boolean|None|None|Realized Financial Loss|None|
|Reputational Damage|boolean|None|None|Reputational Damage|None|
|Root Cause|string|None|None|Root Cause|None|
|Send Reminders|boolean|None|None|Send Reminders|None|
|Status ID|integer|None|None|Status ID|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
  
**task**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Approval Status|boolean|None|None|Approval Status|None|
|Assessments|[]task_assessment_lookup|None|None|Assessments|None|
|Assigned To|entity_user|None|None|Assigned To|None|
|Audits|[]task_audit_lookup|None|None|Audits|None|
|Clients|[]task_client_lookup|None|None|Clients|None|
|Compliance|integer|None|None|Compliance|None|
|Rapid7 AI Event GUID|string|None|None|Rapid7 AI Event GUID|None|
|Rapid7 Key|string|None|None|Rapid7 Key|None|
|Contracts|[]task_contract_lookup|None|None|Contracts|None|
|Controls|[]task_control_lookup|None|None|Controls|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Departments|[]task_department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Due Date|date|None|None|Due Date|None|
|End Date|date|None|None|End Date|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Frequency|integer|None|None|Frequency|None|
|ID|integer|None|None|ID|None|
|Incidents|[]task_incident_lookup|None|None|Incidents|None|
|Instructions|string|None|None|Instructions|None|
|Integrations|[]task_integration_lookup|None|None|Integrations|None|
|Is Archived|boolean|None|None|Is Archived|None|
|Is Auditor Request|boolean|None|None|Is Auditor Request|None|
|Is Dynamic Ownership|boolean|None|None|Is Dynamic Ownership|None|
|Is Enabled|boolean|None|None|Is Enabled|None|
|Is Generated By AI|boolean|None|None|Is Generated By AI|None|
|Is Query Driven|boolean|None|None|Is Query Driven|None|
|IT Assets|[]task_it_asset_lookup|None|None|IT Assets|None|
|Locations|[]task_location_lookup|None|None|Locations|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Primary Driver|integer|None|None|Primary Driver|None|
|Queries|[]task_query_lookup|None|None|Queries|None|
|Raise Service Request|boolean|None|None|Raise Service Request|None|
|Require Acknowledgement|boolean|None|None|Require Acknowledgement|None|
|Risks|[]task_risk_lookup|None|None|Risks|None|
|Security Policies|[]task_security_policy_lookup|None|None|Security Policies|None|
|Send Reminders|boolean|None|None|Send Reminders|None|
|Should Repeat|boolean|None|None|Should Repeat|None|
|Should Reset|boolean|None|None|Should Reset|None|
|Start Date|date|None|None|Start Date|None|
|Status ID|integer|None|None|Status ID|None|
|Task Type ID|integer|None|None|Task Type ID|None|
|Trend|string|None|None|Trend|None|
|Vendors|[]task_vendor_lookup|None|None|Vendors|None|
  
**task_vendor_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_risk_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_control_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_it_asset_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_client_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_assessment_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_contract_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_audit_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_incident_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_department_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_location_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_security_policy_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_query_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_integration_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**entity_user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|None|Active|None|
|Associated User ID|integer|None|None|Associated User ID|None|
|RACI Option|integer|None|None|RACI Option|None|
|Title|string|None|None|Title|None|
|User Email|string|None|None|User Email|None|
|User First Name|string|None|None|User First Name|None|
|User Last Name|string|None|None|User Last Name|None|
|Users ID|integer|None|None|Users ID|None|
  
**audit**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assessments|[]assessment_lookup|None|None|Assessments|None|
|Audit Users|[]audit_audit_user_lookup|None|None|Audit Users|None|
|Auditor Findings|[]audit_auditor_finding_lookup|None|None|Auditor Findings|None|
|Control Set|audit_control_set_lookup|None|None|Control Set|None|
|Control Set ID|integer|None|None|Control Set ID|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Documents|[]audit_document_lookup|None|None|Documents|None|
|End Date|date|None|None|End Date|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Frequency|integer|None|None|Frequency|None|
|Frequency Name|string|None|None|Frequency Name|None|
|ID|integer|None|None|ID|None|
|Is Archived|boolean|None|None|Is Archived|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Observation Period End|date|None|None|Observation Period End|None|
|Observation Period Start|date|None|None|Observation Period Start|None|
|Start Date|date|None|None|Start Date|None|
|Status|string|None|None|Status|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
  
**audit_control_set_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**audit_audit_user_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|None|Active|None|
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
|Title|string|None|None|Title|None|
|User Email|string|None|None|User Email|None|
|User First Name|string|None|None|User First Name|None|
|User Last Name|string|None|None|User Last Name|None|
|Users ID|integer|None|None|Users ID|None|
  
**audit_document_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**audit_auditor_finding_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assessments|[]control_set_control_set_assessment_lookup|None|None|Assessments|None|
|Audits|[]control_set_audit_lookup|None|None|Audits|None|
|Compliance|integer|None|None|Compliance|None|
|Rapid7 Key|string|None|None|Rapid7 Key|None|
|Controls|[]control_set_control_lookup|None|None|Controls|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Enabled|boolean|None|None|Enabled|None|
|ID|integer|None|None|ID|None|
|Is Archived|boolean|None|None|Is Archived|None|
|IT Assets|[]control_set_control_set_it_asset_lookup|None|None|IT Assets|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Security Policy Info ID|integer|None|None|Security Policy Info ID|None|
|Type|integer|None|None|Type|None|
  
**control_set_control_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set_control_set_assessment_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set_control_set_it_asset_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set_audit_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Audits|[]assessment_audit_lookup|None|None|Audits|None|
|Compliance|integer|None|None|Compliance|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Due Date|date|None|None|Due Date|None|
|Enabled|boolean|None|None|Enabled|None|
|Form Entry Name|string|None|None|Form Entry Name|None|
|Frequency|integer|None|None|Frequency|None|
|ID|integer|None|None|ID|None|
|Is Accepted|boolean|None|None|Is Accepted|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Risks|[]assessment_risk_lookup|None|None|Risks|None|
|Should Populate Answers|boolean|None|None|Should Populate Answers|None|
|Should Repeat|boolean|None|None|Should Repeat|None|
|Start Date|date|None|None|Start Date|None|
|Submitted Date|date|None|None|Submitted Date|None|
|Summary|string|None|None|Summary|None|
|Tasks|[]assessment_task_lookup|None|None|Tasks|None|
|Times Duplicated|integer|None|None|Times Duplicated|None|
|Trend|string|None|None|Trend|None|
|Users|[]assessment_user_lookup|None|None|Users|None|
|Was Submitted|boolean|None|None|Was Submitted|None|
  
**assessment_user_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|None|Email|None|
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment_risk_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment_task_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment_audit_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**vendor**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access End Date|date|None|None|Access End Date|None|
|Access Start Date|date|None|None|Access Start Date|None|
|Access To Client Data|boolean|None|None|Access To Client Data|None|
|Access To Our System|boolean|None|None|Access To Our System|None|
|Assessments|[]assessment_lookup|None|None|Assessments|None|
|Assigned To|entity_user|None|None|Assigned To|None|
|Compliance|integer|None|None|Compliance|None|
|Rapid7 Key|string|None|None|Rapid7 Key|None|
|Contact Email|string|None|None|Contact Email|None|
|Contact Name|string|None|None|Contact Name|None|
|Contracts|[]contract_lookup|None|None|Contracts|None|
|Controller Or Processor|string|None|None|Controller Or Processor|None|
|Could Vendor Failure Result In Fines|boolean|None|None|Could Vendor Failure Result In Fines|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Date Founded|date|None|None|Date Founded|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Gdpr Compliant|string|None|None|Gdpr Compliant|None|
|Head Quartered|string|None|None|Head Quartered|None|
|Holds Client Data|boolean|None|None|Holds Client Data|None|
|Holds Our Data|boolean|None|None|Holds Our Data|None|
|ID|integer|None|None|ID|None|
|Industry|string|None|None|Industry|None|
|Is Enabled|boolean|None|None|Is Enabled|None|
|Is Holding Client Data|boolean|None|None|Is Holding Client Data|None|
|Is Holding Personal Data|boolean|None|None|Is Holding Personal Data|None|
|Is Insured|boolean|None|None|Is Insured|None|
|Is NDA Signed|boolean|None|None|Is NDA Signed|None|
|IT Assets|[]it_asset_lookup|None|None|IT Assets|None|
|Loss Of Vendor Would Cause Significant Disruption|boolean|None|None|Loss Of Vendor Would Cause Significant Disruption|None|
|Loss Of Vendor Would Have Material Impact|boolean|None|None|Loss Of Vendor Would Have Material Impact|None|
|Loss Of Vendor Would Impact Customers|boolean|None|None|Loss Of Vendor Would Impact Customers|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Negative Impact When Service Down More Than24hr|boolean|None|None|Negative Impact When Service Down More Than24hr|None|
|Public Description|string|None|None|Public Description|None|
|Risks|[]risk_lookup|None|None|Risks|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
|Trend|string|None|None|Trend|None|
|Type|string|None|None|Type|None|
|Type Of Asset|string|None|None|Type Of Asset|None|
|Vendor Could Impact Reputation|boolean|None|None|Vendor Could Impact Reputation|None|
|Vendor Criticality|string|None|None|Vendor Criticality|None|
|Website|string|None|None|Website|None|
  
**risk_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**contract_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**certification**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|ID|integer|None|None|ID|None|
|Is Active|boolean|None|None|Is Active|None|
|IT Assets|[]it_asset_lookup|None|None|IT Assets|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
  
**it_asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|A1|integer|None|None|A1|None|
|A2|integer|None|None|A2|None|
|A3|integer|None|None|A3|None|
|Assessments|[]assessment_lookup|None|None|Assessments|None|
|Assigned To|entity_user|None|None|Assigned To|None|
|C1|integer|None|None|C1|None|
|C2|integer|None|None|C2|None|
|C3|integer|None|None|C3|None|
|Calculated CIA|string|None|None|Calculated CIA|None|
|Certifications|[]certification_lookup|None|None|Certifications|None|
|Compliance|integer|None|None|Compliance|None|
|Contracts|[]contract_lookup|None|None|Contracts|None|
|Control Sets|[]control_set_lookup|None|None|Control Sets|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Has Personal Data|boolean|None|None|Has Personal Data|None|
|I1|integer|None|None|I1|None|
|I2|integer|None|None|I2|None|
|I3|integer|None|None|I3|None|
|ID|integer|None|None|ID|None|
|Is BCP|boolean|None|None|Is BCP|None|
|Is Client Data Host|boolean|None|None|Is Client Data Host|None|
|Is Client Facing|boolean|None|None|Is Client Facing|None|
|Is DFA|boolean|None|None|Is DFA|None|
|Is DR|boolean|None|None|Is DR|None|
|Is Data Anonymous|boolean|None|None|Is Data Anonymous|None|
|Is Data At-Rest|boolean|None|None|Is Data At-Rest|None|
|Is Data In Transit|boolean|None|None|Is Data In Transit|None|
|Is Desktop App|boolean|None|None|Is Desktop App|None|
|Is Dev In House|boolean|None|None|Is Dev In House|None|
|Is Hosted In Cloud|boolean|None|None|Is Hosted In Cloud|None|
|Is Individual Perms|boolean|None|None|Is Individual Perms|None|
|Is Our Data Host|boolean|None|None|Is Our Data Host|None|
|Is Pre Prod Env|boolean|None|None|Is Pre Prod Env|None|
|Is Prod Data Used In Non Prod Env|boolean|None|None|Is Prod Data Used In Non Prod Env|None|
|Is Production Env|boolean|None|None|Is Production Env|None|
|Is Public Internet Facing|boolean|None|None|Is Public Internet Facing|None|
|Is Role Based|boolean|None|None|Is Role Based|None|
|Is Role Based Access|boolean|None|None|Is Role Based Access|None|
|Is SIEM Monitored|boolean|None|None|Is SIEM Monitored|None|
|Is SSO|boolean|None|None|Is SSO|None|
|Is SSO Authenticated|boolean|None|None|Is SSO Authenticated|None|
|Is SSO Authorised|boolean|None|None|Is SSO Authorised|None|
|Is Security Testing Required|boolean|None|None|Is Security Testing Required|None|
|Is Service Accounts|boolean|None|None|Is Service Accounts|None|
|Is Test Data Personal|boolean|None|None|Is Test Data Personal|None|
|Is Test Env|boolean|None|None|Is Test Env|None|
|Is Tested|boolean|None|None|Is Tested|None|
|Is UAT Env|boolean|None|None|Is UAT Env|None|
|Is Web Based App|boolean|None|None|Is Web Based App|None|
|Life Cycle|integer|None|None|Life Cycle|None|
|Locations|[]location_lookup|None|None|Locations|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Number Of Users|integer|None|None|Number Of Users|None|
|Risks|[]risk_lookup|None|None|Risks|None|
|System Type|integer|None|None|System Type|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
|Trend|string|None|None|Trend|None|
  
**certification_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**location_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|None|Active|None|
|Anti Tampering Enabled|boolean|None|None|Anti Tampering Enabled|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Email|string|None|None|Email|None|
|First Name|string|None|None|First Name|None|
|ID|integer|None|None|ID|None|
|Last Login Date|date|None|None|Last Login Date|None|
|Last Name|string|None|None|Last Name|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Preferred Dictionary|string|None|None|Preferred Dictionary|None|
|Preferred Unit Of Measure|string|None|None|Preferred Unit Of Measure|None|
|Profile Background Color|string|None|None|Profile Background Color|None|
|Theme Preference|string|None|None|Theme Preference|None|
  
**framework_compliance**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Automated Controls Percentage|float|None|None|Percentage of this framework's controls that are evidenced automatically|None|
|Compliance|float|None|None|Compliance score of this framework|None|
|Control Set ID|integer|None|None|ID of the control set these scores belong to|None|
|Date Calculated|string|None|None|When Cyber GRC last calculated these scores|None|
|Linked Controls Percentage|float|None|None|Percentage of this framework's controls that are linked to evidence|None|
|Name|string|None|None|Name of the control set, omitted when the control set itself could not be read|None|
  
**overall_compliance**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Automated Controls Percentage|float|None|None|Mean automated controls percentage of every framework returned|None|
|Compliance|float|None|None|Mean compliance score of every framework returned|None|
|Framework Count|integer|None|None|Number of frameworks the overall scores were averaged over|None|
  
**contract**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Annual Cost|integer|None|None|Annual Cost|None|
|Approval Status|boolean|None|None|Approval Status|None|
|Category|contract_category_lookup|None|None|Category|None|
|Clients|[]contract_client_lookup|None|None|Clients|None|
|Contact Email|string|None|None|Contact Email|None|
|Contact Name|string|None|None|Contact Name|None|
|Contract Category ID|integer|None|None|Contract Category ID|None|
|Contract Documents|[]contract_document_lookup|None|None|Contract Documents|None|
|Contract Subcategory ID|integer|None|None|Contract Subcategory ID|None|
|Contract Type|integer|None|None|Contract Type|None|
|Cost Type|string|None|None|Cost Type|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Currency|string|None|None|Currency|None|
|Days Until Renewal|integer|None|None|Days Until Renewal|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|End Date|date|None|None|End Date|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Generated Date|date|None|None|Generated Date|None|
|Has Enabled Adobe Sync|boolean|None|None|Has Enabled Adobe Sync|None|
|ID|integer|None|None|ID|None|
|Invoice Frequency|integer|None|None|Invoice Frequency|None|
|Is Key Contract|boolean|None|None|Is Key Contract|None|
|IT Assets|[]it_asset_lookup|None|None|IT Assets|None|
|Max Extension|date|None|None|Max Extension|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Notice Date|date|None|None|Notice Date|None|
|Parent Contract|contract_lookup|None|None|Parent Contract|None|
|Parent Contract ID|integer|None|None|Parent Contract ID|None|
|Sequence Number|integer|None|None|Sequence Number|None|
|Start Date|date|None|None|Start Date|None|
|Status|contract_status_lookup|None|None|Status|None|
|Status ID|integer|None|None|Status ID|None|
|Subcategory|contract_category_lookup|None|None|Subcategory|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
|Termination Notice Period|integer|None|None|Termination Notice Period|None|
|Variation Number|integer|None|None|Variation Number|None|
|Vendors|[]contract_vendor_lookup|None|None|Vendors|None|
  
**contract_status_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**contract_category_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**contract_vendor_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**contract_client_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**contract_document_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Blob Name|string|None|None|Blob Name|None|
|Contract ID|integer|None|None|Contract ID|None|
|ID|integer|None|None|ID|None|
|Is Current Version|boolean|None|None|Is Current Version|None|
|Is Working Version|boolean|None|None|Is Working Version|None|
|Title|string|None|None|Title|None|
|Version|string|None|None|Version|None|
  
**discussion**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|None|Comment|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Form Discussion ID|integer|None|None|Form Discussion ID|None|
|ID|integer|None|None|ID|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|User ID|integer|None|None|User ID|None|
  
**compliance_drift**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Compliance Change|float|None|None|Current compliance minus previous compliance, so a fall is negative|None|
|Control Set ID|integer|None|None|ID of the control set whose score moved|None|
|Current Automated Controls Percentage|float|None|None|Automated controls percentage Cyber GRC most recently calculated|None|
|Current Compliance|float|None|None|Compliance score Cyber GRC most recently calculated|None|
|Date Calculated|string|None|None|When Cyber GRC calculated the current score|None|
|Name|string|None|None|Name of the control set|None|
|Previous Automated Controls Percentage|float|None|None|Automated controls percentage recorded on the previous poll|None|
|Previous Compliance|float|None|None|Compliance score recorded on the previous poll|None|
|Reason|string|None|None|Why the drift was reported. Drop means the score fell by at least the Drop Threshold; Below Minimum means it crossed under the Minimum Compliance floor. A fall that does both is reported as Drop|None|
  
**delete_operation_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|FK Violation|boolean|None|None|FK Violation|None|
|FK Violation Table|[]string|None|None|FK Violation Table|None|
|Message|string|None|None|Message|None|
|Success|boolean|None|None|Success|None|


## Troubleshooting

* The URL is the Cyber GRC API host, which is a different host from the one used to sign in to the web interface. If requests answer with the sign-in page instead of JSON, the URL is pointing at the web interface rather than the API
* Every read action accepts OData query options. When an action returns no records, check the Filter expression against the API reference first, because the API rejects an invalid $filter with a 400 response rather than returning an empty result
* An API key carries the permissions of the user it is assigned to, so a 403 response means that user cannot see or change the record in question
* A 401 response does not always mean the API key is wrong. Any path the API does not recognise, such as a misspelled record type or a URL that already ends in /api/v2, falls through to the interactive sign-in scheme and is answered with a 401 whose scheme is not ApiKey. The plugin reports that case separately, so read the error text before regenerating the key
* The typed actions, such as Get Risks, declare the type of every field they return, and a step fails validation if the API answers with a different type than the record schema documents. Generic List Records returns the same records as untyped objects and can be used as a workaround while the mismatch is reported to Rapid7 support
* Upload Flat File calls the v1 Flat File API. On some deployments that endpoint authenticates interactive sessions rather than API keys, and answers 401 with a scheme of compyl-microsoft. If that happens, ask Rapid7 support to enable API key access to the Flat File API for the tenant

# Version History

* 1.0.0 - Initial plugin

# Links

* [Rapid7 Cyber GRC](https://www.rapid7.com)

## References

* [Rapid7 Cyber GRC API reference](https://compyl.readme.io/reference/)
* [Managing your API keys](https://compyl.readme.io/reference/getting-started)