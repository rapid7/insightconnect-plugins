# Description

[Rapid7 tCell](https://www.tcell.io/) is a Next-Gen Cloud WAF that enables web applications to defend themselves by combining in-app instrumentation (RASP) and analytics in the cloud.

This plugin utilizes the [tCell API](https://docs.tcell.io).

# Key Features

* Add and remove IP addresses from blacklists
* Post configuration changes

# Requirements

* Requires an API Key from the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key generated for the tCell account|None|

## Technical Details

### Actions

#### Post Configuration Changes

This action is used to rewrite the app configurations, either in part or in full.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|config|object|None|True|Whole new configuration or a part of it that should be updated|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|'Nothing to update' in case the configuration was not changed|
|id|integer|False|ID of a new, updated configuration|

Example output:

```
{
  "message": "Nothing to update"
}
```

#### List Apps

This action is used to fetch app name and app ID for all apps in a customer environment.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|total|integer|False|The number of items returned|
|apps|[]app|False|A list of apps|

Example output:

```
{
  "total": 7,
  "apps": [
    {
      "id": "MooseLifeTest-gIglw",
      "name": "MooseLife Test"
    },
    {
      "id": "WebGoat-0lWBQ",
      "name": "WebGoat"
    },
    {
      "id": "WebGoatNginx-JMg68",
      "name": "WebGoat Nginx"
    },
    {
      "id": "StephenHynesApp-FDET0",
      "name": "Stephen Hynes App"
    },
    {
      "id": "KomandIntegrations-zKt1g",
      "name": "Komand Integrations"
    },
    {
      "id": "LowprofileappcreatedforKomandplugintests-1oRtT",
      "name": "Low profile app created for Komand plugin tests"
    },
    {
      "id": "LowprofileappcreatedforKomandplugintests-3l1tp",
      "name": "Low profile app created for Komand plugin tests"
    }
  ]
}
```

#### Add Tags

This action is used to add all the tags posted in the body to the set of tags the app already has.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|App ID|None|
|tags|[]string|None|True|List of strings, choosing the new tags for the application|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Successfully updated tags|

Example output:

```
{
  "success": true
}
```

#### Get Route Details

This action is used to fetch details for the route with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|route_id|string|None|True|Route ID|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|route|route|False|Details for the provided route, including the route ID, http method, route pattern used by the framework, and a code signature for the controller|

Example output:

```
{
  "route": {
    "id": "1257378454",
    "method": "post",
    "pattern": "org.eclipse.jetty.server.session.SessionHandler",
    "controller": "org.eclipse.jetty.server.session.SessionHandler"
  }
}
```

#### Get Configuration

This action is used to fetch the configuration with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|config_id|integer|None|True|Configuration ID|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|config|object|False|The configuration data for the given configuration ID|

Example output:

```
{
  "config": {
    "id": 1,
    "version": 1,
    "blockedips": {
      "suspiciousMode": "Disabled",
      "blacklistedIps": [],
      "whitelistedIps": [],
      "version": 1,
      "configId": 1
    },
    "blockedpaths": {
      "paths": [],
      "version": 1,
      "configId": 1
    },
    "login": {
      "loginFailedEnabled": true,
      "loginSuccessEnabled": true,
      "sessionHijackingEnabled": true,
      "version": 1,
      "configId": 1
    },
    "jsconfig": {
      "jsAgentApiKey": "AQEBBAFFIhPMQItOr7VO4duFN47cjDNZw8g4Sru-NamK5PtA0bFdhbX9eFGrOjIxCHGyLIY",
      "allowedScriptPatterns": [],
      "allowedScriptIds": [],
      "excludedPaths": [],
      "notes": {
        "scriptIds": {},
        "scriptPatterns": {}
      },
      "version": 1,
      "configId": 1
    },
    "httpredirect": {
      "allowedDomains": [],
      "version": 1,
      "configId": 1
    },
    "dataexposure": {
      "rules": {
        "database": [],
        "framework": [],
        "request": [],
        "databaseMonitor": []
      },
      "settings": {
        "databaseDataDiscoveryEnabled": false
      },
      "version": 1,
      "configId": 1
    },
    "csp": {
      "directives": [
        {
          "directive": "font-src",
          "source": "'self'"
        },
        {
          "directive": "script-src",
          "source": "'self'"
        },
        {
          "directive": "frame-src",
          "source": "'none'"
        },
        {
          "directive": "style-src",
          "source": "'self'"
        },
        {
          "directive": "connect-src",
          "source": "'self'"
        },
        {
          "directive": "img-src",
          "source": "'self'"
        },
        {
          "directive": "object-src",
          "source": "'none'"
        },
        {
          "directive": "script-src",
          "source": "'unsafe-eval'"
        },
        {
          "directive": "style-src",
          "source": "'unsafe-eval'"
        },
        {
          "directive": "manifest-src",
          "source": "'none'"
        },
        {
          "directive": "media-src",
          "source": "'none'"
        },
        {
          "directive": "worker-src",
          "source": "'none'"
        },
        {
          "directive": "script-src",
          "source": "'unsafe-inline'"
        },
        {
          "directive": "style-src",
          "source": "'unsafe-inline'"
        },
        {
          "directive": "script-src",
          "source": "jsagent.tcell.io"
        },
        {
          "directive": "connect-src",
          "source": "https://api.tcell.io/"
        },
        {
          "directive": "connect-src",
          "source": "https://input.tcell.io/"
        },
        {
          "directive": "frame-src",
          "source": "https://input.tcell.io/"
        }
      ],
      "pathRules": [],
      "version": 2,
      "configId": 1
    },
    "canaries": {
      "items": [],
      "version": 1,
      "configId": 1
    },
    "clickjacking": {
      "frameMode": "Whitelisted",
      "version": 1,
      "configId": 1
    },
    "appfirewall": {
      "payloads": {
        "sendToTcell": {
          "enabled": true,
          "blacklist": [
            "token",
            "client_secret",
            "password",
            "passwd",
            "refresh_token",
            "pf.pass",
            "user.password",
            "j_password",
            "password",
            "pwd",
            "j_sessionid",
            "sessionid",
            "session",
            "token",
            "csrftoken",
            "passwd",
            "refresh_token",
            "user.password",
            "jsessionid"
          ],
          "whitelist": []
        },
        "logLocally": {
          "enabled": false,
          "blacklist": [
            "token",
            "client_secret",
            "password",
            "passwd",
            "refresh_token",
            "pf.pass",
            "user.password",
            "j_password",
            "password",
            "pwd",
            "j_sessionid",
            "sessionid",
            "session",
            "token",
            "csrftoken",
            "passwd",
            "refresh_token",
            "user.password",
            "jsessionid"
          ],
          "whitelist": []
        }
      },
      "sensors": {
        "cmdi": {
          "enabled": true,
          "patterns": [
            "tc-cmdi-1",
            "tc-cmdi-2",
            "tc-cmdi-3"
          ]
        },
        "databaseResultSize": {
          "limit": 0,
          "enabled": false,
          "patterns": []
        },
        "errors": {
          "sqlException": true,
          "csrfException": true,
          "enabled": true,
          "patterns": []
        },
        "fpt": {
          "enabled": true,
          "patterns": [
            "tc-fpt-1",
            "tc-fpt-2",
            "tc-fpt-3",
            "tc-fpt-4"
          ]
        },
        "nullbyte": {
          "enabled": true,
          "patterns": [
            "tc-nullbyte-1"
          ]
        },
        "requestSize": {
          "limit": 7168,
          "enabled": true,
          "patterns": []
        },
        "responseCodes": {
          "s400Series": true,
          "s500Series": true,
          "enabled": true,
          "patterns": []
        },
        "responseSize": {
          "limit": 20480,
          "enabled": true,
          "patterns": []
        },
        "retr": {
          "enabled": true,
          "patterns": [
            "tc-retr-1"
          ]
        },
        "sqli": {
          "libinjection": true,
          "enabled": true,
          "patterns": [
            "tc-sqli-4",
            "tc-sqli-2",
            "tc-sqli-7",
            "tc-sqli-3",
            "tc-sqli-1"
          ]
        },
        "ua": {
          "userAgentEmpty": true,
          "enabled": true,
          "patterns": []
        },
        "xss": {
          "libinjection": true,
          "enabled": true,
          "patterns": [
            "tc-xss-2",
            "tc-xss-8",
            "tc-xss-6",
            "tc-xss-7",
            "tc-xss-4",
            "tc-xss-1",
            "tc-xss-5"
          ]
        },
        "xxe": {
          "enabled": false,
          "patterns": []
        }
      },
      "uriOptions": {
        "collectFullUri": false
      },
      "v1Toggles": {
        "options": {
          "loginFailure": true,
          "fpt": true,
          "null": true,
          "retr": true,
          "respCodes": true,
          "cmdi": true,
          "reqResSize": true,
          "xss": true,
          "sqli": true
        }
      },
      "appFwVersion": 4,
      "notes": {
        "excludedRoutes": {}
      },
      "version": 1,
      "exclusions": [
        {
          "fields": [
            {
              "fieldType": "header",
              "parameters": [
                "accept"
              ]
            }
          ],
          "matches": [
            {
              "sensor": "sqli",
              "patterns": [
                "li"
              ]
            }
          ],
          "enabled": true
        }
      ],
      "configId": 1
    },
    "circuitbreaker": {
      "appfirewall": true,
      "canaries": true,
      "clickjacking": "Report Only",
      "csp": "Report Only",
      "dataexposure": false,
      "httpredirect": "Report Only",
      "login": true,
      "jsconfig": true,
      "cmdi": "Report Only",
      "blockingrules": "Disabled",
      "version": 1,
      "configId": 1
    },
    "cmdi": {
      "enableRouteFingerprints": false,
      "collectFullCommandline": false,
      "commandPolicy": [],
      "compoundStatementPolicy": [],
      "version": 1,
      "configId": 1
    },
    "blocking": {
      "suspiciousMode": "Disabled",
      "suspiciousWhitelist": [],
      "rules": [],
      "version": 1,
      "configId": 1
    }
  }
}
```

#### Get Agent Details

This action is used to fetch details for the agent with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|App ID|None|
|agent_id|string|None|True|Agent ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent|False|Details for the provided agent, including the agent type (ApacheAgent, JVMAgent, etc), version string, earliest and most recent time seen, and whether the agent is currently known to be actively sending data to the tCell service|

Example output:

```
{
  "agent": {
    "id": "ip-10-234-4-117",
    "type": "JVMAgent",
    "version": "1.4.1",
    "from": 1545343683916,
    "to": 1545571386596,
    "active": true
  }
}
```

#### Remove IP Addresses from Blacklist

This action is used to remove IP addresses from the existing blacklist within the blocked IP address configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ips|[]string|None|True|List of IP addresses|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|'Nothing to update' in case the configuration was not changed|
|id|integer|False|ID of a new, updated configuration|

Example output:

```
{
  "id": 9
}
```

#### Add IP Addresses to Blacklist

This action is used to add IP addresses to the existing blacklist within the blocked IP address configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ips|[]string|None|True|List of IP addresses|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|'Nothing to update' in case the configuration was not changed|
|id|integer|False|ID of a new, updated configuration|

Example output:

```
{
  "id": 8
}
```

#### Create IP Address Group

This action is used to upload an IP address group definition to tCell.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group|object|None|True|IP group definition, containing a name and a list of items, in JSON format|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|ID of a new IP group|

Example output:

```
{
  "id": 7
}
```

#### Create App

This action is used to create an application.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_display_name|string|None|True|The display name of your new application (an app ID will be derived from this name)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|app_id|string|False|The application ID for the newly created tCell app|

Example output:

```
{
  "app_id": "LowprofileappcreatedforKomandplugintests-3l1tp"
}
```

#### List Agents

This action is used to fetch details for all seen agents (optionally matching the provided criteria).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|per_page|integer|10|False|Specify number of returned results per page, defaults to 10|None|
|to|integer|None|False|The end (most recent endpoint) of a time window for known agents. Agents which connected to the tCell service outside this window will not be returned. Value in milliseconds from Unix epoch e.g. 15465292953|None|
|from|integer|None|False|The beginning (earliest endpoint) of a time window for known agents. Agents which connected to the tCell service outside this window will not be returned. Value in milliseconds from Unix epoch e.g. 15465292953. Data older than 30 days is not available|None|
|page|integer|1|False|Select which page is returned, default/first page is 1|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|total|integer|False|The number of items returned|
|agents|[]agent|False|A list of agents|

Example output:

```
{
  "total": 4,
  "agents": [
    {
      "id": "cam-mbp-4068.cam.rapid7.com",
      "type": "JVMAgent",
      "version": "1.4.1",
      "from": 1545152494202,
      "to": 1545169881305,
      "active": false
    },
    {
      "id": "ip-10-234-4-117",
      "type": "JVMAgent",
      "version": "1.4.1",
      "from": 1545343683916,
      "to": 1545571446652,
      "active": true
    }
  ]
}
```

#### Get App

This action is used to fetch the display name and app ID for the app with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|app|app|False|A JSON object with the app ID and the user-friendly app display name|

Example output:

```
{
  "app": {
    "id": "LowprofileappcreatedforKomandplugintests-1oRtT",
    "name": "Low profile app created for Komand plugin tests"
  }
}
```

#### List Packages

This action is used to fetch details for all seen packages (matching the provided criteria).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|per_page|integer|10|False|The number of results to be returned per page|None|
|to|integer|None|False|Unix timestamp (in milliseconds; inclusive) until which to fetch events|None|
|from|integer|None|False|Unix timestamp (in milliseconds; exclusive) from which to fetch events|None|
|page|integer|1|False|Select which page is returned, default/first page is 1|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|total|integer|False|The number of items returned|
|packages|[]package|False|A list of packages|

Example output:

```
{
  "total": 127,
  "packages": [
    {
      "id": 129,
      "vendor": "org.eclipse.jetty",
      "name": "jetty-webapp",
      "version": "9.4.6.v20170531",
      "build": "unknown",
      "created_at": 1533134616452
    },
    {
      "id": 43,
      "vendor": "org.springframework",
      "name": "spring-expression",
      "version": "4.3.10.RELEASE",
      "build": "unknown",
      "created_at": 1533091337310
    },
    {
      "id": 120,
      "vendor": "org.eclipse.jetty.websocket",
      "name": "javax-websocket-server-impl",
      "version": "9.4.6.v20170531",
      "build": "unknown",
      "created_at": 1533134616452
    },
    {
      "id": 171,
      "vendor": "commons-codec",
      "name": "commons-codec",
      "version": "1.10",
      "build": "unknown",
      "created_at": 1533134634470
    },
    {
      "id": 8,
      "vendor": "org.codehaus.groovy",
      "name": "groovy-all",
      "version": "2.4.12",
      "build": "unknown",
      "created_at": 1533091337310
    },
    {
      "id": 156,
      "vendor": "org.javassist",
      "name": "javassist",
      "version": "3.21.0-GA",
      "build": "unknown",
      "created_at": 1533134634470
    },
    {
      "id": 11,
      "vendor": "commons-configuration",
      "name": "commons-configuration",
      "version": "1.8",
      "build": "unknown",
      "created_at": 1533091337310
    },
    {
      "id": 138,
      "vendor": "org.springframework.security",
      "name": "spring-security-web",
      "version": "4.2.3.RELEASE",
      "build": "unknown",
      "created_at": 1533134616452
    },
    {
      "id": 166,
      "vendor": "org.eclipse.jetty.websocket",
      "name": "websocket-servlet",
      "version": "9.4.6.v20170531",
      "build": "unknown",
      "created_at": 1533134634470
    },
    {
      "id": 302,
      "vendor": "antlr",
      "name": "antlr",
      "version": "2.7.7",
      "build": "unknown",
      "created_at": 1533134896979
    }
  ]
}
```

#### Get Inline Script Details

This action is used to fetch details for the inline script with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|inline_script_id|string|None|True|Inline Script ID|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|inline_script|inline_script|False|Details for the given inline script, including approved\: whether the script is marked as intended; template\: the script text with literals replaced by ?; created_at\: when the script was added to the tCell database; last_reported_at\: when the jsagent last reported this script|

Example output:

```
{
  "inline_script": {
    "id": "sha256-N9Y4hC_soz7hFmkzqaDrk-r5kW2BaEJFcoZoxBUvSzE=",
    "approved": false,
    "template": "window.serviceUrl = '?';\nwindow.options = { '?': '?' };",
    "created_at": 1533134878993,
    "last_reported_at": 1536937350616
  }
}
```

#### List Routes

This action is used to fetch details for all seen routes (matching the provided criteria).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|per_page|integer|10|False|The number of results to be returned per page, defaults to 10|None|
|to|integer|None|False|The end (most recent endpoint) of a time window for known routes. Routes reported by agents outside this window will not be returned. Value in milliseconds from Unix epoch e.g. 15465292953|None|
|from|integer|None|False|The beginning (earliest endpoint) of a time window for known routes. Routes reported by agents outside this window will not be returned. Value in milliseconds from Unix epoch e.g. 15465292953. Data older than 30 days is not available|None|
|page|integer|1|False|Select which page is returned, default/first page is 1|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|routes|[]route|False|A list of routes|
|total|integer|False|The number of items returned|

Example output:

```
{
  "total": 111,
  "routes": [
    {
      "id": "-393312948",
      "method": "get",
      "pattern": "org.eclipse.jetty.server.session.SessionHandler",
      "controller": "org.eclipse.jetty.server.session.SessionHandler"
    },
    {
      "id": "-744514143",
      "method": "delete",
      "pattern": "org.eclipse.jetty.server.session.SessionHandler",
      "controller": "org.eclipse.jetty.server.session.SessionHandler"
    },
    {
      "id": "-1643970856",
      "method": "update",
      "pattern": "org.eclipse.jetty.servlet.ErrorPageErrorHandler",
      "controller": "org.eclipse.jetty.servlet.ErrorPageErrorHandler"
    },
    {
      "id": "1302020026",
      "method": "delete",
      "pattern": "org.eclipse.jetty.servlet.ErrorPageErrorHandler",
      "controller": "org.eclipse.jetty.servlet.ErrorPageErrorHandler"
    },
    {
      "id": "1257378454",
      "method": "post",
      "pattern": "org.eclipse.jetty.server.session.SessionHandler",
      "controller": "org.eclipse.jetty.server.session.SessionHandler"
    },
    {
      "id": "604462271",
      "method": "update",
      "pattern": "org.eclipse.jetty.server.session.SessionHandler",
      "controller": "org.eclipse.jetty.server.session.SessionHandler"
    },
    {
      "id": "1653221221",
      "method": "get",
      "pattern": "org.eclipse.jetty.servlet.ErrorPageErrorHandler",
      "controller": "org.eclipse.jetty.servlet.ErrorPageErrorHandler"
    },
    {
      "id": "-991054673",
      "method": "post",
      "pattern": "org.eclipse.jetty.servlet.ErrorPageErrorHandler",
      "controller": "org.eclipse.jetty.servlet.ErrorPageErrorHandler"
    },
    {
      "id": "-378147718",
      "method": "post",
      "pattern": "org.springframework.boot.context.embedded.jetty.JettyEmbeddedWebAppContext",
      "controller": "org.springframework.boot.context.embedded.jetty.JettyEmbeddedWebAppContext"
    },
    {
      "id": "-197298172",
      "method": "get",
      "pattern": "org.springframework.boot.context.embedded.jetty.JettyEmbeddedWebAppContext",
      "controller": "org.springframework.boot.context.embedded.jetty.JettyEmbeddedWebAppContext"
    }
  ]
}
```

#### List Configurations

This action is used to fetch details for all configurations (matching the provided criteria).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|per_page|integer|10|False|The number of results to be returned per page|None|
|to|integer|None|False|Unix timestamp (in milliseconds; inclusive) until which to fetch events|None|
|from|integer|None|False|Unix timestamp (in milliseconds; exclusive) from which to fetch events|None|
|page|integer|1|False|Select which page is returned (defaults to 1)|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|configs|[]object|False|A list of configurations matching the provided criteria|
|total|integer|False|The number of items returned|

Example output:

```
{
  "configs": [
    {
      "id": 8,
      "version": 1,
      "blockedips": {
        "suspiciousMode": "Disabled",
        "blacklistedIps": [
          "191.168.0.1",
          "192.168.0.100"
        ],
        "whitelistedIps": [],
        "version": 1,
        "configId": 8
      },
      "blockedpaths": {
        "paths": [],
        "version": 1,
        "configId": 1
      },
      "login": {
        "loginFailedEnabled": false,
        "loginSuccessEnabled": true,
        "sessionHijackingEnabled": true,
        "version": 1,
        "configId": 4
      },
      "jsconfig": {
        "jsAgentApiKey": "AQEBBAFFIhPMQItOr7VO4duFN47cjDNZw8g4Sru-NamK5PtA0bFdhbX9eFGrOjIxCHGyLIY",
        "allowedScriptPatterns": [],
        "allowedScriptIds": [],
        "excludedPaths": [],
        "notes": {
          "scriptIds": {},
          "scriptPatterns": {}
        },
        "version": 1,
        "configId": 1
      },
      "httpredirect": {
        "allowedDomains": [],
        "version": 1,
        "configId": 1
      },
      "dataexposure": {
        "rules": {
          "database": [],
          "framework": [],
          "request": [],
          "databaseMonitor": []
        },
        "settings": {
          "databaseDataDiscoveryEnabled": false
        },
        "version": 1,
        "configId": 1
      },
      "csp": {
        "directives": [
          {
            "directive": "script-src",
            "source": "'unsafe-inline'"
          },
          {
            "directive": "style-src",
            "source": "'unsafe-inline'"
          },
          {
            "directive": "script-src",
            "source": "jsagent.tcell.io"
          },
          {
            "directive": "connect-src",
            "source": "https://api.tcell.io/"
          },
          {
            "directive": "connect-src",
            "source": "https://input.tcell.io/"
          },
          {
            "directive": "frame-src",
            "source": "https://input.tcell.io/"
          }
        ],
        "pathRules": [],
        "version": 2,
        "configId": 1
      },
      "canaries": {
        "items": [],
        "version": 1,
        "configId": 1
      },
      "clickjacking": {
        "frameMode": "Whitelisted",
        "version": 1,
        "configId": 1
      },
      "appfirewall": {
        "payloads": {
          "sendToTcell": {
            "enabled": true,
            "blacklist": [
              "token",
              "client_secret",
              "password",
              "passwd",
              "refresh_token",
              "pf.pass",
              "user.password",
              "j_password",
              "password",
              "pwd",
              "j_sessionid",
              "sessionid",
              "session",
              "token",
              "csrftoken",
              "passwd",
              "refresh_token",
              "user.password",
              "jsessionid"
            ],
            "whitelist": []
          },
          "logLocally": {
            "enabled": false,
            "blacklist": [
              "token",
              "client_secret",
              "password",
              "passwd",
              "refresh_token",
              "pf.pass",
              "user.password",
              "j_password",
              "password",
              "pwd",
              "j_sessionid",
              "sessionid",
              "session",
              "token",
              "csrftoken",
              "passwd",
              "refresh_token",
              "user.password",
              "jsessionid"
            ],
            "whitelist": []
          }
        },
        "sensors": {
          "cmdi": {
            "enabled": true,
            "patterns": [
              "tc-cmdi-1",
              "tc-cmdi-2",
              "tc-cmdi-3"
            ]
          },
          "databaseResultSize": {
            "limit": 0,
            "enabled": false,
            "patterns": []
          },
          "errors": {
            "sqlException": true,
            "csrfException": true,
            "enabled": true,
            "patterns": []
          },
          "fpt": {
            "enabled": true,
            "patterns": [
              "tc-fpt-1",
              "tc-fpt-2",
              "tc-fpt-3",
              "tc-fpt-4"
            ]
          },
          "nullbyte": {
            "enabled": true,
            "patterns": [
              "tc-nullbyte-1"
            ]
          },
          "requestSize": {
            "limit": 7168,
            "enabled": true,
            "patterns": []
          },
          "responseCodes": {
            "s400Series": true,
            "s500Series": true,
            "enabled": true,
            "patterns": []
          },
          "responseSize": {
            "limit": 20480,
            "enabled": true,
            "patterns": []
          },
          "retr": {
            "enabled": true,
            "patterns": [
              "tc-retr-1"
            ]
          },
          "sqli": {
            "libinjection": true,
            "enabled": true,
            "patterns": [
              "tc-sqli-4",
              "tc-sqli-2",
              "tc-sqli-7",
              "tc-sqli-3",
              "tc-sqli-1"
            ]
          },
          "ua": {
            "userAgentEmpty": true,
            "enabled": true,
            "patterns": []
          },
          "xss": {
            "libinjection": true,
            "enabled": true,
            "patterns": [
              "tc-xss-2",
              "tc-xss-8",
              "tc-xss-6",
              "tc-xss-7",
              "tc-xss-4",
              "tc-xss-1",
              "tc-xss-5"
            ]
          },
          "xxe": {
            "enabled": false,
            "patterns": []
          }
        },
        "uriOptions": {
          "collectFullUri": false
        },
        "v1Toggles": {
          "options": {
            "loginFailure": true,
            "fpt": true,
            "null": true,
            "retr": true,
            "respCodes": true,
            "cmdi": true,
            "reqResSize": true,
            "xss": true,
            "sqli": true
          }
        },
        "appFwVersion": 4,
        "notes": {
          "excludedRoutes": {}
        },
        "version": 1,
        "exclusions": [
          {
            "fields": [
              {
                "fieldType": "header",
                "parameters": [
                  "accept"
                ]
              }
            ],
            "matches": [
              {
                "sensor": "sqli",
                "patterns": [
                  "li"
                ]
              }
            ],
            "enabled": true
          }
        ],
        "configId": 1
      },
      "circuitbreaker": {
        "appfirewall": true,
        "canaries": true,
        "clickjacking": "Report Only",
        "csp": "Report Only",
        "dataexposure": false,
        "httpredirect": "Report Only",
        "login": true,
        "jsconfig": true,
        "cmdi": "Report Only",
        "blockingrules": "Disabled",
        "version": 1,
        "configId": 1
      },
      "cmdi": {
        "enableRouteFingerprints": false,
        "collectFullCommandline": false,
        "commandPolicy": [],
        "compoundStatementPolicy": [],
        "version": 1,
        "configId": 1
      },
      "blocking": {
        "suspiciousMode": "Disabled",
        "suspiciousWhitelist": [],
        "rules": [],
        "version": 1,
        "configId": 1
      }
    },
    {
      "id": 7,
      "version": 1,
      "blockedips": {
        "suspiciousMode": "Disabled",
        "blacklistedIps": [
          "191.168.0.1"
        ],
        "whitelistedIps": [],
        "version": 1,
        "configId": 7
      },
      "blockedpaths": {
        "paths": [],
        "version": 1,
        "configId": 1
      },
      "login": {
        "loginFailedEnabled": false,
        "loginSuccessEnabled": true,
        "sessionHijackingEnabled": true,
        "version": 1,
        "configId": 4
      },
      "jsconfig": {
        "jsAgentApiKey": "AQEBBAFFIhPMQItOr7VO4duFN47cjDNZw8g4Sru-NamK5PtA0bFdhbX9eFGrOjIxCHGyLIY",
        "allowedScriptPatterns": [],
        "allowedScriptIds": [],
        "excludedPaths": [],
        "notes": {
          "scriptIds": {},
          "scriptPatterns": {}
        },
        "version": 1,
        "configId": 1
      },
      "httpredirect": {
        "allowedDomains": [],
        "version": 1,
        "configId": 1
      },
      "dataexposure": {
        "rules": {
          "database": [],
          "framework": [],
          "request": [],
          "databaseMonitor": []
        },
        "settings": {
          "databaseDataDiscoveryEnabled": false
        },
        "version": 1,
        "configId": 1
      },
      "csp": {
        "directives": [
          {
            "directive": "style-src",
            "source": "'unsafe-inline'"
          },
          {
            "directive": "script-src",
            "source": "jsagent.tcell.io"
          },
          {
            "directive": "connect-src",
            "source": "https://api.tcell.io/"
          },
          {
            "directive": "connect-src",
            "source": "https://input.tcell.io/"
          },
          {
            "directive": "frame-src",
            "source": "https://input.tcell.io/"
          }
        ],
        "pathRules": [],
        "version": 2,
        "configId": 1
      },
      "canaries": {
        "items": [],
        "version": 1,
        "configId": 1
      },
      "clickjacking": {
        "frameMode": "Whitelisted",
        "version": 1,
        "configId": 1
      },
      "appfirewall": {
        "payloads": {
          "sendToTcell": {
            "enabled": true,
            "blacklist": [
              "token",
              "client_secret",
              "password",
              "passwd",
              "refresh_token",
              "pf.pass",
              "user.password",
              "j_password",
              "password",
              "pwd",
              "j_sessionid",
              "sessionid",
              "session",
              "token",
              "csrftoken",
              "passwd",
              "refresh_token",
              "user.password",
              "jsessionid"
            ],
            "whitelist": []
          },
          "logLocally": {
            "enabled": false,
            "blacklist": [
              "token",
              "client_secret",
              "password",
              "passwd",
              "refresh_token",
              "pf.pass",
              "user.password",
              "j_password",
              "password",
              "pwd",
              "j_sessionid",
              "sessionid",
              "session",
              "token",
              "csrftoken",
              "passwd",
              "refresh_token",
              "user.password",
              "jsessionid"
            ],
            "whitelist": []
          }
        },
        "sensors": {
          "cmdi": {
            "enabled": true,
            "patterns": [
              "tc-cmdi-1",
              "tc-cmdi-2",
              "tc-cmdi-3"
            ]
          },
          "databaseResultSize": {
            "limit": 0,
            "enabled": false,
            "patterns": []
          },
          "errors": {
            "sqlException": true,
            "csrfException": true,
            "enabled": true,
            "patterns": []
          },
          "fpt": {
            "enabled": true,
            "patterns": [
              "tc-fpt-1",
              "tc-fpt-2",
              "tc-fpt-3",
              "tc-fpt-4"
            ]
          },
          "nullbyte": {
            "enabled": true,
            "patterns": [
              "tc-nullbyte-1"
            ]
          },
          "requestSize": {
            "limit": 7168,
            "enabled": true,
            "patterns": []
          },
          "responseCodes": {
            "s400Series": true,
            "s500Series": true,
            "enabled": true,
            "patterns": []
          },
          "responseSize": {
            "limit": 20480,
            "enabled": true,
            "patterns": []
          },
          "retr": {
            "enabled": true,
            "patterns": [
              "tc-retr-1"
            ]
          },
          "sqli": {
            "libinjection": true,
            "enabled": true,
            "patterns": [
              "tc-sqli-4",
              "tc-sqli-2",
              "tc-sqli-7",
              "tc-sqli-3",
              "tc-sqli-1"
            ]
          },
          "ua": {
            "userAgentEmpty": true,
            "enabled": true,
            "patterns": []
          },
          "xss": {
            "libinjection": true,
            "enabled": true,
            "patterns": [
              "tc-xss-2",
              "tc-xss-8",
              "tc-xss-6",
              "tc-xss-7",
              "tc-xss-4",
              "tc-xss-1",
              "tc-xss-5"
            ]
          },
          "xxe": {
            "enabled": false,
            "patterns": []
          }
        },
        "uriOptions": {
          "collectFullUri": false
        },
        "v1Toggles": {
          "options": {
            "loginFailure": true,
            "fpt": true,
            "null": true,
            "retr": true,
            "respCodes": true,
            "cmdi": true,
            "reqResSize": true,
            "xss": true,
            "sqli": true
          }
        },
        "appFwVersion": 4,
        "notes": {
          "excludedRoutes": {}
        },
        "version": 1,
        "exclusions": [
          {
            "fields": [
              {
                "fieldType": "header",
                "parameters": [
                  "accept"
                ]
              }
            ],
            "matches": [
              {
                "sensor": "sqli",
                "patterns": [
                  "li"
                ]
              }
            ],
            "enabled": true
          }
        ],
        "configId": 1
      },
      "circuitbreaker": {
        "appfirewall": true,
        "canaries": true,
        "clickjacking": "Report Only",
        "csp": "Report Only",
        "dataexposure": false,
        "httpredirect": "Report Only",
        "login": true,
        "jsconfig": true,
        "cmdi": "Report Only",
        "blockingrules": "Disabled",
        "version": 1,
        "configId": 1
      },
      "cmdi": {
        "enableRouteFingerprints": false,
        "collectFullCommandline": false,
        "commandPolicy": [],
        "compoundStatementPolicy": [],
        "version": 1,
        "configId": 1
      },
      "blocking": {
        "suspiciousMode": "Disabled",
        "suspiciousWhitelist": [],
        "rules": [],
        "version": 1,
        "configId": 1
      }
    }
  ]
}
```

#### Change Tags

This action is used to assign a completely new set of tags to an app, removing any previously existing tags.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|App ID|None|
|tags|[]string|None|True|List of strings, choosing the new tags for the application|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Successfully updated tags|

Example output:

```
{
  "success": true
}
```

#### Get App Tags

This action is used to fetch the set of tags for a tCell app.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tags|[]string|False|An array of tags for the chosen app|

Example output:

```
{
  "tags": [
    "completely",
    "new",
    "tags"
  ]
}
```

#### List Inline Scripts

This action is used to fetch details for all seen inline scripts (matching the provided criteria).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|per_page|integer|10|False|Specify number of returned results per page, defaults to 10|None|
|to|integer|None|False|The end (most recent endpoint) of a time window for inline scripts. Inline scripts reported by agents outside this window will not be returned. Value in milliseconds from Unix epoch e.g. 15465292953|None|
|from|integer|None|False|The beginning (earliest endpoint) of a time window for inline scripts. Inline scripts reported by agents outside this window will not be returned. Value in milliseconds from Unix epoch e.g. 15465292953. Data older than 30 days is not available|None|
|page|integer|1|False|Select which page is returned, default/first page is 1|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|inline_scripts|[]inline_script|False|A list of inline scripts|
|total|integer|False|The number of items returned|

Example output:

```
{
  "total": 8,
  "inline_scripts": [
    {
      "id": "sha256-N9Y4hC_soz7hFmkzqaDrk-r5kW2BaEJFcoZoxBUvSzE=",
      "approved": false,
      "created_at": 1533134878993,
      "last_reported_at": 1536937350616
    },
    {
      "id": "sha256-RtiOqjbkBeb8R1cWESuz0wUr4iPn0GYPWJZ7rc4Ffh0=",
      "approved": false,
      "created_at": 1533242421798,
      "last_reported_at": 1544509330535
    },
    {
      "id": "sha256-hEgqC4rQ1uyA263sVw3hinGsoL0rMQ6LFdGdsSNjCpk=",
      "approved": false,
      "created_at": 1535008000273,
      "last_reported_at": 1535008000273
    }
  ]
}
```

#### Revert Configuration Changes

This action is used to revert the configuration to the previous iteration.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|App ID|None|
|id|integer|None|True|The ID of the configuration to use|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Revert configuration successful|

Example output:

```
{
  "success": true
}
```

#### Get Package Details

This action is used to fetch details for the package with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|package_id|integer|None|True|Package ID|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|package|package|False|Details for the provided package|

Example output:

```
{
  "package": {
    "id": 129,
    "vendor": "org.eclipse.jetty",
    "name": "jetty-webapp",
    "version": "9.4.6.v20170531",
    "build": "unknown",
    "created_at": 1533134616452
  }
}
```

#### Update IP Address Group

This action is used to upload new items for an IP address group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|items|[]object|None|True|IP group items, in JSON format|None|
|group_name|string|None|True|Name of an existing IP group|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|'Nothing to update' in case the items were not changed|
|id|integer|False|ID of a new, updated IP group|

Example output:

```
{
  "message": "Nothing to update"
}
```

#### Remove Tags

This action is used to remove tags from the application.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|App ID|None|
|tags|[]string|None|True|List of strings, choosing the tags to be removed from the application|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Successfully removed tags|

Example output:

```
{
  "success": true
}
```

#### Get Active Configuration

This action is used to fetch the currently active app configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|config|object|False|The latest configuration data|

Example output:

```
{
  "config": {
    "id": 8,
    "version": 1,
    "blockedips": {
      "suspiciousMode": "Disabled",
      "blacklistedIps": [
        "191.168.0.1",
        "192.168.0.100"
      ],
      "whitelistedIps": [],
      "version": 1,
      "configId": 8
    },
    "blockedpaths": {
      "paths": [],
      "version": 1,
      "configId": 1
    },
    "login": {
      "loginFailedEnabled": false,
      "loginSuccessEnabled": true,
      "sessionHijackingEnabled": true,
      "version": 1,
      "configId": 4
    },
    "jsconfig": {
      "jsAgentApiKey": "AQEBBAFFIhPMQItOr7VO4duFN47cjDNZw8g4Sru-NamK5PtA0bFdhbX9eFGrOjIxCHGyLIY",
      "allowedScriptPatterns": [],
      "allowedScriptIds": [],
      "excludedPaths": [],
      "notes": {
        "scriptIds": {},
        "scriptPatterns": {}
      },
      "version": 1,
      "configId": 1
    },
    "httpredirect": {
      "allowedDomains": [],
      "version": 1,
      "configId": 1
    },
    "dataexposure": {
      "rules": {
        "database": [],
        "framework": [],
        "request": [],
        "databaseMonitor": []
      },
      "settings": {
        "databaseDataDiscoveryEnabled": false
      },
      "version": 1,
      "configId": 1
    },
    "csp": {
      "directives": [
        {
          "directive": "connect-src",
          "source": "https://input.tcell.io/"
        },
        {
          "directive": "frame-src",
          "source": "https://input.tcell.io/"
        }
      ],
      "pathRules": [],
      "version": 2,
      "configId": 1
    },
    "canaries": {
      "items": [],
      "version": 1,
      "configId": 1
    },
    "clickjacking": {
      "frameMode": "Whitelisted",
      "version": 1,
      "configId": 1
    },
    "appfirewall": {
      "payloads": {
        "sendToTcell": {
          "enabled": true,
          "blacklist": [
            "token",
            "client_secret",
            "password",
            "passwd",
            "refresh_token",
            "pf.pass",
            "user.password",
            "j_password",
            "password",
            "pwd",
            "j_sessionid",
            "sessionid",
            "session",
            "token",
            "csrftoken",
            "passwd",
            "refresh_token",
            "user.password",
            "jsessionid"
          ],
          "whitelist": []
        },
        "logLocally": {
          "enabled": false,
          "blacklist": [
            "token",
            "client_secret",
            "password",
            "passwd",
            "refresh_token",
            "pf.pass",
            "user.password",
            "j_password",
            "password",
            "pwd",
            "j_sessionid",
            "sessionid",
            "session",
            "token",
            "csrftoken",
            "passwd",
            "refresh_token",
            "user.password",
            "jsessionid"
          ],
          "whitelist": []
        }
      },
      "sensors": {
        "cmdi": {
          "enabled": true,
          "patterns": [
            "tc-cmdi-1",
            "tc-cmdi-2",
            "tc-cmdi-3"
          ]
        },
        "databaseResultSize": {
          "limit": 0,
          "enabled": false,
          "patterns": []
        },
        "errors": {
          "sqlException": true,
          "csrfException": true,
          "enabled": true,
          "patterns": []
        },
        "fpt": {
          "enabled": true,
          "patterns": [
            "tc-fpt-1",
            "tc-fpt-2",
            "tc-fpt-3",
            "tc-fpt-4"
          ]
        },
        "nullbyte": {
          "enabled": true,
          "patterns": [
            "tc-nullbyte-1"
          ]
        },
        "requestSize": {
          "limit": 7168,
          "enabled": true,
          "patterns": []
        },
        "responseCodes": {
          "s400Series": true,
          "s500Series": true,
          "enabled": true,
          "patterns": []
        },
        "responseSize": {
          "limit": 20480,
          "enabled": true,
          "patterns": []
        },
        "retr": {
          "enabled": true,
          "patterns": [
            "tc-retr-1"
          ]
        },
        "sqli": {
          "libinjection": true,
          "enabled": true,
          "patterns": [
            "tc-sqli-4",
            "tc-sqli-2",
            "tc-sqli-7",
            "tc-sqli-3",
            "tc-sqli-1"
          ]
        },
        "ua": {
          "userAgentEmpty": true,
          "enabled": true,
          "patterns": []
        },
        "xss": {
          "libinjection": true,
          "enabled": true,
          "patterns": [
            "tc-xss-2",
            "tc-xss-8",
            "tc-xss-6",
            "tc-xss-7",
            "tc-xss-4",
            "tc-xss-1",
            "tc-xss-5"
          ]
        },
        "xxe": {
          "enabled": false,
          "patterns": []
        }
      },
      "uriOptions": {
        "collectFullUri": false
      },
      "v1Toggles": {
        "options": {
          "loginFailure": true,
          "fpt": true,
          "null": true,
          "retr": true,
          "respCodes": true,
          "cmdi": true,
          "reqResSize": true,
          "xss": true,
          "sqli": true
        }
      },
      "appFwVersion": 4,
      "notes": {
        "excludedRoutes": {}
      },
      "version": 1,
      "exclusions": [
        {
          "fields": [
            {
              "fieldType": "header",
              "parameters": [
                "accept"
              ]
            }
          ],
          "matches": [
            {
              "sensor": "sqli",
              "patterns": [
                "li"
              ]
            }
          ],
          "enabled": true
        }
      ],
      "configId": 1
    },
    "circuitbreaker": {
      "appfirewall": true,
      "canaries": true,
      "clickjacking": "Report Only",
      "csp": "Report Only",
      "dataexposure": false,
      "httpredirect": "Report Only",
      "login": true,
      "jsconfig": true,
      "cmdi": "Report Only",
      "blockingrules": "Disabled",
      "version": 1,
      "configId": 1
    },
    "cmdi": {
      "enableRouteFingerprints": false,
      "collectFullCommandline": false,
      "commandPolicy": [],
      "compoundStatementPolicy": [],
      "version": 1,
      "configId": 1
    },
    "blocking": {
      "suspiciousMode": "Disabled",
      "suspiciousWhitelist": [],
      "rules": [],
      "version": 1,
      "configId": 1
    }
  }
}
```

### Triggers

#### Get Events

This trigger is used to fetch events of the provided type.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|False|Filters out events based on a predicate. The syntax is filter=field\:operator\:value, where\: field is a field present in the data operator is one of include (equals), exclude (not equals), gt (greater than), and lt (less than) value is the value to apply the operator to|None|
|source|string|None|True|The type of events to fetch|['appfirewall', 'inline', 'login', 'csp']|
|frequency|integer|5|True|How often the trigger should check for new detections in seconds|None|
|app_id|string|None|True|App ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|event|event|False|Matching event|

Example output:

```
{
  "event": {
    "method": "Post",
    "city": "Bogota",
    "full_uri": null,
    "ip": "192.123.123.123",
    "parameter": null,
    "location": {
      "location": {
        "latitude": 4.6492,
        "longitude": -74.0628,
        "city": "Bogota",
        "country": "Colombia",
        "iso-code": "CO"
      },
      "is-tor": false,
      "asn": {
        "number": "AS3816",
        "name": "TELECOMUNICACIONES S.A. ESP"
      }
    },
    "session_id": "f6e075f9f334a28ab5da8a58bec253450fec0cd212bb7863fd1f72b4f0c6ace8",
    "path": "/some/path/*",
    "detection_point": "s5xx",
    "payload": null,
    "country": "Colombia",
    "stripped_uri": "https://my-side.corp/some/path/*",
    "user_id": null,
    "to": null,
    "pattern_id": null,
    "route_id": 157347626,
    "transaction_id": null,
    "id": "40577ef1-8314-11e7-9d63-8fc126905e2f",
    "from": null,
    "app_id": "DemoB-QX7E7",
    "route": "post /some/path/*",
    "time": 1502950866015
  }
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Usually when trying to update the configuration with the same data, nothing will change
and the API will return an appropriate message. Also, it is usually forbidden to create
an entity with the exact same data (e.g. IP groups), and in that case an exception will be raised.

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [tCell](https://www.tcell.io/)
* [tCell API](https://docs.tcell.io)
* [IP groups documentation](https://github.com/tcellio/tcell-deployment-examples/tree/master/api/ip-groups)

