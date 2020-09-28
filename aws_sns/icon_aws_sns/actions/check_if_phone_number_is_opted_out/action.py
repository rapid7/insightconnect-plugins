# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import CheckIfPhoneNumberIsOptedOutInput, CheckIfPhoneNumberIsOptedOutOutput


class CheckIfPhoneNumberIsOptedOut(AWSAction):

    def __init__(self):
        super().__init__(
            name='check_if_phone_number_is_opted_out',
            description='Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your account',
            input=CheckIfPhoneNumberIsOptedOutInput(),
            output=CheckIfPhoneNumberIsOptedOutOutput(),
            aws_service='sns',
            aws_command='check_if_phone_number_is_opted_out',
            pagination_helper=None
        )
