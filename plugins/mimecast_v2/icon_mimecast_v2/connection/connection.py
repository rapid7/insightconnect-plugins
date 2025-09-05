import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from .schema import ConnectionSchema, Input
from typing import Dict, Tuple
from icon_mimecast_v2.util.api import API

# Custom imports below
from datetime import datetime, timezone

ALL_PERMISSION_SET_LOGS = ["receipt", "ttp_url", "ttp_attachment", "ttp_impersonation"]


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client_id = None
        self.client_secret = None
        self.api = None

    def connect(self, params={}) -> None:
        self.logger.info("Connect: Connecting...")
        self.client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey", "").strip()
        self.client_id = params.get(Input.CLIENT_ID, {}).get("secretKey", "").strip()
        self.api = API(client_id=self.client_id, client_secret=self.client_secret, logger=self.logger)
        self.api.authenticate()

    def test(self) -> Dict[str, bool]:
        try:
            now_date = datetime.now(tz=timezone.utc).date()
            self.api.get_siem_logs(log_type="receipt", query_date=now_date, page_size=1, max_threads=1, next_page=None)
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)

    def test_task(self) -> Tuple[Dict[str, bool], str]:
        try:
            # Starting message definition
            return_message = "The connection test to Mimecast was successful."

            # Pull permitted logs to be received
            permitted_log_types = self.api.validate_permissions()

            # In case we have no permissions at all, raise an ConnectionTestException
            if not permitted_log_types:
                raise PluginException(
                    cause="Configured credentials do not have permission for any log types (SIEM or TTP).",
                    assistance="Please ensure credentials have required permissions and try again.",
                )

            # Log out the permissions we do and do not have
            for log_type in ALL_PERMISSION_SET_LOGS:
                if log_type in permitted_log_types:
                    successful_message = f"SUCCESS: Permission is correctly configured to access log type: {log_type}."
                    self.logger.info(successful_message)
                    return_message += f"\n{successful_message}"
                else:
                    warning_message = f"WARNING: No required permission set to access log type: {log_type}. That log type will be skipped during ingestion."
                    self.logger.info(warning_message)
                    return_message += f"\n{warning_message}"
            return {"success": True}, return_message
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
