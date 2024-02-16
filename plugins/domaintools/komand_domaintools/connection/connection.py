import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from .schema import ConnectionSchema, Input

# Custom imports below
from domaintools import API
from domaintools.exceptions import NotAuthorizedException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        username = params.get(Input.USERNAME)
        key = params.get(Input.API_KEY, {}).get("secretKey")
        api = API(username, key)
        try:
            response = api.account_information()
            response.data()
        except NotAuthorizedException as exception:
            self.logger.error(f"DomainTools: Connect: error {exception}")
            raise ConnectionTestException(
                cause="DomainTools: Connect: Authorization failed",
                assistance="Please review your connection details",
                data=response,
            )
        except Exception as exception:
            self.logger.error(f"DomainTools: Connect: error {exception}")
            raise ConnectionTestException(cause=f"DomainTools: Connect: Failed to connect to server {exception}", data=response)
        self.api = api

    def test(self):
        try:
            response = self.api.account_information()
            response.data()
        except NotAuthorizedException as exception:
            self.logger.error(f"DomainTools: Connect: error {exception}")
            raise ConnectionTestException(
                cause="DomainTools: Connect: Authorization failed",
                assistance="Please review your connection details",
                data=response,
            )
        except Exception as exception:
            self.logger.error(f"DomainTools: Connect: error {exception}")
            raise ConnectionTestException(
                cause=PluginException.Preset.UNKNOWN,
                assistance=PluginException.Preset.UNKNOWN,
                data=exception,
            )
        return {"success": True}
