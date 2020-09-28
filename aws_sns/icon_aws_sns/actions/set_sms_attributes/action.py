# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import SetSmsAttributesInput, SetSmsAttributesOutput


class SetSmsAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='set_sms_attributes',
            description='Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports',
            input=SetSmsAttributesInput(),
            output=SetSmsAttributesOutput(),
            aws_service='sns',
            aws_command='set_sms_attributes',
            pagination_helper=None
        )
