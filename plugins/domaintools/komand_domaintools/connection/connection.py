import insightconnect_plugin_runtime
from domaintools import API
from domaintools.exceptions import NotAuthorizedException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from .schema import ConnectionSchema


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        username = params.get("username")
        key = params.get("api_key").get("secretKey")
        api = API(username, key)
        try:
            response = api.account_information()
            response.data()
        except NotAuthorizedException:
            self.logger.error("DomainTools: Connect: error %s")
            raise ConnectionTestException(cause="DomainTools: Connect: Authorization failed. Please try again")
        except Exception as e:
            self.logger.error("DomainTools: Connect: error %s", str(e))
            raise ConnectionTestException(
                cause="DomainTools: Connect: Authorization failed. Please try again", assistance=e
            )

        self.api = api
