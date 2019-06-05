import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_git.util.git import GitRepository


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        repository_url = params.get('url')
        secret = params.get('credentials').get('password')
        username = params.get('credentials').get('username', None)

        if not username:
            self.logger.info(
                'Connect: Username not provided, using secret via "x-auth-token"'
            )
            username = 'x-auth-token'

        self.git_repository = GitRepository(
            repository_url, username, secret, self.logger
        )
