# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import SetSubscriptionAttributesInput, SetSubscriptionAttributesOutput


class SetSubscriptionAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='set_subscription_attributes',
            description='Allows a subscription owner to set an attribute of the topic to a new value',
            input=SetSubscriptionAttributesInput(),
            output=SetSubscriptionAttributesOutput(),
            aws_service='sns',
            aws_command='set_subscription_attributes',
            pagination_helper=None
        )
