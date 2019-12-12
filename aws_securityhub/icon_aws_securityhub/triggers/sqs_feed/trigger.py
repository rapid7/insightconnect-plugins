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
        attrNames = params.get(Input.ATTRIBUTENAMES)
        maxMsgs = params.get(Input.MAXNUMBEROFMESSAGES)
        msgAttrNames = params.get(Input.MESSAGEATTRIBUTENAMES)
        recReqAttemptId = params.get(Input.RECEIVEREQUESTATTEMPTID)
        visTimeout = params.get(Input.VISIBILITYTIMEOUT)
        waitTime = params.get(Input.WAITTIMESECONDS)

        valid_attrNames = {
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

        if set(attrNames) - valid_attrNames:
            invalid_attrnames = set(attrNames) - valid_attrNames
            raise Exception(
                f"""Attribute Names: {invalid_attrnames} and invalid \n Valid Attribute Names: 'All','Policy','VisibilityTimeout','MaximumMessageSize','MessageRetentionPeriod','ApproximateNumberOfMessages','ApproximateNumberOfMessagesNotVisible','CreatedTimestamp','LastModifiedTimestamp','QueueArn','ApproximateNumberOfMessagesDelayed','DelaySeconds','ReceiveMessageWaitTimeSeconds', 'RedrivePolicy', 'FifoQueue', 'ContentBasedDeduplication', 'KmsMasterKeyId', 'KmsDataKeyReusePeriodSeconds'"""
            )

        while True:
            # get Message/messages
            response = client.receive_message(
                QueueUrl=sqs_url,
                AttributeNames=attrNames,
                MaxNumberOfMessages=maxMsgs,
                MessageAttributeNames=msgAttrNames,
                VisibilityTimeout=visTimeout,
                WaitTimeSeconds=waitTime,
                ReceiveRequestAttemptId=recReqAttemptId,
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
                            Output.SECURITYHUBEVENT: security_hub_event,
                            Output.RESPONSEMETADATA: response["ResponseMetadata"]
                        }
                    )
                    receipt_handle = message["ReceiptHandle"]
                    client.delete_message(
                        QueueUrl=sqs_url, ReceiptHandle=receipt_handle
                    )

            time.sleep(params.get("interval", 5))
