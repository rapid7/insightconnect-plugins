import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from .schema import ConnectionSchema, Input
from icon_mimecast_v2.util.api import API

# Custom imports below
from datetime import datetime, timezone


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey", "").strip()
        self.client_id = params.get(Input.CLIENT_ID, {}).get("secretKey", "").strip()
        self.api = API(client_id=self.client_id, client_secret=self.client_secret, logger=self.logger)
        self.api.authenticate()

    def test(self):
        try:
            now_date = datetime.now(tz=timezone.utc).date()
            self.api.get_siem_logs(log_type="receipt", query_date=now_date, page_size=1, max_threads=1, next_page=None)
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)

    def test_task(self):
        try:
            now_date = datetime.now(tz=timezone.utc).date()
            self.api.get_siem_logs(log_type="receipt", query_date=now_date, page_size=1, max_threads=1, next_page=None)
            return_messsage = "The connection test to Mimecast was successful."
            self.logger.info(return_messsage)
            return {"success": True}, return_messsage
        except PluginException as error:
            return_message = ""
            failed_message = "The connection test to Mimecast for has failed."
            self.logger.info(failed_message)
            return_message += f"{failed_message}\n"

            cause_message = f"This failure was caused by: '{error.cause}'"
            self.logger.info(cause_message)
            return_message += f"{cause_message}\n"

            self.logger.info(error.assistance)
            return_message += f"{error.assistance}\n"
            raise ConnectionTestException(
                cause="Configured credentials do not have permission for this API endpoint.",
                assistance="Please ensure credentials have required permissions.",
                data=return_message,
            )
