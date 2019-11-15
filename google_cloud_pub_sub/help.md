# Description

[Google Cloud PubSub](https://cloud.google.com/pubsub/) is a fully-managed real-time messaging service that allows you to send and receive messages. The InsightConnect plugin allows you to automate sending and receiving messages. Trigger of of receiving new messages and take action with the message content
This plugin utilizes the [Google Cloud PubSub API](https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/pubsub).

# Key Features

* Publish messages
* Pull new messages from a subscription
* Create new topics
* Create new subscriptions

# Requirements

* A JWT With permissions to Google Cloud Pub Sub
* Google Cloud Pub Sub API enabled

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|private_key|password|None|True|Private Key from service credentials|None|
|admin_user|string|None|False|Admin user to impersonate, e.g. admin@domain.com|None|
|private_key_id|password|None|True|Private Key ID from service credentials|None|
|token_uri|string|https\://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|
|auth_provider_x509_cert_url|string|https\://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|
|auth_uri|string|https\://accounts.google.com/o/oauth2/auth|True|None|None|
|client_email|string|None|True|Client email from service credentials|None|
|client_id|string|None|True|Client ID e.g. 109587155068933904953|None|
|project_id|string|None|True|Project ID from service credentials e.g. subpub-1528163449245|None|
|client_x509_cert_url|string|None|True|X509 cert URL from service credentials|None|

## Technical Details

### Actions

#### Create Topic

This action is used to create a new topic.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|The name of the topic|None|
|project_id|string|None|False|The project ID for the topic e.g. subpub-1528163449245. If left blank the plugin will use the project ID found in the connection|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|topic|string|False|Return info on the new topic|

Example output:

```

{
  "topic": "projects/subpub-1528163449245/topics/komand_topic_test"
}

```

#### Create Subscription

This action is used to create a new subscription to a topic.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|The name of the topic to subscribe to|None|
|subscription_name|string|None|True|The name of the subscription to create|None|
|project_id|string|None|False|The project ID for the topic e.g. subpub-1528163449245. If left blank the plugin will use the project ID found in the connection|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|subscription|string|False|Return information on the new subscription|

Example output:

```

{
  "subscription": "projects/subpub-1528163449245/subscriptions/komand_sub_test"
}

```

#### List Topics

This action is used to list all topics within a project.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|project_id|string|None|False|The Project ID to find related topics for e.g. subpub-1528163449245. If left blank the plugin will use the project ID found in the connection|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|topics|[]string|False|A list of topics found|

Example output:

```

{
  "topics": [
    "projects/subpub-1528163449245/topics/test",
    "projects/subpub-1528163449245/topics/new_test",
    "projects/subpub-1528163449245/topics/komand_topic_test",
    "projects/subpub-1528163449245/topics/woo_its_a_topic2",
    "projects/subpub-1528163449245/topics/woo_its_a_topic"
  ]
}

```

#### Publish

This action is used to publish to a topic.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|The name of the topic to publish to|None|
|message|string|None|True|The message to publish to the topic|None|
|project_id|string|None|False|The project ID for the topic e.g. subpub-1528163449245. If left blank the plugin will use the project ID found in the connection|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Return true if it worked|

Example output:

```

{
  "success": true
}

```

### Triggers

#### Subscription

This trigger is used to pull new messages from a subscription.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|number_of_messages|integer|1|True|The number of messages to return at one time as a list. Must be 1 or more|None|
|project_id|string|None|True|The project ID for the subscription e.g. subpub-1528163449245|None|
|subscription|string|None|True|The subscription to pull from|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|messages|[]string|False|Messages found in the subscription|

Example output:

```
{
  "messages": ["test message 1","test message 2","test message 3"]
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin requires a Google [service account](https://cloud.google.com/storage/docs/authentication#generating-a-private-key).

* If using an admin user, the service account must have the necessary permissions to impersonate the admin user.
* The admin user or service account must have the necessary permissions to perform the desired action.

# Version History

* 3.1.1 - Fix typo in plugin spec
* 3.1.0 - Update connection to make `admin_user` an optional input
* 3.0.0 - Update trigger to allow for the return of multiple messages at one time
* 2.0.0 - Update to new credential types
* 1.0.0 - Initial plugin

# Links

## References

* [API docs](https://google-cloud-python.readthedocs.io/en/latest/pubsub/index.html)

