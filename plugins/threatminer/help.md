# Description

[Threat Miner](https://www.threatminer.org) is an open source search engine for fast threat intelligence research and pivoting with context. 
With the Threat Miner plugin for Rapid7 InsightConnect, users can lookup various pieces of information for threat intelligence gathering
The Threat Miner plugin can aid in phishing analysis through its various lookup actions for domains, IP addresses, and
email addresses. In addition, it can assist in malicious attachment detection when used with email plugins using its hash report feature.

# Key Features
  
* AV Report  
* Domain Lookup  
* Domain Lookup Extended  
* IP Lookup  
* IP Lookup Extended  
* Get Samples  
* Hash Report  
* Hash Samples  
* SSDeep Report  
* SSDeep Sample  
* SSL Hosts  
* SSL Report  
* Email Reverse WHOIS - Domain  
* AV Detection Samples  
* Search IOC Reports  
* Search APTNotes

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
* 2024-03-14

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### AV Report
  
This action is used to retrieve the antivirus (AV) report for a specific malware

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Name of the virus for which the AV report is requested|None|ExampleVirusname|
  
Example input:

```
{
  "query": "ExampleVirusname"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"filename":"ExampleFilename1","year":"2018","URL":"https://www.threatminer.org/report.php?q=ExampleFilename1&y=2018"},{"filename":"ExampleFilename2","year":"2017","URL":"https://www.threatminer.org/report.php?q=ExampleFilename2&y=2017"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "URL": "https://www.threatminer.org/report.php?q=ExampleFilename1&y=2018",
        "filename": "ExampleFilename1",
        "year": "2018"
      },
      {
        "URL": "https://www.threatminer.org/report.php?q=ExampleFilename2&y=2017",
        "filename": "ExampleFilename2",
        "year": "2017"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### AV Detection Samples
  
This action is used to fetches information related to a virus

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Virus name to query|None|Trojan.Enfal|
  
Example input:

```
{
  "query": "Trojan.Enfal"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"value":"f1b341d3383b808ecfacfa22dcbe9196"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "value": "f1b341d3383b808ecfacfa22dcbe9196"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Domain Lookup
  
This action is used to fetch information related to a domain by URIs, certificates, or related samples

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain to search|None|example.com|
|query_type|string|None|True|Specify the type of query to be executed|["WHOIS", "PASSIVE DNS", "Example Query URI", "Report Tagging"]|WHOIS|
  
Example input:

```
{
  "domain": "example.com",
  "query_type": "WHOIS"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200, "status_message": "Results found.", "results": [{"domain": "example.com", "is_subdomain": true, "root_domain": "example.com", "whois": {"updated_date": "", "whois_md5": [], "billing_info": {"Organization": "", "City": "", "State": "", "Country": "", "Postal_Code": ""}, "registrant_info": {"Organization": "", "State": "", "Postal_Code": "", "Country": "", "City": ""}, "creation_date": "", "whois_server": "", "emails": {"admin": "", "tech": "", "registrant": "", "billing": ""}, "tech_info": {"Organization": "", "City": "", "State": "", "Country": "", "Postal_Code": ""}, "admin_info": {"Organization": "", "City": "", "State": "", "Country": "", "Postal_Code": ""}, "nameservers": [], "expiration_date": "", "email_hashes": {"admin": "", "tech": "", "registrant": "", "billing": ""}, "registrar": "", "date_checked": "", "reg_info": {"Organization": "", "City": "", "State": "", "Country": "", "Postal_Code": ""}}, "last_updated": {"sec": 1581089938, "usec": 463000}}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "domain": "example.com",
        "is_subdomain": true,
        "last_updated": {
          "sec": 1581089938,
          "usec": 463000
        },
        "root_domain": "example.com",
        "whois": {
          "admin_info": {
            "City": "",
            "Country": "",
            "Organization": "",
            "Postal_Code": "",
            "State": ""
          },
          "billing_info": {
            "City": "",
            "Country": "",
            "Organization": "",
            "Postal_Code": "",
            "State": ""
          },
          "creation_date": "",
          "date_checked": "",
          "email_hashes": {
            "admin": "",
            "billing": "",
            "registrant": "",
            "tech": ""
          },
          "emails": {
            "admin": "",
            "billing": "",
            "registrant": "",
            "tech": ""
          },
          "expiration_date": "",
          "nameservers": [],
          "reg_info": {
            "City": "",
            "Country": "",
            "Organization": "",
            "Postal_Code": "",
            "State": ""
          },
          "registrant_info": {
            "City": "",
            "Country": "",
            "Organization": "",
            "Postal_Code": "",
            "State": ""
          },
          "registrar": "",
          "tech_info": {
            "City": "",
            "Country": "",
            "Organization": "",
            "Postal_Code": "",
            "State": ""
          },
          "updated_date": "",
          "whois_md5": [],
          "whois_server": ""
        }
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Domain Lookup Extended
  
This action is used to fetches information related to a domain by subdomains or related samples

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain to search|None|example.com|
|query_type|string|None|True|Specify the type of query to be executed|["Related Samples", "Subdomains"]|Subdomains|
  
Example input:

```
{
  "domain": "example.com",
  "query_type": "Subdomains"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"domain":"example.com","subdomains":["sub1.example.com","sub2.example.com","sub3.example.com"]}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "domain": "example.com",
        "subdomains": [
          "sub1.example.com",
          "sub2.example.com",
          "sub3.example.com"
        ]
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Email Reverse WHOIS - Domain
  
This action is used to fetches information related to an email address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|True|Email address to search|None|user@example.com|
  
Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"value":"example.com"}, {"value":"example2.com"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "value": "example.com"
      },
      {
        "value": "example2.com"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Email Reverse WHOIS - Report Tagging
  
This action is used to fetches information related to an email address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|True|Email address to search|None|user@example.com|
  
Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"value":"example.com"}, {"value":"example2.com"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "value": "example.com"
      },
      {
        "value": "example2.com"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Hash Report
  
This action is used to fetches information related to a hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|SHA1 hash to search e.g. 1f4f257947c1b713ca7f9bc25f914039|None|02699626f388ed830012e5b787640e71c56d42d8|
  
Example input:

```
{
  "query": "02699626f388ed830012e5b787640e71c56d42d8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code": 200, "status_message": "Results found.", "results": [{"hash": "e1faffd7f97e38b1d5c6f2bcbc7f5d3d", "type": "MD5", "first_seen": "2022-01-01 10:30:00", "last_seen": "2022-01-05 14:45:00", "samples": [{"sample": "sample1.exe", "date": "2022-01-01", "source": "malware-database"}, {"sample": "sample2.exe", "date": "2022-01-02", "source": "malware-database"}], "relationships": [{"type": "Related IP", "value": "192.168.1.100"}, {"type": "Related Domain", "value": "example.com"}]}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "first_seen": "2022-01-01 10:30:00",
        "hash": "e1faffd7f97e38b1d5c6f2bcbc7f5d3d",
        "last_seen": "2022-01-05 14:45:00",
        "relationships": [
          {
            "type": "Related IP",
            "value": "192.168.1.100"
          },
          {
            "type": "Related Domain",
            "value": "example.com"
          }
        ],
        "samples": [
          {
            "date": "2022-01-01",
            "sample": "sample1.exe",
            "source": "malware-database"
          },
          {
            "date": "2022-01-02",
            "sample": "sample2.exe",
            "source": "malware-database"
          }
        ],
        "type": "MD5"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Hash Samples
  
This action is used to fetches information related to a hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|SHA1 hash to search e.g. 1f4f257947c1b713ca7f9bc25f914039|None|02699626f388ed830012e5b787640e71c56d42d8|
  
Example input:

```
{
  "query": "02699626f388ed830012e5b787640e71c56d42d8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"value":"4c60f3f5cccdfad6137eb0a3218ec4caa3294b164c86dbda8922f1c9a75558fd"},{"value":"2acf0cb8b4bd9f4ae4298cbe4e6ac0b4ab410a29fe1b0c0d1f23996c2d08269b"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "value": "4c60f3f5cccdfad6137eb0a3218ec4caa3294b164c86dbda8922f1c9a75558fd"
      },
      {
        "value": "2acf0cb8b4bd9f4ae4298cbe4e6ac0b4ab410a29fe1b0c0d1f23996c2d08269b"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### IP Lookup
  
This action is used to fetches information related to an IP by Whois, URIs, passive DNS, or report tagging

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IP address to search|None|192.0.2.0/24|
|query_type|string|None|True|Specify the type of query to be executed|["WHOIS", "PASSIVE DNS", "URIs", "Report Tagging"]|WHOIS|
  
Example input:

```
{
  "address": "192.0.2.0/24",
  "query_type": "WHOIS"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200, "status_message": "Results found.", "results": [{"reverse_name": "reverse.in-addr.", "bgp_prefix": "192.0.2.0/24", "cc": "", "asn": "", "asn_name": "", "org_name": "ExampleOrgName", "register": "example.com"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "asn": "",
        "asn_name": "",
        "bgp_prefix": "192.0.2.0/24",
        "cc": "",
        "org_name": "ExampleOrgName",
        "register": "example.com",
        "reverse_name": "reverse.in-addr."
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### IP Lookup Extended
  
This action is used to fetches information related to an IP by certificates, or related samples

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IP address to search|None|192.0.2.0/24|
|query_type|string|None|True|Specify the type of query to be executed|["Related Samples", "SSL Certificates"]|Related Samples|
  
Example input:

```
{
  "address": "192.0.2.0/24",
  "query_type": "Related Samples"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"value":"02699626f388ed830012e5b787640e71c56d42d8"},{"value":"02699626f388ed830012e5b787640e71c56d42d8"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "value": "02699626f388ed830012e5b787640e71c56d42d8"
      },
      {
        "value": "02699626f388ed830012e5b787640e71c56d42d8"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Search IOC Reports
  
This action is used to fetches information related to an indicator by domains, hosts, emails, or samples

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filename|string|None|True|Indicator to search|None|C5_APT_C2InTheFifthDomain.pdf|
|query_type|string|None|True|Specify the type of query to be executed|["Domains", "Hosts", "Emails", "Samples"]|Domains|
|year|string|None|True|Year to search|None|2013|
  
Example input:

```
{
  "filename": "C5_APT_C2InTheFifthDomain.pdf",
  "query_type": "Domains",
  "year": 2013
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"value":"example.com"}, {"value":"example2.com"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "value": "example.com"
      },
      {
        "value": "example2.com"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Get Samples
  
This action is used to fetches samples of data intelligence data by metadata, HTTP traffic, hosts, mutants, registry 
keys, AV detections, or report tagging

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|MD5, SHA1, or SHA256 hash to search|None|9de5069c5afe602b2ea0a04b66beb2c0|
|query_type|string|None|True|Specify the type of query to be executed|["Metadata", "HTTP Traffic", "Hosts", "Mutants", "Registry keys", "AV detections", "Report Tagging"]|Metadata|
  
Example input:

```
{
  "query": "9de5069c5afe602b2ea0a04b66beb2c0",
  "query_type": "Metadata"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|Response|{"status_code":200,"status_message":"Results found.","results":[{"md5":"e6ff1bf0821f00384cdd25efb9b1cc09","sha1":"16fd388151c0e73b074faa33698b9afc5c024b59","sha256":"555b3689dec6ad888348c595426d112d041de5c989d4929284594d1e09f3d85f","sha512":"7be8545c03f26192feb6eaf361b78b91966de28d2917ba1902508ad8589e0f0df748e82a265513f0426b50fedfda8fa6947c8b9e511b5d9a771ab20dc748367b","ssdeep":"3072:HcRtvDzz\/rup4\/skvknm+GytbPlIyWYmxHznEt3xnDn\/1iyG6mb2LoUEb:HEtvD7MkvVIpPlIjYQjQ3N\/MV1AtE","imphash":"dc73a9bd8de0fd640549c85ac4089b87","file_type":"PE32 executable (GUI) Intel 80386, for MS Windows","architecture":"32 Bit","authentihash":"f3ec83f9862e9b09203a21ddac5ecdc4f874a591c2b03ffc4d9a5749e4655e28","file_name":"installaware.15-patch.exe","file_size":"546304 bytes","date_analysed":"2016-03-13 03:46:38"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "architecture": "32 Bit",
        "authentihash": "f3ec83f9862e9b09203a21ddac5ecdc4f874a591c2b03ffc4d9a5749e4655e28",
        "date_analysed": "2016-03-13 03:46:38",
        "file_name": "installaware.15-patch.exe",
        "file_size": "546304 bytes",
        "file_type": "PE32 executable (GUI) Intel 80386, for MS Windows",
        "imphash": "dc73a9bd8de0fd640549c85ac4089b87",
        "md5": "e6ff1bf0821f00384cdd25efb9b1cc09",
        "sha1": "16fd388151c0e73b074faa33698b9afc5c024b59",
        "sha256": "555b3689dec6ad888348c595426d112d041de5c989d4929284594d1e09f3d85f",
        "sha512": "7be8545c03f26192feb6eaf361b78b91966de28d2917ba1902508ad8589e0f0df748e82a265513f0426b50fedfda8fa6947c8b9e511b5d9a771ab20dc748367b",
        "ssdeep": "3072:HcRtvDzz/rup4/skvknm+GytbPlIyWYmxHznEt3xnDn/1iyG6mb2LoUEb:HEtvD7MkvVIpPlIjYQjQ3N/MV1AtE"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### Search APTNotes
  
This action is used to fetches information related to a text search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Text to search|None|sofacy|
|query_type|string|None|True|Specify the type of query to be executed|["Full Text", "By Year"]|Full Text|
  
Example input:

```
{
  "query": "sofacy",
  "query_type": "Full Text"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":"200","status_message":"Results found.","results":[{"filename":"ExampleFilename.pdf","year":"2016","URL":"https:\/\/www.threatminer.org\/report.php?q=ExampleFilename.pdf&y=2016"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "URL": "https://www.threatminer.org/report.php?q=ExampleFilename.pdf&y=2016",
        "filename": "ExampleFilename.pdf",
        "year": "2016"
      }
    ],
    "status_code": "200",
    "status_message": "Results found."
  }
}
```

#### SSDeep Report
  
This action is used to fetches information related to a fuzzy hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|SSDeep fuzzy hash to search|None|1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l|
  
Example input:

```
{
  "query": "1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|Response|{"status_code":200,"status_message":"Results found.","results":[{"hash":"3:6QKm2A3T:6QKm2A3T","similarity":"97","matches":[{"file_name":"file1.exe","file_size":"1536","ssdeep_hash":"3:6QKm2A3T:6QKm2A3T"},{"file_name":"file2.exe","file_size":"1536","ssdeep_hash":"3:6QKm2A3T:6QKm2A3T"}]}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "hash": "3:6QKm2A3T:6QKm2A3T",
        "matches": [
          {
            "file_name": "file1.exe",
            "file_size": "1536",
            "ssdeep_hash": "3:6QKm2A3T:6QKm2A3T"
          },
          {
            "file_name": "file2.exe",
            "file_size": "1536",
            "ssdeep_hash": "3:6QKm2A3T:6QKm2A3T"
          }
        ],
        "similarity": "97"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### SSDeep Sample
  
This action is used to fetches information related to a fuzzy hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|SSDeep fuzzy hash to search|None|1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l|
  
Example input:

```
{
  "query": "1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"value":"ecc5943b5c2ec75065ba1bdb668bb0a2c63c0451be259dea47a902811b318c00"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "value": "ecc5943b5c2ec75065ba1bdb668bb0a2c63c0451be259dea47a902811b318c00"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### SSL Hosts
  
This action is used to fetches host information related to a certificate

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Certificate SHA1 hash to search|None|42a8d5b3a867a59a79f44ffadd61460780fe58f2|
  
Example input:

```
{
  "query": "42a8d5b3a867a59a79f44ffadd61460780fe58f2"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":200,"status_message":"Results found.","results":[{"value":"149.154.157.170"},{"value":"149.154.157.171"}]}|
  
Example output:

```
{
  "response": {
    "results": [
      {
        "value": "149.154.157.170"
      },
      {
        "value": "149.154.157.171"
      }
    ],
    "status_code": 200,
    "status_message": "Results found."
  }
}
```

#### SSL Report
  
This action is used to fetches information related to a certificate

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Certificate SHA1 hash to search|None|42a8d5b3a867a59a79f44ffadd61460780fe58f2|
  
Example input:

```
{
  "query": "42a8d5b3a867a59a79f44ffadd61460780fe58f2"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|response|False|The results returned from the Threatminer API|{"status_code":404,"status_message":"No results found.","results":[]}|
  
Example output:

```
{
  "response": {
    "results": [],
    "status_code": 404,
    "status_message": "No results found."
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Results|[]object|None|False|The actual results of the API request|None|
|Status Code|integer|None|False|Numerical code representing the status of the request|None|
|Status Message|string|None|False|Brief message related to the status of the request|None|

The raw object returned by each action looks like this:

```

"response": {
  "status_message": "Results found.",
  "results": [],
  "status_code": 200
}

```

An example raw response from the domain action:

```

"response": {
  "status_message": "Results found.",
  "results": [
    {
      "ip": "",
      "last_seen": "2014-07-17 16:51:28",
      "domain": "vwrm.com",
      "uri": "http://vwrm.com/maps/iexplorer.zip"
    },
    {
      "ip": "",
      "last_seen": "2013-04-23 18:48:53",
      "domain": "vwrm.com",
      "uri": "http://vwrm.com/"
    }
  ],
  "status_code": 200
}

```

Working through the `[]results` object array which resides in the `result` object, will require some JSON manipulation to get what you need.
The [jq](https://extensions.rapid7.com/extension/jq) and [JSON](https://extensions.rapid7.com/extension/json-edit) plugins are great at sifting through the data.

## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 3.0.0 - Updated SDK to the latest version | Updated packages | Added unittests | Removed `Email Report` action as it's not handled by the current API
* 2.0.1 - Updated Requests version to 2.20.0
* 2.0.0 - Update to v3 Python plugin architecture | Convert import_hash_report API status codes to int | Update documentation
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Rename "Email (Reverse WHOIS) - Report tagging" action to "Email (Reverse WHOIS) - Report Tagging"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Threat Miner](https://www.threatminer.org)

## References

* [Threat Miner](https://www.threatminer.org)
* [Threat Miner API](http://www.threatminer.org/api.php)
