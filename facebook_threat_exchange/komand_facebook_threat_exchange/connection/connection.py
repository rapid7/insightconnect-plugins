import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.appid = None
        self.appsecret = None

    def connect(self, params={}):
        try:
            self.logger.info("Connect: Connecting..")
            self.appid = params['app_id']
            self.appsecret = params.get('secret_key').get('secretKey')
        except:
            self.logger.error("Unable to set credentials")
            raise
