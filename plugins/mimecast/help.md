# Description

[Mimecast](https://www.mimecast.com) is a set of cloud services designed to provide next generation protection against advanced email-borne threats such as malicious URLs, malware, impersonation attacks, as well as internally generated threats, with a focus on email security. This plugin utilizes the [Mimecast API](https://www.mimecast.com/developer/documentation)

# Key Features

* Email security
* Malicious URL and attachment detection

# Requirements

* Mimecast API 2.0 Client ID
* Mimecast API 2.0 Client Secret

# Supported Product Versions

* Mimecast API 2.0 2025-06-18

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|string|None|True|The Mimecast 2.0 Application Client ID|None|ZA7vkbu7NqcfBcGrXyWW8Rzk2sv2un2DCY7GGCX4BFWgJBZM|None|None|
|client_secret|credential_secret_key|None|True|The Mimecast 2.0 Application Client Secret|None|ohknqKJpCd99XTkHjeVuc2TgYaKWrWn4tEEHCLkXFZhFgDRdcpNGVx3EipX2CvmE|None|None|

Example input:

```
{
  "client_id": "ZA7vkbu7NqcfBcGrXyWW8Rzk2sv2un2DCY7GGCX4BFWgJBZM",
  "client_secret": "ohknqKJpCd99XTkHjeVuc2TgYaKWrWn4tEEHCLkXFZhFgDRdcpNGVx3EipX2CvmE"
}
```

## Technical Details

### Actions


#### Add Group Member

This action is used to add an email address or domain to a group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|False|A domain to add to a group. Use either email address or domain|None|https://example.com|None|None|
|email_address|string|None|False|The email address of a user to add to a group. Use either email address or domain|None|user@example.com|None|None|
|id|string|None|True|The Mimecast ID of the group to add to|None|eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA|None|None|
  
Example input:

```
{
  "domain": "https://example.com",
  "email_address": "user@example.com",
  "id": "eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|email_address|string|False|The email address of the user that was added to the group|user@example.com|
|folder_id|string|False|The Mimecast ID of the group that the user / domain was added to|eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_|
|id|string|False|The Mimecast ID of the user / domain that was added to the group|eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA|
|internal|boolean|False|Whether or not the user or domain is internal|True|
  
Example output:

```
{
  "email_address": "user@example.com",
  "folder_id": "eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_",
  "id": "eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA",
  "internal": true
}
```

#### Create Blocked Sender Policy

This action is used to create a blocked sender policy

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|True|A description for the policy which is kept with the email in the archive for future reference|None|A description|None|None|
|from_part|string|envelope_from|True|Must be: envelope_from, header_from or both|["envelope_from", "header_from", "both"]|envelope_from|None|None|
|from_type|string|individual_email_address|True|Can be one of: everyone, internal_addresses, external_addresses, email_domain, profile_group or individual_email_address|["everyone", "internal_addresses", "external_addresses", "email_domain", "profile_group", "individual_email_address"]|internal_addresses|None|None|
|from_value|string|None|False|Required if `From Type` is one of email_domain, profile_group, individual_email_address. Expected values: If `From Type` is email_domain, a domain name without the @ symbol. If `From Type` is profile_group, the ID of the profile group. If `From Type` is individual_email_address, an email address|None|user@example.com|None|None|
|option|string|block_sender|True|The block, option must be: no_action or block_sender|["block_sender", "no_action"]|block_sender|None|None|
|source_ips|string|None|False|A comma separated list of IP addresses using CIDR notation (X.X.X.X/XX). When set the policy only applies for connections from matching addresses|None|198.51.100.0/24|None|None|
|to_type|string|individual_email_address|True|Can be one of: everyone, internal_addresses, external_addresses, email_domain, profile_group or individual_email_address|["everyone", "internal_addresses", "external_addresses", "email_domain", "profile_group", "individual_email_address"]|everyone|None|None|
|to_value|string|None|False|Required if `To Type` is one of email_domain, profile_group, individual_email_address. Expected values: If `To Type` is email_domain, a domain name without the @ symbol. If `To Type` is profile_group, the ID of the profile group. If `To Type` is individual_email_address, an email address|None|user@example.com|None|None|
  
Example input:

```
{
  "description": "A description",
  "from_part": "envelope_from",
  "from_type": "individual_email_address",
  "from_value": "user@example.com",
  "option": "block_sender",
  "source_ips": "198.51.100.0/24",
  "to_type": "individual_email_address",
  "to_value": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|sender_policy|[]sender_policy|False|The policy that was created|[{"option": "block_sender", "id": "eNo1jU0LgjAYgP_LrgpusZl2EzWwUoaKJHibb7W-pk4tif57euj-fHyQBjF0IGu0QW0c20cSFkXgKt_Z2Zz6nNN8wjqU5aqyEuOcRmP6arfgGXl_Si_X_UE0-p0pGFhl6RsyUaPuUkxLjzDiONREYtC9ekAnVA3zxc-SgHhrl9GZHqHTUj1n-G_mUwPRYmNM8fcHIHEysg", "policy": {"description": "komand test", "fromPart": "envelope_from", "from": {"type": "email_domain", "emailDomain": "example.com"}, "to": {"type": "everyone"}, "fromType": "email_domain", "fromValue": "example.com", "toType": "everyone", "fromEternal": True, "toEternal": True, "fromDate": "1900-01-01T00:00:00+0000", "toDate": "2100-01-01T23:59:59+0000", "override": False, "bidirectional": False, "conditions": {}, "createTime": "2019-01-28T17:09:01+0000", "lastUpdated": "2019-01-28T17:09:01+0000"}}]|
  
Example output:

```
{
  "sender_policy": [
    {
      "id": "eNo1jU0LgjAYgP_LrgpusZl2EzWwUoaKJHibb7W-pk4tif57euj-fHyQBjF0IGu0QW0c20cSFkXgKt_Z2Zz6nNN8wjqU5aqyEuOcRmP6arfgGXl_Si_X_UE0-p0pGFhl6RsyUaPuUkxLjzDiONREYtC9ekAnVA3zxc-SgHhrl9GZHqHTUj1n-G_mUwPRYmNM8fcHIHEysg",
      "option": "block_sender",
      "policy": {
        "bidirectional": false,
        "conditions": {},
        "createTime": "2019-01-28T17:09:01+0000",
        "description": "komand test",
        "from": {
          "emailDomain": "example.com",
          "type": "email_domain"
        },
        "fromDate": "1900-01-01T00:00:00+0000",
        "fromEternal": true,
        "fromPart": "envelope_from",
        "fromType": "email_domain",
        "fromValue": "example.com",
        "lastUpdated": "2019-01-28T17:09:01+0000",
        "override": false,
        "to": {
          "type": "everyone"
        },
        "toDate": "2100-01-01T23:59:59+0000",
        "toEternal": true,
        "toType": "everyone"
      }
    }
  ]
}
```

#### Create Managed URL

This action is used to create a managed URL

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|block|True|Set to "block" to blacklist the URL, "permit" to whitelist it|["block", "permit"]|block|None|None|
|comment|string|None|False|A comment about the why the URL is managed; for tracking purposes|None|Deemed malicious by VirusTotal|None|None|
|disable_log_click|boolean|None|True|Disable logging of user clicks on the URL|None|False|None|None|
|disable_rewrite|boolean|None|True|Disable rewriting of this URL in emails. Applies only if action = 'permit'|None|True|None|None|
|disable_user_awareness|boolean|None|True|Disable User Awareness challenges for this URL. Applies only if action = 'permit'|None|False|None|None|
|match_type|string|explicit|True|Set to "explicit" to block or permit only instances of the full URL. Set to "domain" to block or permit any URL with the same domain|["explicit", "domain"]|explicit|None|None|
|url|string|None|True|The URL to block or permit. Do not include a fragment|None|https://example.com|None|None|
  
Example input:

```
{
  "action": "block",
  "comment": "Deemed malicious by VirusTotal",
  "disable_log_click": false,
  "disable_rewrite": true,
  "disable_user_awareness": false,
  "match_type": "explicit",
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]managed_url|False|Managed URL that was created|[{"id": "wOi3MCwjYFqOT7D-I9AbwlwvY3ImP7QVjTLhGwOgsDbzzFK8SjGLNE4", "scheme": "https", "domain": "www.test.net", "port": -1, "path": "/", "queryString": "", "matchType": "explicit", "action": "permit", "comment": "", "disableUserAwareness": False, "disableRewrite": False, "disableLogClick": False}]|
  
Example output:

```
{
  "response": [
    {
      "action": "permit",
      "comment": "",
      "disableLogClick": false,
      "disableRewrite": false,
      "disableUserAwareness": false,
      "domain": "www.test.net",
      "id": "wOi3MCwjYFqOT7D-I9AbwlwvY3ImP7QVjTLhGwOgsDbzzFK8SjGLNE4",
      "matchType": "explicit",
      "path": "/",
      "port": -1,
      "queryString": "",
      "scheme": "https"
    }
  ]
}
```

#### Decode URL

This action is used to decode a Mimecast encoded URL

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|encoded_url|string|None|True|The Mimecast encoded URL|None|https://url.xx.m.mimecastprotect.com/TXH7fhe|None|None|
  
Example input:

```
{
  "encoded_url": "https://url.xx.m.mimecastprotect.com/TXH7fhe"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|decoded_url|string|True|Original decoded URL|https://example.com|
  
Example output:

```
{
  "decoded_url": "https://example.com"
}
```

#### Delete Blocked Sender Policy

This action is used to delete a blocked sender policy

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The Mimecast secure ID of an existing policy to be deleted|None|eWtOL3XZCOwG96BOiFTZRiC5rdvDmP4FFdwU2Y1DC1Us-gh7KyL5trUrZ9aEuzQMV7pPWWxTnPVtsJ6x3fajAh3cRskP0w8hNjaFFVkZB6G9dOytLM2ssQ7HY-p7gJoi|None|None|
  
Example input:

```
{
  "id": "eWtOL3XZCOwG96BOiFTZRiC5rdvDmP4FFdwU2Y1DC1Us-gh7KyL5trUrZ9aEuzQMV7pPWWxTnPVtsJ6x3fajAh3cRskP0w8hNjaFFVkZB6G9dOytLM2ssQ7HY-p7gJoi"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Success status of delete request|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Group Member

This action is used to delete an email address or domain from a group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|False|A domain to remove from group. Use either email address or domain|None|example.com|None|None|
|email_address|string|None|False|The email address to remove from group. Use either email address or domain|None|user@example.com|None|None|
|id|string|None|True|The Mimecast ID of the group to remove from|None|eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA|None|None|
  
Example input:

```
{
  "domain": "example.com",
  "email_address": "user@example.com",
  "id": "eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Status of success of the delete operation|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Managed URL

This action is used to delete a managed URL

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The Mimecast secure ID of the managed URL|None|wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLhHMy6V8J3VOvTNMW2G-txx3o4zL0YXqWxuCVlGQ-1viE|None|None|
  
Example input:

```
{
  "id": "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLhHMy6V8J3VOvTNMW2G-txx3o4zL0YXqWxuCVlGQ-1viE"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Success status of delete request|True|
  
Example output:

```
{
  "success": true
}
```

#### Find Groups

This action is used to find groups that match a given query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|False|A string to query for|None|mygroup|None|None|
|source|string|cloud|True|A group source to filter on, either "cloud" or "ldap"|["cloud", "ldap"]|cloud|None|None|
  
Example input:

```
{
  "query": "mygroup",
  "source": "cloud"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|groups|[]group|False|A list of groups that mach the query|[{"id": "eNoVzrEOgjAUQNF_eTMDaLGBDSUCBjAWjDqS9qGYlmorRjH-u7jfnNwPWOSDwU5ACJkbXJLZklWJ5nlBajWyFaeY3uPFZu2r9Mj6Qvbvck-TMTtHJ1e98uZQX7e6JYxGO3BAiuYGYdtIiw7wwT60QsO1wIlfVWXsRTTwyRQ-0dhO9xB6DrRaCjT_BULn1Pv-ACT0L3A", "description": "Relay", "source": "cloud", "parentId": "eNoVzr0OgjAUQOF3uasMkFAq3RqJ4h8E1IAjaS8EU6i2oqLx3cX95Mv5gEUxGGwlMHgWzUgCvk2t0HbI5iFXM0kxvkXBZkm6uMz7verH5ERX73XDz2732lXF8ZLq2s8pz8ABJasrsLpSFh0Qg73rDo3QEid-cUgij9OQ-FP4QGNb3QPzHKi1kmj-C-73B7L7LyY", "userCount": 0, "folderCount": 0}, {"id": "eNoVzssOgjAQQNF_mTWJoGAjOwIqGkVFQUnc1HYgaKHaCvER_x3c35zcL2hkjcKSgwsqbWlmJmx6Hmz9NNAXJymam8LwEYyXM6cKT3G9FvU7Ssj8syi8zKxeK3o8XDcyt2Pi7cAAwekd3JwKjQawRj9lhYpJjr3v76PA8sjEsfuwRaVLWYNrGZBLwVH9H2wyIsNfB8G2MJw", "description": "Permitted senders", "source": "cloud", "parentId": "eNoVzr0OgjAUQOF3uasMkFAq3RqJ4h8E1IAjaS8EU6i2oqLx3cX95Mv5gEUxGGwlMHgWzUgCvk2t0HbI5iFXM0kxvkXBZkm6uMz7verH5ERX73XDz2732lXF8ZLq2s8pz8ABJasrsLpSFh0Qg73rDo3QEid-cUgij9OQ-FP4QGNb3QPzHKi1kmj-C-73B7L7LyY", "userCount": 0, "folderCount": 0}]|
  
Example output:

```
{
  "groups": [
    {
      "description": "Relay",
      "folderCount": 0,
      "id": "eNoVzrEOgjAUQNF_eTMDaLGBDSUCBjAWjDqS9qGYlmorRjH-u7jfnNwPWOSDwU5ACJkbXJLZklWJ5nlBajWyFaeY3uPFZu2r9Mj6Qvbvck-TMTtHJ1e98uZQX7e6JYxGO3BAiuYGYdtIiw7wwT60QsO1wIlfVWXsRTTwyRQ-0dhO9xB6DrRaCjT_BULn1Pv-ACT0L3A",
      "parentId": "eNoVzr0OgjAUQOF3uasMkFAq3RqJ4h8E1IAjaS8EU6i2oqLx3cX95Mv5gEUxGGwlMHgWzUgCvk2t0HbI5iFXM0kxvkXBZkm6uMz7verH5ERX73XDz2732lXF8ZLq2s8pz8ABJasrsLpSFh0Qg73rDo3QEid-cUgij9OQ-FP4QGNb3QPzHKi1kmj-C-73B7L7LyY",
      "source": "cloud",
      "userCount": 0
    },
    {
      "description": "Permitted senders",
      "folderCount": 0,
      "id": "eNoVzssOgjAQQNF_mTWJoGAjOwIqGkVFQUnc1HYgaKHaCvER_x3c35zcL2hkjcKSgwsqbWlmJmx6Hmz9NNAXJymam8LwEYyXM6cKT3G9FvU7Ssj8syi8zKxeK3o8XDcyt2Pi7cAAwekd3JwKjQawRj9lhYpJjr3v76PA8sjEsfuwRaVLWYNrGZBLwVH9H2wyIsNfB8G2MJw",
      "parentId": "eNoVzr0OgjAUQOF3uasMkFAq3RqJ4h8E1IAjaS8EU6i2oqLx3cX95Mv5gEUxGGwlMHgWzUgCvk2t0HbI5iFXM0kxvkXBZkm6uMz7verH5ERX73XDz2732lXF8ZLq2s8pz8ABJasrsLpSFh0Qg73rDo3QEid-cUgij9OQ-FP4QGNb3QPzHKi1kmj-C-73B7L7LyY",
      "source": "cloud",
      "userCount": 0
    }
  ]
}
```

#### Get Audit Events

This action is used to get audit of events in Mimecast service

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|audit_events_data|audit_events_data|None|True|Data for request|None|{"categories": ["test", "malware"], "endDateTime": "2022-02-02T08:15:30-05:00", "query": "example query", "startDateTime": "2022-02-02T08:15:30-05:00"}|None|None|
|audit_events_pagination|audit_events_request_pagination|None|False|Pagination object for request|None|{"pageSize": 25, "pageToken": "9de5069c5afe602b2ea0a04b66beb2c0"}|None|None|
  
Example input:

```
{
  "audit_events_data": {
    "categories": [
      "test",
      "malware"
    ],
    "endDateTime": "2022-02-02T08:15:30-05:00",
    "query": "example query",
    "startDateTime": "2022-02-02T08:15:30-05:00"
  },
  "audit_events_pagination": {
    "pageSize": 25,
    "pageToken": "9de5069c5afe602b2ea0a04b66beb2c0"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|pagination|pagination|False|Pagination for request|{'pageSize': 25, 'pageToken': '9de5069c5afe602b2ea0a04b66beb2c0'}|
|response|[]audit_events_response|True|Event logs data|[{"id": "wOi3MCwj2RMAhvN30QSmqOT7D-g10nypvPqTB5X5oQtdKJE4Qkl51X5Ue_U", "scheme": "https", "domain": "www.testset3444412312.net", "port": -1, "path": "/", "queryString": "", "matchType": "explicit", "action": "block", "comment": "", "disableUserAwareness": False, "disableRewrite": False, "disableLogClick": False}]|
  
Example output:

```
{
  "pagination": {
    "pageSize": 25,
    "pageToken": "9de5069c5afe602b2ea0a04b66beb2c0"
  },
  "response": [
    {
      "action": "block",
      "comment": "",
      "disableLogClick": false,
      "disableRewrite": false,
      "disableUserAwareness": false,
      "domain": "www.testset3444412312.net",
      "id": "wOi3MCwj2RMAhvN30QSmqOT7D-g10nypvPqTB5X5oQtdKJE4Qkl51X5Ue_U",
      "matchType": "explicit",
      "path": "/",
      "port": -1,
      "queryString": "",
      "scheme": "https"
    }
  ]
}
```

#### Get Managed URL

This action is used to get information on a managed URL

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|none|False|Filter on whether or not the action is "block" or "permit"|["none", "block", "permit"]|block|None|None|
|disable_log_click|string|None|False|Filter on whether or not clicks are logged for this URL|["None", "False", "True"]|True|None|None|
|disable_rewrite|string|None|False|Filter on whether or not rewriting of this URL in emails is enabled|["None", "False", "True"]|False|None|None|
|disable_user_awareness|string|None|False|Filter on whether or not User Awareness challenges for this URL|["None", "False", "True"]|False|None|None|
|domain|string|None|False|The managed domain|None|https://example.com|None|None|
|domainOrUrl|string|None|False|A domain or URL to filter results|None|https://example.com|None|None|
|exactMatch|boolean|False|False|If true, the domainOrUrl value to act as an exact match value. If false, any partial matches will be returned|None|False|None|None|
|id|string|None|False|Filter on the Mimecast secure ID of the managed URL|None|wOi3MCwjYFYhZfkYlp2RMAhwOgsDZixCK43rDjLP0YPWrtBgqVtVbzzFK8SjGLNE4|None|None|
|match_type|string|none|False|Filter on whether or not the match type is "explicit" or "domain"|["none", "explicit", "domain"]|domain|None|None|
|scheme|string|None|False|Filter on whether or not the protocol is HTTP or HTTPS|None|http|None|None|
  
Example input:

```
{
  "action": "none",
  "disable_log_click": "None",
  "disable_rewrite": "None",
  "disable_user_awareness": "None",
  "domain": "https://example.com",
  "domainOrUrl": "https://example.com",
  "exactMatch": false,
  "id": "wOi3MCwjYFYhZfkYlp2RMAhwOgsDZixCK43rDjLP0YPWrtBgqVtVbzzFK8SjGLNE4",
  "match_type": "none",
  "scheme": "http"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]managed_url|False|Managed URLs matching |[{"id": "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLho3KMtTMfYm2C21vDPXvKC5vmEJWDAcvTHtH4L4Kw20c", "scheme": "https", "domain": "steam.com", "port": -1, "matchType": "explicit", "action": "block", "comment": "ui test", "disableUserAwareness": True, "disableRewrite": True, "disableLogClick": False}]|
  
Example output:

```
{
  "response": [
    {
      "action": "block",
      "comment": "ui test",
      "disableLogClick": false,
      "disableRewrite": true,
      "disableUserAwareness": true,
      "domain": "steam.com",
      "id": "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLho3KMtTMfYm2C21vDPXvKC5vmEJWDAcvTHtH4L4Kw20c",
      "matchType": "explicit",
      "port": -1,
      "scheme": "https"
    }
  ]
}
```

#### Get TTP URL Logs

This action is used to get TTP URL logs

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|from|string|None|False|Start date of logs to return in the following format 2015-11-16T14:49:18+0000. Default is the start of the current day|None|2018-11-22T14:49:18+0000|None|None|
|max_pages|integer|100|False|Max pages returned, default 100|None|10|None|None|
|oldest_first|boolean|False|False|When true return results in descending order with oldest result first|None|False|None|None|
|page_size|integer|10|False|The number of results to request|None|10|None|None|
|route|string|all|True|Filters logs by route, must be one of inbound, outbound, internal, or all|["all", "inbound", "outbound", "internal"]|inbound|None|None|
|scan_result|string|all|True|Filters logs by scan result, must be one of clean, malicious, or all|["clean", "malicious", "all"]|malicious|None|None|
|to|string|None|False|End date of logs to return in the following format 2015-11-16T14:49:18+0000. Default is time of request|None|2018-11-22T14:49:18+0000|None|None|
|url_to_filter|string|None|False|Regular expression to filter on. e.g. `examp` will return only URLs with the letters examp in them|None|exam.*|None|None|
  
Example input:

```
{
  "from": "2018-11-22T14:49:18+0000",
  "max_pages": 100,
  "oldest_first": false,
  "page_size": 10,
  "route": "all",
  "scan_result": "all",
  "to": "2018-11-22T14:49:18+0000",
  "url_to_filter": "exam.*"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|click_logs|[]click_logs|False|Click Logs|[{"userEmailAddress": "user@example.com", "url": "https://example.com", "ttpDefinition": "Default URL Protection Definition", "action": "warn", "adminOverride": "N/A", "userOverride": "None", "scanResult": "malicious", "category": "Compromised", "userAwarenessAction": "N/A", "date": "2019-04-23T19:50:28+0000", "route": "inbound"}]|
  
Example output:

```
{
  "click_logs": [
    {
      "action": "warn",
      "adminOverride": "N/A",
      "category": "Compromised",
      "date": "2019-04-23T19:50:28+0000",
      "route": "inbound",
      "scanResult": "malicious",
      "ttpDefinition": "Default URL Protection Definition",
      "url": "https://example.com",
      "userAwarenessAction": "N/A",
      "userEmailAddress": "user@example.com",
      "userOverride": "None"
    }
  ]
}
```

#### Permit or Block Sender

This action is used to permit or block a sender

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|block|True|Either "permit" (to bypass spam checks) or "block" (to reject the email)|["block", "permit"]|block|None|None|
|sender|string|None|True|The email address of the external sender|None|user@example.com|None|None|
|to|string|None|True|The email address of the internal recipient|None|user@example.com|None|None|
  
Example input:

```
{
  "action": "block",
  "sender": "user@example.com",
  "to": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]managed_sender|False|The Managed Sender that was created|[{"id": "MTOKEN:eNoVzbEOgjAUQNF_eTMDGArK1oC2GARFjTpi-zQQ28ZWDGr8d3G-ybkfcCh6i62EBM4MB5Z2hpIiWlM_n0tecYv8nkXLBVH8WOvVTb_Kfcze-ZWefDUUzWHXVeYS1jHdgAeidw-j0AojcRTTbZkFNJ6RcGxPtK41GpLAA9Voh1r-t5OATL8_1zIraQ", "sender": "user@example.com", "to": "user@example.com", "type": "Block"}]|
  
Example output:

```
{
  "response": [
    {
      "id": "MTOKEN:eNoVzbEOgjAUQNF_eTMDGArK1oC2GARFjTpi-zQQ28ZWDGr8d3G-ybkfcCh6i62EBM4MB5Z2hpIiWlM_n0tecYv8nkXLBVH8WOvVTb_Kfcze-ZWefDUUzWHXVeYS1jHdgAeidw-j0AojcRTTbZkFNJ6RcGxPtK41GpLAA9Voh1r-t5OATL8_1zIraQ",
      "sender": "user@example.com",
      "to": "user@example.com",
      "type": "Block"
    }
  ]
}
```

#### Track Messages

This action is used to search for messages processing, and current state using specific message information. Either one
 of `Send From`, `Send To`, `Subject`, `Sender IP` fields, or `Message ID` must not be empty

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_date|date|None|False|The date and time of the latest message to track|None|Example Reason|None|None|
|message_id|string|None|False|The internet message id of the message to track|None|ExampleID|None|None|
|routes|[]string|None|False|An array of routes to filter by. Possible values are internal, outbound and inbound|None|["internal", "outbound"]|None|None|
|search_reason|string|None|False|Reason for Tracking a email, used for activity tracking purposes|None|Example Reason|None|None|
|send_from|string|None|False|The sending email address or domain of the messages to track|None|user@example.com|None|None|
|send_to|string|None|False|The recipient email address or domain of the messages to track|None|user@example.com|None|None|
|sender_ip|string|None|False|The source IP address of messages to track|None|192.168.0.1|None|None|
|start_date|date|None|False|The date and time of the earliest message to track|None|Example Reason|None|None|
|subject|string|None|False|The subject of the messages to track|None|Example Email Subject|None|None|
  
Example input:

```
{
  "end_date": "Example Reason",
  "message_id": "ExampleID",
  "routes": [
    "internal",
    "outbound"
  ],
  "search_reason": "Example Reason",
  "send_from": "user@example.com",
  "send_to": "user@example.com",
  "sender_ip": "192.168.0.1",
  "start_date": "Example Reason",
  "subject": "Example Email Subject"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|tracked_emails|[]tracked_emails|True|An array of found tracked emails|[{"detectionLevel": "", "fromEnv": {"emailAddress": "user@example.com"}, "fromHdr": {"emailAddress": ""}, "id": "123456789", "info": "Envelope Rejected", "received": "2022-12-01T12:49:46+0000", "route": "inbound", "senderIP": "192.168.0.1", "sent": "2022-12-01T12:49:46+0000", "spamScore": 0, "status": "rejected", "subject": "Example Subject", "to": [{"displayableName": "Example User", "emailAddress": "user@example.com"}]}]|
  
Example output:

```
{
  "tracked_emails": [
    {
      "detectionLevel": "",
      "fromEnv": {
        "emailAddress": "user@example.com"
      },
      "fromHdr": {
        "emailAddress": ""
      },
      "id": "123456789",
      "info": "Envelope Rejected",
      "received": "2022-12-01T12:49:46+0000",
      "route": "inbound",
      "senderIP": "192.168.0.1",
      "sent": "2022-12-01T12:49:46+0000",
      "spamScore": 0,
      "status": "rejected",
      "subject": "Example Subject",
      "to": [
        {
          "displayableName": "Example User",
          "emailAddress": "user@example.com"
        }
      ]
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**managed_url**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|Action to take for when URL is clicked. Either block or permit|None|
|Comment|string|None|False|The comment that was posted in the request|None|
|Click Logging|boolean|None|False|If logging of user clicks on the URL is disabled|None|
|URL Rewriting|boolean|None|False|If rewriting of this URL in emails is disabled|None|
|User Awareness|boolean|None|False|If User Awareness challenges for this URL are disabled|None|
|Domain|string|None|False|The managed domain|None|
|ID|string|None|False|The Mimecast secure ID of the managed URL|None|
|Match Type|string|None|False|The type of URL to match against|None|
|Path|string|None|False|The resource path of the managed URL|None|
|Port|integer|None|False|The specified in the managed URL. Default value is -1 if no port was provided|None|
|Query string|string|None|False|The query string of the managed URL|None|
|Scheme|string|None|False|The protocol to apply for the managed URL. Either HTTP or HTTPS|None|
  
**managed_sender**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The Mimecast secure ID of the managed sender object|None|
|Sender|string|None|False|The email address of the external sender|None|
|To|string|None|False|The email address of the internal recipient|None|
|Type|string|None|False|Either 'permit' (to bypass spam checks) or 'block' (to reject the email)|None|
  
**policy**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Bidirectional|boolean|None|False|If the policy is also applied in the reverse of the email flow, i.e. where the specified recipient in the policy becomes the sender, and the specified sender in the policy becomes the recipient|None|
|Conditions|object|None|False|An object with fields describing additional conditions that should affect when the policy is applied|None|
|Description|string|None|False|The description for the policy which is kept with the email in the archive for future reference|None|
|From|object|None|False|An object containing type and value fields defining which sender addresses the policy applies to|None|
|From Date|string|None|False|The date that the policy will apply from|None|
|From Eternal|boolean|None|False|If the policy is always applied or if there is a specific start date|None|
|From Part|string|None|False|Which from address is used in the policy. Can be any of envelope_from, header_from, both|None|
|From Type|string|None|False|Which sender addresses the policy applies to. Can be one of everyone, internal_addresses, external_addresses, email_domain, profile_group, address_attribute_value, individual_email_address, free_mail_domains, header_display_name|None|
|From Value|string|None|False|A value defining which senders the policy applies to|None|
|Override|boolean|None|False|If true, this option overrides the order in which the policy is applied, and forces it to be applied first if there are multiple applicable policies, unless more specific policies of the same type have been configured with an override as well|None|
|To|object|None|False|An object containing type and value fields defining which recipient addresses the policy applies to|None|
|To Date|string|None|False|The date that the policy will apply until|None|
|To Eternal|boolean|None|False|If the policy should always be applied or if there is an end date|None|
|To Type|string|None|False|Which recipient addresses the policy applies to. Can be one of everyone, internal_addresses, external_addresses, email_domain, profile_group, address_attribute_value, individual_email_address, free_mail_domains, header_display_name|None|
  
**sender_policy**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The Mimecast ID of the policy. Used when updating the policy|None|
|Option|string|None|False|The option set for the policy. Will be one of no_action, block_sender|None|
|Policy|policy|None|False|The policy that was created|None|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|The name of the group|None|
|Folder Count|integer|None|False|Number of folders allocated to this group|None|
|ID|string|None|False|ID of the group|None|
|Parent ID|string|None|False|The parent ID|None|
|Source|string|None|False|Source of the group, either cloud or LDAP|None|
|User Count|integer|None|False|Number of users in the group|None|
  
**click_logs**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|The action that was taken for the click|None|
|Admin Override|string|None|False|The action defined by the administrator for the URL|None|
|Category|string|None|False|The category of the URL clicked|None|
|Date|string|None|False|The date that the URL was clicked|None|
|Route|string|None|False|The route of the email that contained the link|None|
|Scan Result|string|None|False|The result of the URL scan|None|
|TTP Definition|string|None|False|The description of the definition that triggered the URL to be rewritten by Mimecast|None|
|URL|string|None|False|The URL clicked|None|
|User Awareness Action|string|None|False|The action taken by the user if user awareness was applied|None|
|User Email Address|string|None|False|The email address of the user who clicked the link|None|
|User Override|string|None|False|The action requested by the user|None|
  
**audit_events_data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Categories|[]string|None|False|A list of audit category types|["test", "malware"]|
|End Date Time|string|None|True|The end date of events in ISO 8601 date time format|2015-12-03T10:15:30+0000|
|Query|string|None|False|A character string to search for the audit events|test query|
|Start Date Time|string|None|True|The start date of events in ISO 8601 date time format|2011-12-03T10:15:30+0000|
  
**audit_events_request_pagination**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Page Size|integer|25|False|The number of results to request|None|
|Page Token|string|None|False|The value of the next or previous fields from an earlier request|None|
  
**audit_events_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Audit Type|string|None|False|The Mimecast audit type of the event|None|
|Category|string|None|False|The category of the event|None|
|Event Info|string|None|False|The detailed event information|None|
|Event Time|string|None|False|The time of the event in ISO 8601 format|None|
|ID|string|None|False|The Mimecast unique id of the event|None|
  
**pagination**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Next|string|None|False|A pageToken value that can be used to request the next page of results. Only returned if there are more results to return|None|
|Page Size|integer|None|False|The number of results requested|None|
|Previous|string|None|False|A pageToken value that can be used to request the previous page of results. Only returned if there is a previous page|None|
  
**search_criteria_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|End|string|None|False|The end date of messages included in ISO 8601 format|None|
|File Hash|string|None|False|The file hash used in creation of the remediation incident|None|
|From|string|None|False|The sender address of the message|None|
|Message ID|string|None|False|The message id use in creation of the remediation incident|None|
|Restore Code|string|None|False|The restore code used if the incident type is restore|None|
|Start|string|None|False|The start date of messages included in ISO 8601 format|None|
|Subject|string|None|False|Message subject line of the remediated message|None|
|To|string|None|False|The recipient email address of the message|None|
|Unremediate Code|string|None|False|The Mimecast code used to restore a previously remediated message|None|
|URL|string|None|False|URL used to create the remediation incident, if remediation type is URL|None|
  
**response_remediation_incident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|The incident code generated at creation, to be used as a reference for the remediation incident lookup|None|
|Create|string|None|False|Timestamp of the incident creation in ISO 8601 format|None|
|Failed|integer|None|False|The number of messages that failed to remediate|None|
|File Remediation Can be Cancelled|boolean|None|False|Indicates whether the file remediation incident can still be cancelled|None|
|File Remediation Cancelled|string|None|False|Timestamp of an incident cancellation, if it has been cancelled, in ISO 8601 format|None|
|File Remediation Expiry Time|string|None|False|Timestamp of a file-bases remediation should expiration in ISO 8601 format|None|
|ID|string|None|False|The Mimecast secure ID of the remediation incident|None|
|Identified|integer|None|False|Number of messages identified with provided search criteria|None|
|Modified|string|None|False|Timestamp of the incident's last modification date in ISO 8601 format|None|
|Reason|string|None|False|The reason provided at the creation of the remediation incident|None|
|Remediated by|string|None|False|Email address of the user who created the remediation incident|None|
|Remove From Device|string|None|False|The devices where the downloaded file should be removed from|None|
|Restored|integer|None|False|The number of messages that were restored, if incident was a restore|None|
|Search Criteria Object|search_criteria_object|None|False|The search criteria used to identify messages|None|
|Successful|integer|None|False|The number of successfully remediated messages|None|
|Type|string|None|False|Type of incident|None|
  
**searchCriteria**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|End|string|None|False|The end date from the remediation incident creation|None|
|File Hash|string|None|False|The file hash provided during the remediation incident creation|None|
|From|string|None|False|The sender address provided at the remediation incident creation|None|
|Message ID|string|None|False|The message ID provided during the remediation incident creation|None|
|Restore Code|string|None|False|The code provided to restore a message|None|
|Start|string|None|False|The start date from the remediation incident creation|None|
|To|string|None|False|The recipient address provided at the remediation incident creation|None|
|Unremediate Code|string|None|False|Code used to restore messages that were previously removed by remediation incident|None|
  
**get_remediation_incident_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|Incident code, used as a reference for a remediation incident|None|
|Create|string|None|False|Date that the remediation incident was created|None|
|Failed|integer|None|False|The number of messages that failed to remediate as part of the incident|None|
|ID|string|None|False|The Mimecast ID of the remediation incident, provided when the incident was created|None|
|Identified|integer|None|False|Number of messages identified by the search criteria|None|
|Modified|string|None|False|Date that the remediation incident was last updated|None|
|Reason|string|None|False|The reason provided when an incident was created|None|
|Restored|integer|None|False|The number of messages restored as part of the incident|None|
|Searchcriteria|[]searchCriteria|None|False|Conditions used to build a remediation incident. Includes messageId, file-hash, from or to addresses.|None|
|Successful|integer|None|False|The number of messages successfully remediated as part of the incident|None|
|Type|string|None|False|The type of incident action taken. Can be one of notify_only, automatic, manual or restored|None|
  
**find_remediation_searchBy**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Field Name|string|None|False|Incident fields to filter based on|None|
|Value|string|None|False|The text used to filter results|None|
  
**find_remediation_filterBy**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Type|string|None|False|Specify the type of incidents to return|None|
  
**searchCritera**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|End|string|None|False|Date of most recent incidents to return|None|
|File Hash|string|None|False|File hash used to create remediation incident|None|
|From|string|None|False|Sender address or domain name used to create remediation incident|None|
|Message ID|string|None|False|Message ID used to create remediation incident|None|
|Restore Code|string|None|False|Restore code for remediation event|None|
|Start|string|None|False|Date of oldest results to return|None|
|To|string|None|False|Recipient address or domain name used to create remediation incident|None|
|Unremediate Code|string|None|False|Code required to perform a message restoration|None|
  
**incidents**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|The remediation incident unique code|None|
|Create|string|None|False|The time stamp of the incident creation|None|
|Failed|integer|None|False|The number of messages that failed to remediate|None|
|ID|string|None|False|The Mimecast secure ID of the remediation incident|None|
|Identified|integer|None|False|The total number of messages identified as part of the remediation incident|None|
|Modified|string|None|False|The time stamp of the last modification to the incident|None|
|Reason|string|None|False|The reason provided when the remediation incident was created|None|
|Restored|integer|None|False|The number of messages restored from the remediation incident|None|
|Search Criteria|searchCritera|None|False|Criteria used when the remediation incident was created|None|
|Successful|integer|None|False|The number of messages sucessfully rememdiated|None|
|Type|string|None|False|The incident type|None|
  
**sender**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Display Name|string|None|False|The display name of the sender|None|
|Email Address|string|None|False|The email address of the sender|None|
  
**recipient**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Display Name|string|None|False|The display name of the recipient|None|
|Email Address|string|None|False|The email address of the recipient|None|
  
**tracked_emails**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attachments|boolean|None|False|Indicates whether the message has attachments or not|None|
|Detection Level|string|None|False|The spam scanning level applied to the message|None|
|Envelope From|sender|None|False|An object describing the envelope from address of the message|None|
|Header From|sender|None|False|An object describing the header from address information of the message|None|
|ID|string|None|False|The Mimecast ID of the message|None|
|Received|date|None|False|The date and time the message was received by Mimecast|None|
|Route|string|None|False|The route of the message|None|
|Sender IP Address|string|None|False|The source IP address of the message|None|
|Sent|date|None|False|The date and time that the message was sent / processed by Mimecast|None|
|Spam Score|integer|None|False|The spam score of the received message|None|
|Status|string|None|False|The status of the message|None|
|Subject|string|None|False|The subject of the message|None|
|To|[]recipient|None|False|An array of recipients|None|


## Troubleshooting


# Version History

* 6.0.1 - Addressed Snyk Vulnerability | SDK bump to latest version (6.3.4)
* 6.0.0 - Update to actions and triggers to utilize Mimecast API 2.0 | Update connection requirements to Mimecast API 2.0 requirements | Remove task `monitor_siem_logs` | Update third party documentation links for Mimecast API 2.0
* 5.3.21 - Update Task `monitor_siem_logs` to use new logging and status management | Update SDK to version 6.3.3
* 5.3.20 - Update Task `monitor_siem_logs` bump default rate limit period to 10 minutes and catch unexpected errors
* 5.3.19 - Update Task `monitor_siem_logs` to delay retry if a rate limit error is returned from Mimecast | Update SDK to version 6.2.0
* 5.3.18 - Fix task connection test | Trim whitespace from connection inputs | bump SDK to version 6.1.2
* 5.3.17 - Task `monitor_siem_logs` update the mapping used for the USBCOM region
* 5.3.16 - Task `monitor_siem_logs` Limit the number of events per run to 7500 | bump SDK to version 6.1.0
* 5.3.15 - Fix snyk vulnerabilities | bump SDK to version 6.0.1 | Allow for the task connection tests to pass back a message along side a status
* 5.3.14 - Improving task connection tests logging | bump SDK to version 5.6.1
* 5.3.13 - Adding in task connection tests | bump SDK to version 5.5.5 | Fix issue with logging bad JSON error
* 5.3.12 - Task `monitor_siem_logs` to ingest events if there is no datetime field | bump version of werkzeug used
* 5.3.11 - Task `monitor_siem_logs` to now use 24hrs as initial lookback, then 7 days for normal running | Task `monitor_siem_logs` allowing for a date to be supplied as a custom config | Task `monitor_siem_logs` to now log the request id of failed request to Mimecast | bump SDK to version 5.4.9
* 5.3.10 - Task `monitor_siem_logs`: To move token to next file even if there is no files found | bump SDK to 5.4.7
* 5.3.9 - Task `monitor_siem_logs`: Add in better error messages if the wrong region is provided
* 5.3.8 - Task `monitor_siem_logs` Update to use SDK 5.4.4 | Add additional logger for traceability when no logs returned | Improve error handling.
* 5.3.7 - Task `monitor_siem_logs` adding in sanitization for names of files to be read in | Include SDK 5.4 which adds new task custom_config parameter | Bump setuptools.
* 5.3.6 - Task `monitor_siem_logs` revert filter logic to 24 hours.
* 5.3.5 - Task `monitor_siem_logs` further error logging and bump filter logic to 108 hours.
* 5.3.4 - Task `monitor_siem_logs` exception handling for JSONDecodeError.
* 5.3.3 - Task `monitor_siem_logs` improved error logging and sanitization of filenames | SDK bump | fix schema for `find_groups` & `get_audit_events` | bump validators version.
* 5.3.2 - Connection: added regions USB and USBCOM | Monitor SIEM Logs: added logs for request and results information, removed `token` input parameter, updated pagination handler
* 5.3.1 - Monitor SIEM Logs: stop parsing datetime field
* 5.3.0 - Handled rate limiting error messaging | Update to latest plugin SDK
* 5.2.2 - Handled status code for `Monitor SIEM Logs` | Request limit set to 1 minute in `Monitor SIEM Logs`
* 5.2.1 - Connection: add connection version
* 5.2.0 - New task added `Monitor SIEM Logs` | Update plugin to be cloud enabled
* 5.1.0 - Create Blocked Sender Policy: Changed defaults to `individual_email_address` | New actions added `Delete Blocked Sender Policy`, `Track Messages`
* 5.1.0 - Create Blocked Sender Policy: Changed defaults to `individual_email_address` | New actions added `Delete Blocked Sender Policy`, `Track Messages`
* 5.0.2 - Add Group Member: Fix issue when users were running into email validation error when they add a domain, and leave the email address blank on the input section.
* 5.0.1 - Add Sandbox availability in region
* 5.0.0 - Update SDK version | Add new action Get Audit Events | Add unit tests for all actions | Update error handling for all action | Create separate class for API communication | Add base URL of API for plugin
* 4.1.2 - Fix bug in connection test where it could succeed when an empty response was returned
* 4.1.1 - Fix bug where the connection test would sometimes pass even with invalid credentials
* 4.1.0 - Update Get TTP URL Logs action to use pagination
* 4.0.1 - Add example inputs
* 4.0.0 - Update Get TTP URL Logs to allow for better URL filtering
* 3.1.0 - New action Delete Managed URL and Delete Group Member
* 3.0.1 - New spec and help.md format for the Extension Library
* 3.0.0 - Add URL in Get TTP URL Logs action to filter output | Update connection settings to the proper authentication supported by the Mimecast API
* 2.5.0 - New action Decode URL
* 2.4.0 - New action Get TTP URL Logs
* 2.3.0 - New actions Add Group Member and Find Group
* 2.2.0 - New action Create Blocked Sender Policy
* 2.1.0 - New action Permit or Block Sender
* 2.0.0 - Add Get Managed URL Action | Update descriptions and output titles
* 1.0.0 - Initial plugin

# Links

* [Mimecast](http://mimecast.com)

## References

* [Mimecast API](https://developer.services.mimecast.com/api-overview)