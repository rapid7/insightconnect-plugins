# Chardet

## About

[Chardet](https://chardet.readthedocs.io/en/latest/index.html) is a python compatible character encoding detector.

## Actions

### Detect Encoding

This action is used to detect encoding.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|bytes_to_analyze|bytes|None|True|Bytes to analyze|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|recommendation|recommendation|False|Recommendation|

Example output:

```
{
  "recommendation": {
    "encoding": "Windows-1254",
    "confidence": 0.2105891645091143,
    "language": "Turkish"
  }
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

_This plugin does not contain a connection._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Find encoding of unknown set of bytes

## Versions

* 1.0.0 - Initial plugin

## References

* [Chardet](https://chardet.readthedocs.io/en/latest/index.html)
* [How it Works](https://chardet.readthedocs.io/en/latest/how-it-works.html)

## Custom Output Types

### recommendation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|confidence|number|False|Confidence|
|encoding|string|False|Encoding|
|language|string|False|Language|
