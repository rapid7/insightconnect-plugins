# Microsoft Teams

## About

[Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software) is a unified communications platform that combines persistent workplace chat, video meetings, file storage, and application integration.

This plugin uses [webhooks](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/connectors/connectors-using) to send messages to an instance of Microsoft Teams.

## Actions

### Send message

This action is used to send a message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|True|Message to send|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was send successful|

Example output:

```
{
  "success": true
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|webhook|string|None|True|Webhook|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Send message to Microsoft Teams

## Versions

* 1.0.0 - Initial plugin

## References

* [Microsoft Teams](LINK TO PRODUCT/VENDOR WEBSITE)

## Custom Output Types

_This plugin does not contain any custom output types._
