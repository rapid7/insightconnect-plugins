import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
import json
import requests # nosec B113
import urllib


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def check(self, url):
        r = requests.post(
            "https://checkurl.phishtank.com/checkurl/",
            data={
                "format": "json",
                "url": urllib.quote(url),
                "app_key": self.parameters.get("credentials").get("secretKey"),
            },
        )
        result = r.json()["results"]

        if result.get("phish_detail_page"):
            result["phish_detail_url"] = result["phish_detail_page"]
            del result["phish_detail_page"]

        return result

    def connect(self, params):  # pylint: disable=unused-argument
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']
        """
        self.logger.info("Connecting to Phishtank...")
