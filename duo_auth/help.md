
# Duo Auth API

## About

[Duo](https://duo.com/)'s Trusted Access platform verifies the identity of your users with two-factor authentication and
security health of their devices before they connect to the apps they use. This plugin makes calls to the Duo Auth API V2.

## Actions

### Auth

This action is used to perform second-factor authentication.

#### Options

The "Options" field is used to specify additional parameters that may be necessary depending on the authentication factor selected. "Options" accepts the following parameters in json format `username`, `passcode`, `pushinfo`, `type`.

Example input:

```
{
    "type": "Transfer",
    "pushinfo": {
        "hello": "world",
        "host": "suspicious-host"
    }
}
```


##### Push
|Parameter|Required?|Description|
|---------|---------|-----------|
|device|Required|ID of the device. This device must have the "push" capability. You may also specify "auto" to use the first of the user's devices with the "push" capability.|
|type|Optional|This string is displayed in the Duo Mobile app before the word "request". The default is "Login", so the phrase "Login request" appears in the push notification text and on the request details screen. You may want to specify "Transaction", "Transfer", etc.|
|display_username|Optional|String to display in Duo Mobile in place of the user's Duo username.|
|pushinfo|Optional|A set of URL-encoded key/value pairs with additional contextual information associated with this authentication attempt. The Duo Mobile app will display this information to the user. For example: from=login%20portal&domain=example.com. The URL-encoded string's total length must be less than 20,000 bytes.|

##### Passcode
|Parameter|Required?|Description|
|---------|---------|-----------|
|passcode|true|Passcode entered by the user.|

##### Phone
|Parameter|Required?|Description|
|---------|---------|-----------|
|device|true|ID of the device to call. This device must have the "phone" capability. You may also specify "auto" to use the first of the user's devices with the "phone" capability.|

##### SMS
|Parameter|Required?|Description|
|---------|---------|-----------|
|device|true|ID of the device to send passcodes to. This device must have the "sms" capability. You may also specify "auto" to use the first of the user's devices with the "sms" capability.|

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|Username is required if user_id is not provided|None|
|user_id|string|None|False|User ID|None|
|factor|string|auto|False|Factor to use for authentication|['auto', 'push', 'passcode', 'sms', 'phone']|
|device|string|auto|False|Device ID to use for auth|None|
|async|bool|None|False|Set to true for an async response|None|
|ipaddr|string|None|False|The IP address of the user to be authenticated, in dotted quad format. This will cause an 'allow' response to be sent if appropriate for requests from a trusted network.|None|
|options|object|None|False|Additional options required by the API.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|
|status_msg|string|False|None|
|trusted_device_token|string|False|None|
|result|string|False|Either allow or deny|
|txid|string|False|None|

Example output:

```

{
  "log": "Connect: Connecting..\n",
  "status": "ok",
  "meta": {},
  "output": {
    "result": "allow",
    "status": "allow",
    "status_msg": "Success. Logging you in..."
  }

```

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_hostname|string|None|False|API hostname|None|
|secret_key|password|None|False|None|None|
|integration_key|string|None|False|None|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* 2FA authentication in workflows

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Add example output
* 1.0.1 - Add "type" parameter option to Duo push

## References

* [Duo](https://duo.com/)
* [Duo Auth API V2](https://duo.com/docs/authapi)
