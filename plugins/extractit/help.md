# Description

The ExtractIt plugin is a collection of data extraction actions. This plugin allows users to extract various pieces of information from blocks of text. The pieces of information this plugin can extract include IPs, URLs, file paths, dates, domains, hashes, MAC addresses, and email addresses.

# Key Features

* Extract dates from a string or file for use in subsequent workflow actions
* Extract domains from a string or file for use in subsequent workflow actions
* Extract email addresses from a string or file for use in subsequent workflow actions
* Extract file paths from a string or file for use in subsequent workflow actions
* Extract indicators of compromise from a string or file for use in subsequent workflow actions
* Extract URLs from a string or file for use in subsequent workflow actions
* Extract IP addresses from a string or file for use in subsequent workflow actions
* Extract MAC addresses from a string or file for use in subsequent workflow actions
* Extract MD5, SHA1, SHA256, and SHA512 hashes from a string or file for use in subsequent workflow actions
* Extract UUIDs from a string or file for use in subsequent workflow actions
* Extract CVEs from a string or file for use in subsequent workflow actions
* Extract all indicators from a string or file for use in subsequent workflow actions

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Extract All

This action extracts all UUIDs, CVEs, dates, domains, emails, filepaths, IOCs, IPs, MACs, MD5 hashes, SHA1 hashes, SHA256 hashes, SHA 512 hashes and URLs from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|date_format|string|None|True|Dates matching this format are extracted - If All Formats is selected, found dates will be processed in the listed order documented|['dd/mm/yyyy', 'mm/dd/yyyy', 'dd/mm/yyyy', 'dd\\mm\\yyyy', 'dd.mm.yyyy', 'dd-mm-yyyy', 'dd.mm.yy', 'dd-mm-yy', 'dd/mm/yy', 'dd\\mm\\yy', 'mm/dd/yyyy', 'mm\\dd\\yyyy', 'mm.dd.yyyy', 'mm-dd-yyyy', 'mm/dd/yy', 'mm\\dd\\yy', 'mm.dd.yy', 'mm-dd-yy', 'dd/mmm/yyyy', 'dd\\mmm\\yyyy', 'dd.mmm.yyyy', 'dd-mmm-yyyy', 'dd/mmm/yy', 'dd\\mmm\\yy', 'dd.mmm.yy', 'dd-mmm-yy', 'yyyy.mm.dd', 'yyyy-mm-dd', 'yyyy/mm/dd', 'yyyy\\mm\\dd', 'yyyy.mmm.dd', 'yyyy-mmm-dd', 'yyyy/mmm/dd', 'yyyy\\mmm\\dd', 'yy.mm.dd', 'yy-mm-dd', 'yy/mm/dd', 'yy\\mm\\dd', 'yyyy-mm-ddThh:mm', 'yyyy-mm-ddThh:mm:ss', 'All Formats', '']|dd/mm/yyyy|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|dGVzdCBzdHJpbmcgb2YgZXh0cmFjdCBDVkUtMTIzNC0xMjM0NTY3IDEyLzEyLzIzMTIgMTIzZTQ1NjctZTEyYi0zNGMzLWE0NTYtNDI2Nzg5MTI0MDAwIHVzZXJAZXhhbXBsZS5jb20gMzM5NTg1NmNlODFmMmI3MzgyZGVlNzI2MDJmNzk4YjY0MmYxNDE0MCAyNzVhMDIxYmJmYjY0ODllNTRkNDcxODk5ZjdkYjlkMTY2M2ZjNjk1ZWMyZmUyYTJjNDUzOGFhYmY2NTFmZDBmIDE5OC41MS4xMDAuMC8yNCAxLjEuMS4x|
|str|string|None|False|Input string|None|test string of extract CVE-1234-1234567 12/12/2312 123e4567-e12b-34c3-a456-426789124000 user@example.com 3395856ce81f2b7382dee72602f798b642f14140 275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f 198.51.100.0/24 1.1.1.1|

Example input:

