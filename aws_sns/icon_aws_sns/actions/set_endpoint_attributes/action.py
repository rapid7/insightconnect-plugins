# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import insightconnect_plugin_runtime
from ...common import AWSAction
from .schema import SetEndpointAttributesInput, SetEndpointAttributesOutput


class SetEndpointAttributes(AWSAction):

    def __init__(self):
        super().__init__(
            name='set_endpoint_attributes',
            description='Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM and APNS',
            input=SetEndpointAttributesInput(),
            output=SetEndpointAttributesOutput(),
            aws_service='sns',
            aws_command='set_endpoint_attributes',
            pagination_helper=None
        )
