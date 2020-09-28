# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import GetSmsAttributesInput, GetSmsAttributesOutput


class GetSmsAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='get_sms_attributes',
            description='Returns the settings for sending SMS messages from your account',
            input=GetSmsAttributesInput(),
            output=GetSmsAttributesOutput(),
            aws_service='sns',
            aws_command='get_sms_attributes',
            pagination_helper=None
        )
