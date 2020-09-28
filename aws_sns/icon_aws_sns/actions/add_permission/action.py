# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import AddPermissionInput, AddPermissionOutput


class AddPermission(AWSAction):

    def __init__(self):
        super().__init__(
            name='add_permission',
            description='Adds a statement to a topics access control policy, granting access for the specified AWS accounts to the specified actions',
            input=AddPermissionInput(),
            output=AddPermissionOutput(),
            aws_service='sns',
            aws_command='add_permission',
            pagination_helper=None
        )
