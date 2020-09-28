# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import DeleteEndpointInput, DeleteEndpointOutput


class DeleteEndpoint(AWSAction):

    def __init__(self):
        super().__init__(
            name='delete_endpoint',
            description='Deletes the endpoint for a device and mobile app from Amazon SNS',
            input=DeleteEndpointInput(),
            output=DeleteEndpointOutput(),
            aws_service='sns',
            aws_command='delete_endpoint',
            pagination_helper=None
        )
