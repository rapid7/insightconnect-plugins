# Description

The [Zenhub](https://www.zenhub.com) plugin allows for agile project management in GitHub. This plugin will allow you to manage issues, epics, and pipelines in a ZenHub enable Git repository.

This plugin utilizes the [Zenhub API](https://github.com/ZenHubIO/API) to manage ZenHub Epics, Pipelines, and Estimates.

# Key Features

* Create an Issue
* Create an Epic
* Move an issue to another pipeline

# Requirements

* ZenHub API token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_token|password|None|True|ZenHub API Token|None|

A ZenHub API Token can be obtained [here](https://dashboard.zenhub.io/#/settings).

## Technical Details

### Actions

#### Get Issue Events

This action is used to get the ZenHub events for a github issue.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|issue_number|integer|None|False|GitHub Issue Number|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]issue_event|False|List of ZenHub Issue Events|

Example output:

```

{
  "data": [
    {
      "user_id": 7100147,
      "created_at": "2017-06-25T22:58:49.100Z",
      "to_estimate_value": -1,
      "type": "addIssueToEpic",
      "to_pipeline_name": "",
      "from_estimate_value": -1,
      "from_pipeline_name": ""
    },
    {
      "user_id": 7100147,
      "created_at": "2017-06-25T22:58:49.058Z",
      "to_estimate_value": -1,
      "type": "convertIssueToEpic",
      "to_pipeline_name": "",
      "from_estimate_value": -1,
      "from_pipeline_name": ""
    },
    ...
  ]
}

```

#### Remove Issue from Epic

This action is used to remove a github issue from a ZenHub epic.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|issue|issue_reference|None|False|A GitHub Issue to remove from the ZenHub Epic|None|
|epic_id|integer|None|False|GitHub Issue Number of the ZenHub Epic|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|
|issue|issue_reference|False|The GitHub Issue removed from the ZenHub Epic|

#### Get Epic Data

This action is used to get the ZenHub data for a ZenHub epic.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|epic_id|integer|None|False|GitHub Issue Number of the ZenHub Epic|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|epic_data|False|ZenHub Epic Data|

Example output:

```

{
  "issues": [
     {
       "issue_number": 3,
       "repo_id": 25762944,
       "position": -1,
       "pipeline_name": "",
       "plus_ones": [],
       "is_epic": false,
       "estimate_value": -1
     }
   ],
   "pipeline_name": "Review/QA",
   "estimate_value": 2,
   "total_epic_estimates_value": 2
}

```

#### Convert Issue to Epic

This action is used to convert a github issue to a ZenHub epic.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|issues|[]issue_reference|None|False|GitHub Issues to add to ZenHub Epic|None|
|issue_number|integer|None|False|GitHub Issue Number|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

#### Set Estimate Value for Issue

This action is used to set the ZenHub estimate value for a github issue.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|estimate_value|integer|None|False|ZenHub Estimate Value|None|
|issue_number|integer|None|False|GitHub Issue Number|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|
|estimate_value|integer|False|Set ZenHub Estimate Value|

#### Convert Epic to Issue

This action is used to convert a ZenHub epic back to a Github issue.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|epic_id|integer|None|False|GitHub Issue Number of the ZenHub Epic|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

#### Add Issue to Epic

This action is used to add a github issue to a ZenHub epic.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|issue|issue_reference|None|False|A GitHub Issue to add to the ZenHub Epic|None|
|epic_id|integer|None|False|GitHub Issue Number of the ZenHub Epic|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|
|issue|issue_reference|False|The GitHub Issue added to the ZenHub Epic|

Example output:

```

{
  "issue": {
    "repo_id": 25762944,
    "issue_url": "",
    "issue_number": 3
  },
  "status_code": 200
}

```

#### Get Repository Epics

This action is used to get the ZenHub epics for a github repository.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|epics|[]issue_reference|False|List of ZenHub Repository Epics|

Example output:

```

{
  "data": [
    {
      "issue_url": "https://github.com/arvindch/pockyt/issues/6",
      "repo_id": 25762944,
      "issue_number": 6
    }
  ]
}

```

#### Move Issue Between Pipelines

This action is used to move a github issue between ZenHub pipelines.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|position|integer|None|False|New Position in the ZenHub Pipeline (-1\: bottom, 0\: top, n\: nth index)|None|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|issue_number|integer|None|False|GitHub Issue Number|None|
|pipeline_id|string|None|False|ZenHub Pipeline ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

#### Get Repository Board Data

This action is used to get the ZenHub board data for a github repository.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|repository_data|False|ZenHub Repository Board Data|

Example output:

```

{
 "data": {
   "pipelines": [
     {
       "pipeline_name": "New Issues",
       "issues": [
         {
           "position": 0,
           "plus_ones": [],
           "pipeline_name": "New Issues",
           "issue_number": 7,
           "is_epic": false,
           "repo_id": 25762944,
           "estimate_value": -1
         }
       ],
       ...
       "pipeline_id": "594b2b2c34dc3b7183584382"
     }
  }
}

```

#### Get Issue Data

This action is used to get the ZenHub data for a github issue.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|repo_id|integer|None|False|GitHub Repository ID e.g. 24237263|None|
|issue_number|integer|None|False|GitHub Issue Number|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|issue_data|False|ZenHub Issue Data|

Example output:

```

{
  "data": {
    "pipeline_name": "Review/QA",
    "is_epic": true,
    "issue_number": 6,
    "estimate_value": 2,
    "plus_ones": [],
    "position": -1,
    "repo_id": 25762944
  }
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Note: GitHub Repository IDs (repo_id) can be obtained via the GitHub API at the [GET /user/repos endpoint](https://developer.github.com/v3/repos/#list-your-repositories).

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Rename "Move Issue between Pipelines" action to "Move Issue Between Pipelines"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [ZenHub](https://zenhub.com)
* [ZenHub API](https://github.com/ZenHubIO/API)

