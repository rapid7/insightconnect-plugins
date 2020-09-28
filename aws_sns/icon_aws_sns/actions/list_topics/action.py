# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import ListTopicsInput, ListTopicsOutput
from ...common import PaginationHelper


class ListTopics(AWSAction):

    def __init__(self):
        super().__init__(
            name='list_topics',
            description='Returns a list of the requesters topics',
            input=ListTopicsInput(),
            output=ListTopicsOutput(),
            aws_service='sns',
            aws_command='list_topics',
            pagination_helper=PaginationHelper(
                input_token=['next_token'],
                output_token=['next_token'],
                result_key=['Topics']
            )
        )
