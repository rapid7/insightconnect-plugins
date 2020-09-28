# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import ListSubscriptionsInput, ListSubscriptionsOutput
from ...common import PaginationHelper


class ListSubscriptions(AWSAction):

    def __init__(self):
        super().__init__(
            name='list_subscriptions',
            description='Returns a list of the requesters subscriptions',
            input=ListSubscriptionsInput(),
            output=ListSubscriptionsOutput(),
            aws_service='sns',
            aws_command='list_subscriptions',
            pagination_helper=PaginationHelper(
                input_token=['next_token'],
                output_token=['next_token'],
                result_key=['Subscriptions']
            )
        )
