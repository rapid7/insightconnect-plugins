# Description

The RSS plugin can monitor any generic [RSS](https://en.wikipedia.org/wiki/RSS) feed.

This plugin returns a generic `object` since each RSS feed can have its own data structure.
Use [input templating](https://docs.rapid7.com/insightconnect/format-strings-with-templates/), [Python Script plugin](https://docs.rapid7.com/insightconnect/python-2-or-3-script/), or the [JQ plugin](https://market.komand.com/plugins/komand/jq/0.1.3) to retrieve specific outputs.

# Key Features

* Monitor an RSS feed

# Requirements

* The URL for the feed you want to monitor

# Documentation

## Setup

This plugin requires a RSS feed URL.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|Feed URL|None|https://example.com/rss/current|

Example input:

```
{
  "url": "https://example.com/rss/current"
}
```

## Technical Details

### Actions

_This plugin does not contain any actions._

### Triggers

#### Poll Feed

This trigger monitors an RSS feed for the latest event.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|15|True|How frequently (in seconds) to poll for new entries|None|15|

Example input:

```
{
  "frequency": 15
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|True|RSS data|

Example output:

```

{
  "results": {
    "title": "Interesting Article on Marcus Hutchins",
    "title_detail": {
      "type": "text/plain",
      "language": null,
      "base": "https://www.schneier.com/blog/atom.xml",
      "value": "Interesting Article on Marcus Hutchins"
    },
    "links": [
      {
        "rel": "alternate",
        "type": "text/html",
        "href": "https://www.schneier.com/blog/archives/2018/03/interesting_art_1.html"
      }
    ],
    "link": "https://www.schneier.com/blog/archives/2018/03/interesting_art_1.html",
    "id": "tag:www.schneier.com,2018:/blog//2.11498",
    "guidislink": false,
    "published": "2018-03-16T11:12:59Z",
    "published_parsed": [
      2018,
      3,
      16,
      11,
      12,
      59,
      4,
      75,
      0
    ],
    "updated": "2018-03-16T11:12:59Z",
    "updated_parsed": [
      2018,
      3,
      16,
      11,
      12,
      59,
      4,
      75,
      0
    ],
    "summary": "This is a good article on the complicated story of hacker Marcus Hutchins....",
    "summary_detail": {
      "type": "text/plain",
      "language": null,
      "base": "https://www.schneier.com/blog/atom.xml",
      "value": "This is a good article on the complicated story of hacker Marcus Hutchins...."
    },
    "authors": [
      {
        "name": "Bruce Schneier"
      }
    ],
    "author_detail": {
      "name": "Bruce Schneier"
    },
    "author": "Bruce Schneier",
    "tags": [
      {
        "term": "bitcoin",
        "scheme": "http://www.sixapart.com/ns/types#tag",
        "label": "bitcoin"
      },
      {
        "term": "cybersecurity",
        "scheme": "http://www.sixapart.com/ns/types#tag",
        "label": "cybersecurity"
      },
      {
        "term": "fraud",
        "scheme": "http://www.sixapart.com/ns/types#tag",
        "label": "fraud"
      },
      {
        "term": "hacking",
        "scheme": "http://www.sixapart.com/ns/types#tag",
        "label": "hacking"
      },
      {
        "term": "killswitch",
        "scheme": "http://www.sixapart.com/ns/types#tag",
        "label": "kill switch"
      },
      {
        "term": "privacy",
        "scheme": "http://www.sixapart.com/ns/types#tag",
        "label": "privacy"
      },
      {
        "term": "ransomware",
        "scheme": "http://www.sixapart.com/ns/types#tag",
        "label": "ransomware"
      }
    ],
    "content": [
      {
        "type": "text/html",
        "language": "en-us",
        "base": "https://www.schneier.com/blog/",
        "value": "<p><a href=\"https://nymag.com/selectall/2018/03/marcus-hutchins-hacker.html\">This</a> is a good article on the complicated story of hacker Marcus Hutchins.</p>"
      }
    ]
  }
}

```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Between workflow runs, new items will *not* be reported on.

# Version History

* 1.0.5 - Update links to Rapid7 documentation in `help.md` to use new [Rapid7 documentation URL](https://docs.rapid7.com/insightconnect/)
* 1.0.4 - Change Frequency input description in Poll Feed trigger | Add example inputs
* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Fixed issue where Poll Feed was logging unnecessary information
* 1.0.1 - Support web server mode
* 1.0.0 - Update to v2 Python plugin architecture | Add granular object output
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Feedparser](https://github.com/kurtmckee/feedparser)
* [Input Templating](https://docs.rapid7.com/insightconnect/format-strings-with-templates/)
* [Python Script plugin](https://docs.rapid7.com/insightconnect/python-2-or-3-script/)
