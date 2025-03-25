# Description

[Mimecast](https://www.mimecast.com) is a set of cloud services designed to provide next generation protection against advanced email-borne threats such as malicious URLs, malware, impersonation attacks, as well as internally generated threats, with a focus on email security. This plugin utilizes the [Mimecast API](https://www.mimecast.com/developer/documentation)

# Key Features

* Email security
* Malicious URL and attachment detection

# Requirements

* Mimecast 2.0 Application Client ID
* Mimecast 2.0 Application Client Secret

# Supported Product Versions

* Mimecast 2.0 API 2025-01-23

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|credential_secret_key|None|True|The Mimecast 2.0 Application Client ID|None|ZA7vkbu7NqcfBcGrXyWW8Rzk2sv2un2DCY7GGCX4BFWgJBZM|Client ID|Enter the Client ID obtained from the Mimecast 2.0 API Application|
|client_secret|credential_secret_key|None|True|The Mimecast 2.0 Application Client Secret|None|ohknqKJpCd99XTkHjeVuc2TgYaKWrWn4tEEHCLkXFZhFgDRdcpNGVx3EipX2CvmE|Client Secret|Enter the Client ID obtained from the Mimecast 2.0 API Application|

Example input:

```
{
  "client_id": "ZA7vkbu7NqcfBcGrXyWW8Rzk2sv2un2DCY7GGCX4BFWgJBZM",
  "client_secret": "ohknqKJpCd99XTkHjeVuc2TgYaKWrWn4tEEHCLkXFZhFgDRdcpNGVx3EipX2CvmE"
}
```

## Technical Details

### Actions
  
*This plugin does not contain any actions.*
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks


#### Monitor SIEM Logs

This task is used to monitor and retrieve the latest logs

##### Input
  
*This task does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]object|True|List of logs|[{"processingId": "processingId", "aggregateId": "aggregateId", "spamProcessingDetail": "Spam Processing Detail", "numberAttachments": "1", "subject": "siem_recipient - email subject line", "tlsVersion": "TLSv1.2", "senderEnvelope": "user@example.com", "messageId": "messageId", "senderHeader": "user@example.com", "rejectionType": "rejectionType", "eventType": "receipt", "accountId": "C0A0", "recipients": "user@example.com", "tlsCipher": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "action": "Allow", "subType": "Allow", "spamInfo": null, "senderIp": "123.123.123.123", "timestamp": 1689685338597, "direction": "Inbound", "spamScore": "0", "spamDetectionLevel": "0"}]|
  
Example output:

```
{
  "data": [
    {
      "accountId": "C0A0",
      "action": "Allow",
      "aggregateId": "aggregateId",
      "direction": "Inbound",
      "eventType": "receipt",
      "messageId": "messageId",
      "numberAttachments": "1",
      "processingId": "processingId",
      "recipients": "user@example.com",
      "rejectionType": "rejectionType",
      "senderEnvelope": "user@example.com",
      "senderHeader": "user@example.com",
      "senderIp": "123.123.123.123",
      "spamDetectionLevel": "0",
      "spamInfo": null,
      "spamProcessingDetail": "Spam Processing Detail",
      "spamScore": "0",
      "subType": "Allow",
      "subject": "siem_recipient - email subject line",
      "timestamp": 1689685338597,
      "tlsCipher": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
      "tlsVersion": "TLSv1.2"
    }
  ]
}
```

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting


# Version History

* 1.0.4 - `Monitor SIEM Logs` Fix issue where duplicate batches in a page are processed
* 1.0.3 - `Monitor SIEM Logs` Fix issue retrieving logs from larger log files
* 1.0.2 - `Monitor SIEM Logs` Limit the amount of logs used to deduplicate logs in subsequent runs
* 1.0.1 - Update SDK | Improve output for a successful connection test
* 1.0.0 - Initial plugin

# Links

* [Mimecast](http://mimecast.com)

## References

* [Mimecast API](https://www.mimecast.com/developer/documentation)