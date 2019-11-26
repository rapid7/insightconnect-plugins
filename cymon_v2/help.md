# Description

[Cymon](https://cymon.io/) is the largest open tracker of malware, phishing, botnets, spam, and more.
This plugin utilizes the Cymon [v2 API](http://docs.cymon.io/) and implements all its available actions.

**NOTE:** The Cymon service will be discontinued on April 30, 2019. Please plan to transition off this plugin before then.

The Cymon [v1 API](http://docs.cymon.io/v1/) actions can still be used in the original [Cymon](https://market.komand.com/plugins/rapid7/cymon/1.0.0) plugin.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_credentials|credential_username_password|None|False|Cymon API v2 credentials|None|

Cymon API supports anonymous access but with a rate limit. To use anonymous access, supply a username and password of `anonymous`.

## Technical Details

### Actions

#### Create Feed

This action is used to create a new feed for threat reports.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Feed name|None|
|privacy|string|public|True|Can be set to either `private` or `public` (default)|['private', 'public']|
|tos|string|None|False|Terms of Use for this feed|None|
|tags|[]string|None|True|List of tags to categorize and help others find this feed|None|
|admins|[]string|None|False|List of usernames that have `update`, `post`, and `read` permissions to this feed|None|
|link|string|None|False|URL for blog or website where users can learn more about this feed|None|
|guests|[]string|None|False|List of usernames that have `read` permission to this feed|None|
|members|[]string|None|False|List of usernames that have `post` and `read` permissions to this feed|None|
|logo|string|None|False|URL for small thumbnail for this feed (must be hosted on imgur CDN)|None|
|description|string|None|False|Feed description text|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|feed|feed|True|Newly created feed|

Example output:

```
{
  "feed": {
    "updated": "2018-11-17T20:01:02.875Z",
    "name": "A totally different test feed for Komand",
    "privacy": "private",
    "slug": "a-totally-different-test-feed-for-komand",
    "tags": [
      "malware",
      "ransomware"
    ],
    "created": "2018-11-17T20:01:02.874Z",
    "admins": [],
    "guests": [],
    "members": [],
    "owner": "komand_test",
    "id": "AWcjQynluPEX_z4v01Q3"
  }
}
```

#### Search

This action is used to search threat reports.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|search_by|string|None|True|Type of search value|['ip_address', 'domain_name', 'hostname', 'md5_hash', 'sha1_hash', 'sha256_hash', 'ssdeep_hash', 'term', 'feed_id']|
|value|string|None|True|The query value to search for|None|
|start_date|string|None|False|The start date for searching|None|
|end_date|string|None|False|The end date for searching|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|hits|[]searched_threat_report|True|Threat reports matching search value|

Example output:

```
{
  "hits": [
    {
      "feed": "senderbase.org",
      "title": "Spam activity",
      "reported_by": "cymon",
      "timestamp": "2018-07-14T04:06:08.000Z",
      "tags": [
        "spam"
      ],
      "feed_id": "AVsGXxCjVjrVcoBZyoh-",
      "link": "http://www.senderbase.org/lookup/?search_string=66.220.155.142",
      "location": {
        "country": "US",
        "city": "New York",
        "point": {
          "lat": 40.7143,
          "lon": -74.006
        }
      },
      "ioc": {
        "ip": "66.220.155.142",
        "domain": "facebook.com",
        "hostname": "66-220-155-142.mail-mail.facebook.com"
      },
      "id": "91bd5f515a1e0a93a4f4d689b123409fb214c1990e2735be8fb3f4b2a960e2b5"
    },
    {
      "feed": "hosts-file.net",
      "description": "Website: facebook.com.179863857.connect.user.19472973904038575.ajslyr36hur85.replymprevivaldi.angelas.cl \nIP: 192.141.168.137 \nClassification: PSH \nAdded: 5/30/2018 3:49:09 PM \nAdded By: TeMerc",
      "title": "Phishing activity",
      "reported_by": "cymon",
      "timestamp": "2018-05-30T15:49:00.000Z",
      "tags": [
        "phishing"
      ],
      "feed_id": "AVsGZTOOVjrVcoBZyoiQ",
      "link": "http://hosts-file.net/?s=facebook.com.179863857.connect.user.19472973904038575.ajslyr36hur85.replymprevivaldi.angelas.cl",
      "ioc": {
        "ip": "192.141.168.137",
        "domain": "angelas.cl",
        "hostname": "facebook.com.179863857.connect.user.19472973904038575.ajslyr36hur85.replymprevivaldi.angelas.cl"
      },
      "id": "402735dcb98b47e572da48723e53837b2fd067da211b05464322e2da37be9e77"
    },
    {
      "feed": "hosts-file.net",
      "description": "Website: facebook.com.3s3s.ru \nIP: 104.131.65.219 \nClassification: PSH \nAdded: 5/28/2018 8:56:10 AM \nAdded By: Stefan",
      "title": "Phishing activity",
      "reported_by": "cymon",
      "timestamp": "2018-05-28T08:56:00.000Z",
      "tags": [
        "phishing"
      ],
      "feed_id": "AVsGZTOOVjrVcoBZyoiQ",
      "link": "http://hosts-file.net/?s=facebook.com.3s3s.ru",
      "location": {
        "country": "US",
        "city": "Clifton",
        "point": {
          "lat": 40.8326,
          "lon": -74.1307
        }
      },
      "ioc": {
        "ip": "104.131.65.219",
        "domain": "3s3s.ru",
        "hostname": "facebook.com.3s3s.ru"
      },
      "id": "83af27ad4c6a9efd77a66c06ea230562447473c770fb21ef6d426a310d45cb8b"
    },
    {
      "feed": "hosts-file.net",
      "description": "Website: notify-facebook.com \nIP: 91.211.245.129 \nClassification: PSH \nAdded: 5/24/2018 5:14:10 PM \nAdded By: TeMerc",
      "title": "Phishing activity",
      "reported_by": "cymon",
      "timestamp": "2018-05-24T17:14:00.000Z",
      "tags": [
        "phishing"
      ],
      "feed_id": "AVsGZTOOVjrVcoBZyoiQ",
      "link": "http://hosts-file.net/?s=notify-facebook.com",
      "ioc": {
        "ip": "91.211.245.129",
        "domain": "notify-facebook.com",
        "hostname": "notify-facebook.com"
      },
      "id": "953ed52afc089cdceb7036d463889829eff582fd17e63736a58871246ebfead9"
    }
  ]
}
```

#### Submit Report

This action is used to upload a threat report with observables.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|report|uploaded_report|None|True|Report to upload|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|threat_report|True|Uploaded report|

Example output:

```
{
  "report": {
    "feed": "Test feed for komand",
    "description": "Very technical text",
    "tags": [
      "malware"
    ],
    "reported_by": "komand_test",
    "timestamp": 1509396994,
    "title": "New test report",
    "feed_id": "AWcd2qUMuPEX_z4v01Q2",
    "ioc": {
      "url": "https://google.com",
      "ip": "8.8.8.8",
      "domain": "google.com"
    },
    "id": "0d0f19991d5450a1d34d945971eed08d9d27e183d474d2ee14bca8bf7e569617"
  }
}
```

#### Submit Reports in Bulk

This action is used to upload multiple threat reports in one request. Each bulk request can support up to 500 records. Each record in the request can be as large as 1 MB, up to a limit of 5 MB for the entire request, including feed IDs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|reports|[]uploaded_report|None|True|Reports to upload|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reports|[]threat_report|True|Uploaded reports|

Example output:

```
{
  "reports": [
    {
      "feed": "Test feed for komand",
      "description": "Very technical text for bulk",
      "tags": [
        "malware"
      ],
      "reported_by": "komand_test",
      "timestamp": 1500396994,
      "title": "New test bulk report",
      "feed_id": "AWcd2qUMuPEX_z4v01Q2",
      "ioc": {
        "url": "https://google.com",
        "ip": "8.8.8.8",
        "domain": "google.com"
      },
      "id": "0d0f19991d5450a1d34d945971eed08d9d27e183d474d2ee14bca8bf7e569617"
    },
    {
      "feed": "Test feed for komand",
      "description": "Very technical text for bulk 2",
      "tags": [
        "malware"
      ],
      "reported_by": "komand_test",
      "timestamp": 1500396994,
      "title": "New test bulk report 2",
      "feed_id": "AWcd2qUMuPEX_z4v01Q2",
      "ioc": {
        "url": "https://really-google.com",
        "ip": "1.1.1.1",
        "domain": "not-google.com"
      },
      "id": "1d625197863fde4dd78a1c4e4f20b2461ed0931e52f7702cca8b36e1b067b465"
    }
  ]
}
```

#### List All Feeds

This action is used to get the list of feeds.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|privacy|string|None|False|Return list of `private` or `public` feeds|['all', 'private', 'public']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|feeds|[]feed|True|Feeds|

Example output:

```
{
  "feeds": [
    {
      "updated": "2018-11-16T18:25:46.241Z",
      "is_owner": true,
      "name": "A test feed",
      "created": "2018-11-16T18:25:46.241Z",
      "is_member": false,
      "privacy": "public",
      "slug": "a-test-feed",
      "is_admin": false,
      "is_guest": false,
      "id": "AWcdxZFyuPEX_z4v01Q1",
      "tags": [
        "malware"
      ]
    },
    {
      "updated": "2018-11-16T18:47:35.606Z",
      "is_owner": true,
      "name": "A test feed for Komand",
      "created": "2018-11-16T18:47:35.606Z",
      "is_member": false,
      "privacy": "public",
      "slug": "a-test-feed-for-komand",
      "is_admin": false,
      "is_guest": false,
      "id": "AWcd2Yw4ZDr3mu5zLPTF",
      "tags": [
        "malware"
      ]
    },
    {
      "updated": "2018-11-16T20:14:19.451Z",
      "is_owner": true,
      "name": "Test feed for komand",
      "created": "2018-11-16T18:48:47.524Z",
      "is_member": false,
      "privacy": "public",
      "slug": "test-feed-for-komand",
      "is_admin": false,
      "is_guest": false,
      "id": "AWcd2qUMuPEX_z4v01Q2",
      "tags": [
        "malware",
        "ransomware"
      ],
      "description": "Hello World"
    }
  ]
}
```

#### Update Feed

This action is used to update details of an existing feed.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|description|string|None|False|Feed description text|None|
|privacy|string|public|False|Can be set to either `private` or `public` (default)|['private', 'public']|
|tos|string|None|False|Terms of Use for this feed|None|
|tags|[]string|None|False|List of tags to categorize and help others find this feed|None|
|admins|[]string|None|False|List of usernames that have `update`, `post`, and `read` permissions to this feed|None|
|feed_id|string|None|True|The feed ID|None|
|link|string|None|False|URL for blog or website where users can learn more about this feed|None|
|guests|[]string|None|False|List of usernames that have `read` permission to this feed|None|
|members|[]string|None|False|List of usernames that have `post` and `read` permissions to this feed|None|
|logo|string|None|False|URL for small thumbnail for this feed (must be hosted on imgur CDN)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|feed|feed|True|Updated feed|

Example output:

```
{
  "feed": {
    "updated": "2018-11-16T23:12:20.648Z",
    "name": "Test feed for komand",
    "privacy": "public",
    "slug": "test-feed-for-komand",
    "tags": [
      "malware",
      "ransomware"
    ],
    "created": "2018-11-16T18:48:47.524Z",
    "admins": [],
    "guests": [],
    "members": [],
    "owner": "komand_test",
    "id": "AWcd2qUMuPEX_z4v01Q2",
    "description": "Hello World"
  }
}
```

#### Get Feed Details

This action is used to get a feed object.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|feed_id|string|None|True|Feed ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|feed|feed|True|Feed|

Example output:

```
{
  "feed": {
    "updated": "2017-06-12T14:28:22.519Z",
    "is_owner": false,
    "name": "zeustracker.abuse.ch",
    "created": "2017-03-25T17:25:57.534Z",
    "is_member": false,
    "privacy": "public",
    "slug": "zeustracker.abuse.ch",
    "link": "https://zeustracker.abuse.ch",
    "logo": "https://i.imgur.com/rBvuwon.jpg",
    "is_admin": false,
    "is_guest": false,
    "id": "AVsGgNL4VjrVcoBZyoib",
    "tags": [
      "malware",
      "c2",
      "c&c",
      "zeus",
      "tracker"
    ],
    "description": "This feed is run by @abuse_ch (as well as all other abuse.ch projects) for non-profit. For questions please refer to: https://zeustracker.abuse.ch"
  }
}
```

#### Get Report Document

This action is used to get the threat report from a feed.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|feed_id|string|None|True|Feed ID|None|
|report_id|string|None|True|Report ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|feed|feed|True|Feed|
|report|searched_threat_report|True|Report|

Example output:

```
{
  "feed": {
    "updated": "2017-06-12T13:59:28.961Z",
    "is_owner": false,
    "name": "hosts-file.net",
    "created": "2017-03-25T16:55:47.281Z",
    "is_member": false,
    "privacy": "public",
    "slug": "hostsfile.net",
    "link": "http://hosts-file.net",
    "logo": "https://i.imgur.com/v8qHr0t.png",
    "is_admin": false,
    "is_guest": false,
    "id": "AVsGZTOOVjrVcoBZyoiQ",
    "tags": [
      "malware",
      "phishing",
      "exploit",
      "ek"
    ],
    "description": "hpHosts is a community that manages and maintains hosts files that allows an additional layer of protection against access to ad, tracking and malicious websites."
  },
  "report": {
    "feed": "hosts-file.net",
    "description": "Website: notify-facebook.com \nIP: 91.211.245.129 \nClassification: PSH \nAdded: 5/24/2018 5:14:10 PM \nAdded By: TeMerc",
    "title": "Phishing activity",
    "reported_by": "cymon",
    "timestamp": "2018-05-24T17:14:00.000Z",
    "tags": [
      "phishing"
    ],
    "feed_id": "AVsGZTOOVjrVcoBZyoiQ",
    "link": "http://hosts-file.net/?s=notify-facebook.com",
    "ioc": {
      "ip": "91.211.245.129",
      "domain": "notify-facebook.com",
      "hostname": "notify-facebook.com"
    },
    "id": "953ed52afc089cdceb7036d463889829eff582fd17e63736a58871246ebfead9"
  }
}
```

#### List User Feeds

This action is used to get the list of feeds that a user has access to.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|feeds|[]feed|True|Feeds|

Example output:

```
{
  "feeds": [
    {
      "updated": "2018-11-16T18:25:46.241Z",
      "is_owner": true,
      "name": "A test feed",
      "created": "2018-11-16T18:25:46.241Z",
      "is_member": false,
      "privacy": "public",
      "slug": "a-test-feed",
      "is_admin": false,
      "is_guest": false,
      "id": "AWcdxZFyuPEX_z4v01Q1",
      "tags": [
        "malware"
      ]
    },
    {
      "updated": "2018-11-16T18:47:35.606Z",
      "is_owner": true,
      "name": "A test feed for Komand",
      "created": "2018-11-16T18:47:35.606Z",
      "is_member": false,
      "privacy": "public",
      "slug": "a-test-feed-for-komand",
      "is_admin": false,
      "is_guest": false,
      "id": "AWcd2Yw4ZDr3mu5zLPTF",
      "tags": [
        "malware"
      ]
    },
    {
      "updated": "2018-11-16T20:14:19.451Z",
      "is_owner": true,
      "name": "Test feed for komand",
      "created": "2018-11-16T18:48:47.524Z",
      "is_member": false,
      "privacy": "public",
      "slug": "test-feed-for-komand",
      "is_admin": false,
      "is_guest": false,
      "id": "AWcd2qUMuPEX_z4v01Q2",
      "tags": [
        "malware",
        "ransomware"
      ],
      "description": "Hello World"
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.3 - New spec and help.md format for the Hub
* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Add discontinuation of Cymon notice
* 1.0.0 - Initial plugin

# Links

## References

* [Cymon](https://cymon.io/)
* [Cymon API](http://docs.cymon.io/)

