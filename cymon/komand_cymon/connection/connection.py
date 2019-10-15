import komand
from .schema import ConnectionSchema
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
        if 'cred_token' not in params:
            token = ''
            self.logger.info('Connect: Unauthenticated API will be used')
        else:
            token = params.get('api_key').get('secretKey')

        server = params.get('url', 'https://cymon.io:443')

        self.token = token
        self.server = server
