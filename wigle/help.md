
# WiGLE

## About

[WiGLE](https://wigle.net/index) (Wireless Geographic Logging Engine) consolidates location and information of wireless networks world-wide to a central database, and has user-friendly desktop and web applications that can map, query and update the database via the web.

This plugin utilizes the [WiGLE API](https://api.wigle.net/swagger).

## Actions

### Get Network Details

This action is used to get details and observation records for a single network. It provides unique information for a WiFi or cell network to request detailed information. Providing a netid value searches WiFi, operator searches GSM, and system searches CDMA.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|network|integer|None|False|None|None|
|cid|integer|None|False|GSM Cell ID|None|
|operator|integer|None|False|GSM Operator ID|None|
|basestation|integer|None|False|CDMA Base Station ID|None|
|netid|string|None|False|The WiFi Network BSSID to search|None|
|system|integer|None|False|CDMA System ID|None|
|lac|integer|None|False|GSM Location Area Code|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|wifi|boolean|False|None|
|cdma|boolean|False|None|
|gsm|boolean|False|None|
|results|[]network_record|False|None|
|addresses|[]geocode|False|None|

Example output:

```
{
  "cdma": false,
  "gsm": false,
  "wifi": false,
  "addresses": [
    {
      "address": {
        "country": "",
        "country_code": "jp"
      },
      "lat": 36.5748441,
      "lon": 139.2394179,
      "importance": 0.90670922399871,
      "place_id": 174823796,
      "licence": "Data OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright",
      "osm_type": "relation",
      "display_name": "",
      "boundingbox": [
        20.2145811,
        45.7112046,
        122.7141754,
        154.205541
      ]
    }
  ],
  "results": [
    {
      "trilat": 34.73895264,
      "trilong": 137.40457153,
      "ssid": "1B701C0F5DABA53F414E1A9D367131E9",
      "qos": 2,
      "transid": "20150725-00538",
      "firsttime": "2015-07-26T19:58:22.000Z",
      "lasttime": "2016-03-29T06:15:31.000Z",
      "lastupdt": "2018-08-29T08:32:52.000Z",
      "netid": "00:1D:73:0B:4F:B0",
      "type": "infra",
      "comment": "Appended by test_user on 2018-08-29 01:05:54:\n\nA comment\n\nAppended by test_user on 2018-08-29 01:32:40:\n\nAcomment\n\nAppended by test_user on 2018-08-29 01:32:52:\n\nA comment",
      "wep": "W",
      "channel": 11,
      "bcninterval": 0,
      "freenet": "?",
      "dhcp": "?",
      "paynet": "?",
      "locationData": [
        {
          "alt": 74,
          "accuracy": 4,
          "lastupdt": "2015-07-26T04:05:07.000Z",
          "latitude": 34.7383728,
          "longitude": 137.40545654,
          "month": "201507",
          "ssid": "1B701C0F5DABA53F414E1A9D367131E9",
          "time": "2015-07-26T19:58:22.000Z",
          "signal": -80,
          "name": "Clever name",
          "netId": "126484172720",
          "noise": 0,
          "snr": 0,
          "wep": "W",
          "encryptionValue": "WPA"
        }
      ],
      "encryption": "wpa"
    }
  ]
}
```

### Get Files Status

This action is used to get the status of files uploaded by the current user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pagestart|integer|0|False|Most recent record to fetch descending chronologically. Defaults to 0|None|
|pageend|integer|100|False|Number of results to fetch from offset. Defaults to 100|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]transaction|True|Information about uploaded files|
|processingQueueDepth|integer|True|None|

Example output:

```
{
  "results": [
    {
      "transid": "string",
      "username": "string",
      "firstTime": "2018-08-28T17:24:07.478Z",
      "lastupdt": "2018-08-28T17:24:07.478Z",
      "fileName": "string",
      "fileSize": 0,
      "fileLines": 0,
      "status": "string",
      "discoveredGps": 0,
      "discovered": 0,
      "total": 0,
      "totalGps": 0,
      "totalLocations": 0,
      "percentDone": 0,
      "timeParsing": 0,
      "genDiscovered": 0,
      "genDiscoveredGps": 0,
      "genTotal": 0,
      "genTotalGps": 0,
      "genTotalLocations": 0,
      "wait": 0
    }
  ],
  "processingQueueDepth": 0
}
```

### Get Metadata

This action is used to get metadata for cell networks - optionally filter by country and network codes (MCC and MNC).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|mnc|string|None|False|Network code (MNC) to filter|None|
|mcc|string|None|False|Country code (MCC) to filter|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cell_network_metadata|[]cell_mcc|True|Metadata for cell networks, arranged by MCC, then by MNC|

Example output:

```
{
  "cell_network_metadata": [
    {
      "mcc": "288",
      "cell_mncs": [
        {
          "mnc": "01",
          "metadata": {
            "type": "National",
            "countryName": "Faroe Islands (Kingdom of Denmark)",
            "countryCode": "FO",
            "mcc": "288",
            "mnc": "01",
            "brand": "Faroese Telecom",
            "operator": "Faroese Telecom",
            "status": "Operational",
            "bands": "GSM 900 / UMTS 900 / UMTS 2100 / LTE 800 / LTE 1800"
          }
        },
        {
          "mnc": "02",
          "metadata": {
            "type": "National",
            "countryName": "Faroe Islands (Kingdom of Denmark)",
            "countryCode": "FO",
            "mcc": "288",
            "mnc": "02",
            "brand": "Hey",
            "operator": "Vodafone Faroe Islands",
            "status": "Operational",
            "bands": "GSM 900 / UMTS 2100 / LTE 1800",
            "notes": "Former Kall, also uses MCC 274 MNC 02 (Iceland)"
          }
        },
        {
          "mnc": "03",
          "metadata": {
            "type": "National",
            "countryName": "Faroe Islands (Kingdom of Denmark)",
            "countryCode": "FO",
            "mcc": "288",
            "mnc": "03",
            "operator": "Edge Mobile Sp/F",
            "status": "Not operational",
            "bands": "GSM 1800",
            "notes": "Planned"
          }
        }
      ]
    }
  ]
}
```

### Get Region Statistics

This action is used to get statistics for a specified country, organized by region.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|country|string|us|False|The two-letter code of the country for which you'd like a regional breakdown. Defaults to 'US'|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|regions|[]object|True|None|
|country|string|True|None|
|postalCode|[]object|True|None|
|encryption|[]object|True|None|

Example output:

```
{
  "country": "jp",
  "regions": [
    {
      "region": "",
      "count": 5907792
    },
    {
      "region": "",
      "count": 750393
    }
  ],
  "encryption": [
    {
      "wep": "2",
      "count": 7160339
    },
    {
      "wep": "Y",
      "count": 1941846
    }
  ],
  "postalCode": [
    {
      "postalCode": "052-201-4814",
      "count": 80525
    },
    {
      "postalCode": "460-8688",
      "count": 79119
    }
  ]
}
```

### Get User Profile

This action is used to get the user object for the current logged-in user.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|session|string|False|None|
|joindate|date|True|None|
|lastlogin|date|True|None|
|donate|string|True|None|
|userid|string|True|None|
|email|string|True|None|

Example output:

```
{
  "userid": "test_user",
  "email": "test@example.org",
  "donate": "?",
  "joindate": "2018-08-08T17:23:04.000Z",
  "lastlogin": "2018-08-29T14:50:30.000Z"
}
```

### Get Country Statistics

This action is used to get statistics organized by country.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|countries|[]object|True|All countries and basic stats|

Example output:

```
{
  "countries": [
    {
      "country": "US",
      "count": 203188123
    },
    {
      "country": "DE",
      "count": 34100489
    },
    {
      "country": "NL",
      "count": 24067503
    },
    {
      "country": "CA",
      "count": 21483456
    },
    {
      "country": "JP",
      "count": 12013736
    }
  ]
}
```

### Search Cells

This action is used to query the WiGLE cell database for paginated results based on multiple criteria. API and session authentication default to a page size of 100 results/page. COMMAPI defaults to a page size of 25 with a maximum of 1000 results per return. Number of daily queries allowed per user are throttled based on history and participation.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|longrange1|float|None|False|Lesser of two longitudes by which to bound the search (specify both)|None|
|longrange2|float|None|False|Greater of two longitudes by which to bound the search (specify both)|None|
|latrange2|float|None|False|Greater of two latitudes by which to bound the search (specify both)|None|
|latrange1|float|None|False|Lesser of two latitudes by which to bound the search (specify both)|None|
|notmine|string|None|False|Only search for networks first seen by other users|None|
|onlymine|string||False|Search only for points first discovered by the current user. Use any string to set, leave unset for general search. Can't be used with COMMAPI auth, since these are points you have locally|None|
|cell_net|string|None|False|Cell LAC (GSM/LTE/WCDMA) or Network (CDMA) ID parameter by which to filter|None|
|cell_id|string|None|False|Cell ID(GSM/LTE/WCDMA) or Basestation (CDMA) parameter by which to filter|None|
|ssidlike|string|None|False|Include only cell towers matching the string network name, allowing wildcards '%' (any string) and '_' (any character)|None|
|searchAfter|integer|None|False|Previous page's search_after to get the next page. Use this instead of 'first'|None|
|minQoS|integer|None|False|Minimum Quality of Signal (0-7)|None|
|cell_op|string|None|False|Cell Operator (GSM/LTE/WCDMA) or System (CDMA) ID parameter by which to filter|None|
|showCdma|string|None|False|Include CDMA cell networks|None|
|showGsm|string|None|False|Include GSM cell networks|None|
|ssid|string|None|False|Include only cell towers exactly matching the string network name|None|
|endTransID|string|None|False|Latest transaction ID by which to bound (year-level precision only)|None|
|lastupdt|string|None|False|Filter points by how recently they've been updated, condensed date/time numeric string format yyyyMMdd[hhmm[ss]]|None|
|startTransID|string|None|False|Earliest transaction ID by which to bound (year-level precision only)|None|
|resultsPerPage|integer|None|False|How many results to return per request. Defaults to 25 for COMMAPI, 100 for site. Bounded at 1000 for COMMAPI, 100 for site|None|
|variance|float|None|False|How tightly to bound queries against the provided latitude/longitude box. Value must be between 0.001 and 0.2. Intended for use with non-exact decimals and geocoded bounds|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_after|integer|False|None|
|last|integer|True|None|
|resultCount|integer|True|None|
|totalResults|integer|True|None|
|results|[]cell_record|True|Matched cells|
|first|integer|True|None|

Example output:

```
{
  "totalResults": 999,
  "search_after": 20,
  "first": 1,
  "last": 2,
  "resultCount": 2,
  "results": [
    {
      "trilat": 48.01654816,
      "trilong": 37.82863617,
      "ssid": "MTS UKR",
      "qos": 2,
      "transid": "20120817-00000",
      "firsttime": "2012-08-17T08:00:00.000Z",
      "lasttime": "2012-11-24T07:00:00.000Z",
      "lastupdt": "2018-03-28T22:00:00.000Z",
      "city": "",
      "region": "",
      "country": "UA",
      "id": "25501_60827_12832",
      "attributes": "GPRS;ua",
      "gentype": "GSM"
    },
    {
      "trilat": 37.49578476,
      "trilong": 13.44348812,
      "qos": 0,
      "transid": "20150424-00000",
      "firsttime": "2015-04-24T20:00:00.000Z",
      "lasttime": "2015-04-24T20:00:00.000Z",
      "lastupdt": "2018-03-28T22:00:00.000Z",
      "housenumber": "",
      "road": "Strada Statale Corleonese Agrigentina",
      "city": "",
      "region": "SIC",
      "country": "IT",
      "id": "22288_45091_38424959",
      "attributes": "UMTS;it",
      "gentype": "GSM"
    }
  ]
}
```

### Get General Statistics

This action is used to get a named map of general statistics.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|statistics|object|True|None|

Example output:

```
{
  "statistics": {
    "octet": false,
    "netwpa2": 297891746,
    "android": false,
    "netwpa3": 1,
    "gentotal": 10001758,
    "manufacturer": true,
    "netnowep": 20677147,
    "dfltssid": 13104735,
    "dfltwpkn": 0,
    "trans2da": 961,
    "netwpa": 29079578,
    "trans1da": 1064,
    "nettotal": 471916436,
    "nettoday": 38103,
    "netwep?": 92491408,
    "loctotal": 6730417785,
    "netwep": 32294041,
    "ssidStatistics": [
      {
        "name": "xfinitywifi",
        "value": 9533081
      },
      {
        "name": "linksys",
        "value": 3079971
      }
    ],
    "netwwwd3": 221378,
    "manufacturerStatistics": [
      {
        "name": "Cisco Systems, Inc",
        "value": 28263824
      },
      {
        "name": "Netgear",
        "value": 27731830
      }
    ],
    "transtot": 2341560,
    "ieeeManufacturerStatistics": [
      {
        "name": "Cisco Systems, Inc",
        "value": 28454480
      },
      {
        "name": "NETGEAR",
        "value": 27731830
      }
    ],
    "dfltnowp": 0,
    "genloc": 9946019,
    "netlocdy": 37856,
    "netloc": 466651973,
    "transtdy": 178,
    "userstot": 216687,
    "netlocd2": 292860
  }
}
```

### Add Comment

This action is used to add a comment to the network.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|The comment to attach|None|
|netid|string|None|False|The BSSID of the network for the comment, e.g. '0A\:2C\:EF\:3D\:25\:1B'|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comment|string|False|None|
|netid|string|False|None|

Example output:

```
{
  "comment": "Appended by anon on 2018-08-29 01:05:54:\n\nA comment",
  "netid": "00:1D:73:0B:4F:B0"
}
```

### Get KML

This action is used to get a KML summary approximation for a successfully processed file uploaded by the current user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|transid|string|None|True|The unique transaction ID for the file|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|kml|string|False|String representing a KML summary approximation|

Example output:

```
{
  "kml": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n            <kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:gx=\"http://www.google.com/kml/ext/2.2\" xmlns:xal=\"urn:oasis:names:tc:ciq:xsdschema:xAL:2.0\" xmlns:atom=\"http://www.w3.org/2005/Atom\">\n                <Document>\n                    <name>MyMarkers</name>\n                    <Style id=\"highConfidence\">\n                        <IconStyle id=\"highConfidenceStyle\">\n                            <scale>1.0</scale>\n                            <heading>0.0</heading>\n                            <Icon>\n                                <href>http://maps.google.com/mapfiles/kml/pushpin/grn-pushpin.png</href>\n                                <refreshInterval>0.0</refreshInterval>\n                                <viewRefreshTime>0.0</viewRefreshTime>\n                                <viewBoundScale>0.0</viewBoundScale>\n                            </Icon>\n                        </IconStyle>\n                    </Style>\n                    <Style id=\"mediumConfidence\">\n                        <IconStyle id=\"medConfidenceStyle\">\n                            <scale>1.0</scale>\n                            <heading>0.0</heading>\n                            <Icon>\n                                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>\n                                <refreshInterval>0.0</refreshInterval>\n                                <viewRefreshTime>0.0</viewRefreshTime>\n                                <viewBoundScale>0.0</viewBoundScale>\n                            </Icon>\n                        </IconStyle>\n                    </Style>\n                    <Style id=\"lowConfidence\">\n                        <IconStyle id=\"lowConfidenceStyle\">\n                            <scale>1.0</scale>\n                            <heading>0.0</heading>\n                            <Icon>\n                                <href>http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png</href>\n                                <refreshInterval>0.0</refreshInterval>\n                                <viewRefreshTime>0.0</viewRefreshTime>\n                                <viewBoundScale>0.0</viewBoundScale>\n                            </Icon>\n                        </IconStyle>\n                    </Style>\n                    <Style id=\"zeroConfidence\">\n                        <IconStyle id=\"zeroConfidenceStyle\">\n                            <scale>1.0</scale>\n                            <heading>0.0</heading>\n                            <Icon>\n                                <href>http://maps.google.com/mapfiles/kml/pushpin/wht-pushpin.png</href>\n                                <refreshInterval>0.0</refreshInterval>\n                                <viewRefreshTime>0.0</viewRefreshTime>\n                                <viewBoundScale>0.0</viewBoundScale>\n                            </Icon>\n                        </IconStyle>\n                    </Style>\n                    <Placemark>\n                        <name>COMPLETELYNEWSSID123456</name>\n                        <open>1</open>\n                        <description>Network ID: AA:29:CC:BB:BB:BB\n            Encryption: WPA2\n            Time: 2018-07-16T17:18:00.000-07:00\n            Signal: -87.0\n            Accuracy: 1071.0\n            </description>\n                        <styleUrl>#zeroConfidence</styleUrl>\n                        <Point>\n                            <coordinates>11.5,50.11000061</coordinates>\n                        </Point>\n                    </Placemark>\n                </Document>\n            </kml>\n            "
}
```

### Get User Tokens

This action is used to get all authorization tokens for the logged-in user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|type|string|None|False|Token types - 'API', 'COMMAPI', or 'ANDROID'|['API', 'COMMAPI', 'ANDROID']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tokens|[]token|True|List of matching tokens or an empty list|

Example output:

```
{
  "tokens": [
    {
      "authName": "AID5945ddaae0f0aec31e334e3be768e815",
      "token": "2f3e1b24382059f9ebc5eb518c4ecf50",
      "status": "STATUS_ACTIVE",
      "type": "API",
      "personId": 221291
    }
  ]
}
```

### Get Network Geocode

This action is used to get coordinates for an address for use in searching. Relies on OpenStreetMap nominatim.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|addresscode|string|None|False|An address string, Street, City, State/Region, Country|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]geocode|True|Matched geocode|

