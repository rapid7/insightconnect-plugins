import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from icon_zoom.util.api import ZoomAPI
from icon_zoom.util.api import AuthenticationRetryLimitError, AuthenticationError


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.zoom_api = None

    def connect(self, params):
        account_id = params.get(Input.ACCOUNT_ID)
        client_id = params.get(Input.CLIENT_ID)
        client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey")
        oauth_authentication_retry_limit = params.get(Input.AUTHENTICATION_RETRY_LIMIT, 5)

        self.zoom_api = ZoomAPI(
            logger=self.logger,
            account_id=account_id,
            client_id=client_id,
            client_secret=client_secret,
            oauth_retry_limit=oauth_authentication_retry_limit,
        )

    def test(self):
        try:
            # Return self to confirm API and key is working
            self.zoom_api.authenticate()
            self.zoom_api.get_user("me")
            return {"success": True}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e)
        except AuthenticationRetryLimitError:
            raise ConnectionTestException(
                cause="OAuth authentication retry limit was met.",
                assistance="Ensure your OAuth connection credentials are valid. "
                "If running a large number of integrations with Zoom, consider "
                "increasing the OAuth authentication retry limit to accommodate.",
            )
        except AuthenticationError:
            raise ConnectionTestException(
                cause="The OAuth token credentials provided in the connection configuration is invalid.",
                assistance="Please verify the credentials are correct and try again.",
            )

    def test_task(self):
        self.logger.info("Running a connection test to Zoom")
        return_message = "The connection test to Zoom has failed \n"
        try:
            _ = self.zoom_api.get_user_activity_events()
            message = "The connection test to Zoom was successful"
            self.logger.info(message)
            return {"success": True}, message

        except AuthenticationError:
            return_message += "401 Authentication Error. Please ensure the supplied credentials are valid.\n "
            self.logger.info(return_message)

            raise ConnectionTestException(
                cause="The OAuth token credentials provided in the connection configuration is invalid.",
                assistance="Please verify the credentials are correct and try again.",
                data=return_message,
            )

        except AuthenticationRetryLimitError:
            return_message += "The authentication retry limit has exceeded the maximum allowance. Please ensure your credentials are correct and try again."
            raise ConnectionTestException(
                cause="OAuth authentication retry limit was met.",
                assistance="Ensure your OAuth connection credentials are valid. "
                "If running a large number of integrations with Zoom, consider "
                "increasing the OAuth authentication retry limit to accommodate.",
                data=return_message,
            )

        except PluginException:
            return_message += "Please verify the setup within Zoom is correct and try again."
            self.logger.info(
                "Please check the setup within Zoom is correct and try again. This can also be caused by the appropriate scopes not added (found within App Marketplace) or the required permissions are not granted for the API endpoint."
            )
            raise ConnectionTestException(
                cause="Configured credentials do not have permission for this API endpoint.",
                assistance="Please ensure credentials have required permissions.",
                data=return_message,
            )

            self.logger.error(error)
            raise ConnectionTestException(data=return_message)
