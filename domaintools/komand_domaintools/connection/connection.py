import komand
from .schema import ConnectionSchema
# Custom imports below
from domaintools import API
from domaintools.exceptions import NotAuthorizedException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        username = params.get('username')
        key = params.get('api_key').get('secretKey')
        api = API(username, key)
        try:
            response = api.account_information()
            response.data()
        except NotAuthorizedException:
            self.logger.error('DomainTools: Connect: error %s')
            raise Exception('DomainTools: Connect: Authorization failed. Please try again')
        except Exception as e:
            self.logger.error('DomainTools: Connect: error %s', str(e))
            raise Exception('DomainTools: Connect: Failed to connect to server {}'.format(e))

        self.api = api