Example output:

```
{
  "results": [
    {
      "address": {
        "country": "",
        "country_code": "jp"
      },
      "lat": 36.5748441,
      "lon": 139.2394179,
      "importance": 0.90670922399871,
      "place_id": 174823796,
      "licence": "Data OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright",
      "osm_type": "relation",
      "display_name": "",
      "boundingbox": [
        20.2145811,
        45.7112046,
        122.7141754,
        154.205541
      ]
    }
  ]
}
```

### Get Group Statistics

This action is used to get statistics organized by group.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|groups|[]object|True|All groups and basic stats|

Example output:

```
{
  "groups": [
    {
      "groupId": "20041206-00006",
      "groupName": "Netstumbler Forum users",
      "owner": "g8tk33per",
      "discovered": 21695080,
      "total": 28180457,
      "genDisc": 63853,
      "members": 151,
      "joined": false,
      "groupOwner": false
    },
    {
      "groupId": "20060104-00055",
      "groupName": "The netherlands wireless",
      "owner": "redlin",
      "discovered": 7552591,
      "total": 12977197,
      "genDisc": 116475,
      "members": 23,
      "joined": false,
      "groupOwner": false
    }
  ]
}
```

### Get User Statistics

This action is used to get statistics and badge image for the authenticated user.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|monthRank|integer|True|None|
|statistics|standing|True|None|
|user|string|True|None|
|imageBadgeUrl|string|True|None|
|message|string|False|None|
|rank|integer|True|None|

