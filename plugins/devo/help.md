# Description

[Devo](https://www.devo.com/) is the cloud-native logging and security analytics solution that delivers real-time visibility for security and operations teams

# Key Features

* Query for log results
* Trigger workflows on new alerts

# Requirements

* A Devo authentication token

# Documentation

## Setup

To use the Devo plugin, you will need to create an authentication token. 

1. In Devo go to the left nav and choose Administration > Credentials
2. From the credentials screen, choose Authentication Tokens from the top tabs
3. Click 'CREATE NEW TOKEN'

The Devo authentication token must have access to the tables you are building your query for. In addition, if you are using the alert trigger, the access token will need access to: 
`siem.logtrust.alert.info`

For testing purposes, to give access to all tables, use `*.*.**`. This is not recommended for final production use, but can be used to rule out access errors when configuring the plugin for hte first time.  

[Authentication Token Documentation](https://docs.devo.com/confluence/ndt/latest/domain-administration/security-credentials/authentication-tokens) 


The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|authentication_token|credential_secret_key|None|True|Devo authentication token|None|9de5069c5afe602b2ea0a04b66beb2c0|
|region|string|None|True|Region|['USA', 'EU', 'VDC (Spain)']|USA|

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from_date|string|None|True|Earliest date to query events from, will accept relative or absolute times, e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now|None|5 minutes ago|
|query|string|None|True|A Query. The response be limited to 200 mb of raw data or 1000 entries whichever is hit first|None|from demo.ecommerce.data select *|
|to_date|string|Now|True|Latest date to query events from, will accept relative or absolute times, e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now|None|Now|

Example input:

```
{
  "from_date": "5 minutes ago",
  "query": "from demo.ecommerce.data select *",
  "to_date": "Now"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|query_result|True|An object containing information and results about the query that was run|

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

This trigger is used to get new alerts.

##### Input

_This trigger does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|object|True|An alert|

Example output:

```
{
  "alert": {
    "eventdate": 1622747437335,
    "alertHost": "backoffice",
    "domain": "rapid7",
    "priority": 3,
    "context": "my.alert.rapid7.example",
    "category": "my.context",
    "status": 0,
    "alertId": "26004002",
    "username": "user@example.com",
    "engine": "pil01-pro-custom-us-aws",
    "extraData": "{\"clientIpAddress\":\"192.168.50.1\",\"timeTaken\":\"176\",\"protocol\":\"HTTP+1.1\",\"bytesTransferred\":\"3295\",\"method\":\"GET\",\"cookie\":\"3djv1l0ebi7cmsai1131pf2a65%3A-\",\"userAgent\":\"Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F42.0.2311.135+Safari%2F537.36+Edge%2F12.246\",\"referralUri\":\"http%3A%2F%2Fwww.google.com%2Fcategory.screen%3Fcategory_id%3DBEDROOM%26JSESSIONID%3DSD1SL6FF5ADFF2\",\"uri\":\"%2Fcategory.screen%3Fcategory_id%3DBEDROOM%26JSESSIONID%3DSD1SL6FF5ADFF2\",\"eventdate\":\"2021-06-03+19%3A10%3A28.676\",\"timestamp\":\"03%2FJun%2F2021%3A19%3A10%3A26+%2B0000\",\"statusCode\":\"500\"}"
  }
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

* The plugin doesn't return all my results from a query. 

   The plugin is limited to 1000 entries or 200MB of data for queries, whichever is hit first. 

   To avoid this issue either rewrite your query to return fewer results, or you can use the `offset` keyword to paginate data. 

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Devo](https://www.devo.com/)
* [Authentication Token Documentation](https://docs.devo.com/confluence/ndt/latest/domain-administration/security-credentials/authentication-tokens)
