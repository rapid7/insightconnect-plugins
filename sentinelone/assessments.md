
## Assessment
### Run

<details>

```
root@stretch:/insightconnect-plugins/sentinelone# icon-plugin run -R tests/get_threats.json
INFO[0000] Running command:  docker run --rm -i rapid7/sentinelone:2.1.1 --debug run < tests/get_threats.json
Connect: Connecting...
Starting new HTTPS connection (1): usea1-partners.sentinelone.net:443
https://usea1-partners.sentinelone.net:443 "POST /web/api/v2.0/users/login HTTP/1.1" 200 None
Token: *************6c471
rapid7/SentinelOne:2.1.1. Step name: get_threats
Get Threats: trigger started
Calling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats
Starting new HTTPS connection (1): usea1-partners.sentinelone.net:443
https://usea1-partners.sentinelone.net:443 "GET /web/api/v2.0/threats?resolved=False&agentIsActive=True&limit=1&createdAt__gt=2020-08-14+14%3A09%3A44.959263 HTTP/1.1" 200 None
Calling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats
Starting new HTTPS connection (1): usea1-partners.sentinelone.net:443
https://usea1-partners.sentinelone.net:443 "GET /web/api/v2.0/threats?resolved=False&agentIsActive=True&limit=1&createdAt__gt=2020-08-14+14%3A09%3A45.580209 HTTP/1.1" 200 None
Calling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats
Starting new HTTPS connection (1): usea1-partners.sentinelone.net:443
https://usea1-partners.sentinelone.net:443 "GET /web/api/v2.0/threats?resolved=False&agentIsActive=True&limit=1&createdAt__gt=2020-08-14+14%3A09%3A51.226464 HTTP/1.1" 200 None
Calling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats
Starting new HTTPS connection (1): usea1-partners.sentinelone.net:443
https://usea1-partners.sentinelone.net:443 "GET /web/api/v2.0/threats?resolved=False&agentIsActive=True&limit=1&createdAt__gt=2020-08-14+14%3A09%3A56.883488 HTTP/1.1" 200 None
Threat found: 957856540417109953
{"body": {"meta": {}, "output": {"threat": {"accountId": "433241117337583618", "accountName": "SentinelOne", "agentComputerName": "so-agent-win12", "agentDomain": "WORKGROUP", "agentId": "901345720792880606", "agentInfected": false, "agentIp": "128.177.65.3", "agentIsActive": true, "agentIsDecommissioned": false, "agentMachineType": "server", "agentNetworkStatus": "disconnected", "agentOsType": "windows", "agentVersion": "4.1.4.82", "automaticallyResolved": false, "classification": "Trojan", "classificationSource": "Cloud", "classifierName": "STATIC", "cloudVerdict": "black", "collectionId": "939037052510055221", "createdAt": "2020-08-14T14:09:57.673535Z", "createdDate": "2020-08-14T14:09:57.667573Z", "description": "malware detected - not mitigated yet (static engine)", "engines": ["sentinelone_cloud"], "fileContentHash": "a2138f21ea96d97ce00cd51971696f7464e5db89", "fileDisplayName": "test.txt", "fileExtensionType": "Document", "fileIsExecutable": false, "fileIsSystem": false, "fileObjectId": "D7E420310A19D922", "filePath": "\\Device\\HarddiskVolume2\\Users\\Administrator\\Desktop\\test.txt", "fileVerificationType": "NotSigned", "fromCloud": false, "fromScan": false, "id": "957856540417109953", "indicators": [], "initiatedBy": "agentPolicy", "initiatedByDescription": "Agent Policy", "isCertValid": false, "isInteractiveSession": false, "isPartialStory": false, "maliciousGroupId": "A4924ABC618C3EE3", "markedAsBenign": false, "mitigationMode": "protect", "mitigationReport": {"kill": {"status": "success"}, "network_quarantine": {}, "quarantine": {"status": "success"}, "remediate": {}, "rollback": {}, "unquarantine": {}}, "mitigationStatus": "mitigated", "rank": 7, "resolved": false, "siteId": "521580416395045459", "siteName": "Rapid7", "threatAgentVersion": "4.1.4.82", "threatName": "test.txt", "updatedAt": "2020-08-14T14:09:58.402902Z", "whiteningOptions": ["hash"]}}, "log": "Connect: Connecting...\nToken: *************6c471\nrapid7/SentinelOne:2.1.1. Step name: get_threats\nGet Threats: trigger started\nCalling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats\nCalling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats\nCalling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats\nCalling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats\nThreat found: 957856540417109953\n"}, "type": "trigger_event", "version": "v1"}
Calling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats
Starting new HTTPS connection (1): usea1-partners.sentinelone.net:443
https://usea1-partners.sentinelone.net:443 "GET /web/api/v2.0/threats?cursor=eyJpZF9jb2x1bW4iOiAiVGhyZWF0Vmlldy5pZCIsICJpZF92YWx1ZSI6IDk1Nzg1NjU0MDQxNzEwOTk1MywgInNvcnRfYnlfY29sdW1uIjogIlRocmVhdFZpZXcuaWQiLCAic29ydF9ieV92YWx1ZSI6IDk1Nzg1NjU0MDQxNzEwOTk1MywgInNvcnRfb3JkZXIiOiAiYXNjIn0%253D&limit=1 HTTP/1.1" 200 None
Calling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats
Starting new HTTPS connection (1): usea1-partners.sentinelone.net:443
https://usea1-partners.sentinelone.net:443 "GET /web/api/v2.0/threats?resolved=False&agentIsActive=True&limit=1&createdAt__gt=2020-08-14+14%3A10%3A03.354546 HTTP/1.1" 200 None
Calling endpoint: https://usea1-partners.sentinelone.net/web/api/v2.0/threats
Starting new HTTPS connection (1): usea1-partners.sentinelone.net:443
https://usea1-partners.sentinelone.net:443 "GET /web/api/v2.0/threats?resolved=False&agentIsActive=True&limit=1&createdAt__gt=2020-08-14+14%3A10%3A09.000236 HTTP/1.1" 200 None

```

