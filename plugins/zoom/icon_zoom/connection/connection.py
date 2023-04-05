import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from icon_zoom.util.api import ZoomAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.zoom_api = None

    def connect(self, params):
        secret_key = "secretKey"

        account_id = params.get(Input.ACCOUNT_ID, {}).get(secret_key)
        client_id = params.get(Input.CLIENT_ID, {}).get(secret_key)
        client_secret = params.get(Input.CLIENT_SECRET, {}).get(secret_key)
        jwt_token = params.get(Input.JWT_TOKEN, {}).get(secret_key)

        if jwt_token is not None:
            self.zoom_api = ZoomAPI(logger=self.logger, jwt_token=jwt_token)
        elif (account_id is not None) and (client_id is not None) and (client_secret is not None):
            self.zoom_api = ZoomAPI(
                logger=self.logger, account_id=account_id, client_id=client_id, client_secret=client_secret,
            )
        else:
            raise PluginException(cause="Credentials for either JWT Token or OAuth are required, "
                                        "although none were provided.",
                                  assistance="If using JWT, please input only the JWT Token in your connection "
                                             "configuration. If using OAuth, please input only the "
                                             "Account ID, Client ID, and Client Secret.")

    def test(self):
        try:
            # Return self to confirm API and key is working
            self.zoom_api.get_user("me")
            return {"success": True}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e)
