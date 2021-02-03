# Description

[InsightAppSec’s](https://www.rapid7.com/products/insightappsec/) DAST capabilities and InsightConnect’s automation prowess can help you simplify your SDLC Process with this scan management plugin. The need for automation becomes paramount in the fast moving landscape of modern web scanning and automating you web app scanning with this plugin can save you loads of time to allow you to focus on remediating issues to get your app into product faster!

This plugin utilizes the [Rapid7 InsightAppSec API](https://insightappsec.help.rapid7.com/docs/get-started-with-the-insightappsec-api).

# Key Features

* Create and configure scans
* Run scans and return results

# Requirements

* Requires an API Key from Insight platform

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|The API key for InsightAppSec|None|abc12345-abc1-2345-abc1-abc123456789|
|url|string|https://us.api.insight.rapid7.com|True|The region specific URL endpoint for InsightAppSec|None|https://us.api.insight.rapid7.com|

Example input:

```
{
  "api_key": {
    "secretKey": "abc12345-abc1-2345-abc1-abc123456789"
  },
  "url": "https://us.api.insight.rapid7.com"
}
```

## Technical Details

### Actions

#### Get All Attack Templates

This action is used to get a list of all the available attack templates.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|integer|0|False|The page number of the return data set|None|1|
|size|integer|100|False|The data set size or the max number of apps to return per page|None|100|
|sort|string|ASC|False|How to sort the response|None|ASC|

Example input:

```
{
  "index": 1,
  "size": 100,
  "sort": "ASC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]attack_template|False|App data|
|links|[]link|False|Links to data|
|metadata|object|False|Metadata for the app results|

Example output:

```
{
  "data": [

    {
      "id": "11111111-0000-0000-0000-000000000002",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/attack-templates/11111111-0000-0000-0000-000000000002",
          "rel": "self"
        }
      ],
      "name": "OWASP 2013",
      "system_defined": true
    },
    {
      "id": "11111111-0000-0000-0000-000000000001",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/attack-templates/11111111-0000-0000-0000-000000000001",
          "rel": "self"
        }
      ],
      "name": "Crawl only",
      "system_defined": true
    }
    ],
    "links": [
      {
        "href": "https://us.api.insight.rapid7.com:443/ias/v1/attack-templates",
        "rel": "self"
      }
    ],
    "metadata": {
      "index": 0,
      "size": 100,
      "total_data": 2,
      "total_pages": 1
    }
  }
```

#### One Attack Template

This action is used to get one atack template.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|UUID os the attack template|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attack_template|attack_template|False|The full attack template|

Example output:

```
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "links": [
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/attack-templates/11111111-0000-0000-0000-000000000004",
      "rel": "self"
    }
  ],
  "name": "Passive analysis",
  "system_defined": true
}
```

#### Dissociate a User from an Application

This action is used to remove a user from accessing an application.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|Application UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|
|user_id|string|None|True|User UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "user_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 204
}
```

#### Get Users Associated with an Application

This action is used to a list of users with access to an application.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|Application UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user_id|[]submitter|False|A list of users UUID|

Example output:

```
{
  "user_id": [
    {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
  ]
}
```

#### Submit Scan

This action is used to submit a new scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_config_id|string|None|True|UUID of the scan config to use|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "scan_config_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_id|string|True|Scan UUID|

Example output:

```
{
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Associate a User to an Application

This action is used to add a user for access to an application.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|Application UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|
|user_id|string|None|True|User UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "user_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 201
}
```

#### Update an Existing Application

This action is used to update the name or description of an existing Application.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_description|string|None|False|Describe the application|None|Do not scan during business hours|
|app_id|string|None|True|Application UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|
|app_name|string|None|True|The name of an application|None|Application Name|

Example input:

```
{
  "app_description": "Do not scan during business hours",
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "app_name": "Application Name"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 200
}
```

#### Delete Application

