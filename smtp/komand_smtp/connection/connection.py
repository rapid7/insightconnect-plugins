import komand
from .schema import ConnectionSchema
# Custom imports below
from smtplib import SMTP


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(ConnectionSchema())

    def get(self):
        params = self.params
        self.logger.info("Connecting to %s:%d", params['host'], params['port'])
        self.client = SMTP(params['host'], params['port'], timeout=60)
        self.client.ehlo()
        if params.get('use_ssl'):
            self.client.starttls()

        if params.get('credentials').get('username') and params.get('credentials').get('password'):
            self.client.login(params.get('credentials').get('username'), params.get('credentials').get('password'))

        return self.client

    def connect(self, params={}):
        """ Connect to SMTP server  """
        self.params = params
        return None
