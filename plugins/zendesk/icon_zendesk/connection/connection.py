import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
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
            raise PluginException(cause="Could not authenticate to Zendesk.",
                                  assistance="Please provide a password or API key.")

        self.client = zenpy.Zenpy(**creds)
        self.logger.info("Connect: Connecting...")
