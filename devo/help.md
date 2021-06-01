# Description

Devo is the cloud-native logging and security analytics solution that delivers real-time visibility for security and operations teams

# Key Features

* Query for log results

# Requirements

* A Devo authentication token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|authentication_token|credential_secret_key|None|True|Authentication Token|None|9de5069c5afe602b2ea0a04b66beb2c0|
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
|from_date|string|None|True|Earliest date to query events from, will accept relative or absolute times. e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now|None|5 minutes ago|
|query|string|None|True|A Query. The response be limited to 200 mb of raw data or 1000 entries whichever is hit first|None|from from demo.ecommerce.data select *|
|to_date|string|Now|True|Latest date to query events from, will accept relative or absolute times. e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now|None|Now|

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

_This plugin does not contain any triggers._

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

* [devo](LINK TO PRODUCT/VENDOR WEBSITE)
