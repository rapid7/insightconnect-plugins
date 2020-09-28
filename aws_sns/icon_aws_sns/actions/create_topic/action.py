# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import CreateTopicInput, CreateTopicOutput


class CreateTopic(AWSAction):

    def __init__(self):
        super().__init__(
            name='create_topic',
            description='Creates a topic to which notifications can be published',
            input=CreateTopicInput(),
            output=CreateTopicOutput(),
            aws_service='sns',
            aws_command='create_topic',
            pagination_helper=None
        )
