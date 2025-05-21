# Description

[Python](https://www.python.org/) is a language for fast development and integration. The plugin runs Python 3.12.8 with standard library and libraries like:

* [requests](https://requests.readthedocs.io/en/latest/)
* [arrow](https://pypi.org/project/arrow/)
* [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/)

It supports loading custom modules and passing credentials (`username`, `password`, `secret_key`, `secret_credential_1`, `secret_credential_2`, `secret_credential_3`)

# Key Features

* Run a Python 3 Script to securely orchestrate, automate, and respond to (almost) anything

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* Python 3.12.8

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|modules|[]string|None|False|List of third-party modules to install for use in the supplied Python script|None|["pandas", "numpy"]|None|None|
|script_secret_key|credential_secret_key|None|False|Credential secret key available in script as python variable (`secret_key`)|None|{"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"}|None|None|
|script_username_and_password|credential_username_password|None|False|Username and password available in script as python variables (`username`, `password`)|None|{"username": "user", "password": "mypassword"}|None|None|
|secret_credential_1|credential_secret_key|None|False|Additional secret connection field available in script as Python variable (`secret_credential_1`)|None|{"secretKey": "s083jh3ggJbsunb92hwbvacaiNAvsiz"}|None|None|
|secret_credential_2|credential_secret_key|None|False|Additional secret connection field available in script as Python variable (`secret_credential_2`)|None|{"secretKey": "PXctwsnevfobd9sbskb2cXistwb0"}|None|None|
|secret_credential_3|credential_secret_key|None|False|Additional secret connection field available in script as Python variable (`secret_credential_3`)|None|{"secretKey": "Mhga68YusiBo00shVsziapan7wgbw"}|None|None|
|timeout|integer|60|True|Timeout (in seconds) for installing third-party modules|None|120|None|None|

Example input:

```
{
  "modules": [
    "pandas",
    "numpy"
  ],
  "script_secret_key": {
    "secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"
  },
  "script_username_and_password": {
    "password": "mypassword",
    "username": "user"
  },
  "secret_credential_1": {
    "secretKey": "s083jh3ggJbsunb92hwbvacaiNAvsiz"
  },
  "secret_credential_2": {
    "secretKey": "PXctwsnevfobd9sbskb2cXistwb0"
  },
  "secret_credential_3": {
    "secretKey": "Mhga68YusiBo00shVsziapan7wgbw"
  },
  "timeout": 60
}
```

## Technical Details

### Actions


#### Run Function

This action is used to run a Python 3 function

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|function|python|def run(params={}):\n    return {}|True|Function definition. Must be named `run`. Accepts the `input` object as params. Returns the dict as output. In this action you can use `username`, `password`, `secret_key` variables if defined in connection|None|def run(params={}):\n\tprint(params.get('some_input'))\n\tprint(username, password)\n\treturn {}|None|None|
|input|object|None|False|Input object to be passed as `params={}` to the `run` function|None|{"some_input": "example input"}|None|None|
|timeout|integer|30|False|Timeout (in minutes) for function execution. If this value is null it will default to 30 minutes|None|30|None|None|
  
Example input:

```
{
  "function": "def run(params={}):\\n    return {}",
  "input": {
    "some_input": "example input"
  },
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result1|string|False|Sample output result1 (delete or edit)|example output 1|
|result2|string|False|Sample output result2 (delete or edit)|example output 2|
  
Example output:

```
{
  "result1": "example output 1",
  "result2": "example output 2"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Some third-party modules defined in the Modules connection input (such as pandas) can take a long time to install. If installation fails, try increasing the Timeout connection input to 900 (15 minutes)

# Version History

* 5.2.1 - Addressed Snyk Vulnerability | SDK bump to latest version (6.3.4)
* 5.2.0 - Added 3 additional `Secret Credential Fields` as optional connection inputs
* 5.1.2 - `timeout` description updated within `run` action | Updated SDK to the latest version (6.3.3)
* 5.1.1 - Updated SDK to the latest version (6.2.5)
* 5.1.0 - Action `Run`: Added `timeout` optional parameter | Updated SDK to the latest version
* 5.0.1 - Updated SDK to the latest version | Initial updates for fedramp compliance
* 5.0.0 - Updated SDK to the latest version | Removing records as its not maintained | Replacing maya with arrow (maya not maintained)
* 4.0.10 - Updated the SDK to the latest version | Updated Python version to `3.9.19` | Fixed issue with invalid unicode character
* 4.0.9 - Updated the SDK to the latest version to address memory usage issues
* 4.0.8 - Updated the SDK to latest version | Fix issue where input argument was too long
* 4.0.7 - Updated the SDK | Updated Python version to `3.9.18` | Added handler to run function separately
* 4.0.6 - Added empty `__init__.py` file to `unit_test` folder | Refreshed with new tooling
* 4.0.5 - Updated the SDK version to include output masking | Updated all dependencies to the newest versions
* 4.0.4 - Update Pyyaml to version 6.0.0
* 4.0.3 - Run: Fix logging issue
* 4.0.2 - Run: Fix issue with indentation where users have non-empty credentials for input function
* 4.0.1 - Resolve issue where users experience issues with installing Python packages, and indentation for input function
* 4.0.0 - Add custom script credentials in Connection
* 3.0.0 - Add custom credentials in Run action
* 2.0.4 - Update help documentation for installing third-party modules
* 2.0.3 - Update `docs_url` in plugin spec with a new link to [plugin setup guide](https://docs.rapid7.com/insightconnect/python-2-or-3-script/)
* 2.0.2 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://insightconnect.help.rapid7.com/docs/python-2-or-3-script)
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Add the ability to download and install third-party libraries for use while configuring the plugin Connection
* 1.0.6 - Fix issue where undefined output exceptions were not being handled correctly
* 1.0.5 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.4 - Fix issue where run action was excluded from plugin on build
* 1.0.3 - Update to v2 Python plugin architecture | Support web server mode | Add and pin 3rd party libraries: lxml, beautifulsoup, pyyaml, maya, and records;
* 1.0.2 - SDK update
* 1.0.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Python](https://www.python.org/)

## References

* [Python 3 Language Reference](https://docs.python.org/3/reference/index.html)
* [InsightConnect Python Plugin Guide](https://docs.rapid7.com/insightconnect/python-2-or-3-script/)