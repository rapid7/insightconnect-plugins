# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import DeleteTopicInput, DeleteTopicOutput


class DeleteTopic(AWSAction):

    def __init__(self):
        super().__init__(
            name='delete_topic',
            description='Deletes a topic and all its subscriptions',
            input=DeleteTopicInput(),
            output=DeleteTopicOutput(),
            aws_service='sns',
            aws_command='delete_topic',
            pagination_helper=None
        )
