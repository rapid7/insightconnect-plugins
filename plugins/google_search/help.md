# Description

[Google](https://www.google.com/) allows you to search the world's information, including webpages, images, videos and more. With this plugin search the web with queries.

This plugin utilizes the Python [google library](https://pypi.python.org/pypi/google) to perform searches.

# Key Features

* Search with Google
* Request webpages

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

* 2022-03-31

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Search

This action is used to return URLs from a Google Search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|lang|string|en|True|Language, default is en|None|en|
|num|integer|10|True|Number of results per page, default is 10|None|10|
|pause|float|1|True|Lapse to wait between HTTP requests. A lapse too long will make the search slow, but a lapse too short may cause Google to block your IP. Your mileage may vary|None|1.0||num|integer|10|True|Number of results per page, default is 10|None|10|
|query|string|None|True|Query string. Must NOT be URL-encoded|None|example.com|
|stop|integer|16|True|Number of results to retrieve to limit amount, default is 16 and the search will allows return at least 16 results if available. This option seems to have odd behavior|None|16|

Example input:

```
{
  "lang": "en",
  "pause": 1.0,
  "query": "example.com",
  "num": 1,
  "stop": 16
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|urls|[]string|True|List of URLs|

Example output:

```
{
   "urls": [
     "https://example.com"
   ]
}
```

#### Get Page

This action is used to request the given URL and return the response page, using the cookie jar.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL to retrieve e.g. https://www.google.com|None|https://example.com|

Example input:

```
{
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|web_page|string|True|Web page|

Example output:

```
{
   "web_page": '<!DOCTYPE html>\\n<html>\\n    <head>\\n        <title>Example</title>\\n    </head>\\n    <body>\\n        <p>This is an example of a simple HTML page with one paragraph.</p>\\n    </body>\\n</html>'
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Bug fix for Search action | Removal of retired Search action parameter | Update to Insight Connect SDK
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Bug fix for no google module
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Google](https://www.google.com/)
* [Python Google library](https://pypi.python.org/pypi/google)
* [Python Google library docs](https://pythonhosted.org/google/)
