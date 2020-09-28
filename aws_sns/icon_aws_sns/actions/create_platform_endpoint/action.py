# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import CreatePlatformEndpointInput, CreatePlatformEndpointOutput


class CreatePlatformEndpoint(AWSAction):

    def __init__(self):
        super().__init__(
            name='create_platform_endpoint',
            description='Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM and APNS',
            input=CreatePlatformEndpointInput(),
            output=CreatePlatformEndpointOutput(),
            aws_service='sns',
            aws_command='create_platform_endpoint',
            pagination_helper=None
        )
