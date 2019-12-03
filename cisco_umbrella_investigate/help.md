# Description

[Cisco Umbrella Enforcement](https://docs.umbrella.com/developer/networkdevices-api/) allows partners and customers with their own homegrown SIEM/Threat Intelligence Platform (TIP) environments to inject events and/or threat intelligence into their Umbrella environment. These events are then instantly converted into visibility and enforcement that can extend beyond the perimeter and thus the reach of the systems that might have generated those events or threat intelligence.
The Cisco Umbrella Enforcement InsightConnect plugin allows you to lookup sample artifacts, sample connections, sample samples, WHOIS details, IP and domain history etc.
This plugin utilizes the [Python OpenDNS Investigate](https://github.com/opendns/pyinvestigate) library.

# Key Features

* Retrieve details of sample artifacts, sample connections, sample samples
* Retrieve WHOIS details by email, domain and name server
* Retrieve IP's and domain's history
* Retrieve domain's security features, content category, security category

# Requirements

* Cisco Umbrella Investigate API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|Enter API key e.g. 1111-2222-3333-4444|None|

The API key is a UUID-v4 [customer key](https://docs.umbrella.com/developer/enforcement-api/authentication-and-versioning/).

## Technical Details

### Actions

#### DNS RR History for IP Address

This action is used to return the history that umbrella has seen for a given IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|IP|string|None|True|IP address|None|
|type|string|None|False|DNS record query type (A, NS, MX, TXT and CNAME are supported)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rrs|[]ip_resource_record|True|None|
|features|[]ip_feature|True|None|

#### WHOIS by Nameserver

This action is used to allows you to search a nameserver to find all domains registered by that nameserver.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|nameserver|string|None|True|Nameserver's domain name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain|[]email_whois|True|Array of WHOIS results for the domain provided with all available information|

#### Co-occurrences for a Domain

This action is used to return co-occurences for the specified domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cooccurrences|array|True|Array of [domain name, scores] tuples. The values range between 0 and 1 and should not exceed 1. All co-occurences of requests from client IPs are returned for the previous seven days whether the co-occurence is suspicious or not|

#### WHOIS by Domain

This action is used to a standard WHOIS response record for a single domain with all available WHOIS data returned in an array.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name without wildcards and including TLD|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|whois|array|True|Array of WHOIS results for the domain provided with all available information|

#### Related Domains

This action is used to returns a list of domain names that have been frequently seen.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|related|array|True|Array of [domain name, scores] tuples where the score is the number of client IP requests to the site in 60 seconds from the time of the original lookup request|

#### File Sample

This action is used to return a file, or a file-like object, such as a process running in memory.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|Search sample by hash (SHA-256, SHA-1 or MD5)|None|
|limit|string|None|False|Default of 10, can be extended for a larger data set|None|
|offset|string|None|False|The offset of the individual entities in the query's response, used for pagination|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sample|sample_info|False|None|

#### DNS RR History

This action is used to return the history that Umbrella has seen for a given domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name|None|
|type|string|None|False|DNS record query type (A, NS, MX, TXT and CNAME are supported)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|features|[]feature|True|None|
|rrs_tf|[]resource_record|True|RRS TF|

#### Latest Malicious Domains by IP

This action is used to return associated malicious domains for an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|IP|string|None|True|IP Address to check for malicious domains|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]string|True|The block list domain associated with the IP|

#### Sample Artifacts

This action is used to return artifacts which are files created or modified during a sample analysis.
*Note:* Only Threat Grid customers have access to artifact data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|Search sample by hash (SHA-256, SHA-1 or MD5)|None|
|limit|string|None|False|Default of 10, can be extended for a larger data set|None|
|offset|string|None|False|Used to paginate between sets of data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|artifacts|array|True|None|

#### WHOIS Information by Email

This action is used to returns the WHOIS information for the specified email address(es), nameserver(s) and domains.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email address following rfc5322 conventions|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email_whois|[]email_whois|True|Domains registered by this email address|

#### Sample Connections

This action is used to return network activity information associated with a sample.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|Search sample by hash (SHA-256, SHA-1 or MD5)|None|
|limit|string|None|False|Default of 10, can be extended for a larger data set|None|
|offset|string|None|False|Used to paginate between sets of data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|connections|array|True|None|

#### Pattern Search

This action is used to the pattern search functionality in investigate uses regular expressions (regex) to search against the investigate database.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|start|string|None|True|If specifying in absolute, use millisecond timestamp within the last 30 days as the Start. If specifying in relative, use either seconds, minutes, hours, days or weeks with a minus sign in front. As an example -1days, -1000minutes|None|
|expression|string|None|True|A standard RegEx pattern search|None|
|limit|integer|None|False|Default is 1000, limit request response|None|
|include_category|boolean|None|False|Default is false, if set to true this will include security categories in the results and may slow the return times|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|matches|array|True|Each match will contain the name of the domain matches, the and the first seen time, both in Epoch and ISO time format. This endpoint returns the security categories as strings rather than integers (eg: 'malware','botnet', etc) if includeCategory is true|
|limit|integer|True|Default is 100, can be expanded to 1000 which is the maximum number of results for this endpoint|
|totalResults|integer|True|Total results from this search string. The default number of results is 100 and can be expanded using the limit parameter|
|expression|string|True|This is the RegEx in the query as seen from the API. If results from your query do not match what you may have expected, check to see that the RegEx matches the one you tried to enter and that characters are correctly escaped in the query string|
|moreDataAvailable|boolean|True|Whether more data is available than what is displayed. Will be true if totalResults exceed limit. We recommend refining your filter if this value is true|

#### Domain Status and Categorization

This action is used to return if domain has been flagged as malicious by the cisco security labs team.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domains|[]string|None|True|Domain names|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|categories|[]category|True|Information about content categories and security categories|

#### Domain Tags

This action is used to returns the date range when the domain being queried was a part of the umbrella block list.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain_tags|[]tag_date|True|Date range for which this domain has been in the block list, domain tag such as malware or phishing, identifying the security category of the domain, if available or possible, list the specific URL hosting the malicious content|

#### Samples by Domain

This action is used to return all samples associated with the domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|URL|string|None|True|Search sample by domain, IP or URL|None|
|limit|string|None|False|The number of responses; default of 10 as a limit on response, can be extended|None|
|sortby|string|None|False|Default is score. Choose from ['first-seen', 'last-seen', 'score']. 'first-seen' sorts the samples in date descending order. 'last-seen' sorts the samples in ascending order. 'score' sorts the samples by the ThreatScore|None|
|offset|string|None|False|Default to 0, used to pagination between sets of data if limit is exceeded|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|limit|integer|True|Number of sample results|
|moreDataAvailable|boolean|True|If more data is available. Extend the limit and/or offset to view|
|samples|[]sample_info|True|Information about the actual sample|
|offset|integer|True|The offset of the individual entities in the query's response; used for pagination|
|query|string|True|What string was queried or seen by the API|
|totalResults|integer|True|The number of results returned. Same as limit if limit is reached and moreDataAvailable is true|

#### Other Samples

This action is used to return other samples associated with a sample.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|Search sample by hash (SHA-256, SHA-1 or MD5)|None|
|limit|string|None|False|Default of 10, can be extended for a larger data set|None|
|offset|string|None|False|Used to paginate between sets of data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|samples|array|True|None|

#### Security Information

This action is used to returns scores or security features.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dga_score|number|True|Domain Generation Algorithm. This score is generated based on the likeliness of the domain name being generated by an algorithm rather than a human|
|geoscore|number|True|A score that represents how far the different physical locations serving this name are from each other|
|asn_score|number|False|ASN reputation score, ranges from -100 to 0 with -100 being very suspicious|
|ks_test|number|True|Kolmogorov-Smirnov test on geodiversity. 0 means that the client traffic matches what is expected for this TLD|
|pagerank|number|True|Popularity according to Google's pagerank algorithm|
|entropy|number|True|The number of bits required to encode the domain name, as a score. This score is to be used in conjunction with DGA and Perplexity|
|perplexity|number|True|A second score on the likeliness of the name to be algorithmically generated, on a scale from 0 to 1|
|threat_type|string|False|The type of the known attack, such as botnet or APT. Returns blank if no known threat associated with domain|
|tld_geodiversity|array|True|A score that represents the TLD country code geodiversity as a percentage of clients visiting the domain. Occurs most often with domains that have a ccTLD. Score is normalized ratio between 0 and 1|
|rip_score|number|False|RIP ranks domains given their IP addresses and the reputation score of these IP addresses. Ranges from -100 to 0, -100 being very suspicious|
|securerank2|number|True|Securerank is designed to identify hostnames requested by known infected clients but never requested by clean clients, assuming these domains are more likely to be bad. Scores range from -100 (suspicious) to 100 (benign)|
|popularity|number|True|The number of unique client IPs visiting this site, relative to the all requests to all sites. A score of how many different client/unique IPs go to this domain compared to others|
|attack|string|False|The name of any known attacks associated with this domain. Returns blank if no known threat associated with domain|
|geodiversity|array|True|A score representing the number of queries from clients visiting the domain, broken down by country. Score is a non-normalized ratio between 0 and 1|
|prefix_score|number|False|Prefix ranks domains given their IP prefixes (an IP prefix is the first three octets in an IP address) and the reputation score of these prefixes. Ranges from -100 to 0, -100 being very suspicious|
|geodiversity_normalized|array|True|A score representing the amount of queries for clients visiting the domain, broken down by country. Score is a normalized ratio between 0 and 1|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.3 - New spec and help.md format for the Hub
* 1.0.2 - Added change allowing categorization to work with a Tier1 API key by utilizing the single domain API endpoint instead of the bulk API endpoint when a single-element array of domains is passed in
* 1.0.1 - Add connection test | Fix where connection was returning "Wrong api_key" on valid keys | Run plugin as least privileged user | Update to use the `komand/python-3-slim-plugin` Docker image to reduce plugin size
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Cisco Umbrella Investigate](https://learn-umbrella.cisco.com/threat-intelligence/cisco-umbrella-investigate-overview)
* [Python OpenDNS Investigate](https://github.com/opendns/pyinvestigate)
* [Authentication](https://docs.umbrella.com/developer/enforcement-api/authentication-and-versioning/)