Example output:

```
{
  "groups": [
    {
      "groupId": "20041206-00006",
      "groupName": "Netstumbler Forum users",
      "owner": "g8tk33per",
      "discovered": 21695080,
      "total": 28180457,
      "genDisc": 63853,
      "members": 151,
      "joined": false,
      "groupOwner": false
    },
    {
      "groupId": "20060104-00055",
      "groupName": "The netherlands wireless",
      "owner": "redlin",
      "discovered": 7552591,
      "total": 12977197,
      "genDisc": 116475,
      "members": 23,
      "joined": false,
      "groupOwner": false
    }
  ]
}
```

### Search Networks

This action is used to query the WiGLE network database for paginated results based on multiple criteria. API and session authentication default to a page size of 100 results/page. COMMAPI defaults to a page size of 25 with a maximum of 1000 results per return. Number of daily queries allowed per user are throttled based on history and participation.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|longrange1|float|None|False|Lesser of two longitudes by which to bound the search (specify both)|None|
|longrange2|float|None|False|Greater of two longitudes by which to bound the search (specify both)|None|
|latrange2|float|None|False|Greater of two latitudes by which to bound the search (specify both)|None|
|latrange1|float|None|False|Lesser of two latitudes by which to bound the search (specify both)|None|
|notmine|string|None|False|Only search for networks first seen by other users|None|
|onlymine|string||False|Search only for points first discovered by the current user. Use any string to set, leave unset for general search. Can't be used with COMMAPI auth, since these are points you have locally|None|
|paynet|boolean|False|False|Include only networks that have been marked as for-pay access|None|
|ssidlike|string|None|False|Include only networks matching the string network name, allowing wildcards '%' (any string) and '_' (any character)|None|
|searchAfter|integer|None|False|Previous page's search_after to get the next page. Use this instead of 'first'|None|
|minQoS|integer|None|False|Minimum Quality of Signal (0-7)|None|
|ssid|string|None|False|Include only networks exactly matching the string network name|None|
|endTransID|string|None|False|Latest transaction ID by which to bound (year-level precision only)|None|
|lastupdt|string|None|False|Filter points by how recently they've been updated, condensed date/time numeric string format yyyyMMdd[hhmm[ss]]|None|
|encryption|string|None|False|Encryption detected\: 'None', 'WEP', 'WPA', 'WPA2', 'WPA3', 'Unknown'. Case insensitive|['None', 'WEP', 'WPA', 'WPA2', 'WPA3', 'Unknown']|
|netid|string|None|False|Include only networks matching the string network BSSID, e.g. '0A\:2C\:EF\:3D\:25\:1B' or '0A\:2C\:EF'. The first three octets are required|None|
|freenet|boolean|False|False|Include only networks that have been marked as free access|None|
|startTransID|string|None|False|Earliest transaction ID by which to bound (year-level precision only)|None|
|resultsPerPage|integer|None|False|How many results to return per request. Defaults to 25 for COMMAPI, 100 for site. Bounded at 1000 for COMMAPI, 100 for site|None|
|variance|float|None|False|How tightly to bound queries against the provided latitude/longitude box. Value must be between 0.001 and 0.2. Intended for use with non-exact decimals and geocoded bounds|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_after|integer|False|None|
|last|integer|True|None|
|resultCount|integer|True|None|
|totalResults|integer|True|None|
|results|[]network_record|True|Matched networks|
|first|integer|True|None|

