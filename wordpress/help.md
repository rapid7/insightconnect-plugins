# Description

The [WordPress](https://wordpress.com/) plugin allows you to manage users on the WordPress platform. Only users can be deleted or suspended from the wordpress application.

# Key Features

* Delete users
* Suspend Users

# Requirements

* WordPress configuration (see connection details)
* WordPress administrative username and password
* WordPress host name

# Documentation

## Setup

This plugin requires that the WordPress instance be configured as follows:

1. WordPress [REST APIv2 plugin](https://wordpress.org/plugins/rest-api/) must be installed
2. The default Basic Auth or Application Password plugins must not be installed

Users may choose to install the [Application-Password plugin](https://github.com/georgestephanis/application-passwords)
to avoid passing plain text passwords over http. Otherwise, users must install the Basic Auth plugin.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Password should be basic Auth or Application password|None|
|host|string|None|True|Host URL|None|

## Technical Details

### Actions

#### Suspend User

This action can be used to suspend a user from a WordPress instance.

This action does not use any additional WordPress plugins such as Disable User. Instead, it sets the users role to `[]`.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|User Suspended|

#### Delete User

This action can be used to delete a user from a WordPress instance.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|reassignee|string|None|True|Username to reassign posts to|None|
|username|string|None|True|Username|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|User Deleted|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Users will *not* show up to administrators unless they have [previously published a post](https://wordpress.org/support/topic/cant-get-user-information/).
This can be rectified by WordPress users modifying the REST plugin PHP. If users are unable to authorize, it may also be necessary to edit `.htaccess` as
described [here](http://stackoverflow.com/questions/36470998/cant-authenticate-with-basic-authentication-using-wp-rest-api-2-0-plugin) as well as adding
the following line:

```

Header always set Access-Control-Allow-Headers: Authorization

```

The Basic Auth plugin that can be searched for in the WordPress admin console does not function properly. Instead, [this plugin](https://github.com/WP-API/Basic-Auth)
should be used though application passwords are *strongly* recommended. Testing the plugin is difficult due to the distributed nature of the WordPress API. Additionally,
the discovery process does not work on locally run web servers, as the API root will be given as `localhost` as opposed to the host IP.

# Version History

* 2.0.1 - Change docker image from `komand/python-pypy3-plugin` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Use input and output constants | Removed duplicated code | Changed `Exception` to `PluginException` | Added "f" strings | copy test from action to connection
* 2.0.0 - New spec and help.md format for the Hub | Added titles for the actions
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [WordPress](https://wordpress.com/)
* [WordPress REST Plugin](https://wordpress.org/plugins/rest-api/)
* [WordPress Basic Auth Plugin](https://github.com/WP-API/Basic-Auth)
* [WordPress Application Passwords Plugin](https://github.com/georgestephanis/application-passwords)

