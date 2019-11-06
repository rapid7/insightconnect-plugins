# Description

[Facebook Threat Exchange](https://developers.facebook.com/docs/threat-exchange/) is a platform for sharing threat information between selected entities.
This plugin utilizes the [Threat Exchange API](https://developers.facebook.com/docs/threat-exchange/v2.11).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|secret_key|credential_secret_key|None|True|Secret to Facebook application e.g 3ef3234587654093fc954381043fc348|None|
|app_id|string|None|False|Facebook application ID e.g 1234567890123456|None|

## Technical Details

### Actions

#### Threat Descriptors Search

This action is used to enable searching for subjective opinions on indicators of compromise stored in Threat Exchange.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|False|A description of the maliciousness [status](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type) of any object within ThreatExchange|['', 'UNKNOWN', 'NON_MALICIOUS', 'SUSPICIOUS', 'MALICIOUS']|
|min_confidence|integer|None|False|Define the minimum allowed confidence value for the data returned|None|
|tags|[]string|None|False|Comma separated list of tags to filter results|None|
|text|string|None|False|Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects|None|
|review_status|string|None|False|A given [ReviewStatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type)|['', 'UNKNOWN', 'UNREVIEWED', 'PENDING', 'REVIEWED_MANUALLY', 'REVIEWED_AUTOMATICALLY']|
|share_level|string|None|False|The following [Share Level Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type) designations are based on the [US-CERT's Traffic Light Protocol](https://www.us-cert.gov/tlp/) and govern how ThreatData may be re-shared both within and outside of ThreatExchange|['', 'RED', 'AMBER', 'GREEN', 'WHITE']|
|max_confidence|integer|None|False|Define the maximum allowed confidence value for the data returned|None|
|strict_text|boolean|None|False|When set to 'true', the API will not do approximate matching on the value in text|None|
|owner|[]string|None|False|Comma separated list of AppIDs of the person who submitted the data|None|
|include_expired|boolean|False|False|When set to true, the API can return data which has expired|None|
|fields|[]string|None|False|A list of fields to return in the response|None|
|since|string|None|False|Returns descriptors collected after a timestamp|None|
|sort_by|string|None|False|Sort search results by RELEVANCE or by CREATE_TIME. When sorting by RELEVANCE, your query will return results sorted by similarity against your text query|['', 'RELEVANCE', 'CREATE_TIME']|
|sort_order|string|None|False|An ordering with which to [sort](https://developers.facebook.com/docs/threat-exchange/reference/apis/sort-order-type) ThreatExchange results|['', 'ASCENDING', 'DESCENDING']|
|limit|integer|None|False|Defines the maximum size of a page of result|None|
|type|string|None|False|The [type](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type/) of descriptor to search for|['', 'ADJUST_TOKEN', 'API_KEY', 'AS_NUMBER', 'BANNER', 'CMD_LINE', 'COOKIE_NAME', 'CRX', 'DEBUG_STRING', 'DEST_PORT', 'DIRECTORY_QUERIED', 'DOMAIN', 'EMAIL_ADDRESS', 'FILE_CREATED', 'FILE_DELETED', 'FILE_MOVED', 'FILE_NAME', 'FILE_OPENED', 'FILE_READ', 'FILE_WRITTEN', 'GET_PARAM', 'HASH_IMPHASH', 'HASH_MD5', 'HASH_SHA1', 'HASH_SHA256', 'HASH_SSDEEP', 'HTML_ID', 'HTTP_REQUEST', 'IP_ADDRESS', 'IP_SUBNET', 'ISP', 'LATITUDE', 'LAUNCH_AGENT', 'LOCATION', 'LONGITUDE', 'MALWARE_NAME', 'MEMORY_ALLOC', 'MEMORY_PROTECT', 'MEMORY_WRITTEN', 'MUTANT_CREATED', 'MUTEX', 'NAME_SERVER', 'OTHER_FILE_OP', 'PASSWORD', 'PASSWORD_SALT', 'PAYLOAD_DATA', 'PAYLOAD_TYPE', 'POST_DATA', 'PROTOCOL', 'REFERER', 'REGISTRAR', 'REGISTRY_KEY', 'REG_KEY_CREATED', 'REG_KEY_DELETED', 'REG_KEY_ENUMERATED', 'REG_KEY_MONITORED', 'REG_KEY_OPENED', 'REG_KEY_VALUE_CREATED', 'REG_KEY_VALUE_DELETED', 'REG_KEY_VALUE_MODIFIED', 'REG_KEY_VALUE_QUERIED', 'SIGNATURE', 'SOURCE_PORT', 'TELEPHONE', 'URI', 'USER_AGENT', 'VOLUME_QUERIED', 'WEBSTORAGE_KEY', 'WEB_PAYLOAD', 'WHOIS_NAME', 'WHOIS_ADDR1', 'WHOIS_ADDR2', 'XPI']|
|until|string|None|False|Returns descriptors collected before a timestamp |None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|paging|paging|True|Paging Information|
|data|[]descriptor_data|True|Information around the indicator such as the Indicator, Type and ID|

#### Threat Indicator Search

This action is used to search for indicators of compromise stored in Threat Exchange.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|text|string|None|False|Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects|None|
|threat_type|string|None|False|The broad [threat type](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-type/) the indicator is associated with|['', 'ADJUST_TOKEN', 'API_KEY', 'AS_NUMBER', 'BANNER', 'CMD_LINE', 'COOKIE_NAME', 'CRX', 'DEBUG_STRING', 'DEST_PORT', 'DIRECTORY_QUERIED', 'DOMAIN', 'EMAIL_ADDRESS', 'FILE_CREATED', 'FILE_DELETED', 'FILE_MOVED', 'FILE_NAME', 'FILE_OPENED', 'FILE_READ', 'FILE_WRITTEN', 'GET_PARAM', 'HASH_IMPHASH', 'HASH_MD5', 'HASH_SHA1', 'HASH_SHA256', 'HASH_SSDEEP', 'HTML_ID', 'HTTP_REQUEST', 'IP_ADDRESS', 'IP_SUBNET', 'ISP', 'LATITUDE', 'LAUNCH_AGENT', 'LOCATION', 'LONGITUDE', 'MALWARE_NAME', 'MEMORY_ALLOC', 'MEMORY_PROTECT', 'MEMORY_WRITTEN', 'MUTANT_CREATED', 'MUTEX', 'NAME_SERVER', 'OTHER_FILE_OP', 'PASSWORD', 'PASSWORD_SALT', 'PAYLOAD_DATA', 'PAYLOAD_TYPE', 'POST_DATA', 'PROTOCOL', 'REFERER', 'REGISTRAR', 'REGISTRY_KEY', 'REG_KEY_CREATED', 'REG_KEY_DELETED', 'REG_KEY_ENUMERATED', 'REG_KEY_MONITORED', 'REG_KEY_OPENED', 'REG_KEY_VALUE_CREATED', 'REG_KEY_VALUE_DELETED', 'REG_KEY_VALUE_MODIFIED', 'REG_KEY_VALUE_QUERIED', 'SIGNATURE', 'SOURCE_PORT', 'TELEPHONE', 'URI', 'USER_AGENT', 'VOLUME_QUERIED', 'WEBSTORAGE_KEY', 'WEB_PAYLOAD', 'WHOIS_NAME', 'WHOIS_ADDR1', 'WHOIS_ADDR2', 'XPI']|
|since|date|None|False|Returns indicators collected after a timestamp|None|
|sort_by|string|None|False|Sort results by Relevance, create_time |['RELEVANCE', 'CREATE_Time']|
|sort_order|string|None|False|[Sorts](https://developers.facebook.com/docs/threat-exchange/reference/apis/sort-order-type) responses by ascending or descending|['ASCENDING', 'DESCENDING']|
|strict_text|boolean|False|False|When set to 'true', the API will not do approximate matching on the value in text|None|
|limit|string|None|False|Defines the maximum size of a page of results. The maximum is 1,000|None|
|type|string|None|False|The type of indicators to search for [IndicatorTypes](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type/)|['', 'ADJUST_TOKEN', 'API_KEY', 'AS_NUMBER', 'BANNER', 'CMD_LINE', 'COOKIE_NAME', 'CRX', 'DEBUG_STRING', 'DEST_PORT', 'DIRECTORY_QUERIED', 'DOMAIN', 'EMAIL_ADDRESS', 'FILE_CREATED', 'FILE_DELETED', 'FILE_MOVED', 'FILE_NAME', 'FILE_OPENED', 'FILE_READ', 'FILE_WRITTEN', 'GET_PARAM', 'HASH_IMPHASH', 'HASH_MD5', 'HASH_SHA1', 'HASH_SHA256', 'HASH_SSDEEP', 'HTML_ID', 'HTTP_REQUEST', 'IP_ADDRESS', 'IP_SUBNET', 'ISP', 'LATITUDE', 'LAUNCH_AGENT', 'LOCATION', 'LONGITUDE', 'MALWARE_NAME', 'MEMORY_ALLOC', 'MEMORY_PROTECT', 'MEMORY_WRITTEN', 'MUTANT_CREATED', 'MUTEX', 'NAME_SERVER', 'OTHER_FILE_OP', 'PASSWORD', 'PASSWORD_SALT', 'PAYLOAD_DATA', 'PAYLOAD_TYPE', 'POST_DATA', 'PROTOCOL', 'REFERER', 'REGISTRAR', 'REGISTRY_KEY', 'REG_KEY_CREATED', 'REG_KEY_DELETED', 'REG_KEY_ENUMERATED', 'REG_KEY_MONITORED', 'REG_KEY_OPENED', 'REG_KEY_VALUE_CREATED', 'REG_KEY_VALUE_DELETED', 'REG_KEY_VALUE_MODIFIED', 'REG_KEY_VALUE_QUERIED', 'SIGNATURE', 'SOURCE_PORT', 'TELEPHONE', 'URI', 'USER_AGENT', 'VOLUME_QUERIED', 'WEBSTORAGE_KEY', 'WEB_PAYLOAD', 'WHOIS_NAME', 'WHOIS_ADDR1', 'WHOIS_ADDR2', 'XPI']|
|until|date|None|False|Returns indicators collected before a timestamp|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|fields|[]string|False|A list of fields to return in the response|
|paging|paging|True|Paging Information|
|data|[]data|True|Information around the indicator such as the Indicator, Type and ID|

#### Submit Descriptors

This action is used to submit data to Facebook's graph API.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|True|Indicates if the indicator is labeled as malicious|None|
|first_active|date|None|False|Time when the opinion first became valid|None|
|description|string|None|True|A short summary of the indicator and threat|None|
|last_active|date|None|False|Time when the opinion  became valid|None|
|tags|[]string|None|False|A comma separated list of tags you want to publish. This will overwrite any existing tags|None|
|add_tags|string|None|False|To add tags to an object without overwriting existing tags|None|
|review_status|string|None|False|Describes how the indicator was vetted, see [ReviewStatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type) for the list of allowed values|['', 'UNKNOWN', 'UNREVIEWED', 'PENDING', 'REVIEWED_MANUALLY', 'REVIEWED_AUTOMATICALLY']|
|indicator|string|None|True|The indicator data being submitted|None|
|precision|string|None|False|[Precision](https://developers.facebook.com/docs/threat-exchange/reference/apis/precision-type) is the degree of accuracy of the indicator|['', 'UNKNOWN', 'LOW', 'MEDIUM', 'HIGH']|
|privacy_members|[]string|None|False|A comma-delimited list of [ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) allowed to see the indicator and only applies when privacy_type is set to HAS_WHITELIST|None|
|share_level|string|None|True|The following Share Level Type designations are based on the US-CERT's Traffic Light Protocol and govern how ThreatData may be re-shared both within and outside of ThreatExchange|['RED', 'AMBER', 'GREEN', 'WHITE']|
|confidence|integer|None|False|A score for how likely the indicator's status is accurate, ranges from 0 to 100|None|
|severity|string|None|False|[Severity](https://developers.facebook.com/docs/threat-exchange/reference/apis/severity-type) is a description of the dangerousness of the threat associated with a ThreatIndicator object|['', 'UNKNOWN', 'INFO', 'WARNING', 'SUSPICIOUS', 'SEVERE', 'APOCALYPSE']|
|expired_on|date|None|False|Time the indicator is no longer considered a threat, in ISO 8601 date format|None|
|privacy_type|string|None|True|[Privacy Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type) is the kind of privacy for the indicator|['', 'HAS_PRIVACY_GROUP', 'HAS_WHITELIST', 'VISIBLE']|
|remove_tags|string|None|False|Remove tags associated with an object|None|
|type|string|None|True|The kind of indicator being described, see [IndicatorType](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type) for the list of allowed values|['ADJUST_TOKEN', 'API_KEY', 'AS_NUMBER', 'BANNER', 'CMD_LINE', 'COOKIE_NAME', 'CRX', 'DEBUG_STRING', 'DEST_PORT', 'DIRECTORY_QUERIED', 'DOMAIN', 'EMAIL_ADDRESS', 'FILE_CREATED', 'FILE_DELETED', 'FILE_MOVED', 'FILE_NAME', 'FILE_OPENED', 'FILE_READ', 'FILE_WRITTEN', 'GET_PARAM', 'HASH_IMPHASH', 'HASH_MD5', 'HASH_SHA1', 'HASH_SHA256', 'HASH_SSDEEP', 'HTML_ID', 'HTTP_REQUEST', 'IP_ADDRESS', 'IP_SUBNET', 'ISP', 'LATITUDE', 'LAUNCH_AGENT', 'LOCATION', 'LONGITUDE', 'MALWARE_NAME', 'MEMORY_ALLOC', 'MEMORY_PROTECT', 'MEMORY_WRITTEN', 'MUTANT_CREATED', 'MUTEX', 'NAME_SERVER', 'OTHER_FILE_OP', 'PASSWORD', 'PASSWORD_SALT', 'PAYLOAD_DATA', 'PAYLOAD_TYPE', 'POST_DATA', 'PROTOCOL', 'REFERER', 'REGISTRAR', 'REGISTRY_KEY', 'REG_KEY_CREATED', 'REG_KEY_DELETED', 'REG_KEY_ENUMERATED', 'REG_KEY_MONITORED', 'REG_KEY_OPENED', 'REG_KEY_VALUE_CREATED', 'REG_KEY_VALUE_DELETED', 'REG_KEY_VALUE_MODIFIED', 'REG_KEY_VALUE_QUERIED', 'SIGNATURE', 'SOURCE_PORT', 'TELEPHONE', 'URI', 'USER_AGENT', 'VOLUME_QUERIED', 'WEBSTORAGE_KEY', 'WEB_PAYLOAD', 'WHOIS_NAME', 'WHOIS_ADDR1', 'WHOIS_ADDR2', 'XPI']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|Identifier for the submission made|
|success|boolean|False|Returns true if submission was successful|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Facebook](https://facebook.com)
* [Facebook Threat Exchange API](https://developers.facebook.com/docs/threat-exchange/)
* [Indicator Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type/)
* [Status Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type)
* [Review Status Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type)
* [Share Level Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type)
* [Sort Order Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/sort-order-type)
* [Threat Types](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-type/)
* [Percision Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/precision-type)
* [Privacy Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type)
* [Privacy Members](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member)
* [Severity Type](https://developers.facebook.com/docs/threat-exchange/reference/apis/severity-type)

