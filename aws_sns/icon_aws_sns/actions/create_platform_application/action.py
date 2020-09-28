# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import CreatePlatformApplicationInput, CreatePlatformApplicationOutput


class CreatePlatformApplication(AWSAction):

    def __init__(self):
        super().__init__(
            name='create_platform_application',
            description='Creates a platform application object for one of the supported push notification services, such as APNS and GCM, to which devices and mobile apps may register',
            input=CreatePlatformApplicationInput(),
            output=CreatePlatformApplicationOutput(),
            aws_service='sns',
            aws_command='create_platform_application',
            pagination_helper=None
        )