Example output:

```
{
  "totalResults": 471931729,
  "search_after": 377910,
  "first": 1,
  "last": 100,
  "resultCount": 100,
  "results": [
    {
      "trilat": 43.0449028,
      "trilong": 141.29222107,
      "ssid": "0AFEE49737B2C7167C005095768C3228",
      "qos": 0,
      "transid": "20150603-00000",
      "firsttime": "2015-05-31T16:00:00.000Z",
      "lasttime": "2015-06-02T22:00:00.000Z",
      "lastupdt": "2015-06-15T09:00:00.000Z",
      "housenumber": "",
      "road": "",
      "city": "",
      "region": "",
      "country": "JP",
      "netid": "00:1D:73:0B:4F:75",
      "type": "infra",
      "wep": "Y",
      "channel": 5,
      "bcninterval": 0,
      "freenet": "?",
      "dhcp": "?",
      "paynet": "?",
      "userfound": false,
      "encryption": "wep"
    },
    {
      "trilat": 34.73895264,
      "trilong": 137.40457153,
      "ssid": "1B701C0F5DABA53F414E1A9D367131E9",
      "qos": 2,
      "transid": "20150725-00000",
      "firsttime": "2015-07-26T12:00:00.000Z",
      "lasttime": "2016-03-28T23:00:00.000Z",
      "lastupdt": "2016-03-28T23:00:00.000Z",
      "housenumber": "",
      "road": "",
      "city": "",
      "region": "",
      "country": "JP",
      "netid": "00:1D:73:0B:4F:B0",
      "type": "infra",
      "wep": "W",
      "channel": 11,
      "bcninterval": 0,
      "freenet": "?",
      "dhcp": "?",
      "paynet": "?",
      "userfound": false,
      "encryption": "wpa"
    }
  ]
}
```

