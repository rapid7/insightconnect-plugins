# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import PublishInput, PublishOutput


class Publish(AWSAction):

    def __init__(self):
        super().__init__(
            name='publish',
            description='Sends a message to all of a topics subscribed endpoints',
            input=PublishInput(),
            output=PublishOutput(),
            aws_service='sns',
            aws_command='publish',
            pagination_helper=None
        )
