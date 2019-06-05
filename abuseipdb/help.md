
# AbuseIPDB

## About

[AbuseIPDB](https://www.abuseipdb.com) is a free service which allows you to look up IP reports, or report an abusive IP.
This plugin utilizes the [AbuseIPDB](https://www.abuseipdb.com/api.html).

## Actions

### Report IP

This action is used to report an abusive IP address.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Describe the type of malicious activity e.g. Brute forcing Wordpress login|None|
|categories|string|None|True|Comma delineated list of category IDs e.g. 10,12,15. Entire list is available at https\://www.abuseipdb.com/categories|None|
|address|string|None|True|IPv4 or IPv6 address to report e.g. 8.8.8.8, \:\:1|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip|string|False|IP address submitted|
|success|boolean|False|Submission success|

Example output:

```

{
  "ip": "68.66.205.227",
  "success": True
}

```

If an error occurs with the API, the action will return a structured output indicating the error.

Example output:

```

[
  {
    "id": "Unprocessable Entity",
    "links": {
      "about": "https:\\/\\/www.abuseipdb.com\\/api"
    },
    "status": "422",
    "code": "1002",
    "title": "The request was well-formed but was unable to be followed due to semantic errors.",
    "detail": "We expected an IPv4 or IPv6 address (e.g. 8.8.8.8)."
  }
]

```

### Check IP

This action is used to look up an IP address in the database.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IPv4 or IPv6 address e.g. 8.8.8.8, \:\:1|None|
|verbose|boolean|True|True|When set, reports will include the comment (if any) and the reporter's user id number (0 if reported anonymously)|None|
|days|string|30|True|Check for IP reports in the last x days|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|Whether an IP address was found in the database|
|list|ip|False|List of IP reports|

Example output:

```

{
  "found": true
  [
    {
      "ip": "8.8.8.8",
      "category": [
        9,
        13,
        14
      ],
      "created": "Wed, 16 May 2018 20:24:36 +0000",
      "country": "United States",
      "isoCode": "US",
      "isWhitelisted": true
    },
    {
      "ip": "8.8.8.8",
      "category": [
        4,
        14
      ],
      "created": "Fri, 11 May 2018 22:30:54 +0000",
      "country": "United States",
      "isoCode": "US",
      "isWhitelisted": true
    },
    ...
  ]
}

```

If AbuseIPDB has no information about the IP address, the action will return an empty list and the value of `found` will be `false`.
This makes it easy to perform another action in a workflow based on whether desired information is present using an Automated Decision step.

Example output:

```

{
  "list": [],
  "found": false
}

```

If an error occurs with the API, the action will return a structured output indicating the error.

Example output:

```

[
  {
    "id": "Unprocessable Entity",
    "links": {
      "about": "https:\\/\\/www.abuseipdb.com\\/api"
    },
    "status": "422",
    "code": "1002",
    "title": "The request was well-formed but was unable to be followed due to semantic errors.",
    "detail": "We expected an IPv4 or IPv6 address (e.g. 8.8.8.8)."
  }
]

```

### Check CIDR

This action is used to look up a CIDR address in the database.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr|string|None|True|IPv4 address block in CIDR notation e.g. 207.126.144.0/20|None|
|days|string|30|True|Check for CIDR reports in the last x days|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|netmask|string|False|Netmask|
|networkAddress|string|False|Network address|
|maxAddress|string|False|Maximum address|
|reportedIPs|[]reportedIPs|False|List of reported IPs|
|numPossibleHosts|integer|False|Number of possible hosts|
|addressSpaceDesc|string|False|Address space description|
|minAddress|string|False|Minimum address|

Example output:

```

{
  "networkAddress": "207.126.144.0",
  "netmask": "255.255.240.0",
  "minAddress": "207.126.144.1",
  "maxAddress": "207.126.159.254",
  "numPossibleHosts": 4094,
  "addressSpaceDesc": "Internet",
  "reportedIPs": [
    {
      "IP": "207.126.159.254",
      "NumReports": 1,
      "MostRecentReport": "2018-05-04 06:04:22",
      "Public": 1,
      "CountryCode": "US",
      "IsWhitelisted": 0,
      "abuseConfidenceScore": 0
    }
  ]
}

```

If an error occurs with the API, the action will return a structured output indicating the error.

Example output:

```

[
  {
    "id": "Unprocessable Entity",
    "links": {
      "about": "https:\\/\\/www.abuseipdb.com\\/api"
    },
    "status": "422",
    "code": "1025",
    "title": "The request was well-formed but was unable to be followed due to semantic errors.",
    "detail": "Invalid CIDR format.",
    "source": {
      "parameter": "network"
    }
  }
]

```

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_secret_key|None|True|API key|None|

## Troubleshooting

There's a rate limit on the free API service. The following error messags `429 Client Error: Too Many Requests for url` indicates that threshold has been hit.

## Versions

* 1.0.0 - Initial plugin
* 2.0.0 - Add `found` output to Check IP action | Support new credential type
* 3.0.0 - Support new credential_secret_key type

## Workflows

Examples:

* Intelligence

## References

* [AbuseIPDB](https://www.abuseipdb.com)
* [AbuseIPDB API](https://www.abuseipdb.com/api.html)
