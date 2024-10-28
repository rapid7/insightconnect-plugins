# Description

[Devo](https://www.devo.com/) is the cloud-native logging and security analytics solution that delivers real-time visibility for security and operations teams

# Key Features

* Query for log results
* Trigger workflows on new alerts

# Requirements

* A Devo authentication token

# Supported Product Versions

* v7.8.0

# Documentation

## Setup

To use the Devo plugin, you will need to create an authentication token. 

1. In Devo go to the left nav and choose Administration > Credentials
2. From the credentials screen, choose Authentication Tokens from the top tabs
3. Click 'CREATE NEW TOKEN'

The Devo authentication token must have access to the tables you are building your query for. In addition, if you are using the alert trigger, the access token will need access to: 
`siem.logtrust.alert.info`.

For testing purposes, to give access to all tables, use `*.*.**`. This is not recommended for final production use, but can be used to rule out access errors when configuring the plugin for the first time.  

[Authentication Token Documentation](https://docs.devo.com/confluence/ndt/latest/domain-administration/security-credentials/authentication-tokens) 

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|authentication_token|credential_secret_key|None|True|Devo authentication token|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|region|string|None|True|Region|["USA", "EU", "VDC (Spain)"]|USA|None|None|

Example input:

```
{
  "authentication_token": "9de5069c5afe602b2ea0a04b66beb2c0",
  "region": "USA"
}
```

## Technical Details

### Actions


#### Query Logs

This action is used to run a LINQ query against the logs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|from_date|string|None|True|Earliest date to query events from, will accept relative or absolute times, e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now|None|5 minutes ago|None|None|
|query|string|None|True|A query. The response is limited to 200MB of raw data or 1000 entries, whichever is hit first|None|from demo.ecommerce.data select *|None|None|
|to_date|string|Now|True|Latest date to query events from, will accept relative or absolute times, e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now|None|Now|None|None|
  
Example input:

```
{
  "from_date": "5 minutes ago",
  "query": "from demo.ecommerce.data select *",
  "to_date": "Now"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|query_result|True|An object containing information and results about the query that was run|None|
  
Example output:

```
{
  "results": {
    "timestamp": 1622211663530,
    "cid": "24d4cd197626",
    "status": 0,
    "object": [
      {
        "eventdate": 1622211602031,
        "clientIpAddress": "198.162.50.1",
        "timestamp": "28/May/2021:14:19:55 +0000",
        "method": "GET",
        "uri": "/category.screen?category_id=FURNITURE&JSESSIONID=SD10SL8FF6ADFF7",
        "protocol": "HTTP 1.1",
        "statusCode": 408,
        "bytesTransferred": 697,
        "referralUri": "http://www.example.com/cart.do?action=changequantity&itemId=LOG-69&product_id=235-40LSZ-09823&JSESSIONID=SD10SL8FF6ADFF7",
        "userAgent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "cookie": "mc0ocue109c4n9fkvof64ou0i1:-",
        "timeTaken": 891
      }
    ]
  }
}
```
### Triggers


#### Get New Alerts

This trigger is used to get new alerts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|10|False|Interval time in seconds|None|5|None|None|
  
Example input:

```
{
  "interval": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]object|True|An object containing information and results about the alerts from interval time|None|
  
Example output:

```
{
  "alerts": [
    {
      "alertHost": "backoffice",
      "alertId": "123456",
      "category": "my.context",
      "context": "my.alert.rapid7.asdf",
      "domain": "rapid7",
      "engine": "pil01-pro-custom-us-aws",
      "eventdate": 1643377735505,
      "extraData": "{\"clientIpAddress\":\"%2F87.210.152.183\",\"timeTaken\":\"909\",\"protocol\":\"HTTP+1.1\",\"bytesTransferred\":\"1381\",\"method\":\"GET\",\"cookie\":\"mc0ocue109c4n9fkvof64ou0i1%3A-\",\"userAgent\":\"Mozilla%2F5.0+%28Macintosh%3B+U%3B+Intel+Mac+OS+X+10_6_3%3B+en-US%29+AppleWebKit%2F533.4+%28KHTML%2C+like+Gecko%29+Chrome%2F5.0.375.38+Safari%2F533.4\",\"referralUri\":\"http%3A%2F%2Fwww.bing.com%2Fcategory.screen%3Fcategory_id%3DFURNITURE%26JSESSIONID%3DSD8SL8FF10ADFF4\",\"uri\":\"%2Fcart.do%3Faction%3Dview%26itemId%3DLOG-77%26product_id%3D009-73CKH-JASKD%26JSESSIONID%3DSD8SL8FF10ADFF4\",\"eventdate\":\"2022-01-28+13%3A48%3A36.498\",\"timestamp\":\"28%2FJan%2F2022%3A13%3A48%3A27+%2B0000\",\"statusCode\":\"500\"}",
      "priority": 3,
      "status": 0,
      "username": "user@example.com"
    },
    {
      "alertHost": "backoffice",
      "alertId": "12345",
      "category": "my.context",
      "context": "my.alert.rapid7.asdf",
      "domain": "rapid7",
      "engine": "pil01-pro-custom-us-aws",
      "eventdate": 1643379230038,
      "extraData": "{\"clientIpAddress\":\"%2F87.210.152.183\",\"timeTaken\":\"545\",\"protocol\":\"HTTP+1.1\",\"bytesTransferred\":\"3403\",\"method\":\"GET\",\"cookie\":\"mc0ocue109c4n9fkvof64ou0i1%3A-\",\"userAgent\":\"Opera%2F9.80+%28X11%3B+Linux+i686%3B+Ubuntu%2F14.10%29+Presto%2F2.12.388+Version%2F12.16\",\"referralUri\":\"http%3A%2F%2Fwww.logcasts.com%2Fcategory.screen%3Fcategory_id%3DBEDROOM%26JSESSIONID%3DSD3SL8FF6ADFF2\",\"uri\":\"%2Fcategory.screen%3Fcategory_id%3DBEDROOM%26JSESSIONID%3DSD3SL8FF6ADFF2\",\"eventdate\":\"2022-01-28+14%3A13%3A30.056\",\"timestamp\":\"28%2FJan%2F2022%3A14%3A13%3A18+%2B0000\",\"statusCode\":\"500\"}",
      "priority": 3,
      "status": 0,
      "username": "user@example.com"
    }
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert Host|string|None|False|Alert host|None|
|Alert ID|string|None|False|Alert ID|None|
|Application|string|None|False|Application|None|
|Category|string|None|False|Category|None|
|Context|string|None|False|Context|None|
|Domain|string|None|False|Domain|None|
|Destination Host|string|None|False|Destination host|None|
|Destination IP|string|None|False|Destination IP|None|
|Destination Port|string|None|False|Destination port|None|
|Engine|string|None|False|Engine|None|
|Event Date|integer|None|False|Event date|None|
|Extra Data|string|None|False|Extra data|None|
|Priority|float|None|False|Priority|None|
|Protocol|string|None|False|Protocol|None|
|Source Host|string|None|False|Source host|None|
|Source IP|string|None|False|Source IP|None|
|Source Port|string|None|False|Source port|None|
|Status|integer|None|False|Status|None|
|Username|string|None|False|Username|None|
  
**log_entry**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Bytes Transferred|integer|None|False|Bytes transferred|None|
|Client IP Address|string|None|False|Client IP address|None|
|Cookie|string|None|False|Cookie|None|
|Event Date|integer|None|False|Event date|None|
|Method|string|None|False|Method|None|
|Protocol|string|None|False|Protocol|None|
|Referral URI|string|None|False|Referral URI|None|
|Status Code|integer|None|False|Status code|None|
|Time Taken|integer|None|False|Time taken|None|
|Timestamp|string|None|False|Timestamp|None|
|URI|string|None|False|URI|None|
|User Agent|string|None|False|User agent|None|
  
**query_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CID|string|None|False|CID|None|
|Message|string|None|False|Message|None|
|Log Entries|[]log_entry|None|False|Log entries|None|
|Status|integer|None|False|Status|None|
|Timestamp|integer|None|False|Timestamp|None|


## Troubleshooting

* The plugin doesn't return all my results from a query. 

   The plugin is limited to 1000 entries or 200MB of data for queries, whichever is hit first. 

   To avoid this issue either rewrite your query to return fewer results, or you can use the `offset` keyword to paginate data. 

# Version History

* 3.0.2 - Bumping requirements.txt | SDK Bump to 6.1.4
* 3.0.1 - Fix an issue in Get New Alerts trigger to catch missing alerts
* 3.0.0 - Fix an issue in Get New Alerts trigger to filter duplicate alerts. Output contains list of new alerts
* 2.0.0 - Configuration for interval input parameter
* 1.0.0 - Initial plugin

# Links

* [Devo](https://www.devo.com/)

## References

* [Devo](https://www.devo.com/)
* [Authentication Token Documentation](https://docs.devo.com/confluence/ndt/latest/domain-administration/security-credentials/authentication-tokens)