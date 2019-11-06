# Description

[Qualys SSL Labs](https://www.ssllabs.com) is used to test SSL servers available on the public Internet.
This plugin uses the [Assessment APIs](https://github.com/ssllabs/ssllabs-scan/blob/stable/ssllabs-api-docs.md).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Info

This action is used to check SSL Labs server availability.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|newAssessmentCoolOff|integer|False|None|
|clientMaxAssessments|integer|False|None|
|currentAssessments|integer|False|None|
|messages|[]string|False|None|
|engineVersion|string|False|None|
|criteriaVersion|string|False|None|
|maxAssessments|integer|False|None|

Example response:

```

{
  "currentAssessments": 0,
  "clientMaxAssessments": 25,
  "criteriaVersion": "2009o",
  "engineVersion": "1.28.5",
  "newAssessmentCoolOff": 1000,
  "maxAssessments": 25,
  "messages": [
    "This assessment service is provided free of charge by Qualys SSL Labs, subject to our terms and conditions: https://www.ssllabs.com/about/terms.html"
  ]
}

```

#### Status

This action is used to retrieve status codes.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|statusDetails|object|False|None|

#### Analyze

This action is used to initialize an SSL assessment.

**Note:** If no `endpoints` data is returned by the Qualys SSL API then that key will be set to an empty array i.e. `[]` and it will be logged:

```

INFO:root:Endpoints not found in response

```

See the Output section for an example.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|max_age|integer|None|False|Max report age in hours|None|
|all|string|None|True|Full information returned vs returned only if assessment is done|['Done', 'On']|
|publish|boolean|None|True|Publish on public results boards|None|
|host|string|None|True|Server hostname|None|
|start_new|string|None|True|Cached results ignored; New assessment started|['Off', 'On']|
|from_cache|string|None|True|Always deliver cached assessment reports if available|['Off', 'On']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|
|testTime|integer|False|None|
|protocol|string|False|None|
|startTime|integer|False|None|
|engineVersion|string|False|None|
|criteriaVersion|string|False|None|
|host|string|False|None|
|isPublic|boolean|False|None|
|endpoints|[]object|False|None|
|port|integer|False|None|

Note that the API server constantly updates the data and thus two subsequent requests of the same inputs could have differing amounts of data output. E.g.

First request:

```

{
  "status": "DNS",
  "isPublic": false,
  "engineVersion": "1.28.5",
  "startTime": 1496267559768,
  "endpoints": [],
  "criteriaVersion": "2009o",
  "host": "mail.cloudbizz.lu",
  "statusMessage": "Resolving domain names",
  "testTime": 0,
  "port": 443,
  "protocol": "HTTP"
}

```

Second request:

```

{
  "status": "IN_PROGRESS",
  "endpoints": [
    {
      "eta": -1,
      "delegation": 1,
      "ipAddress": "37.157.154.211",
      "statusDetails": "TESTING_NPN",
      "progress": -1,
      "details": {
        "prefixDelegation": false,
        "nonPrefixDelegation": true,
        "cert": {},
        "chain": {},
        "protocols": [],
        "key": {},
        "suites": {},
        "hostStartTime": 1496267559768
      },
      "statusDetailsMessage": "Testing NPN",
      "statusMessage": "In progress"
    }
  ],
  "isPublic": false,
  "port": 443,
  "startTime": 1496267559768,
  "testTime": 0,
  "criteriaVersion": "2009o",
  "engineVersion": "1.28.5",
  "protocol": "HTTP",
  "host": "mail.cloudbizz.lu"
}

```

The difference is that the response to the second request contains `endpoints` data, which may not always be available.

#### Endpoint

This action is used to retrieve detailed endpoint info.

**Note**: The server may not have any information for the requests as it's being made. If this is the case the action will fail.
To handle this, add this action to a loop in the Workflow Builder where the loop exits when the plugin's `$success = true`. Enabling
`Continue workflow on step failure` in the action's configuration of the Workflow Builder is required for this to work.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip|string|None|True|Server IP Address|None|
|host|string|None|True|Server hostname|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|hasWarnings|boolean|False|None|
|grade|string|False|None|
|statusMessage|string|False|None|
|delegation|integer|False|None|
|eta|integer|False|None|
|details|detail|False|None|
|isExceptional|boolean|False|None|
|duration|integer|False|None|
|progress|integer|False|None|
|gradeTrustIgnore|string|False|None|
|ipAddress|string|False|None|

#### Certificate

This action is used to retrieve root certificates.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|certificates|bytes|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - Fix typo in plugin spec
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Qualys SSL Labs](https://www.ssllabs.com)
* [Assessment APIs](https://github.com/ssllabs/ssllabs-scan/blob/stable/ssllabs-api-docs.md)

