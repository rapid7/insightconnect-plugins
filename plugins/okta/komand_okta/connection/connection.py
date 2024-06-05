import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_okta.util.helpers import get_hostname, validate_url

# Custom imports below
from komand_okta.util.api import OktaAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        okta_url = params.get(Input.OKTAURL)
        base_url = f"https://{get_hostname(okta_url.rstrip('/'))}"

        valid_url = validate_url(base_url)

        self.api_client = OktaAPI(
            params.get(Input.OKTAKEY, {}).get("secretKey"), base_url, logger=self.logger, valid_url=valid_url
        )

    def test(self):
        try:
            self.api_client.list_groups()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
