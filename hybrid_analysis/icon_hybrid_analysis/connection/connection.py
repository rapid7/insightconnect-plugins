import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def get(self, hash):
        if self.params.get('url'):

            url = self.params.get('url') + '/scan/' + hash
        else:
            url = 'https://www.hybrid-analysis.com/api' + '/scan/' + hash

        return requests.get(url, {'apikey': self.params.get('api_key').get('secretKey'),
                                  'secret': self.params.get('api_token').get('secretKey')}, headers={
            'User-Agent': 'Bogus UA',
            'From': 'youremail@domain.com'  # This is another valid field
        })

    def connect(self, params={}):
        """
        """
        self.logger.info("Connecting")
        self.params = params