This action is used to delete an existing application.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|Application UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 204
}
```

#### Get One App

This action is used to get limited details about an existing App.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|Application UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx|

Example input:

```
{
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|app_description|string|False|Describe the application|
|app_id|string|False|Application UUID|
|app_name|string|False|The name of the application|
|links|[]link|False|A list of links|

Example output:

```
{
  "app_description": "Describe the application",
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
  "app_name": "app.example.com",
  "links": [
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/apps/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
      "rel": "self"
    }
  ]
}
```

#### Create App

This action is used to create a new app asset.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_description|string|None|False|Describe the application|None|An optional description|
|app_name|string|None|True|The name of the application|None|Name Of the APP|

Example input:

```
{
  "app_description": "An optional description",
  "app_name": "Name Of the APP"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|app_id|string|True|Application UUID|

Example output:

```
{
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
}
```

#### Get All Apps

This action is used to get a page of all apps.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|integer|0|False|The page number of the return data set|None|1|
|size|integer|100|False|The data set size or the max number of apps to return per page|None|100|
|sort|string|ASC|False|How to sort the response|None|ASC|

Example input:

```
{
  "index": 1,
  "size": 100,
  "sort": "ASC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]app|False|App data|
|links|[]link|False|Links to data|
|metadata|object|False|Metadata for the app results|

Example output:

```
{
  "data": [
    {
      "description": "https://betadash.example.com",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/apps/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "rel": "self"
        }
      ],
      "name": "ZA4-betadash.example.com"
    },
    {
      "description": "http://literature.example.com/",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/apps/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "rel": "self"
        }
      ],
      "name": "36-007-0-literature.example.com/"
    }
  ],
  "links": [
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/apps?index=0\u0026size=2",
      "rel": "first"
    },
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/apps",
      "rel": "self"
    },
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/apps?index=1\u0026size=2",
      "rel": "next"
    },
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/apps?index=793\u0026size=2",
      "rel": "last"
    }
  ],
  "metadata": {
    "index": 0,
    "size": 2,
    "total_data": 1587,
    "total_pages": 794
  }
}


```

#### Get All Schedules

This action is used to get a page of Schedules.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|integer|0|False|The page number of the return data set|None|1|
|size|integer|100|False|The data set size or the max number of apps to return per page|None|100|
|sort|string|ASC|False|How to sort the response|None|ASC|

Example input:

```
{
  "index": 1,
  "size": 100,
  "sort": "ASC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]schedule|False|Response data|
|links|[]link|False|Links to data|
|metadata|object|False|Metadata for the scedules|

Example output:

```
{
  "data": [
    {
      "enabled": true,
      "first_start": "2020-11-16T18:30:00-05:00[US/Eastern]",
      "frequency": {
        "interval": 0,
        "type": "ONCE"
      },
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/schedules/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "rel": "self"
        }
        ],
        "name": "rescan",
        "scan_config": {
          "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        }
      },
      {
        "enabled": true,
        "first_start": "2019-10-23T16:15:00-04:00[US/Eastern]",
        "frequency": {
          "interval": 0,
          "type": "ONCE"
        },
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/schedules/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "rel": "self"
        }
      ],
      "name": "rescan",
      "scan_config": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      }
    }
  ],
  "links": [
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/schedules?index=0\u0026size=2",
      "rel": "first"
      },
      {
        "href": "https://us.api.insight.rapid7.com:443/ias/v1/schedules",
        "rel": "self"
      },
      {
        "href": "https://us.api.insight.rapid7.com:443/ias/v1/schedules?index=1\u0026size=2",
        "rel": "next"
      },
      {
        "href": "https://us.api.insight.rapid7.com:443/ias/v1/schedules?index=382\u0026size=2",
        "rel": "last"
      }
    ],
    "metadata": {
      "index": 0,
      "size": 2,
      "total_data": 765,
      "total_pages": 383
    }
  }
