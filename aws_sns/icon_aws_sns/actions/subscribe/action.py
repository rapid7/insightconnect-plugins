# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import SubscribeInput, SubscribeOutput


class Subscribe(AWSAction):

    def __init__(self):
        super().__init__(
            name='subscribe',
            description='Prepares to subscribe an endpoint by sending the endpoint a confirmation message',
            input=SubscribeInput(),
            output=SubscribeOutput(),
            aws_service='sns',
            aws_command='subscribe',
            pagination_helper=None
        )
