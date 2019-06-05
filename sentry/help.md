
# Sentry

## About

[Sentry](https://sentry.io/) is an open-source error tracking tool that helps developers monitor and fix crashes in real time.
This plugin utilizes the [Sentry API](https://docs.sentry.io/).

## Actions

### Submit Event

This action is used to create a new Sentry event.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|dsn|string|None|True|DSN configuration of a Sentry project (e.g. 'https\://public\:secret@sentry.example.com/1')|None|
|sentry_version|integer|7|False|The protocol version. The current version of the protocol is '7'|None|
|event_json|EventJSON|None|True|Data describing the event|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|ID of a newly created event|

Example output:

```

{
  "id": "afd25d0e868f495fa802179d33ef3b97"
}

```

### List Project Issues

This action is used to return a list of issues (groups) bound to a project.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_slug|string|None|True|The slug of the organization the issues belong to|None|
|query|string|None|False|An optional Sentry structured search query. If not provided an implied 'is\:unresolved; is assumed|None|
|statsPeriod|string||False|An optional stat period (can be one of '24h', '14d', and '')|['24h', '14d', '']|
|shortIdLookup|boolean|None|False|If this is set to true then short IDs are looked up by this function as well. This can cause the return value of the function to return an event issue of a different project which is why this is an opt-in. Set to 1 to enable|None|
|project_slug|string|None|True|The slug of the project the issues belong to|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]Issue|False|A list of issues (groups) bound to a project|

Example output:

```

{
  "issues": [
    {
      "lastSeen": "2018-07-18T19:31:13Z",
      "numComments": 0,
      "userCount": 0,
      "stats": {
        "14d": [
          [
            1531872000,
            3
          ],
          [
            1531958400,
            0
          ],
          [
            1532044800,
            0
          ]
        ]
      },
      "title": "SyntaxError: Wattttt! AHAHAH",
      "id": "612424900",
      "type": "error",
      "annotations": [],
      "metadata": {
        "type": "SyntaxError",
        "value": "Wattttt! AHAHAH"
      },
      "status": "resolved",
      "subscriptionDetails": {
        "reason": "unknown"
      },
      "isPublic": true,
      "hasSeen": true,
      "shortId": "PYTHONTEST-4",
      "shareId": "56aa20f0994d428c90bf9382f1c279a9",
      "firstSeen": "2018-07-18T16:51:40Z",
      "count": "3",
      "permalink": "https://sentry.io/komand-test/pythontest/issues/612424900/",
      "level": "error",
      "isSubscribed": true,
      "isBookmarked": true,
      "project": {
        "slug": "pythontest",
        "id": "1244809",
        "name": "PythonTest"
      },
      "statusDetails": {}
    }
  ]
  }
}

```

### List Issue Events

This action is used to list an issue's events.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|issue_id|string|None|True|The ID of the issue to retrieve|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]Event|False|Issue's events|

Example output:

```

{
  "events": [
    {
      "eventID": "266e5b557237474eb56e9c2eeaac4a15",
      "packages": {},
      "tags": [
        {
          "value": "error",
          "key": "level"
        },
        {
          "value": "\"myself\"",
          "key": "transaction"
        }
      ],
      "contexts": {},
      "dateReceived": "2018-07-18T19:39:30Z",
      "dateCreated": "2018-07-18T19:39:30Z",
      "fingerprints": [
        "e098a2aa93a10a036b357c3d190c56c3"
      ],
      "metadata": {
        "type": "SyntaxError",
        "value": "Hello!"
      },
      "groupID": "612555152",
      "platform": "other",
      "errors": [
        {
          "data": {
            "name": "timestamp",
            "value": "2018-07-16T00:00:00+02:00"
          },
          "message": "Discarded invalid value for parameter 'timestamp'",
          "type": "invalid_data"
        },
        {
          "data": {
            "name": "event_id",
            "value": "\"abcd\""
          },
          "message": "Discarded invalid value for parameter 'event_id'",
          "type": "invalid_data"
        }
      ],
      "context": {},
      "entries": [
        {
          "type": "exception",
          "data": {
            "values": [
              {
                "value": "Hello!",
                "type": "SyntaxError"
              }
            ],
            "hasSystemFrames": false
          }
        }
      ],
      "message": "SyntaxError Hello! \"myself\"",
      "sdk": {
        "version": "1.0.0",
        "name": "komand",
        "upstream": {
          "isNewer": false,
          "name": "komand"
        }
      },
      "type": "error",
      "id": "25152283073",
      "size": 410
    }
  ]
}

```

### Update Issue

This action is used to update an individual issues's attributes (only the attributes submitted are modified).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|False|The new status for the issue. Valid values are 'resolved', 'resolvedInNextRelease', 'unresolved', and 'ignored'|['resolved', 'resolvedInNextRelease', 'unresolved', 'ignored']|
|assignedTo|string|None|False|The actor ID (or username) of the user or team that should be assigned to this issue|None|
|hasSeen|boolean|None|False|In case this API call is invoked with a user context this allows changing of the flag that indicates if the user has seen the event|None|
|issue_id|string|None|True|The ID of the group to retrieve|None|
|isSubscribed|boolean|None|False||None|
|isPublic|boolean|None|False|Sets the issue to public or private|None|
|isBookmarked|boolean|None|False|In case this API call is invoked with a user context this allows changing of the bookmark flag|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|Issue|False|Updated issue|

Example output:

```

{
  "issue": {
    "lastSeen": "2018-07-18T19:31:13Z",
    "numComments": 0,
    "userCount": 0,
    "title": "SyntaxError: Wattttt! AHAHAH",
    "id": "612424900",
    "type": "error",
    "annotations": [],
    "metadata": {
      "type": "SyntaxError",
      "value": "Wattttt! AHAHAH"
    },
    "status": "resolved",
    "subscriptionDetails": {
      "reason": "unknown"
    },
    "isPublic": true,
    "hasSeen": true,
    "shortId": "PYTHONTEST-4",
    "shareId": "0dea15d594a94880bc2016b0e5e498ec",
    "firstSeen": "2018-07-18T16:51:40Z",
    "count": "3",
    "permalink": "https://sentry.io/komand-test/pythontest/issues/612424900/",
    "level": "error",
    "isSubscribed": true,
    "isBookmarked": true,
    "project": {
      "slug": "pythontest",
      "id": "1244809",
      "name": "PythonTest"
    },
    "statusDetails": {}
  }
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|credential_token|None|True|Sentry Auth Token|None|

## Troubleshooting

Make sure that you are using the correct Auth Token (for all actions) and DSN configuration (for submitting an event).
You can find the [https://sentry.io/settings/{organization_slug}/{project_slug}/keys/](DNS configuration) and [https://sentry.io/settings/account/api/auth-tokens/](Auth Tokens), respectively.

## Versions

* 1.0.0 - Initial plugin

## Workflows

Examples:

* Submiting new Sentry events when a step fails
* Resolving existing Sentry issues when a step succeeds

## References

* [Submit Event](https://docs.sentry.io/clientdev/overview/#a-working-example)
* [Update Issue](https://docs.sentry.io/api/events/put-group-details/)
* [List Project Issues](https://docs.sentry.io/api/events/get-project-group-index/)
* [List Issue Events](https://docs.sentry.io/api/events/get-group-events/)
