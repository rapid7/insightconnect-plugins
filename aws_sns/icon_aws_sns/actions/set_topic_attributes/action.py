# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import SetTopicAttributesInput, SetTopicAttributesOutput


class SetTopicAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='set_topic_attributes',
            description='Allows a topic owner to set an attribute of the topic to a new value',
            input=SetTopicAttributesInput(),
            output=SetTopicAttributesOutput(),
            aws_service='sns',
            aws_command='set_topic_attributes',
            pagination_helper=None
        )
