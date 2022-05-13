import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import requests


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.server = "https://urlscan.io/api/v1"
        self.headers = {"User-Agent": "Rapid7 InsightConnect", "Accept": "application/json"}

    def connect(self, params={}):
        if Input.API_KEY in params:
            if params.get(Input.API_KEY).get("secretKey"):
                self.headers["API-Key"] = params[Input.API_KEY]["secretKey"]

    def test(self):
        r = requests.get("https://urlscan.io")
        if r.status_code == 200:
            return {"scan_id": "url.io active"}
