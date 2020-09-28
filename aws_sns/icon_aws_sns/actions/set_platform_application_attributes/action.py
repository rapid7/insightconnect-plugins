# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import SetPlatformApplicationAttributesInput, SetPlatformApplicationAttributesOutput


class SetPlatformApplicationAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='set_platform_application_attributes',
            description='Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM',
            input=SetPlatformApplicationAttributesInput(),
            output=SetPlatformApplicationAttributesOutput(),
            aws_service='sns',
            aws_command='set_platform_application_attributes',
            pagination_helper=None
        )
