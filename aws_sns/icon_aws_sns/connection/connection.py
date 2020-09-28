# *************************************************************************
# COPYRIGHT (C) 2012-2018, Rapid7 LLC, Boston, MA, USA.
# All rights reserved. This material contains unpublished, copyrighted
# work including confidential and proprietary information of Rapid7.
# ************************************************************************/

import botocore.session
import insightconnect_plugin_runtime
from .schema import ConnectionSchema

from ..common import ActionHelper


class Connection(insightconnect_plugin_runtime.Connection):
    client = None
    helper = ActionHelper()

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params=None):
        if not params:
            params = {}

        session = botocore.session.Session()
        self.client = session.create_client(
            'sns',
            aws_access_key_id=params['aws_access_key_id'],
            aws_secret_access_key=params['aws_secret_access_key'],
            region_name=params['region'])
        self.logger.info("Client connection object created...")
