# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import GetTopicAttributesInput, GetTopicAttributesOutput


class GetTopicAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='get_topic_attributes',
            description='Returns all of the properties of a topic',
            input=GetTopicAttributesInput(),
            output=GetTopicAttributesOutput(),
            aws_service='sns',
            aws_command='get_topic_attributes',
            pagination_helper=None
        )
