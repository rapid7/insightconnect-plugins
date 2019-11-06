# Description

[Mimecast](https://www.mimecast.com) is a set of cloud services designed to provide next generation protection against advanced email-borne threats such as malicious URLs, malware, impersonation attacks, as well as internally generated threats.
This plugin utilizes the [Mimecast API](https://www.mimecast.com/developer/documentation).

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
|access_key|credential_secret_key|None|True|The application access key|None|
|app_id|string|None|True|Application ID|None|
|app_key|credential_secret_key|None|True|The application key|None|
|secret_key|credential_secret_key|None|True|The application secret key|None|
|url|string|None|True|The URL for the Mimecast server|None|

## Technical Details

### Actions

#### Create Managed URL

This action is used to create a managed URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|A comment about the why the URL is managed; for tracking purposes|None|
|action|string|block|True|Set to 'block' to blacklist the URL, 'permit' to whitelist it|['block', 'permit']|
|match_type|string|explicit|True|Set to 'explicit' to block or permit only instances of the full URL. Set to 'domain' to block or permit any URL with the same domain|['explicit', 'domain']|
|disable_rewrite|boolean|None|True|Disable rewriting of this URL in emails. Applies only if action = 'permit'|None|
|url|string|None|True|The URL to block or permit. Do not include a fragment|None|
|disable_user_awareness|boolean|None|True|Disable User Awareness challenges for this URL. Applies only if action = 'permit'|None|
|disable_log_click|boolean|None|True|Disable logging of user clicks on the URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|[]managed_url|False|Managed URL that was created|

Example output:

```
{
  "response": [
    {
      "id": "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLhQT4SWBA3wB_E-UNk-s0gc6iZeMRZzgizv28dIpyFWXw",
      "scheme": "http",
      "domain": "youtube.com",
      "port": -1,
      "matchType": "explicit",
      "action": "block",
      "comment": "test",
      "disableUserAwareness": false,
      "disableRewrite": false,
      "disableLogClick": false
    }
  ]
}
```

#### Get Managed URL

This action is used to get information on a managed URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|False|The managed domain|None|
|scheme|string|None|False|Filter on whether or not the protocol is HTTP or HTTPS|None|
|match_type|string|none|False|Filter on whether or not the match type is 'explicit' or 'domain'|['none', 'explicit', 'domain']|
|disable_rewrite|string|none|False|Filter on whether or not rewriting of this URL in emails is enabled|['none', 'false', 'true']|
|disable_user_awareness|string|none|False|Filter on whether or not User Awareness challenges for this URL|['none', 'false', 'true']|
|action|string|none|False|Filter on whether or not the action is 'block' or 'permit'|['none', 'block', 'permit']|
|disable_log_click|string|none|False|Filter on whether or not clicks are logged for this URL|['none', 'false', 'true']|
|id|string|None|False|Filter on the Mimecast secure ID of the managed URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|[]managed_url|False|Managed URLs matching |

Example output:

```
{
  "response": [
    {
      "id": "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLho3KMtTMfYm2C21vDPXvKC5vmEJWDAcvTHtH4L4Kw20c",
      "scheme": "https",
      "domain": "steam.com",
      "port": -1,
      "matchType": "explicit",
      "action": "block",
      "comment": "ui test",
      "disableUserAwareness": true,
      "disableRewrite": true,
      "disableLogClick": false
    }
  ]
}
```

#### Permit or Block Sender

This action is used to permit or block a sender.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|action|string|block|True|Either 'permit' (to bypass spam checks) or 'block' (to reject the email)|['block', 'permit']|
|to|string|None|True|The email address of the internal recipient|None|
|sender|string|None|True|The email address of the external sender|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|[]managed_sender|False|The Managed Sender that was created|

Example output:

```
{
  "response": [
    {
      "id": "MTOKEN:eNoVzbEOgjAUQNF_eTMDGArK1oC2GARFjTpi-zQQ28ZWDGr8d3G-ybkfcCh6i62EBM4MB5Z2hpIiWlM_n0tecYv8nkXLBVH8WOvVTb_Kfcze-ZWefDUUzWHXVeYS1jHdgAeidw-j0AojcRTTbZkFNJ6RcGxPtK41GpLAA9Voh1r-t5OATL8_1zIraQ",
      "sender": "example@example.com",
      "to": "user@example.com",
      "type": "Block"
    }
  ]
}
```

#### Create Blocked Sender Policy

This action is used to create a blocked sender policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|option|string|block_sender|True|The block, option must be\: no_action or block_sender|['block_sender', 'no_action']|
|description|string|None|True|A description for the policy which is kept with the email in the archive for future reference|None|
|from_part|string|envelope_from|True|Must be\: envelope_from, header_from or both|['envelope_from', 'header_from', 'both']|
|from_type|string|everyone|True|Can be one of\: everyone, internal_addresses, external_addresses, email_domain, profile_group or individual_email_address|['everyone', 'internal_addresses', 'external_addresses', 'email_domain', 'profile_group', 'individual_email_address']|
|from_value|string|None|False|Required if `From Type` is one of email_domain, profile_group, individual_email_address. Expected values\: If `From Type` is email_domain, a domain name without the @ symbol. If `From Type` is profile_group, the ID of the profile group. If `From Type` is individual_email_address, an email address|None|
|to_type|string|everyone|True|Can be one of\: everyone, internal_addresses, external_addresses, email_domain, profile_group or individual_email_address|['everyone', 'internal_addresses', 'external_addresses', 'email_domain', 'profile_group', 'individual_email_address']|
|to_value|string|None|False|Required if `To Type` is one of email_domain, profile_group, individual_email_address. Expected values\: If `To Type` is email_domain, a domain name without the @ symbol. If `To Type` is profile_group, the ID of the profile group. If `To Type` is individual_email_address, an email address|None|
|source_ips|string|None|False|A comma separated list of IP addresses using CIDR notation (X.X.X.X/XX). When set the policy only applies for connections from matching addresses|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sender_policy|[]sender_policy|False|The policy that was created|

Example output:

```
{
  "response": [
    {
      "option": "block_sender",
      "id": "eNo1jU0LgjAYgP_LrgpusZl2EzWwUoaKJHibb7W-pk4tif57euj-fHyQBjF0IGu0QW0c20cSFkXgKt_Z2Zz6nNN8wjqU5aqyEuOcRmP6arfgGXl_Si_X_UE0-p0pGFhl6RsyUaPuUkxLjzDiONREYtC9ekAnVA3zxc-SgHhrl9GZHqHTUj1n-G_mUwPRYmNM8fcHIHEysg",
      "policy": {
        "description": "komand test",
        "fromPart": "envelope_from",
        "from": {
          "type": "email_domain",
          "emailDomain": "example.com"
        },
        "to": {
          "type": "everyone"
        },
        "fromType": "email_domain",
        "fromValue": "example.com",
        "toType": "everyone",
        "fromEternal": true,
        "toEternal": true,
        "fromDate": "1900-01-01T00:00:00+0000",
        "toDate": "2100-01-01T23:59:59+0000",
        "override": false,
        "bidirectional": false,
        "conditions": {},
        "createTime": "2019-01-28T17:09:01+0000",
        "lastUpdated": "2019-01-28T17:09:01+0000"
      }
    }
  ]
}
```

#### Add Group Member

This action is used to add an email address or domain to a group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|The Mimecast ID of the group to add to|None|
|email_address|string|None|False|The email address of a user to add to a group. Use either emailAddress or domain|None|
|domain|string|None|False|A domain to add to a group. Use either emailAddress or domain|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|folder_id|string|False|The Mimecast ID of the group that the user / domain was added to|
|email_address|string|False|The email address of the user that was added to the group|
|id|string|False|The Mimecast ID of the user / domain that was added to the group|
|internal|boolean|False|If the user / doamin is internal or not|

Example output:

```
{
  "id": "eNqrVipOTS4tSs1MUbJSctdOd43RNy3K9klKdA038M4xq8otcfIMqTQods2MNIrR99NOD_IsCyovdEt11A4pSQvKyPL2SS4orgjOTy01jdEvzlbSUUouLS7Jz00tSs5PSQUa6hzs52LoaG5pagKUK0stKs7Mz1OyMtRRSsvPSUktysnMywZZbmxgYmFRCwBatS7G",
  "folder_id": "eNoVzrkOgkAUQNF_eTWFIIjQEdk0OEaUgCUyD8HMojNiROO_i_3Nyf2AxmZQ2FPwgUgRxWbnzZOxKwsyiCjP-BnTe7jYxA5Pq1xsmRhJ4Sbv9SU4zfgrq8vjdSdbO3eDPRjAaH0Dv62ZRgOaQT8kR9VIihO_OpDQDFzPsafwiUr3UoBvGtBKRlH9F-ylZXnfH3hjMBs",
  "email_address": "test10@example.com",
  "internal": true
}
```

#### Decode URL

This action is used to decode a Mimecast encoded URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|encoded_url|string|None|True|The Mimecast encoded URL (e.g. https://protect-xx.mimecast.com/...)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decoded_url|string|True|Original decoded URL|

Example output:

```
{
  "decoded_url": "https://example.com"
}
```

#### Find Groups

This action is used to find groups that match a given query.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|False|A string to query for|None|
|source|string|cloud|True|A group source to filter on, either "cloud" or "ldap"|['cloud', 'ldap']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|groups|[]group|False|A list of groups that mach the query|

Example output:

```
{
  "groups": [
    {
      "id": "eNoVzrEOgjAUQNF_eTMDaLGBDSUCBjAWjDqS9qGYlmorRjH-u7jfnNwPWOSDwU5ACJkbXJLZklWJ5nlBajWyFaeY3uPFZu2r9Mj6Qvbvck-TMTtHJ1e98uZQX7e6JYxGO3BAiuYGYdtIiw7wwT60QsO1wIlfVWXsRTTwyRQ-0dhO9xB6DrRaCjT_BULn1Pv-ACT0L3A",
      "description": "Relay",
      "source": "cloud",
      "parentId": "eNoVzr0OgjAUQOF3uasMkFAq3RqJ4h8E1IAjaS8EU6i2oqLx3cX95Mv5gEUxGGwlMHgWzUgCvk2t0HbI5iFXM0kxvkXBZkm6uMz7verH5ERX73XDz2732lXF8ZLq2s8pz8ABJasrsLpSFh0Qg73rDo3QEid-cUgij9OQ-FP4QGNb3QPzHKi1kmj-C-73B7L7LyY",
      "userCount": 0,
      "folderCount": 0
    },
    {
      "id": "eNoVzssOgjAQQNF_mTWJoGAjOwIqGkVFQUnc1HYgaKHaCvER_x3c35zcL2hkjcKSgwsqbWlmJmx6Hmz9NNAXJymam8LwEYyXM6cKT3G9FvU7Ssj8syi8zKxeK3o8XDcyt2Pi7cAAwekd3JwKjQawRj9lhYpJjr3v76PA8sjEsfuwRaVLWYNrGZBLwVH9H2wyIsNfB8G2MJw",
      "description": "Permitted senders",
      "source": "cloud",
      "parentId": "eNoVzr0OgjAUQOF3uasMkFAq3RqJ4h8E1IAjaS8EU6i2oqLx3cX95Mv5gEUxGGwlMHgWzUgCvk2t0HbI5iFXM0kxvkXBZkm6uMz7verH5ERX73XDz2732lXF8ZLq2s8pz8ABJasrsLpSFh0Qg73rDo3QEid-cUgij9OQ-FP4QGNb3QPzHKi1kmj-C-73B7L7LyY",
      "userCount": 0,
      "folderCount": 0
    }
  ]
}
```

#### Get TTP URL Logs

This action is used to get TTP URL logs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|from|string|None|False|Start date of logs to return in the following format 2015-11-16T14:49:18+0000. Default is the start of the current day|None|
|route|string|all|True|Filters logs by route, must be one of inbound, outbound, internal, or all|['all', 'inbound', 'outbound', 'internal']|
|scan_result|string|all|True|Filters logs by scan result, must be one of clean, malicious, or all|['clean', 'malicious', 'all']|
|to|string|None|False|End date of logs to return in the following format 2015-11-16T14:49:18+0000. Default is time of request|None|
|url_to_filter|string|None|False|URL filter results with|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|click_logs|[]click_logs|False|Click Logs|

Example output:

```
{
  [
    {
       "userEmailAddress": "mimecast_dhamilton@example.com",
       "url": "https://www.dummy-mimecast-blacklist.com",
       "ttpDefinition": "Default URL Protection Definition",
       "action": "warn",
       "adminOverride": "N/A",
       "userOverride": "None",
       "scanResult": "malicious",
       "category": "Compromised",
       "userAwarenessAction": "N/A",
       "date": "2019-04-23T19:50:28+0000",
       "route": "inbound"
    }
  ]
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For the Create Managed URL action, the URL must include `http://` or `https://` e.g. `http://google.com`
Most common cloud [URLs](https://www.mimecast.com/tech-connect/documentation/api-overview/global-base-urls/)

# Version History

* 3.0.0 - Add URL in Get TTP URL Logs action to filter output | Update connection settings to the proper authentication supported by the Mimecast API
* 2.5.0 - New action Decode URL
* 2.4.0 - New action Get TTP URL Logs
* 2.3.0 - New actions Add Group Member and Find Group
* 2.2.0 - New action Create Blocked Sender Policy
* 2.1.0 - New action Permit or Block Sender
* 2.0.0 - Add Get Managed URL Action | Update descriptions and output titles
* 1.0.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Mimecast API](https://www.mimecast.com/developer/documentation)