```

#### Create Scan Config

This action is used to create a new scan configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|App UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|
|assignment_environment|string|CLOUD|True|Where the scan will run from ON_PREMISE or CLOUD|['CLOUD', 'ON_PREMISE']|CLOUD|
|assignment_id|string|default|True|The UUID of the engine Group|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|
|assignment_type|string|ENGINE_GROUP|True|The type of engine assignment|None|ENGINE_GROUP|
|attack_template_id|string|None|True|Attack template UUID|None|11111111-0000-0000-0000-000000000000|
|config_description|string|None|False|The description of the scan configuration|None|Description for scan config|
|config_name|string|None|True|The name of the scan configuration|None|Scan Config 1|

Example input:

```
{
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "assignment_environment": "CLOUD",
  "assignment_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "assignment_type": "ENGINE_GROUP",
  "attack_template_id": "11111111-0000-0000-0000-000000000000",
  "config_description": "Description for scan config",
  "config_name": "Scan Config 1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_config_id|string|False|Application UUID|

Example output:

```
{
  "scan_config_id": "00000000-0000-0000-000000000000"
}
```

#### Get Scan Config

This action is used to get a scan configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_config_id|string|None|True|Scan configuration UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx|

Example input:

```
{
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|app_id|string|False|App UUID|
|assignment_environment|string|False|Where the scan engine runs, cloud or on-premise|
|assignment_id|string|False|UUID of the engine group assignment|
|assignment_type|string|False|A static string|
|attack_template_id|string|False|Attack template UUID|
|config_description|string|False|The description of the scan configuration|
|config_name|string|False|The name of the scan configuration|
|errors|[]string|False|A list of errors that detail any current validation failures|
|id|string|False|The UUID of the scan configuration|
|links|[]link|False|A list of links|

Example output:

```
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
  "config_name": "update_test",
  "config_description": "testing update",
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
  "attack_template_id": "11111111-0000-0000-0000-000000000000",
  "errors": [
    "Seed URL list must not be empty",
    "Crawling Scope Constraint list must not be empty"
  ],
  "links": [
    {
      "rel": "self",
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
    }
  ]
}
```

#### Update Scan Config

This action is used to update an existing scan configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|App UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx|
|assignment_environment|string|CLOUD|False|Where the scan will run from ON_PREMISE or CLOUD|['CLOUD', 'ON_PREMISE']|CLOUD|
|assignment_id|string|default|False|The UUID of the engine Group|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|
|assignment_type|string|ENGINE_GROUP|False|The type of engine assignment|None|ENGINE_GROUP|
|attack_template_id|string|None|True|Attack template UUID|None|11111111-0000-0000-0000-000000000000|
|config_description|string|None|False|The description of the scan configuration|None|Description of scan config|
|config_name|string|None|True|The name of the scan configuration|None|Scan Config 1|
|scan_config_id|string|None|True|Scan configuration UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
  "assignment_environment": "CLOUD",
  "assignment_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "assignment_type": "ENGINE_GROUP",
  "attack_template_id": "11111111-0000-0000-0000-000000000000",
  "config_description": "Description of scan config",
  "config_name": "Scan Config 1",
  "scan_config_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 200
}
```

#### Delete Scan Config

This action is used to delete an existing scan config.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_config_id|string|None|True|Scan configuration UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx|

Example input:

```
{
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 204
}
```

#### Get Scan Configs

This action is used to get a page of scan configurations, based on supplied pagination parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|include-errors|boolean|False|False|Include validation errors in scan configs, can be expensive|None|True|
|index|integer|0|False|The page number of the return data set|None|1|
|size|integer|100|False|The data set size or the max number of apps to return per page|None|100|
|sort|string|ASC|False|How to sort the response|None|scanconfig.name,DESC|

Example input:

```
{
  "include-errors": true,
  "index": 1,
  "size": 100,
  "sort": "scanconfig.name,DESC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]scan_config|False|A list of scan configurations|
|links|[]link|False|Links to data|
|metadata|object|False|Metadata for the scan results|

Example output:

```
{
  "data": [
    {
      "app": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      },
      "assignment": {
        "environment": "CLOUD",
        "type": "ENGINE_GROUP"
      },
      "attack_template": {
        "id": "11111111-0000-0000-0000-000000000004"
      },
      "description": "no auth",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "links": [
         {
           "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
           "rel": "self"
         }
       ],
       "name": "00-000-0-EX-WK-Across-CORP"
     },
     {
       "app": {
         "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
       },
       "assignment": {
         "environment": "CLOUD",
         "type": "ENGINE_GROUP"
         },
         "attack_template": {
           "id": "11111111-0000-0000-0000-000000000004"
         },
         "description": "LOHING LOCKED OUT 8/6/2020\nuser: user@example.com",
         "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
         "links": [
           {
             "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
             "rel": "self"
           }
         ],
         "name": "00-003-0-EX3-BE-HCE-EES-LCL-www.test-community"
       }
     ],
     "links": [
       {
         "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs?index=0\u0026size=2",
         "rel": "first"
       },
       {
         "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs",
         "rel": "self"
       },
       {
         "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs?index=1\u0026size=2",
         "rel": "next"
       },
       {
         "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs?index=793\u0026size=2",
         "rel": "last"
       }
     ],
     "metadata": {
       "index": 0,
       "size": 2,
       "total_data": 1587,
       "total_pages": 794
     }
   }
