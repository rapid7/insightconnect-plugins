# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import DeletePlatformApplicationInput, DeletePlatformApplicationOutput


class DeletePlatformApplication(AWSAction):

    def __init__(self):
        super().__init__(
            name='delete_platform_application',
            description='Deletes a platform application object for one of the supported push notification services, such as APNS and GCM',
            input=DeletePlatformApplicationInput(),
            output=DeletePlatformApplicationOutput(),
            aws_service='sns',
            aws_command='delete_platform_application',
            pagination_helper=None
        )
