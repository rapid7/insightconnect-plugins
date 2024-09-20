import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from datetime import datetime, timedelta, timezone

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from icon_palo_alto_cortex_xdr.util.api import CortexXdrAPI
from requests.exceptions import ConnectionError as con_error

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.xdr_api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        api_key = params.get(Input.API_KEY, {}).get("secretKey", "").strip()
        api_key_id = params.get(Input.API_KEY_ID, "")
        fqdn = params.get(Input.URL, "").strip()
        fqdn = self.clean_up_fqdn(fqdn)

        security_level = params.get(Input.SECURITY_LEVEL)

        self.xdr_api = CortexXdrAPI(api_key_id, api_key, fqdn, security_level, self.logger)

    def clean_up_fqdn(self, fqdn):
        # Add trailing slash if needed
        if not fqdn.endswith("/"):
            fqdn = fqdn + "/"

        if not fqdn.startswith("http://") and not fqdn.startswith("https://"):
            fqdn = f"https://{fqdn}"

        return fqdn

    def test(self):
        self.xdr_api.test_connection()
        return {"success": True}

    def test_task(self):
        self.logger.error("Running a Task Connection Test for Palo Alto Cortex")
        return_message = "The connection test to Palo Alto Cortex has failed \n"

        # Gets the current time and converts to  Epoch Unix time
        now = datetime.now(timezone.utc)

        start_time = int((now - timedelta(minutes=5)).timestamp() * 1000)
        end_time = int(now.timestamp() * 1000)
        time_sort_field = "creation_time"

        filters = [
            {"field": time_sort_field, "operator": "gte", "value": start_time},
            {"field": time_sort_field, "operator": "lte", "value": end_time},
        ]

        post_body = {
            "request_data": {
                "search_from": 0,
                "search_to": 100,
                "sort": {"field": time_sort_field, "keyword": "asc"},
                "filters": filters,
            }
        }

        try:
            _, _, _ = self.xdr_api.get_response_alerts(post_body)
            message = "The connection test to Palo Alto Cortex was successful"
            self.logger.info(message)
            return {"success": True}, message

        except PluginException as error:
            return_message = "The connection test to Palo Alto Cortex failed.\n"
            return_message += f"This failure was caused by: '{error.cause}'\n"
            return_message += f"Error assistance: {error.assistance}\n"

            self.logger.info(f"error = {error.cause}")

            raise ConnectionTestException(
                cause="The OAuth token credentials provided in the connection configuration is invalid.",
                assistance="Please verify the credentials are correct and try again.",
                data=return_message,
            )
        except con_error as error:
            self.logger.error(error)
            return_message += "The URL provided in the connection test is unreachable. Please ensure you are providing a valid URL when trying to connect."
            raise ConnectionTestException(
                cause="The connection test to Palo Alto Cortex failed due to the URL being unreachable.",
                assistance="Please ensure the URL is correct before attempting again.",
                data=return_message,
            )
