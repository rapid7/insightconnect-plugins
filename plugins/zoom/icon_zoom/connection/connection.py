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
        account_id = params[Input.ACCOUNT_ID]
        client_id = params[Input.CLIENT_ID]
        client_secret = params[Input.CLIENT_SECRET]

        self.zoom_api = ZoomAPI(account_id=account_id,
                                client_id=client_id,
                                client_secret=client_secret,
                                logger=self.logger)

    def test(self):
        try:
            # Return self to confirm API and key is working
            self.zoom_api.get_user("me")
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e)

        return {}