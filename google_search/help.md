
# Google Search

## About

[Google](https://www.google.com/) allows you to search the world's information, including webpages, images, videos and more.
This plugin utilizes the Python [google library](https://pypi.python.org/pypi/google) to perform searches.

## Actions

### Search

This action is used to return URLs from a Google Search.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|lang|string|en|True|Language, default is en|None|
|start|integer|1|True|First result to retrieve, default is 1|None|
|pause|float|1.0|True|Lapse to wait between HTTP requests. A lapse too long will make the search slow, but a lapse too short may cause Google to block your IP. Your mileage may vary|None|
|num|integer|10|True|Number of results per page, default is 10|None|
|query|string|None|True|Query string. Must NOT be URL-encoded|None|
|stop|integer|16|True|Number of results to retrieve to limit amount, default is 16 and the search will allows return at least 16 results if available. This option seems to have odd behavior|None|
|only_standard|boolean|False|True|Only returns the standard results from each page. If false, it returns every possible link from each page, except for those that point back to Google itself|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|urls|[]string|True|List of URLs|

### Get Page

This action is used to request the given url and return the response page, using the cookie jar.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to retrieve e.g. https://www.google.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|web_page|string|True|Web page|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Search Google

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Bug fix for no google module

## References

* [Google](https://www.google.com/)
* [Python Google library](https://pypi.python.org/pypi/google)
* [Python Google library docs](https://pythonhosted.org/google/)
