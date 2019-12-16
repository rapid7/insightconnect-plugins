# Description

The REST plugin to make it easy to integrate with RESTful services.

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) is a means of communicating over HTTP using verbs and actions to represent operations performed over resources, held in remote locations. It's based off of a document put together by Roy Fielding.
All actions take 2 pieces of configuration: a route, and an optional series of headers. Any headers set this way will overwrite the default ones in the connection.

The route can include a query string and arguments as needed, or just be the remaining path, which will be appended to the base URL specified in the connection.
Additionally, every action except GET will allow you specify a body as part of the request.

All of the actions return the same set of data:

* The response, parsed from JSON as an object if possible
* The response, as a raw string of text
* The status code
* The response headers

# Key Features

* Run REST requests on any HTTP endpoint

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

Configuring a REST connection requires an endpoint to hit, which includes the protocol (`http://` or `https://` should be explicitly set by the user).
Additionally, you can set a series of default Headers for every request to use. This would be useful if every request needed to send an auth token along inside of a header, so you don't need to specify it in each individual action.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|default_headers|object|None|False|None|None|
|base_url|string|None|False|None|None|
|ssl_verify|boolean|True|False|None|None|
|basic_auth_credentials|credential_username_password|None|False|None|None|

## Technical Details

### Actions

#### PUT

This action is used to make a PUT request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|object|None|False|Payload to submit to the server when making the REST call|None|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body_object|object|False|Response payload from the server as an object|
|body_string|string|False|Response payload from the server as a string|
|headers|object|False|Response headers from the server|
|status|int|False|Status code of the response from the server|

Example output:

```
{
  "body_object": {
    "args": {},
    "data": "{\"hello\": \"world\"}",
    "files": {},
    "form": {},
    "headers": {
      "Accept": "*/*",
      "Accept-Encoding": "gzip, deflate",
      "Connection": "close",
      "Content-Length": "18",
      "Content-Type": "application/json",
      "Host": "httpbin.org",
      "Referer": "https://google.com",
      "User-Agent": "Mozilla/5.0"
    },
    "json": {
      "hello": "world"
    },
    "origin": "73.51.89.6",
    "url": "https://httpbin.org/put"
  },
  "body_string": "{\n  \"args\": {}, \n  \"data\": \"{\\\"hello\\\": \\\"world\\\"}\", \n  \"files\": {}, \n  \"form\": {}, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Accept-Encoding\": \"gzip, deflate\", \n    \"Connection\": \"close\", \n    \"Content-Length\": \"18\", \n    \"Content-Type\": \"application/json\", \n    \"Host\": \"httpbin.org\", \n    \"Referer\": \"https://google.com\", \n    \"User-Agent\": \"Mozilla/5.0\"\n  }, \n  \"json\": {\n    \"hello\": \"world\"\n  }, \n  \"origin\": \"73.51.89.6\", \n  \"url\": \"https://httpbin.org/put\"\n}\n",
  "status": 200,
  "headers": {
    "Connection": "keep-alive",
    "Server": "gunicorn/19.9.0",
    "Date": "Thu, 13 Sep 2018 15:21:45 GMT",
    "Content-Type": "application/json",
    "Content-Length": "468",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Via": "1.1 vegur"
  }
}
```

#### POST

This action is used to make a POST request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|object|None|False|Payload to submit to the server when making the REST call|None|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body_object|object|False|Response payload from the server as an object|
|body_string|string|False|Response payload from the server as a string|
|headers|object|False|Response headers from the server|
|status|int|False|Status code of the response from the server|

Example output:

```
{
  "body_object": {
    "args": {},
    "data": "{\"Best\": \"Komand\"}",
    "files": {},
    "form": {},
    "headers": {
      "Accept": "*/*",
      "Accept-Encoding": "gzip, deflate",
      "Connection": "close",
      "Content-Length": "18",
      "Content-Type": "application/json",
      "Host": "httpbin.org",
      "Referer": "https://google.com",
      "User-Agent": "Mozilla/5.0"
    },
    "json": {
      "Best": "Komand"
    },
    "origin": "73.51.89.6",
    "url": "https://httpbin.org/post"
  },
  "body_string": "{\n  \"args\": {}, \n  \"data\": \"{\\\"Best\\\": \\\"Komand\\\"}\", \n  \"files\": {}, \n  \"form\": {}, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Accept-Encoding\": \"gzip, deflate\", \n    \"Connection\": \"close\", \n    \"Content-Length\": \"18\", \n    \"Content-Type\": \"application/json\", \n    \"Host\": \"httpbin.org\", \n    \"Referer\": \"https://google.com\", \n    \"User-Agent\": \"Mozilla/5.0\"\n  }, \n  \"json\": {\n    \"Best\": \"Komand\"\n  }, \n  \"origin\": \"73.51.89.6\", \n  \"url\": \"https://httpbin.org/post\"\n}\n",
  "status": 200,
  "headers": {
    "Connection": "keep-alive",
    "Server": "gunicorn/19.9.0",
    "Date": "Thu, 13 Sep 2018 15:20:59 GMT",
    "Content-Type": "application/json",
    "Content-Length": "469",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Via": "1.1 vegur"
  }
}
```

