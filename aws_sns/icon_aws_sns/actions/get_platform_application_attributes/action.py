# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import GetPlatformApplicationAttributesInput, GetPlatformApplicationAttributesOutput


class GetPlatformApplicationAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='get_platform_application_attributes',
            description='Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM',
            input=GetPlatformApplicationAttributesInput(),
            output=GetPlatformApplicationAttributesOutput(),
            aws_service='sns',
            aws_command='get_platform_application_attributes',
            pagination_helper=None
        )
