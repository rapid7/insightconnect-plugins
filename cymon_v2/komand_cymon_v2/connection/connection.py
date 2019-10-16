import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_cymon_v2.util.api import CymonV2
import maya


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        now = maya.now()
        end = maya.when(string="April 30, 2019")

        if now >= end:
            raise Exception("Error: The Cymon service has been discontinued. "
                            "Please transition off of using this plugin.")
        else:
            self.logger.warning("Warning: The Cymon service will be discontinued on April 30, 2019. "
                                "Please plan to transition off this plugin before then.")

        self.logger.info('Connecting')

        credentials = params.get('api_credentials')
        if credentials:
            username = credentials.get('username')
            password = credentials.get('password')

        if username == 'anonymous' and password == 'anonymous':
            username = None
            password = None

        self.api = CymonV2(username, password, self.logger)

        self.logger.info('Connected')
