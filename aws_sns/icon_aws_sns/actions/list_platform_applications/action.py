# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import ListPlatformApplicationsInput, ListPlatformApplicationsOutput
from ...common import PaginationHelper


class ListPlatformApplications(AWSAction):

    def __init__(self):
        super().__init__(
            name='list_platform_applications',
            description='Lists the platform application objects for the supported push notification services, such as APNS and GCM',
            input=ListPlatformApplicationsInput(),
            output=ListPlatformApplicationsOutput(),
            aws_service='sns',
            aws_command='list_platform_applications',
            pagination_helper=PaginationHelper(
                input_token=['next_token'],
                output_token=['next_token'],
                result_key=['PlatformApplications']
            )
        )