### Get User Standings

This action is used to get user standings.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sort|string|None|False|The criteria by which to sort the results. Values are ['discovered', 'total', 'monthcount', 'prevmonthcount', 'gendisc', 'gentotal', 'firsttransid', 'lasttransid']|['discovered', 'total', 'monthcount', 'prevmonthcount', 'gendisc', 'gentotal', 'firsttransid', 'lasttransid']|
|pagestart|integer|None|False|The first record to request according to the 'sort' parameter|None|
|pageend|integer|None|False|The last record to request according to the 'sort' parameter|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|myUsername|string|True|None|
|pageStart|integer|True|None|
|totalUsers|integer|True|None|
|sortBy|string|True|None|
|eventView|boolean|True|None|
|results|[]standing|True|None|
|pageEnd|integer|True|None|

Example output:

```
{
  "eventView": false,
  "myUsername": "",
  "pageStart": 0,
  "pageEnd": 100,
  "totalUsers": 37023,
  "sortBy": "discovered",
  "results": [
    {
      "rank": 1,
      "monthRank": 0,
      "userName": "anonymous",
      "discoveredWiFiGPS": 36903238,
      "discoveredWiFiGPSPercent": 7.90782,
      "discoveredWiFi": 62723348,
      "discoveredCellGPS": 909784,
      "discoveredCell": 1302131,
      "eventMonthCount": 538224,
      "eventPrevMonthCount": 508524,
      "prevRank": 1,
      "prevMonthRank": 1,
      "totalWiFiLocations": 302954340,
      "first": "20011003-00001",
      "last": "20180829-00227",
      "self": false
    },
    {
      "rank": 2,
      "monthRank": 0,
      "userName": "ccie4526",
      "discoveredWiFiGPS": 12115146,
      "discoveredWiFiGPSPercent": 2.5961,
      "discoveredWiFi": 13522673,
      "discoveredCellGPS": 2155,
      "discoveredCell": 3543,
      "eventMonthCount": 113020,
      "eventPrevMonthCount": 51333,
      "prevRank": 2,
      "prevMonthRank": 15,
      "totalWiFiLocations": 171386632,
      "first": "20030127-00018",
      "last": "20180828-00846",
      "self": false
    }
  ]
}
```

