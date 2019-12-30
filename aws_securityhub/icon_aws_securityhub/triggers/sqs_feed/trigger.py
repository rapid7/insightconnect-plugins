import komand
import time
from .schema import SqsFeedInput, SqsFeedOutput, Input, Output, Component

import json

# Custom imports below


class SqsFeed(komand.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sqs_feed",
            description=Component.DESCRIPTION,
            input=SqsFeedInput(),
            output=SqsFeedOutput(),
        )

    def run(self, params={}):
        """Run the trigger"""
        client = self.connection.aws.client("sqs")
        sqs_url = params.get(Input.QUEUE_URL)
        attribute_names = params.get(Input.ATTRIBUTE_NAMES)
        max_number_of_messages = params.get(Input.MAX_NUMBER_OF_MESSAGES)
        message_attribute_names = params.get(Input.MESSAGE_ATTRIBUTE_NAMES)
        receive_request_attempt_id = params.get(Input.RECEIVE_REQUEST_ATTEMPT_ID)
        visibility_timeout = params.get(Input.VISIBILITY_TIMEOUT)
        wait_time_seconds = params.get(Input.WAIT_TIME_SECONDS)

        valid_attr_names = {
            "All",
            "Policy",
            "VisibilityTimeout",
            "MaximumMessageSize",
            "MessageRetentionPeriod",
            "ApproximateNumberOfMessages",
            "ApproximateNumberOfMessagesNotVisible",
            "CreatedTimestamp",
            "LastModifiedTimestamp",
            "QueueArn",
            "ApproximateNumberOfMessagesDelayed",
            "DelaySeconds",
            "ReceiveMessageWaitTimeSeconds",
            "RedrivePolicy",
            "FifoQueue",
            "ContentBasedDeduplication",
            "KmsMasterKeyId",
            "KmsDataKeyReusePeriodSeconds",
        }

        if set(attribute_names) - valid_attr_names:
            invalid_attribute_names = set(attribute_names) - valid_attr_names
            raise Exception(
                f"""Attribute Names: {invalid_attribute_names} and invalid \n Valid Attribute Names: 'All','Policy','VisibilityTimeout','MaximumMessageSize','MessageRetentionPeriod','ApproximateNumberOfMessages','ApproximateNumberOfMessagesNotVisible','CreatedTimestamp','LastModifiedTimestamp','QueueArn','ApproximateNumberOfMessagesDelayed','DelaySeconds','ReceiveMessageWaitTimeSeconds', 'RedrivePolicy', 'FifoQueue', 'ContentBasedDeduplication', 'KmsMasterKeyId', 'KmsDataKeyReusePeriodSeconds'"""
            )

        while True:
            # get Message/messages
            response = client.receive_message(
                QueueUrl=sqs_url,
                AttributeNames=attribute_names,
                MaxNumberOfMessages=max_number_of_messages,
                MessageAttributeNames=message_attribute_names,
                VisibilityTimeout=visibility_timeout,
                WaitTimeSeconds=wait_time_seconds,
                ReceiveRequestAttemptId=receive_request_attempt_id,
            )
            # send message
            if response.get("Messages"):
                for message in response["Messages"]:
                    security_hub_event = {}
                    # This will always be JSON.
                    if message.get("Body"):
                        try:
                            security_hub_event = json.loads(message["Body"])
                        except Exception as e:
                            self.logger.error(f"An unexpected event occurred when processing the Security Hub Event: {e}")

                    self.send(
                        {
                            Output.MESSAGE: message,
                            Output.SECURITY_HUB_EVENT: security_hub_event,
                            Output.RESPONSE_METADATA: response["ResponseMetadata"]
                        }
                    )
                    receipt_handle = message["ReceiptHandle"]
                    client.delete_message(
                        QueueUrl=sqs_url, ReceiptHandle=receipt_handle
                    )

            time.sleep(params.get("interval", 5))
