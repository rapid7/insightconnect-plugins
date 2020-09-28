# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import RemovePermissionInput, RemovePermissionOutput


class RemovePermission(AWSAction):

    def __init__(self):
        super().__init__(
            name='remove_permission',
            description='Removes a statement from a topics access control policy',
            input=RemovePermissionInput(),
            output=RemovePermissionOutput(),
            aws_service='sns',
            aws_command='remove_permission',
            pagination_helper=None
        )
