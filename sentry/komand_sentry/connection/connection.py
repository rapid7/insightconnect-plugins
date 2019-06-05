import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_sentry.util.auth import SentryConnection


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info('Connect: Verifying Sentry Auth Token ...')
        token = params.get('api_key').get('secretKey')
        api_url = params.get('url')

        try:
            self.sentry_connection = SentryConnection(self, token, api_url)
            self.logger.info('Connect: Sentry Auth Token valid')
        except Exception as e:
            self.logger.error(
                'SentryConnection: Exception: Token authentication failed'
            )
            raise e
