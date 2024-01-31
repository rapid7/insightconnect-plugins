import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from icon_splunk.util.constants import EXCEPTION_MAPPING

from splunklib.client import Service
from splunklib import client


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        # noinspection PyPep8
        (
            self.client,
            self.verify,
            self.host,
            self.port,
            self.username,
            self.password,
            self.scheme,
        ) = (None, None, None, None, None, None, None)

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")

        # noinspection PyPep8
        self.host, self.port, self.username, self.password = (
            params.get(Input.HOST),
            params.get(Input.PORT),
            params.get(Input.CREDENTIALS, {}).get("username"),
            params.get(Input.CREDENTIALS, {}).get("password"),
        )
        license_type = params.get(Input.LICENSE)

        self.scheme = "https"
        if not params.get(Input.USE_SSL):
            self.logger.info("Connect: An insecure HTTP session will be used and SSL/TLS verify will be ignored.")
            self.scheme = "http"
            self.verify = False

        if self.scheme == "https":
            self.verify = True
            if not params.get(Input.SSL_VERIFY):
                self.verify = False
                self.logger.info("Connect: SSL/TLS verification of the Splunk server's certificate is not enabled.")

        self.client = self._create_client(is_enterprise_license=(license_type == "Enterprise"))

    def _create_client(self, is_enterprise_license: bool) -> Service:
        """
        Creates a Splunk client based on the Splunk license input
        :param is_enterprise_license: Whether or not the Splunk client should be configured for an Enterprise license
        :return: Splunk client
        """
        try:
            if is_enterprise_license:
                self.logger.info("Connect: Connecting with Enterprise license configuration...")
                splunk_client = client.connect(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password=self.password,
                    scheme=self.scheme,
                    verify=self.verify,
                )
            else:
                self.logger.info("Connect: Connecting with Free license configuration...")
                # We need to pass 'admin' as the username for the free license
                splunk_client = client.connect(
                    host=self.host,
                    port=self.port,
                    username="admin",
                    scheme=self.scheme,
                    verify=self.verify,
                )
        except Exception as error:
            # noinspection PyTypeChecker
            raise EXCEPTION_MAPPING.get(
                type(error),
                PluginException(
                    cause="An unhandled exception occurred!",
                    assistance="Check the logs for more details.",
                    data=error,
                ),
            )
        return splunk_client

    def test(self):
        try:
            self.client.saved_searches.list()
        except Exception as error:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.INVALID_CREDENTIALS, data=error)
        return {"success": True}
