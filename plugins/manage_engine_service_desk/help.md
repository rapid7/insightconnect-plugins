# Description

< fill in later >

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

* 2022-03-08

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Manage Service Engine API key|None|6A70F2A8-BC42-49A0-98A4-20FECF4C96EC|

Example input:

```
```

## Technical Details

### Actions

#### Get List Request

This action this operation helps you to get all requests.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|help_desk_ticket|True|Returned value for all requests|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### closure_info_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Closure Code|string|False|Closure Codes are codes that denote the reason for closing a request(ticket)/change request, whether the request/change was closed due to completion, rejection, and so on|
|Closure Comments|string|False|Closure comments denotes the reason for closing the request and can only be given by technician|
|Requester Ack Comments|string|False|Comments from the requester in regards to the resolution he/she has been given|
|Requester Ack Solution|boolean|False|Denotes if the requester has acknowledged the resolution he/she has been given|

#### help_desk_ticket

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Approval Status|string|False|Denotes the approval status of this request|
|Assets|string|False|Array of asset objects associated to this request|
|Assigned Time|date|False|Indicates the time at which this request is assigned to a technician|
|Attachments|file|False|Files that are attached to the request with a maximum of 10 files that can be attached to a request|
|Cancel Flag Comments|string|False|Information provided by the requester to cancel a request to the technician|
|Cancellation Requested|boolean|False|Boolean which indicates whether the request is raised for cancelation by the requester|
|Category|string|False|Indicates the category to which the request belongs|
|Closure Info|closure_info_object|False|Contains the closure information when the request is in closed status|
|Completed By Denial|boolean|False|Boolean which denotes whether the request is completed, when the request was denied|
|Completed Time|date|False|Indicates the time at which this request is completed|
|Configuration Items|string|False|Critical Items for which the request has been raised|
|Created By|string|False|Indicates the requester who created this request|
|Created Time|date|False|Indicates the time at which this request is created|
|Delete Pre Template Tasks|boolean|False|The reason for updating this request|
|Deleted Assets|string|False|The assets that are disassociated from this request|
|Deleted Time|date|False|Denotes the time at which the request will be deleted|
|Department|string|False|Indicates the department to which this requester belongs|
|Description|string|False|Details about the request|
|Display ID|integer|False|Indicates the display ID of the request|
|Due By Time|date|False|Indicates the time at which this request is scheduled to be completed|
|Editor|string|False|The user who is configured as the Editor of the request|
|Editor Status|integer|False|The status of the Editor’s review/update|
|Email BCC|string|False|List of email addresses(bcc addresses) which receives the request|
|Email CC|string|False|List of e-mail addresses(cc addresses) which receives the request through e-mail|
|Email IDs to Notify|string|False|Array of Email ids, which needs to be notified about the happenings of this request|
|Email To|string|False|List of email addresses(to addresses) while receiving the request|
|First Response due by Time|date|False|Indicates the time at which the first response for this request is schedule|
|Group|string|False|The group to which the request is assigned to|
|Has Attachments|boolean|False|Boolean value indicating whether this request has any attachments or not|
|Has Change Initiated Request|boolean|False|Boolean to show whether there are requests which are initated by the change|
|Has Draft|boolean|False|Boolean value indicating whether this request has drafts or not|
|Has Linked Requests|boolean|False|Boolean value indicating whether this request has any linked requests or not|
|Has Notes|boolean|False|Boolean value indicating whether this request has any notes or not|
|Has Problem|boolean|False|Boolean value indicating whether this request is associated to a problem or not|
|Has Project|boolean|False|Boolean value indicating whether this request is associated to a project or not|
|Has Purchase Orders|boolean|False|Boolean value indicating whether this request is associated to Purchase Orders|
|Has Request Initiated Change|boolean|False|Boolean value indicating whether this request is initiated a change or not|
|ID|integer|False|Unique identifer of this request|
|Impact|string|False|Indicates the impact of the request|
|Impact Details|string|False|Description about the impact of the request|
|Is Escalated|boolean|False|A boolean value which represents whether the request is escalated or not|
|Is FCR|boolean|False|Boolean value indicating if the request has been marked as First Call Resolution|
|Is First Response Overdue|boolean|False|Boolean value indicating whether this request is in overdue to make first response|
|Is Overdue|boolean|False|Boolean value indicating whether this request is overdue|
|Is Read|boolean|False|Boolean value indicating whether this request’s replies are read or not|
|Is Reopened|boolean|False|Boolean value indicating whether this request is reopened or not|
|Is Service Request|boolean|False|Boolean value indicating whether this request is a service request or not|
|Is Trashed|boolean|False|Boolean value indicating whether this request is in trash|
|Item|string|False|Displays the item of the request|
|Last Updated Time|date|False|Indicates the time when this request is last updated|
|Level|string|False|Denotes the level of the request|
|Lifecycle|string|False|Indicates the lifecycle associated with this request|
|Linked To Request|linked_to_request_object|False|Holds linked request details|
|Mode|string|False|The mode in which this request is created|
|Notification Status|string|False|Shows the current status of request’s replies, whether last one from requester or technician|
|On Behalf Of|string|False|Requesters can raise request on behalf of other users, this field denotes the user, on behalf of who the request has been raised|
|Onhold Scheduler|onhold_scheduler_object|False|Contains the scheduling details for the request, when the request is in Onhold status|
|Priority|string|False|Denotes the priority of the request|
|Request Type|string|False|Indicates the type of the request|
|Requester|string|False|Indicates the requester of this request|
|Resolution|resolution_object|False|A solution for the request|
|Resolved Time|date|False|Indicates the time at which this request is resolved|
|Resources|string|False|Holds the resource data mapped to the request|
|Responded Time|date|False|Indicates the time at which this request is responded|
|Scheduled End Time|date|False|Date and time at which the request is scheduled to end|
|Scheduled Start Time|date|False|Date and time at which the request is scheduled to start|
|Service Approvers|service_approvers_object|False|The configured users will be added to the first stage of approval for the service request which can be added only by requesters|
|Service Category|string|False|Indicates the service category to which this request belongs|
|Service Cost|float|False|Basic cost for the service which we are requesting|
|Site|string|False|Denotes the site to which this request belongs|
|SLA|string|False|The SLA details associated with this request|
|Status|string|False|Indicates the current status of this request|
|Status Change Comments|string|False|The reason why the status is changed|
|Subcategory|string|False|Denotes the subcategory to which the request belongs|
|Subject|string|False|Title of the request|
|Technician|string|False|Denotes the technician assigned to this request|
|Template|string|False|Indicates the template which is used to create this request|
|Time Elapsed|integer|False|Indicates the time spent on this request|
|Total Cost|float|False|Total Cost is the cumulative value of service cost and the cost of the individual resources selected|
|UDF Fields|string|False|Holds user defined fields’ values associated with the request|
|Unreplied Count|integer|False|The number of requester replies for which the technician haven’t replied yet|
|Update Reason|string|False|The reason for which the request has been updated|
|Urgency|string|False|Denotes the urgency of the request|

#### linked_to_request_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Request|string|False|Holds linked request details|

#### onhold_scheduler_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Change to Status|string|False|Status object to which the request is scheduled to move to, after the onhold scheduler is completed|
|Comments|string|False|Details or comments added for linking requests|
|Held By|string|False|The technician who stopped the timer who changed the status to OnHold of the Request|
|Scheduled Time|date|False|Denotes the scheduled time for the onhold scheduler to change the request’s status|

#### resolution_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Content|string|False|Resolution content provided by the technician to resolve this request|
|Submitted By|string|False|No description|

#### service_approvers_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Organisation Role|string|False|Org roles of the service approvers configured|
|Users|string|False|The users who are configured as service approvers for the request|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Manage Engine Service Desk](LINK TO PRODUCT/VENDOR WEBSITE)

