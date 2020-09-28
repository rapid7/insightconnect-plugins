# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import ConfirmSubscriptionInput, ConfirmSubscriptionOutput


class ConfirmSubscription(AWSAction):

    def __init__(self):
        super().__init__(
            name='confirm_subscription',
            description='Verifies an endpoint owners intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action',
            input=ConfirmSubscriptionInput(),
            output=ConfirmSubscriptionOutput(),
            aws_service='sns',
            aws_command='confirm_subscription',
            pagination_helper=None
        )
