# Description

The RPM plugin allows you to download and analyze an RPM package

# Key Features

* Query RPM package metadata from CentOS and Fedora repositories
* Download and inspect RPM packages for name, version, architecture, license, and signature details
* Add custom repositories and GPG keys for package resolution
* Cache package information locally to speed up repeated lookups

# Requirements

* Network access to the target RPM repositories
* No credentials required

# Supported Product Versions

* 2026-03-18

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Info

This action is used to get information about a package

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|arch|string|None|True|System architecture|["x86_64", "i686", "i386", "noarch"]|x86_64|None|None|
|distro|string|None|True|Distribution|["CentOS 6", "CentOS 7", "Fedora 23", "Fedora 24", "Fedora 25", "Fedora 26"]|CentOS 7|None|None|
|epoch|string|None|False|Epoch|None|0|None|None|
|key|string|None|False|GPG key URL|None|https://www.redhat.com/security/data/fd431d51.txt|None|None|
|name|string|None|True|Canonical package name|None|curl|None|None|
|release|string|None|False|Release version|None|54.el7_6.3|None|None|
|repo|string|None|False|Repository URL|None|https://mirror.centos.org/centos/7/os/x86_64/|None|None|
|version|string|None|False|Package version|None|7.29.0|None|None|
  
Example input:

```
{
  "arch": "x86_64",
  "distro": "CentOS 7",
  "epoch": 0,
  "key": "https://www.redhat.com/security/data/fd431d51.txt",
  "name": "curl",
  "release": "54.el7_6.3",
  "repo": "https://mirror.centos.org/centos/7/os/x86_64/",
  "version": "7.29.0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|architecture|string|False|System architecture|x86_64|
|build_date|date|False|Build date|2019-04-01 12:00:00+00:00|
|build_host|string|False|Build host|x86-01.bsys.centos.org|
|description|string|False|Package description|curl is a command line tool for transferring data with URL syntax|
|files|[]file|False|Package files|[{"path": "/usr/bin/curl", "size": 156000, "mtime": "2019-04-01T12:00:00Z", "hash": "d41d8cd98f00b204e9800998ecf8427e", "mode": "0755", "owner": "root", "group": "root", "isconfig": 0, "isdoc": 0, "rdev": 0, "symlink": ""}]|
|found|boolean|False|Package found|True|
|license|string|False|License|MIT|
|name|string|False|Package name|curl|
|packager|string|False|Packager|CentOS BuildSystem|
|release|string|False|Distro release|54.el7_6.3|
|relocations|string|False|Relocations|(not relocatable)|
|signature|signature|False|Signature|{'scheme': 'RSA/SHA256', 'time': '2019-04-01T12:00:00Z', 'key': 'f4a80eb5'}|
|size|integer|False|Package size|533840|
|source_rpm|string|False|Source RPM|curl-7.29.0-54.el7_6.3.src.rpm|
|summary|string|False|Package summary|A utility for getting files from remote servers|
|url|string|False|Package download URL|https://curl.haxx.se/|
|vendor|string|False|Package vendor|CentOS|
|version|string|False|Package version|7.29.0|
  
Example output:

```
{
  "architecture": "x86_64",
  "build_date": "2019-04-01 12:00:00+00:00",
  "build_host": "x86-01.bsys.centos.org",
  "description": "curl is a command line tool for transferring data with URL syntax",
  "files": [
    {
      "group": "root",
      "hash": "d41d8cd98f00b204e9800998ecf8427e",
      "isconfig": 0,
      "isdoc": 0,
      "mode": "0755",
      "mtime": "2019-04-01T12:00:00Z",
      "owner": "root",
      "path": "/usr/bin/curl",
      "rdev": 0,
      "size": 156000,
      "symlink": ""
    }
  ],
  "found": true,
  "license": "MIT",
  "name": "curl",
  "packager": "CentOS BuildSystem",
  "release": "54.el7_6.3",
  "relocations": "(not relocatable)",
  "signature": {
    "key": "f4a80eb5",
    "scheme": "RSA/SHA256",
    "time": "2019-04-01T12:00:00Z"
  },
  "size": 533840,
  "source_rpm": "curl-7.29.0-54.el7_6.3.src.rpm",
  "summary": "A utility for getting files from remote servers",
  "url": "https://curl.haxx.se/",
  "vendor": "CentOS",
  "version": "7.29.0"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Group|string|None|True|None|None|
|MD5 Sum|string|None|True|None|None|
|Config File Flag|integer|None|True|None|None|
|Document File Flag|integer|None|True|None|None|
|Mode|string|None|True|None|None|
|Last Modified|date|None|True|None|None|
|Owner|string|None|True|None|None|
|Path|string|None|True|None|None|
|Rdev|integer|None|True|None|None|
|Size|integer|None|True|None|None|
|Symlink|string|None|True|None|None|
  
**signature**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Hash|string|None|True|None|None|
|Scheme|string|None|True|None|None|
|Datetime of Last Hash|date|None|True|None|None|


## Troubleshooting

* CentOS 7 repositories only support x86_64 architecture
* Ensure the repository URL returns a valid .repo file
* GPG key URLs must be accessible and return a valid RPM-GPG key

# Version History

* 1.0.2 - Modernize plugin to use insightconnect-plugin-runtime and slim base image
* 1.0.1 - New spec and calculation for help.md generation
* 1.0.0 - Initial plugin

# Links

* [Extension Library](https://extensions.rapid7.com)

## References

* [RPM Documentation](https://rpm.org/documentation.html)
* [DNF Documentation](https://dnf.readthedocs.io/)