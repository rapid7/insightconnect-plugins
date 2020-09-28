# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import GetSubscriptionAttributesInput, GetSubscriptionAttributesOutput


class GetSubscriptionAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='get_subscription_attributes',
            description='Returns all of the properties of a subscription',
            input=GetSubscriptionAttributesInput(),
            output=GetSubscriptionAttributesOutput(),
            aws_service='sns',
            aws_command='get_subscription_attributes',
            pagination_helper=None
        )
