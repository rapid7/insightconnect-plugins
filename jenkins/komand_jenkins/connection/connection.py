import komand
from .schema import ConnectionSchema
# Custom imports below
import jenkins
from jenkins import EmptyResponseException, BadHTTPException
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')
        host = params.get('host')

        self.logger.info("Connect: Connecting...")

        self.server = jenkins.Jenkins(host, username=username, password=password)

    def test(self):
        try:
            self.server.get_whoami()
        except EmptyResponseException as e:
            raise ConnectionTestException(cause="An empty response was received while attempting to connect to Jenkins.",
                                          assistance="Double-check your Jenkins server configuration.",
                                          data=e)
        except BadHTTPException as e:
            raise ConnectionTestException(
                cause="A bad HTTP response was received while attempting to connect to Jenkins.",
                assistance="Double-check your Jenkins server configuration and ensure it is reachable.",
                data=e)

        return {"success": True}

