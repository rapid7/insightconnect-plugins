# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import ListEndpointsByPlatformApplicationInput, ListEndpointsByPlatformApplicationOutput
from ...common import PaginationHelper


class ListEndpointsByPlatformApplication(AWSAction):

    def __init__(self):
        super().__init__(
            name='list_endpoints_by_platform_application',
            description='Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM and APNS',
            input=ListEndpointsByPlatformApplicationInput(),
            output=ListEndpointsByPlatformApplicationOutput(),
            aws_service='sns',
            aws_command='list_endpoints_by_platform_application',
            pagination_helper=PaginationHelper(
                input_token=['next_token'],
                output_token=['next_token'],
                result_key=['Endpoints']
            )
        )
