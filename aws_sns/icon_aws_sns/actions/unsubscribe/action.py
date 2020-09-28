# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import UnsubscribeInput, UnsubscribeOutput


class Unsubscribe(AWSAction):

    def __init__(self):
        super().__init__(
            name='unsubscribe',
            description='Deletes a subscription',
            input=UnsubscribeInput(),
            output=UnsubscribeOutput(),
            aws_service='sns',
            aws_command='unsubscribe',
            pagination_helper=None
        )
