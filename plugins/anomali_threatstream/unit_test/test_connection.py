from unittest import TestCase
from komand_anomali_threatstream.connection.connection import Connection
from komand.exceptions import PluginException


class TestConnection(TestCase):
    def test_send_exception(self):
        """
        Create a dummy request that intentionally fails, check that it raises the correct exception,
        and assert that it correctly suppresses the API key parameter value.
        """

        conn = Connection()
        conn.request.url = "https://c02709b0-d8fc-11eb-852a-acde48001122.com"
        conn.request.url, conn.request.method = conn.request.url + "/api_key=MYSECRETKEY&key=value", "GET"
        conn.request.verify = False

        with self.assertRaisesRegex(
            PluginException, "Max retries exceeded with url: /api_key=\*\*\*\*\*\*\*\*&key=value"
        ):
            conn.send(conn.request)