```

#### Get Scan

This action is used to get a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|The scans UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx|

Example input:

```
{
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan|scan|False|Information on the scan|

Example output:

```
{
  "scan": {
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
    "app_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
    "scan_config_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
    "submitter": {
      "type": "USER",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
    },
    "submit_time": "2019-01-08T22:04:46.402",
    "completion_time": "2019-01-08T22:53:38.385",
    "status": "COMPLETE",
    "failure_reason": "",
    "links": [
      {
        "rel": "self",
        "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
      }
    ]
  }
}
```

#### Get Scans

This action is used to get a page of scans, based on supplied pagination parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|integer|0|False|The page index to start form. If blank, index will be 0|None|1|
|size|integer|50|False|The number of entries on each page. If blank, size will be 50|None|50|
|sort|string|ASC|False|How to sort the scans. If blank, sort will be alphabetical by scan name|None|scan.submit_time,DESC|

Example input:

```
{
  "index": 1,
  "size": 50,
  "sort": "scan.submit_time,DESC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]scan|False|A list of scans|
|links|[]link|False|Links to data|
|metadata|object|False|Metadata for the scan results|

Example output:

```
{
  "data": [
    {
      "app": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
      },
      "completion_time": "2020-09-18T05:17:19.023323",
      "failure_reason": "BAD_AUTH",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "rel": "self"
        }
      ],
      "scan_config": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
      },
      "status": "FAILED",
      "submit_time": "2020-09-18T05:01:20.444567",
      "submitter": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
        "type": "USER"
      }
    },
    {
      "app": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
      },
      "completion_time": "2020-09-20T05:26:43.782992",
      "failure_reason": "NETWORK_UNAVAILABLE",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "rel": "self"
        }
      ],
      "scan_config": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
      },
      "status": "FAILED",
      "submit_time": "2020-09-20T05:01:24.252861",
      "submitter": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
        "type": "USER"
      }
    }
  ],
  "links": [
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans?index=0\u0026size=2",
      "rel": "first"
    },
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans",
      "rel": "self"
    },
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans?index=1\u0026size=2",
      "rel": "next"
    },
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans?index=13461\u0026size=2",
      "rel": "last"
    }
  ],
  "metadata": {
    "index": 0,
    "size": 2,
    "total_data": 26924,
    "total_pages": 13462
  }
}
```

#### Delete Scan

This action is used to delete a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|The scans UUID|None|xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 204
}
```

#### Submit Scan Action

This action is used to submit a new scan action.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|Pause|True|Action to take|['Pause', 'Resume', 'Stop', 'Cancel', 'Authenticate']|Pause|
|scan_id|string|None|True|Scan UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|

Example input:

```
{
  "action": "Pause",
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 200
}
```

#### Get Scan Engine Events

This action is used to get the engine events from a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|Scan UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx|

Example input:

```
{
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]event_log|False|An array of event logs and their dates|

Example output:

```
{
  "events": [
    {
      "time": "2019-01-09T20:18:39.536",
      "event": "Scan is awaiting scheduling"
    }
  ]
}
```

#### Get Scan Execution Details

This action is used to get real-time details of the execution of a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|Scan UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx|

Example input:

```
{
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|details|scan_details|False|Detailed information about the scan|

Example output:

```
{
  "details": {
    "logged_in": false,
    "links_in_queue": 0,
    "links_crawled": 0,
    "attacks_in_queue": 0,
    "attacked": 0,
    "vulnerable": 0,
    "requests": 0,
    "failed_requests": 0,
    "network_speed": 0,
    "drip_delay": 0
  }
}
```

#### Get Scan Platform Events

This action is used to get the platform events from a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|Scan UUID|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx|

Example input:

```
{
  "scan_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]event_log|False|An array of event logs and their dates|

Example output:

```
{
  "events": [
    {
      "time": "2019-01-09T20:18:47.751",
      "event": "Sending scan state action START"
    },
    {
      "time": "2019-01-09T20:18:50.464",
      "event": "Sending scan state action CANCEL"
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

* 2.0.0 - Update all actions with better error logging routine and adding all the current endpoints and actions that were missing in previous versions
* 1.0.2 - Update to v4 Python plugin runtime | Add example inputs
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [InsightAppSec API](https://insightappsec.help.rapid7.com/docs/get-started-with-the-insightappsec-api)
