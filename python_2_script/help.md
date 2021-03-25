# Description

[Python](https://www.python.org/) is a programming language that lets you work quickly and integrate systems more effectively. This plugin allows you to run Python 2 code. It includes Python 2.7.15 and its standard library as well as the following 3rd party libraries:

* [requests 2.18.4](https://requests.readthedocs.io/en/master/)
* [maya 0.5.0](https://pypi.python.org/pypi/maya)
* [lxml 4.2.2](http://lxml.de/)
* [beautifulsoup 4.6.0](https://www.crummy.com/software/BeautifulSoup/)
* [pyyaml 3.12](http://pyyaml.org/)
* [records 0.5.2](https://github.com/kennethreitz/records)

# Key Features

* Run a Python 2 script to securely orchestrate, automate, and respond to (almost) anything

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

Check out the [plugin guide](https://insightconnect.help.rapid7.com/docs/python-2-or-3-script) for more details on how to configure this plugin.

This plugin does not contain a connection.

## Technical Details

### Actions

#### Run Function

This action is used to run custom Python code using a function called `run`.

See the [official documentation](https://docs.komand.com/docs/python-script-plugin) for more information.

##### Input

An input object can be supplied will as the params={} parameter for the function.

The `run` function should return an object,
whose fields gets added to the results object, e.g.

```

def run(params={}):
  return { 'hello': 'world' }

```

This returns a string with key `hello` on the output object accessible at {{Step.hello}}.

Make sure you the edit the output variables so that they match the keys returned by the 'run()' function.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|function|python|def run(params={}):
  return { 'result1': 'foo', 'result2': 'bar' }|False|Function definition. Must be named `run`. Accepts the `input` object as params. Returns the dict as output.|None|
|input|object|None|False|Input object to be passed as `params={}` to the `run` function.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result2|string|False|Sample output result2 (delete or edit)|
|result1|string|False|Sample output result1 (delete or edit)|

Make sure you the edit the output variables so that they match the keys returned by the 'run()' function.

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.3 - New spec and help.md format for the Extension Library
* 2.0.2 - Add `utilities` plugin tag for Marketplace searchability
* 2.0.1 - Fix issue where run action was excluded from plugin on build
* 2.0.0 - Update to v2 Python plugin architecture | Support web server mode | Pin Python library versions | Rename action to Run Function
* 1.2.1 - SSL bug fix in SDK
* 1.1.0 - Add 3rd party libraries: datetime, lxml, beautifulsoup, pyyaml, and records
* 1.0.0 - Rename plugin from 'Python Script' to 'Python 2 Script'
* 0.1.0 - Initial plugin

# Links

## References

* [InsightConnect Python Plugin Guide](https://insightconnect.help.rapid7.com/docs/python-2-or-3-script)
