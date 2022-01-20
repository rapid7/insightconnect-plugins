from urllib.parse import urlparse
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.util.constants.constant import SUCCESS_RESPONSE_CODES
from icon_ibm_qradar.util.constants.endpoints import START_ARIEL_SEARCH_ENDPOINT
from unit_test.helpers.helper import Helper, MockResponse


class ArielSearchHelper(Helper):
    """Helper class for the unit test cases."""

    def __init__(self):
        """Initialize Ariel Search Unit test Helper."""
        self.endpoint = START_ARIEL_SEARCH_ENDPOINT

    @staticmethod
    def mock_request(*args, **kwargs):
        """To mock the requests method for unit test."""
        if kwargs.get("auth")[0] == "wrong":
            return MockResponse(401, data={})
        if kwargs.get("auth")[1] == "wrong":
            return MockResponse(401, data={})

        url_component = urlparse(kwargs.get("url"))

        if url_component.hostname == "wrong":
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        if "internalServerError" in url_component.path:
            return MockResponse(500, {})

        if "checkforbidden" in url_component.path:
            return MockResponse(403, {})

        if "checkratelimit" in url_component.path:
            return MockResponse(429, {})

        if url_component.query != "":
            if "wrong" in url_component.query:
                return MockResponse(422, data={"description": "wrong aql", "message": "wrong aql"})

            return MockResponse(SUCCESS_RESPONSE_CODES[1], data={"cursor_id": "test_cursor_id"})

        if "wrong" in url_component.path:
            return MockResponse(422, data={"description": "wrong aql", "message": "wrong aql"})
        return MockResponse(SUCCESS_RESPONSE_CODES[0], data={"cursor_id": "test_cursor_id"})