```
{
  "date_format": "dd/mm/yyyy",
  "file": "dGVzdCBzdHJpbmcgb2YgZXh0cmFjdCBDVkUtMTIzNC0xMjM0NTY3IDEyLzEyLzIzMTIgMTIzZTQ1NjctZTEyYi0zNGMzLWE0NTYtNDI2Nzg5MTI0MDAwIHVzZXJAZXhhbXBsZS5jb20gMzM5NTg1NmNlODFmMmI3MzgyZGVlNzI2MDJmNzk4YjY0MmYxNDE0MCAyNzVhMDIxYmJmYjY0ODllNTRkNDcxODk5ZjdkYjlkMTY2M2ZjNjk1ZWMyZmUyYTJjNDUzOGFhYmY2NTFmZDBmIDE5OC41MS4xMDAuMC8yNCAxLjEuMS4x",
  "str": "test string of extract CVE-1234-1234567 12/12/2312 123e4567-e12b-34c3-a456-426789124000 user@example.com 3395856ce81f2b7382dee72602f798b642f14140 275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f 198.51.100.0/24 1.1.1.1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|indicators|indicators|False|List of extracted indicators|

Example output:

```
{
  "indicators": {
    "cves": [
      "CVE-1234-1234567"
    ],
    "dates": [
      "2312-12-12T00:00:00Z"
    ],
    "email_addresses": [
      "user@example.com"
    ],
    "filepaths": [
      "/24"
    ],
    "mac_addresses": [],
    "hashes": {
      "md5_hashes": [],
      "sha1_hashes": [
        "3395856ce81f2b7382dee72602f798b642f14140"
      ],
      "sha256_hashes": [
        "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
      ],
      "sha512_hashes": []
    },
    "ip_addresses": {
      "ipv4_addresses": [
        "198.51.100.0",
        "1.1.1.1"
      ],
      "ipv6_addresses": []
    },
    "urls": [],
    "uuids": [
      "123e4567-e12b-34c3-a456-426789124000"
    ],
    "domains": [
      "example.com"
    ]
  }
}
```

#### UUID Extractor

This action extracts all UUIDs from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|VGVzdCBzdHJpbmcgb2YgZXh0cmFjdCAxMjNlNDU2Ny1lMTJiLTM0YzMtYTQ1Ni00MjY3ODkxMjQwMDA=|
|str|string|None|False|Input string|None|Test string of extract 123e4567-e12b-34c3-a456-426789124000|

Example input:

```
{
  "file": "VGVzdCBzdHJpbmcgb2YgZXh0cmFjdCAxMjNlNDU2Ny1lMTJiLTM0YzMtYTQ1Ni00MjY3ODkxMjQwMDA=",
  "str": "Test string of extract 123e4567-e12b-34c3-a456-426789124000"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|uuids|[]string|False|List of extracted UUIDs|

Example output:

```
{
  "uuids": [
    "123e4567-e12b-34c3-a456-426789124000"
  ]
}
```

#### CVE Extractor

This action extracts all CVEs from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|dGVzdCBzdHJpbmcgb2YgZXh0cmFjdCBDVkUtMTIzNC0xMjM0NTY3IDIwMTIvMTIvMTI=|
|str|string|None|False|Input string|None|Test string of extract CVE-1234-1234567 2012/12/12|

Example input:

```
{
  "file": "dGVzdCBzdHJpbmcgb2YgZXh0cmFjdCBDVkUtMTIzNC0xMjM0NTY3IDIwMTIvMTIvMTI=",
  "str": "Test string of extract CVE-1234-1234567 2012/12/12"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cves|[]string|False|List of extracted CVEs|

Example output:

```
{
  "cves": [
    "CVE-1234-1234567"
  ]
}
```

#### Date Extractor

This action extracts all dates from a string or file.

##### Input

|Name|Type|Default|Required|Description| Enum             |Example|
|----|----|-------|--------|-----------|------------------|-------|
|date_format|string|None|True|Dates matching this format are extracted - If All Formats is selected, found dates will be processed in the listed order documented|['dd/mm/yyyy', 'mm/dd/yyyy', 'dd/mm/yyyy', 'dd\\mm\\yyyy', 'dd.mm.yyyy', 'dd-mm-yyyy', 'dd.mm.yy', 'dd-mm-yy', 'dd/mm/yy', 'dd\\mm\\yy', 'mm/dd/yyyy', 'mm\\dd\\yyyy', 'mm.dd.yyyy', 'mm-dd-yyyy', 'mm/dd/yy', 'mm\\dd\\yy', 'mm.dd.yy', 'mm-dd-yy', 'dd/mmm/yyyy', 'dd\\mmm\\yyyy', 'dd.mmm.yyyy', 'dd-mmm-yyyy', 'dd/mmm/yy', 'dd\\mmm\\yy', 'dd.mmm.yy', 'dd-mmm-yy', 'yyyy.mm.dd', 'yyyy-mm-dd', 'yyyy/mm/dd', 'yyyy\\mm\\dd', 'yyyy.mmm.dd', 'yyyy-mmm-dd', 'yyyy/mmm/dd', 'yyyy\\mmm\\dd', 'yy.mm.dd', 'yy-mm-dd', 'yy/mm/dd', 'yy\\mm\\dd', 'yyyy-mm-ddThh:mm', 'yyyy-mm-ddThh:mm:ss', 'All Formats', '']|dd/mm/yyyy|
|str|string|None|False|Input string|None|05/12/1982 is an example date|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|MDUvMTIvMTk4MiBpcyBhbiBleGFtcGxlIGRhdGU=|

Example input:

```
{
  "date_format": "dd/mm/yyyy",
  "file": "MDUvMTIvMTk4MiBpcyBhbiBleGFtcGxlIGRhdGU=",
  "str": "05/12/1982 is an example date"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dates|[]date|False|List of extracted dates|

Example output:

```
{
  "dates": [
    "1982-12-05T00:00:00Z"
  ]
}
```

#### Domain Extractor

This action extracts all domain names from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|ZXhhbXBsZS5jb20gaXMgYW4gZXhhbXBsZSBkb21haW4=|
|str|string|None|False|Input string|None|example.com is an example domain|
|subdomain|bool|None|True|Include subdomain in result|None|False|

Example input:

```
{
  "file": "ZXhhbXBsZS5jb20gaXMgYW4gZXhhbXBsZSBkb21haW4=",
  "str": "example.com is an example domain",
  "subdomain": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]string|False|List of extracted Domain names|

Example output:

```
{
  "domains": [
    "example.com"
  ]
}
```

#### Email Extractor

This action extracts all email addresses from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|dXNlckBleGFtcGxlLmNvbSBpcyBhbiBleGFtcGxlIGVtYWls|
|str|string|None|False|Input string|None|user@example.com is an example email|

Example input:

```
{
  "file": "dXNlckBleGFtcGxlLmNvbSBpcyBhbiBleGFtcGxlIGVtYWls",
  "str": "user@example.com is an example email"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|emails|[]string|False|List of extracted Email Addresses|

Example output:

```
{
  "emails": [
    "user@example.com"
  ]
}
```

#### File Path Extractor

This action extracts all file paths from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|L3RtcC9pbWFnZS5qcGcgaXMgYW4gZXhhbXBsZSBmaWxlIHBhdGg=|
|str|string|None|False|Input string|None|/tmp/image.jpg is an example file path|

Example input:

```
{
  "file": "L3RtcC9pbWFnZS5qcGcgaXMgYW4gZXhhbXBsZSBmaWxlIHBhdGg=",
  "str": "/tmp/image.jpg is an example file path"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filepaths|[]string|False|List of extracted file paths|

Example output:

```
{
  "filepaths": [
    "/tmp/image.jpg"
  ]
}
```

#### IOC Extractor

This action extracts all Indicators of Compromise from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|dXNlckBleGFtcGxlLmNvbSwgMTk4LjUxLjEwMC4xMDAgYW5kIDQ0ZDg4NjEyZmVhOGE4ZjM2ZGU4MmUxMjc4YWJiMDJmIGFyZSBJT0MgZXhhbXBsZXM=|
|str|string|None|False|Input string|None|user@example.com, 198.51.100.100 and 44d88612fea8a8f36de82e1278abb02f are IOC examples|

Example input:

```
{
  "file": "dXNlckBleGFtcGxlLmNvbSwgMTk4LjUxLjEwMC4xMDAgYW5kIDQ0ZDg4NjEyZmVhOGE4ZjM2ZGU4MmUxMjc4YWJiMDJmIGFyZSBJT0MgZXhhbXBsZXM=",
  "str": "user@example.com, 198.51.100.100 and 44d88612fea8a8f36de82e1278abb02f are IOC examples"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|iocs|[]string|False|List of extracted Indicators of Compromise|

Example output:

```
{
  "iocs": [
    "example.cop
    "user@example.com",
    "198.51.100.100",
    "44d88612fea8a8f36de82e1278abb02f"
  ]
}
```

#### IP Extractor

This action extracts all IPv4 and IPv6 addresses from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|MTk4LjUxLjEwMC4xMDAgYW5kIDIwMDE6ZGI4Ojg6NDo6MiBhcmUgc2FtcGxlIElQIGFkZHJlc3Nlcw==|
|str|string|None|False|Input string|None|198.51.100.100 and 2001:db8:8:4::2 are sample IP addresses|

Example input:

```
{
  "file": "MTk4LjUxLjEwMC4xMDAgYW5kIDIwMDE6ZGI4Ojg6NDo6MiBhcmUgc2FtcGxlIElQIGFkZHJlc3Nlcw==",
  "str": "198.51.100.100 and 2001:db8:8:4::2 are sample IP addresses"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip_addrs|[]string|False|List of extracted IP Addresses|

Example output:

```
{
  "ip_addrs": [
    "198.51.100.100",
    "2001:db8:8:4::2"
  ]
}
```

#### MAC Extractor

This action extracts all MAC addresses from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|MDA6MTQ6MjI6MDE6MjM6NDUgaXMgYW4gZXhhbXBsZSBNQUMgYWRkcmVzcw==|
|str|string|None|False|Input string|None|00:14:22:01:23:45 is an example MAC address|

Example input:

```
{
  "file": "MDA6MTQ6MjI6MDE6MjM6NDUgaXMgYW4gZXhhbXBsZSBNQUMgYWRkcmVzcw==",
  "str": "00:14:22:01:23:45 is an example MAC address"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|mac_addrs|[]string|False|List of extracted MAC Addresses|

Example output:

```
{
  "mac_addrs": [
    "00:14:22:01:23:45"
  ]
}
```

#### MD5 Hash Extractor

This action extracts all MD5 Hashes from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|NDRkODg2MTJmZWE4YThmMzZkZTgyZTEyNzhhYmIwMmYgaXMgYW4gZXhhbXBsZSBNRDUgaGFzaA==|
|str|string|None|False|Input string|None|44d88612fea8a8f36de82e1278abb02f is an example MD5 hash|

Example input:

```
{
  "file": "NDRkODg2MTJmZWE4YThmMzZkZTgyZTEyNzhhYmIwMmYgaXMgYW4gZXhhbXBsZSBNRDUgaGFzaA==",
  "str": "44d88612fea8a8f36de82e1278abb02f is an example MD5 hash"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|md5|[]string|False|List of extracted MD5 Hashes|

Example output:

```
{
  "md5": [
    "44d88612fea8a8f36de82e1278abb02f"
  ]
}
```

#### SHA1 Hash Extractor

This action extracts all SHA1 Hashes from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|MzM5NTg1NmNlODFmMmI3MzgyZGVlNzI2MDJmNzk4YjY0MmYxNDE0MCBpcyBhbiBleGFtcGxlIFNIQTEgaGFzaA==|
|str|string|None|False|Input string|None|3395856ce81f2b7382dee72602f798b642f14140 is an example SHA1 hash|

Example input:

```
{
  "file": "MzM5NTg1NmNlODFmMmI3MzgyZGVlNzI2MDJmNzk4YjY0MmYxNDE0MCBpcyBhbiBleGFtcGxlIFNIQTEgaGFzaA==",
  "str": "3395856ce81f2b7382dee72602f798b642f14140 is an example SHA1 hash"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha1|[]string|False|List of extracted SHA1 Hashes|

Example output:

```
{
  "sha1": [
    "3395856ce81f2b7382dee72602f798b642f14140"
  ]
}
```

#### SHA256 Hash Extractor

This action extracts all SHA256 Hashes from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|Mjc1YTAyMWJiZmI2NDg5ZTU0ZDQ3MTg5OWY3ZGI5ZDE2NjNmYzY5NWVjMmZlMmEyYzQ1MzhhYWJmNjUxZmQwZiBpcyBhbiBleGFtcGxlIFNIQTI1NiBoYXNo|
|str|string|None|False|Input string|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f is an example SHA256 hash|

Example input:

```
{
  "file": "Mjc1YTAyMWJiZmI2NDg5ZTU0ZDQ3MTg5OWY3ZGI5ZDE2NjNmYzY5NWVjMmZlMmEyYzQ1MzhhYWJmNjUxZmQwZiBpcyBhbiBleGFtcGxlIFNIQTI1NiBoYXNo",
  "str": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f is an example SHA256 hash"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha256|[]string|False|List of extracted SHA256 Hashes|

Example output:

```
{
  "sha256": [
    "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
  ]
}
```

#### SHA512 Hash Extractor

This action extracts all SHA512 Hashes from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|Y2M4MDVkNWZhYjFmZDcxYTRhYjM1MmE5YzUzM2U2NWZiMmQ1Yjg4NTUxOGY0ZTU2NWU2ODg0NzIyM2I4ZTZiODVjYjQ4ZjNhZmFkODQyNzI2ZDk5MjM5YzllMzY1MDVjNjRiMGRjOWEwNjFkOWU1MDdkODMzMjc3YWRhMzM2YWIgaXMgYW4gZXhhbXBsZSBTSEE1MTIgaGFzaA==|
|str|string|None|False|Input string|None|cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab is an example SHA512 hash|

Example input:

```
{
  "file": "Y2M4MDVkNWZhYjFmZDcxYTRhYjM1MmE5YzUzM2U2NWZiMmQ1Yjg4NTUxOGY0ZTU2NWU2ODg0NzIyM2I4ZTZiODVjYjQ4ZjNhZmFkODQyNzI2ZDk5MjM5YzllMzY1MDVjNjRiMGRjOWEwNjFkOWU1MDdkODMzMjc3YWRhMzM2YWIgaXMgYW4gZXhhbXBsZSBTSEE1MTIgaGFzaA==",
  "str": "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab is an example SHA512 hash"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha512|[]string|False|List of extracted SHA512 Hashes|

Example output:

```
{
  "sha512": [
    "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab"
  ]
}
```

#### URL Extractor

This action is used to extract URLs from a string or file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|False|Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS|None|aHR0cHM6Ly9leGFtcGxlLmNvbSBpcyBhbiBleGFtcGxlIFVSTA==|
|str|string|None|False|Input string|None|https://example.com is an example URL|

Example input:

```
{
  "file": "aHR0cHM6Ly9leGFtcGxlLmNvbSBpcyBhbiBleGFtcGxlIFVSTA==",
  "str": "https://example.com is an example URL"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|urls|[]string|False|List of extracted URLs|

Example output:

```
{
  "urls": [
    "https://example.com"
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 3.0.0 - Update to support date format for Date Extractor and Extract All actions
* 2.3.1 - Support special character ! for URL Extractor action
* 2.3.0 - Support extraction from binary files for all actions
* 2.2.1 - Support domain extraction from encoded URL | Fix issue where subdomain removal did not work properly in some cases | Improve domain extraction by limiting the number of false positive results
* 2.2.0 - Add Extract All, UUID Extractor and CVE Extractor actions | Cloud enabled
* 2.1.2 - Rollback URL matching regex used in HTML email extraction.
* 2.1.1 - Rewrite plugin to use the Python SDK | Add input and output examples in plugin.spec and held.md | Fix issue in domain extractor where multiple domains were extracted from a single URL | Fix issue where the URL extractor does not extract URLs containing an email address | Fix issue where hash extractors would return part of SHA256 or SHA512 hashes as SHA1 hash and part of SHA512 hash as SHA256 hash | Update the MD5 regex to exclude spaces or other extra characters in the results | Fix issue where the file path extractor was extracting part of a URL or date as a file path | Add unit tests
* 2.1.0 - Fix issue in domain extractor where a colon could crash the plugin | Update to support unicode domains in extract domain | Fix issue where extract domain output could have invalid characters. e.g. email address and email headers
* 2.0.0 - URL Extractor action no longer falsely identifies email addresses as URLs
* 1.1.7 - New spec and help.md format for the Extension Library
* 1.1.6 - Fix issue where IP Extractor would return inaccurate IPs
* 1.1.5 - Fix issue where URL Extractor parsing was missing URLs
* 1.1.4 - Fix issue where URL Extractor would return IPs
* 1.1.3 - Regenerate with latest Go SDK to solve bug with triggers
* 1.1.2 - Updating to Go SDK 2.6.4
* 1.1.1 - Fix issue where test method for Domain Extractor was not properly testing the action
* 1.1.0 - Port to V2 architecture | Support web server mode | MD5 matching bugfix
* 1.0.1 - Bugfix Email Extractor
* 1.0.0 - Domain Extractor bugfix
* 0.1.0 - Initial plugin

# Links

## References

* None

