import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import zenpy


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        creds = {
            "email": params.get("credentials").get("username"),
            "subdomain": params.get("subdomain"),
        }

        if params.get("credentials").get("password"):
            creds["password"] = params.get("credentials").get("password")
        elif params.get("api_key").get("secretKey"):
            creds["token"] = params.get("api_key").get("secretKey")
        else:
            raise PluginException(
                cause="Could not authenticate to Zendesk.", assistance="Please provide a password or API key."
            )

        self.client = zenpy.Zenpy(**creds)
        self.logger.info("Connect: Connecting...")

    def test(self):
        try:
            self.client.users()
            return {"success": True}
        except zenpy.lib.exception.APIException as error:
            self.logger.debug(error)
            raise ConnectionTestException(
                cause="Zendesk API connection test failed.",
                assistance="Make sure your credentials are correct.",
                data=error,
            )
        except Exception as error:
            self.logger.debug(error)
            raise ConnectionTestException(
                cause="An unexpected error occurred.",
                assistance="Please ensure that you have entered your details correctly and that your internet connection is active.",
                data=error,
            )
