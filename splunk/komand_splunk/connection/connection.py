import komand
from .schema import ConnectionSchema
# Custom imports below
from komand.exceptions import ConnectionTestException
import splunklib
import splunklib.client as client
import xml
import ssl


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        self.host, self.port, self.username, self.password = params.get('host'), \
                                                             params.get('port'), \
                                                             params.get('credentials').get('username'), \
                                                             params.get('credentials').get('password')

        self.scheme = 'https'
        if not params.get('use_ssl'):
            self.logger.info("Connect: An unsecure HTTP session will be used and SSL/TLS verify will be ignored.")
            self.scheme = 'http'
            self.verify = False

        if self.scheme == 'https':
            self.verify = True
            if not params.get('ssl_verify'):
                self.verify = False
                self.logger.info("Connect: SSL/TLS verification of the Splunk server's certificate is not enabled.")

        if params.get('license') == 'Free':
            # We need to pass 'admin' as the username for the free license
            self.logger.info("Connect: Connecting with Splunk's free license configuration")
            try:
                self.client = client.connect(
                    host=self.host,
                    port=self.port,
                    username='admin',
                    scheme=self.scheme,
                    verify=self.verify
                )
            except splunklib.binding.HTTPError:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.USERNAME_PASSWORD,
                )
            except ValueError:
                raise ConnectionTestException(
                    cause="Unable to connect to Splunk at the provided address.",
                    assistance="Check that the Connection contains the correct host or IP address "
                    "and not in URL format."
                )
            except xml.etree.ElementTree.ParseError:
                raise ConnectionTestException(
                    cause="Splunk returned an unreadable response.",
                    assistance="It's likely that the WUI port was provided instead of the Splunk API port. "
                    "Please verify that the Connection contains the Splunk API port (default: 8089)."
                )
            except ConnectionResetError:
                raise ConnectionTestException(
                    cause="Splunk reset the connection.",
                    assistance="Check that the host and SSL/TLS settings in the Connection match your Splunk "
                    "server's configuration."
                )
            except ssl.SSLError:
                raise ConnectionTestException(
                    cause="Splunk returned an SSL error.",
                    assistance="Check that the SSL/TLS settings in the Connection match your Splunk your server's "
                    "configuration and that the Splunk API port (default: 8089) is being specified."
                )

        if params.get('license') == 'Enterprise':
            # Enterprise license
            self.logger.info("Connect: Connecting with Splunk's enterprise license configuration")

            try:
                self.client = client.connect(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password=self.password,
                    scheme=self.scheme,
                    verify=self.verify
                )
            except splunklib.binding.HTTPError:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.USERNAME_PASSWORD,
                )
            except ValueError:
                raise ConnectionTestException(
                    cause="Unable to connect to Splunk at the provided address.",
                    assistance="Check that the Connection contains the correct host or IP address "
                    "and not in URL format."
                )
            except xml.etree.ElementTree.ParseError:
                raise ConnectionTestException(
                    cause="Splunk returned an unreadable response",
                    assistance="It's likely that the WUI port was provided instead of the Splunk API port. "
                    "Please verify that the Connection contains the Splunk API port (default: 8089)."
                )
            except ConnectionResetError:
                raise ConnectionTestException(
                    cause="Splunk reset the connection.",
                    assistance="Check that the host and SSL/TLS settings in the Connection match your Splunk "
                    "server's configuration."
                )
            except ssl.SSLError:
                raise ConnectionTestException(
                    cause="Splunk returned an SSL error.",
                    assistance="Check that the SSL/TLS settings in the Connection match your Splunk your server's "
                    "configuration and that the Splunk API port (default: 8089) is being specified."
                )


    def test(self):
        return { 'Test': 'Success' }
