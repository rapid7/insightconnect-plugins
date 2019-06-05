import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info('Listen: Listening...')
        user = params.get('credentials').get('username')
        passwd = params.get('credentials').get('password')

        if user is None:
            user = ''
        if passwd is None:
            passwd = ''

        self.auth_key = '{}:{}'.format(user, passwd)
