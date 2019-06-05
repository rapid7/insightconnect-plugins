# Microsoft Office 365 ATP Safe Links

## About

[Microsoft ATP Safe Links](https://docs.microsoft.com/en-us/office365/securitycompliance/atp-safe-links) is a service that helps protect your organization by providing time-of-click verification of web addresses (URLs) in email messages and Office documents.

## Actions

### Decode Safe Links

This action is used to decode a Microsoft Safe Link.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Safe Link to be decoded|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|True|Result of the decoded Safe Link|

Example output:

```
{
  "result":"https://aomediacodec.github.io/av1-spec/av1-spec.pdf"
}
```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 1.0.0 - Initial plugin

## Workflows

Examples:

* Decode Safe Link for further enrichment of the URL

## References

* [Microsoft ATP Safe Links](https://docs.microsoft.com/en-us/office365/securitycompliance/atp-safe-links)
