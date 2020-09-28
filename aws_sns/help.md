## About
[Amazon Simple Notification Service (SNS)](https://aws.amazon.com/documentation/sns) is a Amazon Simple Notification Service (Amazon SNS) is a web service that enables you to build distributed web-enabled applications
This plugin utilizes the [Amazon Simple Notification Service (SNS) API](https://docs.aws.amazon.com/sns/latest/api/Welcome.html).

## Actions

### Add Permission

Adds a statement to a topics access control policy, granting access for the specified AWS accounts to the specified actions. See [https://docs.aws.amazon.com/sns/latest/api/API_AddPermission.html](https://docs.aws.amazon.com/sns/latest/api/API_AddPermission.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|True|The ARN of the topic whose access control policy you wish to modify.|None|
|label|string|None|True|A unique identifier for the new policy statement.|None|
|aws_account_id|[]string|None|True|The AWS account IDs of the users (principals) who will be given access to the specified actions.|None|
|action_name|[]string|None|True|The action you want to allow for the specified principal(s).|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Check If Phone Number Is Opted Out

Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your account. See [https://docs.aws.amazon.com/sns/latest/api/API_CheckIfPhoneNumberIsOptedOut.html](https://docs.aws.amazon.com/sns/latest/api/API_CheckIfPhoneNumberIsOptedOut.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|phone_number|string|None|True|The phone number for which you want to check the opt out status.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|is_opted_out|boolean|False|Indicates whether the phone number is opted out\:    true – The phone number is opted out, meaning you cannot publish SMS messages to it.|

### Confirm Subscription

Verifies an endpoint owners intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action. See [https://docs.aws.amazon.com/sns/latest/api/API_ConfirmSubscription.html](https://docs.aws.amazon.com/sns/latest/api/API_ConfirmSubscription.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|True|The ARN of the topic for which you wish to confirm a subscription.|None|
|token|string|None|True|Short-lived token sent to an endpoint during the Subscribe action.|None|
|authenticate_on_unsubscribe|string|None|False|Disallows unauthenticated unsubscribes of the subscription.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|subscription_arn|string|False|The ARN of the created subscription.|

### Create Platform Application

Creates a platform application object for one of the supported push notification services, such as APNS and GCM, to which devices and mobile apps may register. See [https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformApplication.html](https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformApplication.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.|None|
|platform|string|None|True|The following platforms are supported\: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Google Cloud Messaging).|None|
|attributes|object|None|True|For a list of attributes, see SetPlatformApplicationAttributes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|platform_application_arn|string|False|PlatformApplicationArn is returned.|

### Create Platform Endpoint

Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM and APNS. See [https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformEndpoint.html](https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformEndpoint.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|platform_application_arn|string|None|True|PlatformApplicationArn returned from CreatePlatformApplication is used to create a an endpoint.|None|
|token|string|None|True|Unique identifier created by the notification service for an app on a device.|None|
|custom_user_data|string|None|False|Arbitrary user data to associate with the endpoint.|None|
|attributes|object|None|False|For a list of attributes, see SetEndpointAttributes.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|endpoint_arn|string|False|EndpointArn returned from CreateEndpoint action.|

### Create Topic

Creates a topic to which notifications can be published. See [https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|The name of the topic you want to create.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|topic_arn|string|False|The Amazon Resource Name (ARN) assigned to the created topic.|

### Delete Endpoint

Deletes the endpoint for a device and mobile app from Amazon SNS. See [https://docs.aws.amazon.com/sns/latest/api/API_DeleteEndpoint.html](https://docs.aws.amazon.com/sns/latest/api/API_DeleteEndpoint.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|endpoint_arn|string|None|True|EndpointArn of endpoint to delete.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Delete Platform Application

Deletes a platform application object for one of the supported push notification services, such as APNS and GCM. See [https://docs.aws.amazon.com/sns/latest/api/API_DeletePlatformApplication.html](https://docs.aws.amazon.com/sns/latest/api/API_DeletePlatformApplication.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|platform_application_arn|string|None|True|PlatformApplicationArn of platform application object to delete.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Delete Topic

Deletes a topic and all its subscriptions. See [https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html](https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|True|The ARN of the topic you want to delete.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Get Endpoint Attributes

Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM and APNS. See [https://docs.aws.amazon.com/sns/latest/api/API_GetEndpointAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetEndpointAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|endpoint_arn|string|None|True|EndpointArn for GetEndpointAttributes input.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|attributes|object|False|Attributes include the following\:    CustomUserData -- arbitrary user data to associate with the endpoint.|

### Get Platform Application Attributes

Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM. See [https://docs.aws.amazon.com/sns/latest/api/API_GetPlatformApplicationAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetPlatformApplicationAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|platform_application_arn|string|None|True|PlatformApplicationArn for GetPlatformApplicationAttributesInput.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|attributes|object|False|Attributes include the following\:    EventEndpointCreated -- Topic ARN to which EndpointCreated event notifications should be sent.|

### Get Sms Attributes

Returns the settings for sending SMS messages from your account. See [https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|attributes|[]string|None|False|A list of the individual attribute names, such as MonthlySpendLimit, for which you want values.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|attributes|object|False|The SMS attribute names and their values.|

### Get Subscription Attributes

Returns all of the properties of a subscription. See [https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|subscription_arn|string|None|True|The ARN of the subscription whose properties you want to get.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|attributes|object|False|A map of the subscriptions attributes.|

### Get Topic Attributes

Returns all of the properties of a topic. See [https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|True|The ARN of the topic whose properties you want to get.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|attributes|object|False|A map of the topics attributes.|

### List Endpoints By Platform Application

Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM and APNS. See [https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html](https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|platform_application_arn|string|None|True|PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|endpoints|[]endpoint|False|Endpoints returned for ListEndpointsByPlatformApplication action.|

### List Phone Numbers Opted Out

Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them. See [https://docs.aws.amazon.com/sns/latest/api/API_ListPhoneNumbersOptedOut.html](https://docs.aws.amazon.com/sns/latest/api/API_ListPhoneNumbersOptedOut.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|next_token|string|None|False|A NextToken string is used when you call the ListPhoneNumbersOptedOut action to retrieve additional records that are available after the first page of results.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|phone_numbers|[]string|False|A list of phone numbers that are opted out of receiving SMS messages.|
|next_token|string|False|A NextToken string is returned when you call the ListPhoneNumbersOptedOut action if additional records are available after the first page of results.|

### List Platform Applications

Lists the platform application objects for the supported push notification services, such as APNS and GCM. See [https://docs.aws.amazon.com/sns/latest/api/API_ListPlatformApplications.html](https://docs.aws.amazon.com/sns/latest/api/API_ListPlatformApplications.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|platform_applications|[]platform_application|False|Platform applications returned when calling ListPlatformApplications action.|

### List Subscriptions

Returns a list of the requesters subscriptions. See [https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|subscriptions|[]subscription|False|A list of subscriptions.|

### List Subscriptions By Topic

Returns a list of the subscriptions to a specific topic. See [https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|True|The ARN of the topic for which you wish to find subscriptions.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|subscriptions|[]subscription|False|A list of subscriptions.|

### List Topics

Returns a list of the requesters topics. See [https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|topics|[]topic|False|A list of topic ARNs.|

### Opt In Phone Number

Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number. See [https://docs.aws.amazon.com/sns/latest/api/API_OptInPhoneNumber.html](https://docs.aws.amazon.com/sns/latest/api/API_OptInPhoneNumber.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|phone_number|string|None|True|The phone number to opt in.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Publish

Sends a message to all of a topics subscribed endpoints. See [https://docs.aws.amazon.com/sns/latest/api/API_Publish.html](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|False|The topic you want to publish to.|None|
|target_arn|string|None|False|Either TopicArn or EndpointArn, but not both.|None|
|phone_number|string|None|False|The phone number to which you want to deliver an SMS message.|None|
|message|string|None|True|The message you want to send to the topic.|None|
|subject|string|None|False|Optional parameter to be used as the Subject line when the message is delivered to email endpoints.|None|
|message_structure|string|None|False|Set MessageStructure to json if you want to send a different message for each protocol.|None|
|message_attributes|object|None|False|Message attributes for Publish action.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|message_id|string|False|Unique identifier assigned to the published message.|

### Remove Permission

Removes a statement from a topics access control policy. See [https://docs.aws.amazon.com/sns/latest/api/API_RemovePermission.html](https://docs.aws.amazon.com/sns/latest/api/API_RemovePermission.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|True|The ARN of the topic whose access control policy you wish to modify.|None|
|label|string|None|True|The unique label of the statement you want to remove.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Set Endpoint Attributes

Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM and APNS. See [https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|endpoint_arn|string|None|True|EndpointArn used for SetEndpointAttributes action.|None|
|attributes|object|None|True|A map of the endpoint attributes.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Set Platform Application Attributes

Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM. See [https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|platform_application_arn|string|None|True|PlatformApplicationArn for SetPlatformApplicationAttributes action.|None|
|attributes|object|None|True|A map of the platform application attributes.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Set Sms Attributes

Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports. See [https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|attributes|object|None|True|The default settings for sending SMS messages from your account.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Set Subscription Attributes

Allows a subscription owner to set an attribute of the topic to a new value. See [https://docs.aws.amazon.com/sns/latest/api/API_SetSubscriptionAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_SetSubscriptionAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|subscription_arn|string|None|True|The ARN of the subscription to modify.|None|
|attribute_name|string|None|True|The name of the attribute you want to set.|None|
|attribute_value|string|None|False|The new value for the attribute in JSON format.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Set Topic Attributes

Allows a topic owner to set an attribute of the topic to a new value. See [https://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|True|The ARN of the topic to modify.|None|
|attribute_name|string|None|True|The name of the attribute you want to set.|None|
|attribute_value|string|None|False|The new value for the attribute.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

### Subscribe

Prepares to subscribe an endpoint by sending the endpoint a confirmation message. See [https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic_arn|string|None|True|The ARN of the topic you want to subscribe to.|None|
|protocol|string|None|True|The protocol you want to use.|None|
|endpoint|string|None|False|The endpoint that you want to receive notifications.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|subscription_arn|string|False|The ARN of the subscription, if the service was able to create a subscription immediately (without requiring endpoint owner confirmation).|

### Unsubscribe

Deletes a subscription. See [https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html](https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html)

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|subscription_arn|string|None|True|The ARN of the subscription to be deleted.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|aws_access_key_id|string|None|True|The ID of the AWS Access Key to use for authentication with AWS|None|
|aws_secret_access_key|password|None|True|The AWS Secret Access Key used for signing requests with the given AWS Access Key ID|None|
|region|string|None|True|The AWS Region to use for requests. An example would be us-east-1|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 0.1.0 - Initial plugin

## Workflows

Examples:
* Example goes here

## References
* [Documentation Overview](https://aws.amazon.com/documentation/sns)
* [API Reference](https://docs.aws.amazon.com/sns/latest/api/Welcome.html)
