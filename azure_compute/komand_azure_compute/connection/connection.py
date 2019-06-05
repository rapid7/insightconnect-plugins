import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']

        The following will setup the var to be accessed
          self.blah = self.parameters['blah']
        in the action and trigger files as:
          blah = self.connection.blah
        """
        # TODO: Implement connection or 'pass' if no connection is necessary

    def get_token_from_client_credentials(self, endpoint, client_id, client_secret):
      try:
        payload = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'resource': 'https://management.azure.com/',
        }
        response = requests.post(endpoint, data=payload).json()
        return response['access_token']
      except Exception, e:
        self.logger.error('Cannot request get access token : %s', e)
        return ""

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        server = params.get("host", "https://management.azure.com")
        api_version = params.get("api_version", "2016-04-30-preview")

        client_id = params.get("client_id", "")
        client_secret = params.get("client_secret").get('privateKey')
        tenant_id = params.get("tenant_id", "")
        
        endpoint = 'https://login.microsoftonline.com/%s/oauth2/token/'%tenant_id

        access_token = self.get_token_from_client_credentials(endpoint=endpoint, client_id=client_id, client_secret=client_secret)
        
        if access_token is "":
          self.logger.info('Connect: Unauthenticated API will be used')

        self.server = server
        self.token = access_token
        self.api_version = api_version