### Upload File

This action is used to transmit a file for processing and incorporation into the database. Supports DStumbler, G-Mon, inSSIDer, Kismac, Kismet, MacStumbler, NetStumbler, Pocket Warrior, Wardrive-Android, WiFiFoFum, WiFi-Where, WiGLE WiFi Wardriving, and Apple consolidated DB formats. One or more files may be enclosed within a zip, tar, or tar.gz archive. Files may not exceed 140MiB, and archives WILL IGNORE more than 200 member files.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|donate|boolean|True|False|Allow commercial use of the file contents - 'on' to allow|None|
|file|file|None|False|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|warning|string|False|None|
|results|file_upload_results|True|None|
|observer|string|False|None|

Example output:

```
{
  "results": {
    "timeTaken": "0",
    "filesize": 6,
    "filename": "1535480859_FILE",
    "transids": [
      {
        "file": "1535480859_FILE",
        "size": 6,
        "transId": "20180828-00527"
      }
    ]
  },
  "observer": "anonymous"
}
```

### Get Site Statistics

This action is used to get a map of short-named statistics used in providing site-wide information.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|statistics|object|True|None|

Example output:

```
{
  "statistics": {
    "netwpa2": 297903981,
    "netwpa3": 1,
    "gentotal": 10004950,
    "netnowep": 20677193,
    "dfltssid": 13104735,
    "dfltwpkn": 0,
    "trans2da": 961,
    "netwpa": 29079784,
    "trans1da": 1064,
    "nettotal": 471930775,
    "nettoday": 52442,
    "netwep?": 92493113,
    "loctotal": 6730687824,
    "netwep": 32294188,
    "netwwwd3": 221378,
    "transtot": 2341606,
    "waitQueue": 0,
    "size": 24,
    "dfltnowp": 0,
    "genloc": 9949211,
    "netlocdy": 52193,
    "netloc": 466666310,
    "transtdy": 224,
    "userstot": 216690,
    "netlocd2": 292860
  }
}
```

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_name|string|None|True|API name provided by WiGLE|None|
|api_token|password|None|True|API token provided by WiGLE|None|

## Troubleshooting

The Upload File action will end successfully even if the file is in the incorrect format or does not introduce any new networks. In those cases, the Get KML action will raise an exception instead of returning an empty KML summary.

Analyzing a DB file takes a while. During that time, the Get KML action will raise an exception. To get the status of a DB file, the Get Files Status action has to be used. The `percentDone` field will indicate if the analysis has ended, and the `discovered` field will indicate if any new networks were discovered and therefore mean a KML file is available.

In the case where this plugin is used extensively, the API can respond with 'Too many queries today'.

## Versions

* 1.0.0 - Initial plugin

## Workflows

Examples:

* Searching for WiFi networks around the world
* Getting the location and other details of a specific network
* Extracting network information from DB files

## References

* [WiGLE](https://wigle.net/index)
* [WiGLE API](https://api.wigle.net/swagger)
* [Example WiGLE DB file](https://wigle.net/phpbb/viewtopic.php?t=1670)
