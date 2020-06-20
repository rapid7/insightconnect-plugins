import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_broadcom_symantec_endpoint_protection.util.api import APIClient, APIException
from insightconnect_plugin_runtime.exceptions import PluginException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params):
        host = params.get(Input.HOST)
        port = params.get(Input.PORT)
        username = params.get(Input.CREDENTIALS)["username"]
        password = params.get(Input.CREDENTIALS)["password"]
        domain = params.get(Input.DOMAIN, "")

        try:
            self.api_client: APIClient = APIClient.new_client(host=host,
                                                              username=username,
                                                              password=password,
                                                              domain=domain,
                                                              port=port,
                                                              logger=self.logger)
            self.logger.info("Connection to Symantec Endpoint Protection console succeeeded!")
        except APIException as e:
            raise PluginException(cause="Authentication to the Symantec Endpoint Protection console failed!",
                                  assistance=e.message)

    def test(self):
        # Implicit connection test happens since connect function is called first
        return {"success": True}
