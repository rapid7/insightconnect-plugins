from urllib.parse import urlparse

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.util.constants.constant import SUCCESS_RESPONSE_CODES
from unit_test.helpers.helper import Helper, MockResponse


class AsstesHelper(Helper):
    """Helper class for the unit test cases."""

    @staticmethod
    def mock_request(*args, **kwargs):
        """To mock the requests method for unit test."""
        if kwargs.get("auth")[0] == "wrong":
            return MockResponse(401, data={})
        if kwargs.get("auth")[1] == "wrong":
            return MockResponse(401, data={})

        url_component = urlparse(kwargs.get("url"))

        if "internalServerError" in url_component.query:
            return MockResponse(500, {})

        if url_component.hostname == "wrong":
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        print("url_component.query", url_component.query)

        if url_component.query == "wrong":
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        return MockResponse(SUCCESS_RESPONSE_CODES[1], data={"data": [{"id": "10001"}]})
