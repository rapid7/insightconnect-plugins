# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import OptInPhoneNumberInput, OptInPhoneNumberOutput


class OptInPhoneNumber(AWSAction):

    def __init__(self):
        super().__init__(
            name='opt_in_phone_number',
            description='Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number',
            input=OptInPhoneNumberInput(),
            output=OptInPhoneNumberOutput(),
            aws_service='sns',
            aws_command='opt_in_phone_number',
            pagination_helper=None
        )
