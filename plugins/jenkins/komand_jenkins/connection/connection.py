import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import jenkins
from jenkins import EmptyResponseException, BadHTTPException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        host = params.get(Input.HOST)
        username = params.get(Input.CREDENTIALS, {}).get("username")
        password = params.get(Input.CREDENTIALS, {}).get("password")

        self.logger.info("Connect: Connecting...")
        self.server = jenkins.Jenkins(host, username=username, password=password)

    def test(self):
        try:
            self.server.get_whoami()
            return {"success": True}
        except EmptyResponseException as error:
            raise ConnectionTestException(
                cause="An empty response was received while attempting to connect to Jenkins.",
                assistance="Double-check your Jenkins server configuration.",
                data=error,
            )
        except BadHTTPException as error:
            raise ConnectionTestException(
                cause="A bad HTTP response was received while attempting to connect to Jenkins.",
                assistance="Double-check your Jenkins server configuration and ensure it is reachable.",
                data=error,
            )
