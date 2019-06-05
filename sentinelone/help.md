# SentinelOne

## About

[SentinelOne](https://www.sentinelone.com/) is a next-gen cybersecurity company focused on protecting the enterprise through the endpoint.

This plugin utilizes the [SentinelOne API](https://usea1-partners.sentinelone.net/apidoc/).

## Actions

### Get Threat Summary

This action is used to get a summary of all threats.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|pagination|pagination|False|Pagination|
|errors|[]object|False|Errors|
|data|[]data|False|Data|

Example output:

```
{
  'data':[
      {
        'agentComputerName':'vagrant-pc',
        'agentDomain':'WORKGROUP',
        'agentId':'560700200554747611',
        'agentInfected':False,
        'agentIp':'xxx.xxx.xxx.xxx',
        'agentIsActive':True,
        'agentIsDecommissioned':False,
        'agentMachineType':'desktop',
        'agentNetworkStatus':'connected',
        'agentOsType':'windows',
        'agentVersion':'3.0.1.3',
        'annotation':None,
        'annotationUrl':None,
        'browserType':None,
        'certId':'',
        'classification':'Malware',
        'classificationSource':'Engine',
        'classifierName':'BLACKLIST',
        'cloudVerdict':'black',
        'collectionId':'433377870883088367',
        'createdAt':'2019-02-13T15:05:21.948892Z',
        'createdDate':'2019-02-13T15:05:21.605000Z',
        'description':'malware detected - not mitigated yet (static engine)',
        'engines':[
            'reputation'
        ],
        'fileContentHash':'3395856ce81f2b7382dee72602f798b642f14140',
        'fileCreatedDate':None,
        'fileDisplayName':'{D5EEFA7C-3EA6-4B78-BED3-56CB49156FD1}-EICAR.com',
        'fileExtensionType':'Executable',
        'fileIsDotNet':None,
        'fileIsExecutable':False,
        'fileIsSystem':False,
        'fileMaliciousContent':None,
        'fileObjectId':'49E6C98245C9F0D8',
        'filePath':'\\Device\\HarddiskVolume2\\ProgramData\\Microsoft\\Windows Defender\\LocalCopy\\{D5EEFA7C-3EA6-4B78-BED3-56CB49156FD1}-EICAR.com',
        'fileSha256':None,
        'fileVerificationType':'NotSigned',
        'fromCloud':False,
        'fromScan':False,
        'id':'560707325754496894',
        'indicators':[

        ],
        'isCertValid':False,
        'isInteractiveSession':False,
        'isPartialStory':False,
        'maliciousGroupId':'B5930C761E06E0CD',
        'maliciousProcessArguments':None,
        'markedAsBenign':None,
        'mitigationMode':'protect',
        'mitigationReport':{
            'kill':{
              'status':'success'
            },
            'network_quarantine':{
              'status':None
            },
            'quarantine':{
              'status':'success'
            },
            'remediate':{
              'status':None
            },
            'rollback':{
              'status':None
            }
        },
        'mitigationStatus':'mitigated',
        'publisher':'',
        'rank':7,
        'resolved':False,
        'siteId':'521580416395045459',
        'siteName':'Rapid7',
        'threatAgentVersion':'3.0.1.3',
        'threatName':None,
        'updatedAt':'2019-02-13T15:05:22.274291Z',
        'username':'',
        'whiteningOptions':[
            'hash'
        ]
      }
  ],
  'pagination':{
      'nextCursor':None,
      'totalItems':1
  }
}
```

### Blacklist by Content Hash

This action is used to add hashed content to global blacklist. The input for this action makes use of `contentHash` from the threat summary.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|Content hash to add to blacklist|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|blacklist_data|True|Result of hashing operation|

Example output:

```
{
  "blacklist_data": {
    "affected": 127
  }
}
```

### Blacklist by IoC Hash

This action is used to add hashed indicator of compromise to global blacklist.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|Indicator of compromise hash to add to blacklist|None|
|agent_id|string|None|True|Agent ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|blacklist_data|True|Result of hashing operation|

Example output:

```
{
  "blacklist_data": {
    "affected": 127
  }
}
```

### Mitigate Threat

This action is used to apply a mitigation action to a threat.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|action|string|None|True|Mitigation action|['rollback-remediation', 'quarantine', 'kill', 'remediate', 'un-quarantine']|
|threat_id|string|None|True|ID of a threat|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

### Mark as Benign

This action is used to mark a threat as resolved.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|threat_id|string|None|True|ID of a threat|None|
|whitening_option|string|None|False|Selected whitening option|['browser-type', 'certificate', 'file-type', 'file_hash', 'path']|
|target_scope|string|None|True|Scope to be used for exclusions|['group', 'site', 'tenant']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

### Create IOC Threat

This action is used to create a threat from an IOC event.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_id|string|None|False|Group ID|None|
|hash|string|None|True|SHA1 hash|None|
|agent_id|string|None|True|Agent ID for the slim threat|None|
|path|string|None|False|Path|None|
|annotation_url|string|None|True|Vigilance annotation URL|None|
|annotation|string|None|True|Vigilance annotation|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

### Mark as Threat

This action is used to mark a suspicious threat as a threat.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|threat_id|string|None|True|ID of a threat|None|
|whitening_option|string|None|False|Selected whitening option|['browser-type', 'certificate', 'file-type', 'file_hash', 'path']|
|target_scope|string|None|True|Scope to be used for exclusions|['group', 'site', 'tenant']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

## Triggers

### Get Threats

This trigger is used to get threats.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|resolved|boolean|None|False|Include resolved threats|None|
|agent_is_active|boolean|None|False|Include agents currently connected to the management console|None|
|frequency|integer|5|False|Poll frequency in seconds|None|
|classifications|[]string|None|False|List of classifications to search|None|
|engines|[]string|None|False|Included engines|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threat|data|False|Threat|

Example output:

```
{
  'threat': {
    'agentComputerName':'vagrant-pc',
    'agentDomain':'WORKGROUP',
    'agentId':'560700200554747611',
    'agentInfected':False,
    'agentIp':'xxx.xxx.xxx.xxx',
    'agentIsActive':True,
    'agentIsDecommissioned':False,
    'agentMachineType':'desktop',
    'agentNetworkStatus':'connected',
    'agentOsType':'windows',
    'agentVersion':'3.0.1.3',
    'annotation':None,
    'annotationUrl':None,
    'browserType':None,
    'certId':'',
    'classification':'Malware',
    'classificationSource':'Engine',
    'classifierName':'BLACKLIST',
    'cloudVerdict':'black',
    'collectionId':'433377870883088367',
    'createdAt':'2019-02-13T15:05:21.948892Z',
    'createdDate':'2019-02-13T15:05:21.605000Z',
    'description':'malware detected - not mitigated yet (static engine)',
    'engines':[
        'reputation'
    ],
    'fileContentHash':'3395856ce81f2b7382dee72602f798b642f14140',
    'fileCreatedDate':None,
    'fileDisplayName':'{D5EEFA7C-3EA6-4B78-BED3-56CB49156FD1}-EICAR.com',
    'fileExtensionType':'Executable',
    'fileIsDotNet':None,
    'fileIsExecutable':False,
    'fileIsSystem':False,
    'fileMaliciousContent':None,
    'fileObjectId':'49E6C98245C9F0D8',
    'filePath':'\\Device\\HarddiskVolume2\\ProgramData\\Microsoft\\Windows Defender\\LocalCopy\\{D5EEFA7C-3EA6-4B78-BED3-56CB49156FD1}-EICAR.com',
    'fileSha256':None,
    'fileVerificationType':'NotSigned',
    'fromCloud':False,
    'fromScan':False,
    'id':'560707325754496894',
    'indicators':[

    ],
    'isCertValid':False,
    'isInteractiveSession':False,
    'isPartialStory':False,
    'maliciousGroupId':'B5930C761E06E0CD',
    'maliciousProcessArguments':None,
    'markedAsBenign':None,
    'mitigationMode':'protect',
    'mitigationReport':{
        'kill':{
          'status':'success'
        },
        'network_quarantine':{
          'status':None
        },
        'quarantine':{
          'status':'success'
        },
        'remediate':{
          'status':None
        },
        'rollback':{
          'status':None
        }
    },
    'mitigationStatus':'mitigated',
    'publisher':'',
    'rank':7,
    'resolved':False,
    'siteId':'521580416395045459',
    'siteName':'Rapid7',
    'threatAgentVersion':'3.0.1.3',
    'threatName':None,
    'updatedAt':'2019-02-13T15:05:22.274291Z',
    'username':'',
    'whiteningOptions':[
        'hash'
    ]
  }
}
```

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Username and password|None|
|url|string|https\://usea1-partners.sentinelone.net/|True|URL and endpoint of SentinelOne instance. For example\: https\://usea1-partners.sentinelone.net/|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Update to add Blacklist by IoC Hash and Blacklist by Content Hash
* 1.1.0 - New trigger Get Threats | New actions Mitigate Threat, Mark as Benign, Mark as Threat and Create IOC Threat

## Workflows

Examples:

* Get a summary of all threats for further analysis
* Blacklist a file by its hash

## References

* [SentinelOne Product Page](https://www.sentinelone.com/)
* [SentinelOne API](https://usea1-partners.sentinelone.net/apidoc/)
