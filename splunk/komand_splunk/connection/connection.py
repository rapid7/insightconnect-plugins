import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from komand.exceptions import ConnectionTestException, PluginException

from splunklib.binding import HTTPError, AuthenticationError
from splunklib.client import Service
import splunklib.client as client

from xml.etree.ElementTree import ParseError
from ssl import SSLError
import socket


class Connection(komand.Connection):

    _EXCEPTIONS = {
        HTTPError: PluginException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD),
        ValueError: PluginException(
            cause="Unable to connect to Splunk at the provided address.",
            assistance="Check that the Connection contains the correct host or IP address "
                       "and not in URL format."),
        ParseError: PluginException(
            cause="Splunk returned an unreadable response",
            assistance="It's likely that the WUI port was provided instead of the Splunk API port. "
                       "Please verify that the Connection contains the Splunk API port (default: 8089)."),
        ConnectionResetError: PluginException(
            cause="Splunk reset the connection.",
            assistance="Check that the host and SSL/TLS settings in the Connection match your Splunk "
                       "server's configuration."),
        SSLError: PluginException(
            cause="Splunk returned an SSL error.",
            assistance="Check that the SSL/TLS settings in the Connection match your Splunk your server's "
                       "configuration and that the Splunk API port (default: 8089) is being specified."),
        AuthenticationError: PluginException(
            cause="Authentication failed.",
            assistance="Verify your credentials are correct and try again."
        ),
        socket.error: PluginException(
            cause="Splunk server is unreachable.",
            assistance="Verify the Splunk server IP address or host is valid and the connection is not being "
                       "interrupted by anything such as a firewall."
        ),
        socket.timeout: PluginException(
            cause="A timeout occurred while connecting to the specified Splunk server.",
            assistance="Verify the Splunk server IP address or host is valid and the connection is not being "
                       "interrupted by anything such as a firewall."
        )
    }

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        # noinspection PyPep8
        self.client, self.verify, self.host, self.port, self.username, self.password, self.scheme = None, \
                                                                                                    None, \
                                                                                                    None, \
                                                                                                    None, \
                                                                                                    None, \
                                                                                                    None, \
                                                                                                    None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")

        # noinspection PyPep8
        self.host, self.port, self.username, self.password = params.get(Input.HOST), \
                                                             params.get(Input.PORT), \
                                                             params.get(Input.CREDENTIALS).get("username"), \
                                                             params.get(Input.CREDENTIALS).get("password")
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
                    verify=self.verify)
            else:
                self.logger.info("Connect: Connecting with Free license configuration...")
                # We need to pass 'admin' as the username for the free license
                splunk_client = client.connect(
                    host=self.host,
                    port=self.port,
                    username="admin",
                    scheme=self.scheme,
                    verify=self.verify)
        except Exception as e:
            # noinspection PyTypeChecker
            raise self._EXCEPTIONS.get(type(e), PluginException(cause="An unhandled exception occurred!",
                                                                assistance="Check the logs for more details.",
                                                                data=e))

        return splunk_client

    def test(self, params={}):
        # No connection test needed - it is implicit with the `connect` function
        pass
