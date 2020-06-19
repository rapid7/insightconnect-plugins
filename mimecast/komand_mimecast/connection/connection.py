import komand
from .schema import ConnectionSchema
# Custom imports below
from komand.exceptions import ConnectionTestException
from komand_mimecast.util import util


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        # set Variables
        self.url = params.get('url')
        self.app_id = params.get('app_id')
        self.app_key = params.get('app_key').get('secretKey')
        self.secret_key = params.get('secret_key').get('secretKey')
        self.access_key = params.get('access_key').get('secretKey')

    def test(self):
        payload = {
            'data': []
        }

        uri = "/api/account/get-account"

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=self.url, uri=uri,
                                       access_key=self.access_key, secret_key=self.secret_key,
                                       app_id=self.app_id, app_key=self.app_key, data=payload)
        if response['meta']['status'] != 200:
            self.logger.error(response)
            raise ConnectionTestException(cause='Server request failed.',
                                          assistance='Status code is {}, see log for details.'.format(
                                          response['meta']['status']),
                                          data=response['fail'])

        return {'connection': 'successful'}
