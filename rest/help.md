# Description

The HTTP Requests plugin allows users to automate HTTP requests to API services such as [RESTful based services](https://en.wikipedia.org/wiki/Representational_state_transfer).
This plugin is often used to integrate with ad-hoc 3rd party API's in a workflow without going through the process of [building a new plugin](https://komand.github.io/python/index.html). It supports DELETE, GET, PATCH, POST, or PUT requests to the provided URI.

# Key Features

* Quickly integrate with 3rd party API's over HTTP

# Requirements

* A RESTFUL HTTP/HTTPS resource and supported authentication, if any

# Documentation

## Setup

Check out the [plugin guide](https://insightconnect.help.rapid7.com/docs/rest) for more details on how to configure this plugin.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_url|string|None|True|Base URL e.g. https://httpbin.org|None|https://httpbin.org/|
|basic_auth_credentials|credential_username_password|None|False||None|{"username": "user@example.com", "password": "mypassword"}|
|default_headers|object|None|False|Default headers to include in all requests associated with this connection e.g. { "User-Agent": "Rapid7 InsightConnect" }|None|{ "User-Agent": "Rapid7 InsightConnect"}|
|ssl_verify|boolean|True|True|Verify SSL certificate|None|True|

Example input:

```
{
  "base_url": "https://httpbin.org/",
  "basic_auth_credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "default_headers": {
    "User-Agent": "Rapid7 InsightConnect"
  },
  "ssl_verify": true
}
```

## Technical Details

### Actions

#### PUT

This action is used to make a PUT request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|body|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|

Example input:

```
{
  "body": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|body|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|

Example input:

```
{
  "body": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|body|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|

Example input:

```
{
  "body": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|

Example input:

```
{
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body_object|object|False|Response payload from the server as an object. Note, if the response has invalid object structure(list, string..) plugin will wrap it with object map|
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|body|object|None|False|Payload to submit to the server when making the HTTP Request call|None|{"user": "user@example.com"}|
|headers|object|None|False|Headers to use for the request. These will override any default headers|None|{"Host": "rapid7.com"}|
|route|string|None|True|The route to append to the base URL e.g. /org/users|None|/org/users|

Example input:

```
{
  "body": {
    "user": "user@example.com"
  },
  "headers": {
    "Host": "rapid7.com"
  },
  "route": "/org/users"
}
```

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

* 3.0.5 - Fix issue where a null body return on a successful request would crash the plugin
* 3.0.4 - Update REST plugin title to HTTP Requests
* 3.0.3 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://insightconnect.help.rapid7.com/docs/rest)
* 3.0.2 - Update to v3 Python plugin architecture | Support get endpoints returning lists
* 3.0.1 - New spec and help.md format for the Extension Library
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

* [HTTP Request Architecture Style](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
* [InsightConnect HTTP Request Plugin Guide](https://insightconnect.help.rapid7.com/docs/rest)
