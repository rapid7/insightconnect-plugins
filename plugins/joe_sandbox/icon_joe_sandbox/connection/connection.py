import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import jbxapi
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        api_key = params.get(Input.API_KEY).get("secretKey")
        api_url = params.get(Input.URL)
        if api_url is None:
            api_url = jbxapi.API_URL

        self.api = jbxapi.JoeSandbox(api_key, api_url)

        self.logger.info("Connect: Connected successfully")

    def test(self):
        try:
            self.api.server_online()
            return {"success": True}
        except jbxapi.MissingParameterError as error:
            raise ConnectionTestException(
                cause=str(error),
                assistance="Please make sure that you are using Joe Sandbox " "according to the documentation.",
            )
        except jbxapi.InvalidParameterError as error:
            raise ConnectionTestException(cause=str(error), assistance="If the issue persists please contact support.")
        except jbxapi.InvalidApiKeyError:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except jbxapi.ServerOfflineError:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except jbxapi.InternalServerError:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR)
        except jbxapi.PermissionError:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
        except jbxapi.ApiError as error:
            raise ConnectionTestException(
                cause="An error occurred: " + str(error),
                assistance="If the issue persists please contact support.",
            )