<summary>
docker run --rm -i rapid7/sentinelone:2.1.0 --debug run < tests/get_threats.json
</summary>
</details>

<details>

```
[*] Validating plugin with all validators at .

[*] Running Integration Validators...
[*] Executing validator HelpValidator
[*] Executing validator ChangelogValidator
[*] Executing validator RequiredKeysValidator
[*] Executing validator UseCaseValidator
[*] Executing validator SpecPropertiesValidator
[*] Executing validator SpecVersionValidator
[*] Executing validator FilesValidator
[*] Executing validator TagValidator
[*] Executing validator DescriptionValidator
[*] Executing validator TitleValidator
[*] Executing validator VendorValidator
[*] Executing validator DefaultValueValidator
[*] Executing validator IconValidator
[*] Executing validator RequiredValidator
[*] Executing validator VersionValidator
[*] Executing validator DockerfileParentValidator
[*] Executing validator LoggingValidator
[*] Executing validator ProfanityValidator
[*] Executing validator AcronymValidator
[*] Executing validator JSONValidator
[*] Executing validator OutputValidator
[*] Executing validator RegenerationValidator
[*] Executing validator HelpInputOutputValidator
Output violations: Action-> "Get Threat Summary": Missing ['|pagination|pagination|False|Pagination|', '|errors|[]object|False|Errors|', '|data|[]data|False|Data|'] in help.md
Action "Initiate Scan" could be missing or title is incorrect in help.md.
Input violations: Action -> "Get Agent Details": Missing ['|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, MAC address, hostname, UUID or agent ID|None|hostname123|'] in help.md
Output violations: Action-> "Get Agent Details": Missing ['|agent|agent_data|False|Detailed information about agent found|'] in help.md
Input violations: Action -> "Quarantine": Missing ['|agent|string|None|True|Agent to perform quarantine action on. Accepts IP address, MAC address, hostname, UUID or agent ID|None|hostname123|', '|whitelist|[]string|None|False|This list contains a set of devices that should not be blocked. This can include IPs, hostnames, UUIDs and agent IDs|None|["198.51.100.100", "hostname123", "901345720792880606", "28db47168fa54f89aeed99769ac8d4dc"]|'] in help.md
Input violations: Trigger -> "Get Threats": Missing ['|agent_is_active|boolean|True|False|Include agents currently connected to the management console|None|None|'] in help.md
[*] Executing validator SupportValidator
[*] Executing validator RuntimeValidator
[*] Executing validator ExceptionValidator
WARNING: Use of 'PluginException' or 'ConnectionTestException' is recommended when raising an exception.
violation: komand_sentinelone/connection/connection.py: line,  152
violation: komand_sentinelone/connection/connection.py: line,  174
violation: komand_sentinelone/connection/connection.py: line,  301
[*] Executing validator CredentialsValidator
[*] Executing validator PasswordValidator
[*] Executing validator PrintValidator
[*] Executing validator ConfidentialValidator
violation: tests/get_threats.json, line: 19
[*] Executing validator DockerValidator
[*] Executing validator URLValidator
WARNING: URLs found that return a 4xx code. Verify they are publicly accessible and if not, update with a working URL.
violation: plugin.spec.yaml[850]: https://example.sentinelone.com
[*] Plugin failed validation! The following validation errors occurred:

Validator "HelpValidator" failed! 
	Cause: Help section is missing title of: #### Initiate Scan

Validator "TitleValidator" failed! 
	Cause: ("actions key 'agents_connect''s title ends with period when it should not.", ValidationException("Title contains a lowercase 'network' when it should not."))

Validator "AcronymValidator" failed! 
	Cause: Acronyms found in plugin.spec.yaml that should be capitalized: ['IoC', 'IoC']
Acronyms found in help.md that should be capitalized: ['IoC', 'IoC']

Validator "HelpInputOutputValidator" failed! 
	Cause: Help.md is not in sync with plugin.spec.yaml. Please regenerate help.md by running 'icon-plugin generate python --regenerate' to rectify violations.


----
[*] Total time elapsed: 21827.811ms


```

<summary>
icon-validate --all .
</summary>
</details>