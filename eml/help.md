
# EML

## About

Extract information from EML files.

## Actions

### Parse EML File

This action is used to extract headers and file attachments.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|eml_file|bytes|None|True|EML File|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|result|False|None|

Example output:

```

{
  {
    "to": "bob@komand.com",
    "from": "Amazon Web Services <aws-receivables-support@email.amazon.com>",
    "subject": "Amazon Web Services Invoice Available "
    "date": "Wed, 3 May 2017 18:29:19 +0000",
    "headers": [
      {
        "key": "Delivered-To",
        "value": "bob@komand.com"
      },
      {
        "key": "Received",
        "value": "by 10.107.15.41 with SMTP id x41csp196334ioi;\n        Wed, 3 May 2017 11:29:23 -0700 (PDT)"
      },
      {
        "key": "X-Received",
        "value": "by 10.129.177.72 with SMTP id p69mr4072825ywh.184.1493836163402;\n        Wed, 03 May 2017 11:29:23 -0700 (PDT)"
      },
      ...
    ],
    "attachments": [
      {
        "contents": "base64_encoded_bytes",
        "filename": "invoice.pdf",
      },
      {
        "contents": "base64_encoded_bytes",
        "filename": "agreement.pdf",
      }
    ]
  }
}

```

### Parse EML File from String

This action is used to extract headers and file attachments from a string.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|eml_file|string|None|True|EML File string|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|result|False|Contents of parsed EML file|

Example output:

```
{
  {
    "to": "bob@komand.com",
    "from": "Amazon Web Services <aws-receivables-support@email.amazon.com>",
    "subject": "Amazon Web Services Invoice Available "
    "date": "Wed, 3 May 2017 18:29:18 +0000",
    "headers": [
      {
        "key": "Delivered-To",
        "value": "bob@komand.com"
      },
      {
        "key": "Received",
        "value": "by 10.107.15.41 with SMTP id x41csp196334ioi;\n        Wed, 3 May 2017 11:29:23 -0700 (PDT)"
      },
      {
        "key": "X-Received",
        "value": "by 10.129.177.72 with SMTP id p69mr4072825ywh.184.1493836163402;\n        Wed, 03 May 2017 11:29:23 -0700 (PDT)"
      },
      ...
    ],
    "attachments": [
      {
        "contents": "base64_encoded_bytes",
        "filename": "invoice.pdf",
      },
      {
        "contents": "base64_encoded_bytes",
        "filename": "agreement.pdf",
      }
    ]
  }
}
```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

* Email parsing

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 0.1.2 - Bug fix body parsing | Updated to v2 architecture
* 0.1.3 - Bug fix for unicode chars and attached emails
* 0.1.4 - Bug fix for emails with no To
* 0.1.5 - Bug fix improved handling of HTML bodies
* 0.1.6 - Bug fix for CI tool incorrectly uploading plugins
* 0.1.7 - Bug fix for better UTF-8 encoding support
* 1.0.0 - Support web server mode
* 1.1.0 - New action Parse EML File from String
* 1.1.1 - Fix issue where plugin would fail on empty date returned

## References

* [EML](http://forensicswiki.org/wiki/EML)
* [RFC0822](https://www.ietf.org/rfc/rfc0822.txt)
