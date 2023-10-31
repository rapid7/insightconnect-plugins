import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from komand_pagerduty.util.api import PagerDutyAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        """
        Connect to PagerDuty
        """

        key = params.get(Input.API_KEY, {}).get("secretKey")
        self.api = PagerDutyAPI(api_key=key, logger=self.logger)

    def test(self):
        try:
            self.api.list_users()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
