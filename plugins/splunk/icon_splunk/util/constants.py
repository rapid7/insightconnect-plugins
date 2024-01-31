from insightconnect_plugin_runtime.exceptions import PluginException
from splunklib.binding import HTTPError, AuthenticationError

from xml.etree.ElementTree import ParseError  # noqa: B405
from ssl import SSLError
import socket

TIMER_STEP = 0.2

EXCEPTION_MAPPING = {
    HTTPError: PluginException(preset=PluginException.Preset.USERNAME_PASSWORD),
    ValueError: PluginException(
        cause="Unable to connect to Splunk at the provided address.",
        assistance="Check that the Connection contains the correct host or IP address " "and not in URL format.",
    ),
    ParseError: PluginException(
        cause="Splunk returned an unreadable response",
        assistance="It's likely that the WUI port was provided instead of the Splunk API port. "
        "Please verify that the Connection contains the Splunk API port (default: 8089).",
    ),
    ConnectionResetError: PluginException(
        cause="Splunk reset the connection.",
        assistance="Check that the host and SSL/TLS settings in the Connection match your Splunk "
        "server's configuration.",
    ),
    SSLError: PluginException(
        cause="Splunk returned an SSL error.",
        assistance="Check that the SSL/TLS settings in the Connection match your Splunk your server's "
        "configuration and that the Splunk API port (default: 8089) is being specified.",
    ),
    AuthenticationError: PluginException(
        cause="Authentication failed.",
        assistance="Verify your credentials are correct and try again.",
    ),
    socket.error: PluginException(
        cause="Splunk server is unreachable.",
        assistance="Verify the Splunk server IP address or host is valid and the connection is not being "
        "interrupted by anything such as a firewall.",
    ),
    socket.timeout: PluginException(
        cause="A timeout occurred while connecting to the specified Splunk server.",
        assistance="Verify the Splunk server IP address or host is valid and the connection is not being "
        "interrupted by anything such as a firewall.",
    ),
}
