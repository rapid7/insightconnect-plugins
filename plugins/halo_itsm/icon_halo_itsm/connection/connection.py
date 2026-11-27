import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from icon_halo_itsm.util.api import HaloItsmApi
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting to Halo ITSM...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        base_url = params.get(Input.BASE_URL, "").strip().rstrip("/")
        client_id = params.get(Input.CLIENT_ID, "").strip()
        client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey", "").strip()
        tenant = params.get(Input.TENANT, "").strip()
        # END INPUT BINDING - DO NOT REMOVE

        self.client = HaloItsmApi(
            base_url=base_url,
            client_id=client_id,
            client_secret=client_secret,
            tenant=tenant,
            logger=self.logger,
        )

    def test(self):
        try:
            self.client.test_connection()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
