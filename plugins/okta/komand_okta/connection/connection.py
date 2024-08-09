import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_okta.util.helpers import get_hostname, validate_url
from komand_okta.util.exceptions import ApiException
from requests.exceptions import ConnectionError as con_err

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

    def test_task(self):
        self.logger.info("Running a connection test to Okta")
        return_message = "The connection test to Okta was unsuccessful \n"
        try:
            _ = self.api_client.list_events("")
            message = "The connection test to Okta was successful"
            self.logger.info(message)
            return {"success": True}, message
        except ApiException as error:
            cause_msg = f"The failed connection test to Okta was caused by: '{error.cause}'"
            return_message += f"{cause_msg}\n"
            self.logger.info(cause_msg)
            self.logger.info(error.assistance)
            return_message += f"{error.assistance}\n"
            self.logger.error(error)
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=return_message)

        # This catches if the user enters a URL in the correct format but is unreachable
        except con_err as error:
            self.logger.error(error)
            raise ConnectionTestException(
                cause="The URL provided in the connection is unreachable. Please ensure you are providing a valid URL when trying to connect.",
                assistance="Please verify the URL specified is valid and reachable before attempting to connect again.",
                data="Please ensure the URL specified can be reached and is valid before trying to reconnect.",
            )
        except ConnectionResetError as error:
            self.logger.error(f"Catching egress rules for connection: '{error}'")
            raise ConnectionTestException(
                cause="Failed to connect to the supplied URL.",
                assistance="Please contact support if this issue persists.",
                data="The connection to Okta has failed. Please ensure your details are correct before attempting to connect again.",
            )
