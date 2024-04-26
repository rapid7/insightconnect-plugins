# Description

The RSS plugin can monitor any generic [RSS](https://en.wikipedia.org/wiki/RSS) feed.

This plugin returns a generic `object` since each RSS feed can have its own data structure.
Use [input templating](https://docs.rapid7.com/insightconnect/format-strings-with-templates/), [Python Script plugin](https://docs.rapid7.com/insightconnect/python-2-or-3-script/), or the [JQ plugin](https://market.komand.com/plugins/komand/jq/0.1.3) to retrieve specific outputs.

# Key Features

* Monitor an RSS feed

# Requirements

* The URL for the feed you want to monitor

# Supported Product Versions
  
*This plugin does not contain any supported product versions.*

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|url|string|None|True|Feed URL|None|https://example.com/rss/current|None|None|

Example input:

```
{
  "url": "https://example.com/rss/current"
}
```

## Technical Details

### Actions
  
*This plugin does not contain any actions.*
### Triggers


#### Poll Feed

This trigger is used to poll feed for latest event

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|15|True|How frequently (in seconds) to poll for new entries|None|15|None|None|
  
Example input:

```
{
  "frequency": 15
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|object|True|RSS data|{"title": "First item title", "title_detail": {"type": "text/plain", "language": null, "base": "", "value": "First item title"}, "links": [{"rel": "alternate", "type": "text/html", "href": "http://example.org/item/1"}, {"url": "", "rel": "enclosure"}], "link": "http://example.org/item/1", "summary": "Watch out for\n<span>\nnasty tricks</span>", "summary_detail": {"type": "text/html", "language": null, "base": "", "value": "Watch out for\n<span>\nnasty tricks</span>"}, "authors": [{"email": "mark@example.org"}], "author": "mark@example.org", "author_detail": {"email": "mark@example.org"}, "tags": [{"term": "Miscellaneous", "scheme": null, "label": null}], "comments": "http://example.org/comments/1", "id": "http://example.org/guid/1", "guidislink": false, "published": "Thu, 05 Sep 2002 0:00:01 GMT"}|
  
Example output:

```
{
  "results": {
    "author": "mark@example.org",
    "author_detail": {
      "email": "mark@example.org"
    },
    "authors": [
      {
        "email": "mark@example.org"
      }
    ],
    "comments": "http://example.org/comments/1",
    "guidislink": false,
    "id": "http://example.org/guid/1",
    "link": "http://example.org/item/1",
    "links": [
      {
        "href": "http://example.org/item/1",
        "rel": "alternate",
        "type": "text/html"
      },
      {
        "rel": "enclosure",
        "url": ""
      }
    ],
    "published": "Thu, 05 Sep 2002 0:00:01 GMT",
    "summary": "Watch out for\n<span>\nnasty tricks</span>",
    "summary_detail": {
      "base": "",
      "language": null,
      "type": "text/html",
      "value": "Watch out for\n<span>\nnasty tricks</span>"
    },
    "tags": [
      {
        "label": null,
        "scheme": null,
        "term": "Miscellaneous"
      }
    ],
    "title": "First item title",
    "title_detail": {
      "base": "",
      "language": null,
      "type": "text/plain",
      "value": "First item title"
    }
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
The `Poll` trigger only pulls the most recent events and runs workflows on them. No new items are reported between workflow runs.

# Version History

* 1.0.6 - `Poll`: Fixed issue where trigger would return all entries on startup
* 1.0.5 - Update links to Rapid7 documentation in `help.md` to use new [Rapid7 documentation URL](https://docs.rapid7.com/insightconnect/)
* 1.0.4 - Change Frequency input description in Poll Feed trigger | Add example inputs
* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Fixed issue where Poll Feed was logging unnecessary information
* 1.0.1 - Support web server mode
* 1.0.0 - Update to v2 Python plugin architecture | Add granular object output
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Feedparser](https://github.com/kurtmckee/feedparser)

## References

* [Feedparser](https://github.com/kurtmckee/feedparser)
* [Input Templating](https://docs.rapid7.com/insightconnect/format-strings-with-templates/)
* [Python Script plugin](https://docs.rapid7.com/insightconnect/python-2-or-3-script/)