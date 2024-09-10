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

        api_key = params.get(Input.API_KEY, {}).get("secretKey")
        api_key_id = params.get(Input.API_KEY_ID, "")
        fqdn = params.get(Input.URL, "")
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

        #Gets the current time and converts to  Epoch Unix time (as get_alerts params require date to be an int)
        now = datetime.now(timezone.utc)
        start_time = (now - timedelta(minutes=5)).isoformat()
        start_time = datetime.fromisoformat(start_time)
        #Timestamp in logs is in Miliseconds
        start_time = int(start_time.timestamp() * 1000)

        end_time = now.isoformat()
        end_time = datetime.fromisoformat(end_time)
        end_time = int(end_time.timestamp() * 1000)

        self.logger.info(f"{start_time= }, {end_time= }")

        try:
            _ = self.xdr_api.get_alerts(start_time, end_time)
            message = "The connection test to Palo Alto Cortex was successful"
            self.logger.info(message)
            return {"success": True}, message

        except PluginException as e:
            if "401" or "402" or "403" or "404" in e.cause:
                return_message += e.assistance
            else:
                return_message += "Please verify the credentials/setup is correct and try"
            self.logger.info(
                f"cause = {e.cause}, assistance = {e.assistance}, data {e.data}, error = {e}"
            )
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
                data=return_message
            )



