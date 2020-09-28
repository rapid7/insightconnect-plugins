# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import ListPhoneNumbersOptedOutInput, ListPhoneNumbersOptedOutOutput


class ListPhoneNumbersOptedOut(AWSAction):

    def __init__(self):
        super().__init__(
            name='list_phone_numbers_opted_out',
            description='Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them',
            input=ListPhoneNumbersOptedOutInput(),
            output=ListPhoneNumbersOptedOutOutput(),
            aws_service='sns',
            aws_command='list_phone_numbers_opted_out',
            pagination_helper=None
        )