#### PATCH

This action is used to make a PATCH request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|object|None|False|Payload to submit to the server when making the REST call|None|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body_object|object|False|Response payload from the server as an object|
|body_string|string|False|Response payload from the server as a string|
|headers|object|False|Response headers from the server|
|status|int|False|Status code of the response from the server|

Example output:

```
{
  "body_object": {
    "args": {},
    "data": "",
    "files": {},
    "form": {},
    "headers": {
      "Accept": "*/*",
      "Accept-Encoding": "gzip, deflate",
      "Connection": "close",
      "Content-Length": "0",
      "Host": "httpbin.org",
      "Referer": "https://google.com",
      "User-Agent": "Mozilla/5.0"
    },
    "json": null,
    "origin": "73.51.89.6",
    "url": "https://httpbin.org/patch"
  },
  "body_string": "{\n  \"args\": {}, \n  \"data\": \"\", \n  \"files\": {}, \n  \"form\": {}, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Accept-Encoding\": \"gzip, deflate\", \n    \"Connection\": \"close\", \n    \"Content-Length\": \"0\", \n    \"Host\": \"httpbin.org\", \n    \"Referer\": \"https://google.com\", \n    \"User-Agent\": \"Mozilla/5.0\"\n  }, \n  \"json\": null, \n  \"origin\": \"73.51.89.6\", \n  \"url\": \"https://httpbin.org/patch\"\n}\n",
  "status": 200,
  "headers": {
    "Connection": "keep-alive",
    "Server": "gunicorn/19.9.0",
    "Date": "Thu, 13 Sep 2018 15:20:25 GMT",
    "Content-Type": "application/json",
    "Content-Length": "384",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Via": "1.1 vegur"
  }
}
```

#### GET

This action is used to make a GET request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body_object|object|False|Response payload from the server as an object|
|body_string|string|False|Response payload from the server as a string|
|headers|object|False|Response headers from the server|
|status|int|False|Status code of the response from the server|

Example output:

```
{
  "body_object": {
    "origin": "73.51.89.6"
  },
  "body_string": "{\n  \"origin\": \"73.51.89.6\"\n}\n",
  "status": 200,
  "headers": {
    "Connection": "keep-alive",
    "Server": "gunicorn/19.9.0",
    "Date": "Thu, 13 Sep 2018 15:19:45 GMT",
    "Content-Type": "application/json",
    "Content-Length": "29",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Via": "1.1 vegur"
  }
}
```

#### DELETE

This action is used to make a DELETE request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|object|None|False|Payload to submit to the server when making the REST call|None|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body_object|object|False|Response payload from the server as an object|
|body_string|string|False|Response payload from the server as a string|
|headers|object|False|Response headers from the server|
|status|int|False|Status code of the response from the server|

Example output:

```
{
  "body_object": {
    "args": {},
    "data": "",
    "files": {},
    "form": {},
    "headers": {
      "Accept": "*/*",
      "Accept-Encoding": "gzip, deflate",
      "Connection": "close",
      "Content-Length": "0",
      "Host": "httpbin.org",
      "Referer": "https://google.com",
      "User-Agent": "Mozilla/5.0"
    },
    "json": null,
    "origin": "73.51.89.6",
    "url": "https://httpbin.org/delete"
  },
  "body_string": "{\n  \"args\": {}, \n  \"data\": \"\", \n  \"files\": {}, \n  \"form\": {}, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Accept-Encoding\": \"gzip, deflate\", \n    \"Connection\": \"close\", \n    \"Content-Length\": \"0\", \n    \"Host\": \"httpbin.org\", \n    \"Referer\": \"https://google.com\", \n    \"User-Agent\": \"Mozilla/5.0\"\n  }, \n  \"json\": null, \n  \"origin\": \"73.51.89.6\", \n  \"url\": \"https://httpbin.org/delete\"\n}\n",
  "status": 200,
  "headers": {
    "Connection": "keep-alive",
    "Server": "gunicorn/19.9.0",
    "Date": "Thu, 13 Sep 2018 15:14:55 GMT",
    "Content-Type": "application/json",
    "Content-Length": "385",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Via": "1.1 vegur"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Any headers set in the action will overwrite the default ones in the connection.

Any issues connecting to the remote service should be present in the log of the job that ran. If you find any issues that represent bugs in the plugin itself, please contact someone at Komand directly.

# Version History

* 3.0.1 - New spec and help.md format for the Hub
* 3.0.0 - Add basic auth support
* 2.0.0 - Update connection to handle SSL verification
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.4 - Bug fix for CI tool incorrectly uploading plugins
* 0.1.3 - Fix post and put actions by using JSON argument instead of body
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Update tags
* 0.1.0 - Initial plugin

# Links

## References

* [REST Architecture Style](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)

