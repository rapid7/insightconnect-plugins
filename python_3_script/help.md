
# Python 3 Script

## About

The Python 3 Script plugin allows you to run Python 3 code. It includes Python 3.6.5 and its standard library as well as the following 3rd party libraries:

* [requests 2.18.4](https://www.python-requests.org/en/master/)
* [maya 0.5.0](https://pypi.python.org/pypi/maya)
* [lxml 4.2.2](http://lxml.de/)
* [beautifulsoup 4.6.0](https://www.crummy.com/software/BeautifulSoup/)
* [pyyaml 3.12](http://pyyaml.org/)
* [records 0.5.2](https://github.com/kennethreitz/records)

## Actions

### Run Function

This action is used to run a Python 3 function. Key names must line up with the parameter names expected by the function.
It works the same way as the [Python Script 2 plugin](https://market.komand.com/plugins/komand/python_script/0.3.0), see [this tutorial](https://docs.komand.com/docs/python-script-plugin) for more guidance.

#### Input

An input object can be supplied as the `params={}` parameter for the function.

The `run` function should return an object, whose fields gets added to the results object, e.g.

```

def run(params={}):
  return { 'hello': 'world' }

```

This returns a string with key `hello` on the output object accessible at `{{Step.hello}}`.

Make sure you the edit the output variables so that they match the keys returned by the 'run()' function.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|function|python|None|False|Function definition|None|
|input|object|None|False|Input object to be passed as `params={}` to the `run` function|None|

#### Output

The default output variables are `result1` and `result2`, both of type `string`. While these may work for you they're intended to be changed by the user to meet their naming and type needs.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result2|string|False|Sample output result2 (delete or edit)|
|result1|string|False|Sample output result1 (delete or edit)|

Make sure you the edit the output variables in the user interface so that they match the keys returned by the 'run()' function.
This allows you to pass the variables to other steps using the names chosen by the user.

Example Output:

```

{
  "result1": "My result",
  "result2": "My result2"
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Custom code

## Versions

* 0.1.0 - Initial plugin
* 1.0.1 - SSL bug fix in SDK
* 1.0.2 - SDK update
* 1.0.3 - Update to v2 Python plugin architecture | Support web server mode | Add and pin 3rd party libraries: lxml, beautifulsoup, pyyaml, maya, and records
* 1.0.4 - Fix issue where run action was excluded from plugin on build
* 1.0.5 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.6 - Fix issue where undefined output exceptions were not being handled correctly
* 2.0.0 - Add the ability to download and install third-party libraries for use while configuring the plugin Connection

## References

* [Python 3 Language Reference](https://docs.python.org/3/reference/index.html)
* [Python Script Plugin Tutorial](https://docs.komand.com/docs/python-script-plugin)
