from typing import Dict

import insightconnect_plugin_runtime
import requests
import validators

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from komand_rss.util.utils import handle_response_exception

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.feed_url = None

    def connect(self, params={}) -> None:
        self.feed_url = params.get(Input.URL, "")

    def test(self) -> Dict[str, bool]:
        if not validators.url(self.feed_url):
            raise ConnectionTestException(
                cause="The provided URL is not valid.",
                assistance="Please make sure that you entered the correct URL and try again.",
            )
        handle_response_exception(requests.request("GET", self.feed_url))
        return {"success": True}
