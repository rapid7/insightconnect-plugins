import logging

import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from ..util.api import API

# Custom imports below
import json
import requests
import urllib


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # creds aren't required - going to fail unit tests if empty - needs handled
        credentials = Input.CREDENTIALS
        logging.info(f"THIS IS FROM CONNECTION - CREDS: {credentials}")
        self.api = API(credentials=credentials)
        logging.info(f"THIS IS FROM CONNECTION - API CREDS: {credentials}")

    def test(self):
        endpoint = "phishtank/status"
        try:
            self.api.check(endpoint)  # changed send to check
            return {"success": True}
        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED, data=exception)
