# Description

[Python](https://www.python.org/) is a programming language that lets you work quickly and integrate systems more effectively. This plugin allows you to run Python 3 code. It includes Python 3.8.1 and its standard library as well as the following 3rd party libraries: 

* [requests 2.31.0](https://requests.readthedocs.io/en/master/)
* [maya 0.6.1](https://pypi.python.org/pypi/maya)
* [lxml 4.9.2](http://lxml.de/)
* [beautifulsoup 4.12.2](https://www.crummy.com/software/BeautifulSoup/)
* [pyyaml 6.0.0](http://pyyaml.org/)
* [records 0.5.3](https://github.com/kennethreitz/records)

The Python 3 Script plugin also allows you to load custom modules via its connection parameters.

Also, this plugin allows you to provide additional credentials in the connection such as username, password, secret_key available in the script as Python variables (`username`, `password`, `secret_key`). 

# Key Features
  
* Run a Python 3 Script to securely orchestrate, automate, and respond to (almost) anything

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
* Python 3.8.1

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|modules|[]string|None|False|List of third-party modules to install for use in the supplied Python script|None|["pandas", "numpy"]|
|script_secret_key|credential_secret_key|None|False|Credential secret key available in script as python variable (`secret_key`)|None|{"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"}|
|script_username_and_password|credential_username_password|None|False|Username and password available in script as python variables (`username`, `password`)|None|{"username": "user", "password": "mypassword"}|
|timeout|integer|60|True|Timeout (in seconds) for installing third-party modules|None|120|
  
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
  "timeout": 60
}
```

## Technical Details

### Actions

#### Run Function

Run a Python 3 function

##### Input

An input object can be supplied as the `params={}` parameter for the function.

The run function should return an object, whose fields gets added to the results object, e.g.

```
def run(params={}):
  return { 'hello': 'world' }
```

This returns a string with key `hello` on the output object accessible at `{{Step.hello}}`.

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|function|python|def run(params={}):\n    return {}|True|Function definition. Must be named `run`. Accepts the `input` object as params. Returns the dict as output. In this action you can use `username`, `password`, `secret_key` variables if defined in connection|None|def run(params={}):\n\tprint(params.get('some_input'))\n\tprint(username, password)\n\treturn {}|
|input|object|None|False|Input object to be passed as `params={}` to the `run` function|None|{"some_input": "example input"}|
  
Example input:

```
{
  "function": "def run(params={}):\n\tprint(params.get('some_input'))\n\tprint(username, password, secret_key)\n\treturn {'result1': 'example output 1', 'result2': 'example output 2'}",
  "input": {
    "some_input": "example input"
  }
}
```

Note that `username`, `password`, and `secret_key` inputs are accessible directly in the script as variable, but arguments from `input` are stored in `params` dictionary.

##### Output

The default output variables are `result1` and `result2`, both of type `string`. While these may work for you they're intended to be changed by the user to meet their naming and type needs.

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result1|string|False|Sample output result1 (delete or edit)|example output 1|
|result2|string|False|Sample output result2 (delete or edit)|example output 2|

Make sure you edit the output variables in the user interface so that they match the keys returned by the `run()` function. This allows you to pass the variables to other steps using the names chosen by the user.

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

Some third-party modules defined in the `Modules` connection input (such as `pandas`) can take a long time to install.
If installation fails, try increasing the `Timeout` connection input to `900` (15 minutes).

# Version History

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
* 1.0.3 - Update to v2 Python plugin architecture | Support web server mode | Add and pin 3rd party libraries: lxml, beautifulsoup, pyyaml, maya, and records
* 1.0.2 - SDK update
* 1.0.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Python](https://www.python.org/)

## References
  
* [Python 3 Language Reference](https://docs.python.org/3/reference/index.html)  
* [InsightConnect Python Plugin Guide](https://docs.rapid7.com/insightconnect/python-2-or-3-script/)
