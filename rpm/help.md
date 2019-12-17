# Description

The [RPM](http://rpm.org/) plugin replicates the `info` (`-i`) capabilities of RPM while utilizing yum to help resolve packages correctly and download them for inspection.

# Key Features

* Download and analyze an RPM package

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Info

This action is used to get information about a package.

##### Input

As input, the plugin takes the expected parts of a complete RPM package label: name<epoch:>-version-release.arch.
For better accuracy in identifying the users intended package, the user is also asked to specify their distro and architecture.
Note that a label must match exactly to find a specific package, and label sections must be specified from left to right.
Thus, release info without the version is ignored when searching. A custom repository URL may also be specified, which will disable all other repos.
If a custom key URL is also given (note: URL), then the key is used to do a checksig on the package downloaded before it is examined by RPM.

Briefly, when given a package, the plugin checks to see if the cache already holds the results of am `rpm -qi --dump`.
If it does not, yumdownloader downloads the package and automatically performs a checksig before inspecting it and caching the result.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Canonical package name|None|
|repo|string|None|False|Repository URL|None|
|epoch|string|None|False|None|None|
|version|string|None|False|Package version|None|
|key|string|None|False|GPG key URL|None|
|release|string|None|False|Release version)|None|
|arch|string|None|True|System architecture|['x86_64', 'i686', 'i386', 'noarch']|
|distro|string|None|True|Distribution|['CentOS 6', 'CentOS 7', 'Fedora 23', 'Fedora 24', 'Fedora 25', 'Fedora 26']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|[]file|False|Package Files|
|vendor|string|False|Package Vendor|
|description|string|False|Package Description|
|build_host|string|False|Build Host|
|relocations|string|False|Relocations|
|source_rpm|string|False|Source RPM|
|packager|string|False|Packager|
|size|integer|False|Package Size|
|build_date|date|False|Build Date|
|name|string|False|Package Name|
|license|string|False|License|
|url|string|False|Package Download URL|
|summary|string|False|Package Summary|
|version|string|False|Package Version|
|architecture|string|False|System Architecture|
|signature|signature|False|Signature|
|release|string|False|Distro Release|
|found|boolean|False|Package Found|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The choice was made to use yum instead of building a custom repo search tool because:

1. Repos organize packages differently (ex: Fedora uses alphabetized directories and CentOS has all of them in one place), and there is no guaranteed labeling scheme for packages (only what is expected). For instance, some packages have different common names than what is in their labels. Thus, a custom tool would have to read repo markdown to match package labels with that which a client is looking for.
2. I would have to make decisions about how to deal with updates to repositories and how to handle caching. Yum keeps a cached record of what packages are available remotely and rolling this manually would be overkill.
3. Instead of asking clients to provide the root directory URL of custom repos, they can provide a .repo file and a remote key file and yum will take care of the rest.

That being said, I was unable to find a library to assist in querying remote repos which would been a major help. In addition, yum will soon be deprecated in favor of DNF, and I have some code written for dnf if we ever have a docker container that runs CentOS or Fedora.
The complexity of this plugin overwhelmingly involves hacking around with yum, which does some strange things. For example, changing the order of architectures specified with --archlist and putting 'noarch' first leads to no results in all cases. In addition, repofiles must be modified in order for yum to work correctly.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode | Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [RPM](http://rpm.org/)

